# Intent profile

**Status:** complete

**Artifact:** `2d87cda6-5271-44b9-a5c6-b0550ebaaf9c`

## Vision

WEMESH is a Team Knowledge Interview Copilot that helps HR match candidates’ personally verifiable knowledge against fast-changing team knowledge gaps, then generate targeted interview verification workflows while keeping humans as final decision-makers.

## Target personas

- Recruiter: Screens many applicants for fast-changing technical teams; wants fast shortlist prioritization, evidence-linked candidate claims, and targeted questions; struggles with polished AI-assisted profiles, unclear candidate knowledge ownership, and time pressure.
- Hiring Manager: Evaluates whether candidates fill current team capability gaps; wants team-goal-aligned ranking, knowledge gap visibility, and claim verification support; struggles with static job descriptions, moving team priorities, and weak signals from resumes.
- HR Interview Operator: Uses Interview Mode during candidate conversations; wants to mark claims as Claimed, Needs Follow-up, Verified, or Not Verified; struggles with tracking claim status manually and turning profile claims into specific verification prompts.

## Core features

- **Authorized LinkedIn Profile Paste and Evidence-Linked Knowledge Graph Extraction** (priority 1)
- **Group Knowledge Graph from Team Member Profiles** (priority 2)
- **Team Goal Knowledge Gap Discovery** (priority 3)
- **Team Gap Fit Candidate Ranking** (priority 4)
- **Targeted Interview Question Generation** (priority 5)
- **Interview Mode Claim Status Management** (priority 6)
- **Candidate Shortlist View** (priority 7)

## Technical constraints

- Use Next.js.
- Use TypeScript.
- Implement two views: Candidate Shortlist and Interview Mode.
- No authentication.
- No database.
- Use local JSON demo data.
- Use LinkedIn profile text paste only.
- Do not scrape LinkedIn.
- Do not use the LinkedIn API.
- Do not include an AI-generated-text detector.
- Do not automatically hire candidates.
- Do not automatically reject candidates.
- HR must remain the final decision-maker.
- The app must run in a Daytona sandbox on port 3000.
- The MVP demo must demonstrate profile-to-graph extraction, team-gap discovery, ranking inversion, recommendation reasons, and targeted interview questions in under 90 seconds.

## Confidence

Overall: **91%**

> The input provides a strong product concept, concrete MVP flow, clear demo constraints, and detailed feature behavior.

| Section | Score | Why | How to Improve |
| --- | --- | --- | --- |
| Vision | 95% | The product problem, core insight, and intended outcome are clearly described. | Add 2-3 measurable product success metrics beyond the 90-second demo, such as recruiter time saved or claim verification accuracy. |
| Target personas | 86% | Recruiters and hiring managers are explicit, with HR interview operator behavior inferable from the Interview Mode workflow. | Define whether candidates, HR admins, or technical interviewers will directly interact with the product in later versions. |
| Core features | 94% | The workflow, MVP scenario, status values, ranking inversion, and success criteria are specific and verifiable. | Specify the scoring formula or weighting for Team Gap Fit versus flat role match. |
| Technical constraints | 96% | The technology stack, demo data approach, exclusions, deployment port, and decision-making boundaries are explicitly stated. | Choose the graph visualization library and clarify whether profile extraction is deterministic mock logic or LLM-backed. |
