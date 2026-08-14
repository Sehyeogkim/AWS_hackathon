# WEMESH — Final Hackathon Plan

> **Find who completes the team. Know exactly what to ask.**

## 1. One-line product definition

**WEMESH is an HR Interview Copilot that ranks candidates by the knowledge a team is missing, then generates targeted interview questions to turn profile claims into interview-verified knowledge.**

한국어 요약:

> **팀의 빈 지식을 가장 잘 메울 후보를 찾고, 그 지식이 진짜인지 확인할 질문까지 만들어주는 HR 인터뷰 도구.**

---

## 2. Customer and user

### Primary customer

- Recruiter / HR
- Hiring Manager

### Situation

- 하나의 포지션에 많은 지원자가 들어온다.
- LinkedIn, 이력서, 포트폴리오가 모두 매끄럽게 작성되어 있다.
- AI가 지원자의 문서 작성을 도울 수 있어, 프로필에 적힌 내용만으로 실제 지식의 깊이를 판단하기 어렵다.
- HR은 누구를 먼저 인터뷰할지, 그리고 무엇을 물어봐야 하는지 빠르게 결정해야 한다.

---

## 3. Pain point

### Core problem

> **AI can make every application look complete, but HR still needs to know which candidate matters to this team and what to ask to verify it.**

전통적인 방식은 주로 후보를 직무 요구사항과 비교한다.

```text
Candidate ↔ Role Requirements
```

이 방식의 한계:

1. 후보의 전체 역량 수는 알 수 있지만, 현재 팀에 새롭게 추가되는 역량은 명확하지 않다.
2. 현재 팀이 이미 보유한 역량과 후보 역량의 중복을 체계적으로 보여주지 않는다.
3. Hiring Manager가 팀의 부족분을 머릿속으로 판단하더라도, 그 판단이 시스템에 명시적으로 표현되지 않는다.
4. LinkedIn과 이력서에 쓰인 지식은 우선 `claim`일 뿐, 인터뷰에서 검증된 지식은 아니다.
5. HR이 각 후보의 결정적인 주장에 맞는 후속 질문을 매번 직접 설계해야 한다.

---

## 4. Solution

WEMESH는 비교 구조를 다음과 같이 바꾼다.

```text
Team Goal Graph
      −
Current Team Knowledge Graph
      =
Team Knowledge Gap

Candidate Knowledge Graph
      ∩
Team Knowledge Gap
      =
Candidate Gap Contribution
```

### Two core questions

1. **Who should HR interview first?**
   - 팀의 Knowledge Gap을 가장 많이 메우는 후보를 우선 추천한다.

2. **What should HR ask?**
   - 후보가 Gap을 메운다고 주장하는 핵심 역량에 대해 구체적인 검증 질문을 생성한다.

---

## 5. Knowledge graph model

### Individual Knowledge Graph

팀원 또는 후보 한 명의 LinkedIn 프로필 텍스트에서 추출한다.

```text
Person
├─ Skills
├─ Tools
├─ Domains
├─ Projects / Experiences
└─ Evidence snippets from the profile
```

모든 추출 노드에는 원문 근거를 연결한다.

```json
{
  "label": "Kafka",
  "type": "skill",
  "status": "claimed",
  "source": "linkedin_text",
  "evidence": "Built a Kafka-based event processing pipeline..."
}
```

### Group Knowledge Graph

팀원들의 Individual Graph를 합쳐 현재 팀의 지식 범위를 만든다.

```text
Individual Graph A
Individual Graph B  ── union ──> Group Knowledge Graph
Individual Graph C
```

### Team Goal Graph

이번 채용으로 팀이 달성해야 하는 구체적인 목표와 필요한 역량이다.

Demo goal:

> **Own payment-platform incidents independently within 90 days.**

### Knowledge Gap

Team Goal에 필요하지만 현재 Group Graph에 없는 역량이다.

---

## 6. Demo data

### Target role graph

Role: **Backend Reliability Engineer**

```text
Python
AWS
PostgreSQL
Payments
Kafka
Distributed Systems
Observability
Incident Response
```

### Current team coverage

합성 LinkedIn 프로필을 가진 팀원 3명을 사용한다.

```text
Covered by current team
✓ Python
✓ AWS
✓ PostgreSQL
✓ Payments
```

### Current team gap

```text
Missing from current team
✗ Kafka
✗ Distributed Systems
✗ Observability
✗ Incident Response
```

### Candidate A — broad but redundant

```text
Python
AWS
PostgreSQL
Payments
Kafka
Docker
```

- Flat role match: **5/8**
- Team gap filled: **1/4**
- Critical outcome: **BLOCKED**

### Candidate B — smaller but gap-completing

Candidate B는 팀원의 실제 LinkedIn 프로필 텍스트를 활용할 수 있다. 실제 프로필이 데모 Gap과 맞지 않으면, 실제 추출 장면만 보여주고 랭킹용 결과는 저장된 demo JSON을 사용한다.

```text
Kafka
Distributed Systems
Observability
Incident Response
```

- Flat role match: **4/8**
- Team gap filled: **4/4**
- Critical outcome: **READY**

### Ranking inversion

| Method | #1 | Reason |
|---|---|---|
| Flat role matching | Candidate A | Matches 5/8 requirements |
| Team Gap Fit | Candidate B | Fills 4/4 missing team capabilities |

Key line:

> **Candidate A looks better alone. Candidate B makes the team complete.**

---

## 7. Matching logic

복잡한 블랙박스 점수 대신 설명 가능한 집합 계산을 사용한다.

```javascript
teamSkills = union(teamMembers.skills)
gapSkills = targetSkills - teamSkills

filledByCandidate = intersection(candidate.skills, gapSkills)
overlapWithTeam = intersection(candidate.skills, teamSkills)
remainingGap = gapSkills - candidate.skills

flatRoleMatch = intersection(candidate.skills, targetSkills).length
teamGapFit = filledByCandidate.length / gapSkills.length
```

### Critical outcome readiness

```javascript
criticalOutcome = {
  name: "Payment Incident Ownership",
  requiredSkills: [
    "Kafka",
    "Distributed Systems",
    "Observability",
    "Incident Response"
  ]
}
```

```text
Candidate A joins → 1/4 covered → BLOCKED
Candidate B joins → 4/4 covered → READY
```

이 데모는 후보 B가 현실에서 반드시 더 좋은 직원이라는 것을 증명하지 않는다. 대신 **채용 전에 선언된 팀 목표를 기준으로 B가 더 큰 증분 기여를 제공한다는 것을 설명 가능하게 보여준다.**

---

## 8. From claimed knowledge to verified knowledge

LinkedIn에서 추출한 역량은 전부 처음에는 `claimed` 상태다.

### Node states

| State | Color | Meaning |
|---|---|---|
| Claimed | Gray | LinkedIn/profile에 작성된 주장 |
| Needs Follow-up | Yellow | 답변의 깊이 또는 개인 소유 범위가 불확실 |
| Verified | Green | 인터뷰에서 구체적인 경험과 근거로 확인 |
| Not Verified | Red | 핵심 질문에 답하지 못했거나 근거가 없음 |

WEMESH는 AI 작성 여부를 판별하지 않는다.

> **We do not detect AI-written answers. We test whether the candidate can explain, defend, and reproduce the claimed knowledge.**

### Example interview questions

Candidate B가 `Kafka Incident Response`를 주장할 때:

1. 직접 겪었던 Kafka consumer lag 장애를 설명해 주세요.
2. 처음 이상을 발견한 정확한 metric은 무엇이었나요?
3. 원인을 어떤 순서로 좁혀갔나요?
4. 본인이 직접 수행한 작업과 팀원이 수행한 작업을 구분해 주세요.
5. 고려했지만 선택하지 않은 해결책은 무엇이며, 왜 제외했나요?
6. 지금 다시 재현한다면 가장 먼저 확인할 세 가지는 무엇인가요?

### Interview output

```text
Potential Gap Fit: 4/4
Interview-Verified Fit: 3/4
Remaining Follow-up: Incident Response
```

최종 판단은 항상 HR과 Hiring Manager가 한다.

---

## 9. MVP screens

### Screen 1 — Candidate Shortlist

- Team goal
- Group Knowledge Graph
- Missing Gap nodes
- Candidate A/B ranking
- Flat Match와 Team Gap Fit 비교
- 추천 이유
- `Recommended for Interview`

### Screen 2 — Interview Mode

- 선택한 후보의 claimed nodes
- 후보가 메우는 team gaps
- `Generate Interview Plan`
- 역량별 targeted questions
- HR용 상태 버튼:
  - Verified
  - Needs Follow-up
  - Not Verified
- Potential Fit과 Interview-Verified Fit 비교

---

## 10. Platform usage

### Forge

Forge에서 다음을 생성하고 기록한다.

- Product Intent
- PRD-Spec
- Architecture
- UI Design
- 구현 가드레일

Forge project name:

```text
WEMESH — Team Knowledge Interview Copilot
```

Presentation line:

> **Forge converted our HR workflow intent into a governed product specification and implementation blueprint.**

Forge 사용 시간 제한: **15–20분**

### Daytona

Forge의 spec을 기반으로 만든 Next.js 앱을 Daytona sandbox에서 실행한다.

```text
Daytona Sandbox
├─ Next.js application
├─ Knowledge graph extraction
├─ Team gap calculation
├─ Candidate ranking
├─ Interview question generation
└─ Preview URL on port 3000
```

Presentation line:

> **Daytona runs the matching and interview engine in an isolated, reproducible sandbox and serves the working demo.**

---

## 11. Technical scope

### Stack

- Next.js
- TypeScript
- Local JSON seed data
- Simple skill dictionary extraction
- React Flow, Cytoscape, or simple SVG graph
- Daytona sandbox / preview URL

### LinkedIn ingestion

- Actual LinkedIn API: **No**
- Scraping: **No**
- Paste LinkedIn profile text: **Yes**
- Optional real owner profile: **Yes, with contact/personal details removed**
- Every extracted node should show its source evidence snippet.

### Backup behavior

- Real profile parsing succeeds → show real extracted graph.
- Parsing or network fails → load cached extraction JSON.
- Graph library fails → show node cards and simple SVG lines.
- Dynamic question generation fails → use deterministic question templates.

---

## 12. Explicitly out of scope

- Login / multi-user accounts
- Database / persistent storage
- LinkedIn API integration or scraping
- Automatic hiring or rejection
- AI-generated-text detector
- Face, emotion, confidence, or voice analysis
- Full interview transcription
- Candidate-facing learning roadmap
- Multiple roles
- More than two demo candidates
- Complex graph algorithms or embedding search
- Production-grade accuracy claims

---

## 13. Three-hour execution plan

### Before 12:00 — Freeze the demo

- Final plan complete
- Forge input prepared
- Demo role, team, Candidate A/B fixed
- No new feature discussion after 12:00

### 12:00–1:00 — Build

#### 12:00–12:20

- Run Forge with Intent + PRD-Spec + Architecture + UI Design
- Save/export Forge outputs and screenshots

#### 12:20–1:00

- Build the two-screen Next.js app
- Add local demo data
- Implement graph merge, gap calculation, candidate ranking
- Implement Candidate Shortlist UI

**1:00 acceptance criterion:**

> `Load Demo` → Group Graph → Knowledge Gap → Candidate B recommended

### 1:00–2:00 — Daytona, Interview Mode, recording

#### 1:00–1:20

- Run app in Daytona
- Obtain preview URL

#### 1:20–1:35

- Implement or finalize Interview Mode
- Add targeted questions and status buttons

#### 1:35–1:45

- Full demo QA
- Verify clean refresh and fallback data

#### 1:45–2:00

- Record at least two complete demo takes

**2:00 acceptance criterion:**

> Working Daytona link + usable recorded demo

### 2:00–3:00 — Slides and submission

- Create three core slides
- Edit/select demo video
- Add Forge and Daytona usage evidence
- Prepare submission description
- Verify all links

### 3:00–3:30 — Submission buffer

- Upload video
- Confirm playback
- Confirm preview URL permissions
- Submit before 3:30

---

## 14. 90-second demo video scenario

### 0–10s — Problem

Visual: multiple polished candidate profiles.

Narration:

> **AI can make every candidate look qualified. HR still needs to know who matters to this team—and what to ask to verify it.**

### 10–25s — Build the team graph

Visual:

- Load three team-member LinkedIn-style profiles.
- Individual graphs merge into one Group Knowledge Graph.
- Four gap nodes appear in red.

Narration:

> **WEMESH combines individual knowledge graphs into one team graph and maps what the team is missing against its 90-day goal.**

### 25–42s — Ranking inversion

Visual:

```text
Flat Role Match
A: 5/8
B: 4/8

Team Gap Fit
A: 1/4
B: 4/4
```

Narration:

> **Candidate A matches more requirements. Candidate B fills the actual team gap.**

### 42–55s — Recommendation reason

Visual:

- Overlay Candidate B on the team graph.
- Four gap nodes become outlined green.
- Show `Potential Fit 4/4` and `Verified 0/4`.

Narration:

> **But these are still claims extracted from a profile—not verified knowledge.**

### 55–75s — Interview Mode

Visual:

- Click `Generate Interview Plan`.
- Show Kafka/incident-response probing questions.
- HR marks one node Verified and one Needs Follow-up.

Narration:

> **WEMESH generates targeted questions for the exact knowledge the team needs, helping HR turn profile claims into interview-verified evidence.**

### 75–85s — Result

Visual:

```text
Potential Gap Fit: 4/4
Interview-Verified Fit: 3/4
Remaining Follow-up: Incident Response
```

Narration:

> **Find who completes the team. Know exactly what to ask.**

### 85–90s — Platform proof

Visual:

```text
Specified with Forge
Running in Daytona
```

---

## 15. PPT-ready slide outline

### Slide 1 — Problem

**Title:** Every candidate looks qualified now.

**Message:**

- AI-polished profiles collapse the signal-to-noise ratio.
- HR must decide who fills this team's actual gap.
- HR also needs the right questions to verify claimed expertise.

### Slide 2 — How WEMESH works

**Title:** Candidate fit is not enough. Measure team completion.

```text
Team Goal − Team Knowledge = Gap
Candidate ∩ Gap = Contribution
```

Visual: Team Graph → red gaps → Candidate overlay.

### Slide 3 — Ranking inversion

**Title:** The candidate with fewer matches can be the better hire for this team.

```text
Candidate A: 5/8 role match, 1/4 team gaps
Candidate B: 4/8 role match, 4/4 team gaps
```

Key line:

> **Candidate A looks better alone. Candidate B makes the team complete.**

### Slide 4 — Human knowledge verification

**Title:** From claimed knowledge to verified knowledge.

- LinkedIn claim → gray
- Needs follow-up → yellow
- Interview verified → green
- Not verified → red

Key line:

> **We do not detect AI-written answers. We verify whether candidates can explain, defend, and reproduce their claimed knowledge.**

### Slide 5 — Platform and enterprise impact

**Title:** Specified with Forge. Running in Daytona.

- Forge: intent, specification, architecture, UI blueprint
- Daytona: isolated runtime, matching engine, live preview
- Enterprise value: faster explainable shortlisting and targeted interviews

---

## 16. Success criteria

The prototype is successful if the demo clearly shows all five moments:

1. LinkedIn profile text becomes an evidence-linked knowledge graph.
2. Individual team graphs merge into a Group Knowledge Graph.
3. Candidate B ranks below A in flat matching but above A in Team Gap Fit.
4. The product explains exactly why Candidate B is recommended.
5. The product generates targeted questions and distinguishes claimed from interview-verified knowledge.

---

## 17. Final messaging

### Primary tagline

> **Find who completes the team. Know exactly what to ask.**

### Product description

> **WEMESH ranks candidates by the knowledge your team is missing, then generates the interview questions HR needs to verify it.**

### AI-era message

> **AI can polish the answer. It cannot replace the depth required to defend it.**

### Closing line

> **From claimed knowledge to verified team capability.**
