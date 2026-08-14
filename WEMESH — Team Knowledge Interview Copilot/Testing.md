# Testing

**Selected Categories:** Functional test cases

**Total Test Cases:** 48


---

## Functional test cases (48)

### FUNCTIONAL-001 — Create Next.js MVP App Shell

- User Story: WO-001
- Objective: Validate functional behavior for "Create Next.js MVP App Shell" against acceptance criteria.
- Expected: Story "Create Next.js MVP App Shell" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: The application is created with Next.js App Router and TypeScript strict mode enabled, and npm scripts exist for development, build, type checking, linting, and testing.
- Check acceptance criterion 2: The root page renders a WEMESH MVP shell with navigation affordances for Candidate Shortlist and Interview Mode placeholders, and includes visible copy that HR remains the final decision-maker.
- Check acceptance criterion 3: Unit tests written and passing: a basic render or component test verifies the shell page and layout render without runtime errors.

### FUNCTIONAL-002 — Establish Quality Automation Baseline

- User Story: WO-002
- Objective: Validate functional behavior for "Establish Quality Automation Baseline" against acceptance criteria.
- Expected: Story "Establish Quality Automation Baseline" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Linting, formatting, type checking, unit testing, and build scripts are available from package.json and return non-zero exit codes on failure.
- Check acceptance criterion 2: The test runner is configured for TypeScript and React or Next.js components, with a committed setup file and at least one passing baseline test.
- Check acceptance criterion 3: Unit tests written and passing: the quality baseline includes a deliberately small test proving the runner, setup, and TypeScript transpilation are functional.

### FUNCTIONAL-003 — Define Shared Domain Schemas

- User Story: WO-003
- Objective: Validate functional behavior for "Define Shared Domain Schemas" against acceptance criteria.
- Expected: Story "Define Shared Domain Schemas" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Zod schemas and inferred TypeScript types exist for all MVP fixture domains needed by candidate intake, evidence-linked claims, team gaps, shortlist ranking, questions, graph data, and interview status.
- Check acceptance criterion 2: Schemas enforce core guardrails including confidence range limits, valid claim status values, required evidence references where applicable, stable entity identifiers, and restricted data classification metadata where relevant.
- Check acceptance criterion 3: Unit tests written and passing: valid and invalid payload tests cover each major schema group, including low-confidence claims and malformed graph links.

### FUNCTIONAL-004 — Configure Daytona Port Runtime

- User Story: WO-004
- Objective: Validate functional behavior for "Configure Daytona Port Runtime" against acceptance criteria.
- Expected: Story "Configure Daytona Port Runtime" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: The development start command binds the Next.js app to port 3000 by default and documents how to override only non-secret operational settings when needed.
- Check acceptance criterion 2: A sandbox runbook or README section explains install, start, validation, reset, and rollback-by-rebuild steps for Daytona demo operators.
- Check acceptance criterion 3: Unit tests written and passing: N/A — this story primarily configures runtime scripts and documentation, with no standalone business logic to unit test.

### FUNCTIONAL-005 — Create Local Demo Fixtures

- User Story: WO-009
- Objective: Validate functional behavior for "Create Local Demo Fixtures" against acceptance criteria.
- Expected: Story "Create Local Demo Fixtures" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Local JSON files exist for candidates, teams, team goals, skills, claims, evidence snippets, questions, and graph relationships, and all files validate against the shared schemas.
- Check acceptance criterion 2: The fixture dataset supports at least one complete scripted demo path with multiple candidates, a team goal, under-covered capabilities, evidence-linked claims, low-confidence warnings, ranking-relevant claims, and targeted questions.
- Check acceptance criterion 3: Unit tests written and passing: fixture validation tests parse every committed JSON file and fail with actionable file-level errors if schema validation fails.

### FUNCTIONAL-006 — Standardize API Response Handling

- User Story: WO-010
- Objective: Validate functional behavior for "Standardize API Response Handling" against acceptance criteria.
- Expected: Story "Standardize API Response Handling" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Shared API helpers produce success responses with data, requestId, and meta.durationMs, and error responses with errors, requestId, and meta.durationMs.
- Check acceptance criterion 2: Centralized error mapping supports expected status codes including 400 for bad input, 403 for missing workflow authorization, 404 for unknown local entities, 409 for invalid state transitions, 422 for unprocessable domain outcomes, and 500 for unexpected failures.
- Check acceptance criterion 3: Unit tests written and passing: response helpers and error mapper tests cover known application errors, Zod validation errors, unexpected exceptions, and redacted logging context.

### FUNCTIONAL-007 — Implement Read-Only Fixture Repositories

- User Story: WO-013
- Objective: Validate functional behavior for "Implement Read-Only Fixture Repositories" against acceptance criteria.
- Expected: Story "Implement Read-Only Fixture Repositories" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Read-only repository interfaces and implementations exist for candidates, teams, goals, skills, claims, evidence, questions, and graph data using local JSON fixtures as the only data source.
- Check acceptance criterion 2: Repository methods return immutable validated data and provide clear not-found behavior for unknown identifiers without exposing raw fixture payloads.
- Check acceptance criterion 3: Unit tests written and passing: repository tests cover successful reads, unknown IDs, invalid fixture load behavior through test doubles, and immutability expectations.

### FUNCTIONAL-008 — Add Health Readiness Endpoint

- User Story: WO-018
- Objective: Validate functional behavior for "Add Health Readiness Endpoint" against acceptance criteria.
- Expected: Story "Add Health Readiness Endpoint" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: A GET health endpoint exists and returns a structured success envelope when the app is running and required local fixtures can be loaded through repositories.
- Check acceptance criterion 2: The health response includes safe operational metadata such as status, app mode, fixture readiness, fixture domain counts, requestId, and meta.durationMs, and excludes restricted candidate profile text, names, and evidence snippets.
- Check acceptance criterion 3: Unit tests written and passing: health readiness logic is tested for healthy fixture state, missing or invalid fixture state through test doubles, and redacted response content.

### FUNCTIONAL-009 — Add Authorized Profile Privacy Notices

- User Story: WO-005
- Objective: Validate functional behavior for "Add Authorized Profile Privacy Notices" against acceptance criteria.
- Expected: Story "Add Authorized Profile Privacy Notices" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: The Candidate Shortlist intake flow displays an authorized-use reminder, a no-scraping and no-platform-API statement, and an explicit acknowledgment control before profile text can be submitted.
- Check acceptance criterion 2: Submitting pasted profile text without the authorization acknowledgment returns a structured forbidden response and the UI shows an actionable message without creating or displaying a candidate analysis artifact.
- Check acceptance criterion 3: All visible intake copy uses manual paste language only and contains no wording that implies LinkedIn scraping, direct import, platform sync, automated hiring, or automated rejection.

### FUNCTIONAL-010 — Display Human Decision Guardrails

- User Story: WO-006
- Objective: Validate functional behavior for "Display Human Decision Guardrails" against acceptance criteria.
- Expected: Story "Display Human Decision Guardrails" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Candidate Shortlist displays a non-dismissive human-review guardrail near ranked results stating that recommendations support review and do not hire or reject candidates automatically.
- Check acceptance criterion 2: Recommendation reason cards avoid final-decision wording and include evidence or gap-trace context so users understand why the system surfaced a candidate without treating rank as an outcome.
- Check acceptance criterion 3: Interview Mode displays guardrail copy explaining that claim statuses are interviewer judgments for verification support, not automated employment decisions.

### FUNCTIONAL-011 — Enforce CSP And Safe Rendering

- User Story: WO-007
- Objective: Validate functional behavior for "Enforce CSP And Safe Rendering" against acceptance criteria.
- Expected: Story "Enforce CSP And Safe Rendering" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: All application pages and relevant API responses include security headers with a restrictive Content Security Policy, X-Content-Type-Options, Referrer-Policy, and frame protection appropriate for the Next.js MVP.
- Check acceptance criterion 2: Pasted profile text, evidence snippets, extracted claims, recommendation reasons, and interview questions are rendered without dangerously setting HTML from user-controlled content.
- Check acceptance criterion 3: A hostile pasted-text fixture containing script tags, event-handler attributes, encoded markup, and malformed HTML is displayed inertly and never executes in Candidate Shortlist or Interview Mode.

### FUNCTIONAL-012 — Capture In-Memory Review Audit Events

- User Story: WO-011
- Objective: Validate functional behavior for "Capture In-Memory Review Audit Events" against acceptance criteria.
- Expected: Story "Capture In-Memory Review Audit Events" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Changing an Interview Mode claim status creates an in-memory audit event containing timestamp, redacted actor label, requestId, resource identifiers, previous status, new status, and operation outcome.
- Check acceptance criterion 2: Submitting shortlist or interview human sign-off creates an in-memory audit event that distinguishes sign-off type, referenced candidate or shortlist resources, and sanitized decision-support context without hire or reject language.
- Check acceptance criterion 3: Audit events are retrievable through a demo-safe API or operator panel for the current process lifetime and are cleared when the server process restarts or an explicit sandbox reset action is invoked.

### FUNCTIONAL-013 — Implement Redacted Structured Logging

- User Story: WO-014
- Objective: Validate functional behavior for "Implement Redacted Structured Logging" against acceptance criteria.
- Expected: Story "Implement Redacted Structured Logging" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Every API route under /api/v1 and the health endpoint emits a structured log event with requestId, operation, status, durationMs, and redacted actor context for success and failure paths.
- Check acceptance criterion 2: Log output never contains raw pasted profile text, candidate names, evidence snippets, full interview notes, authorization payloads, stack traces, or user-controlled HTML content.
- Check acceptance criterion 3: Extraction, ranking, question generation, status update, sign-off, and feedback operations include safe count-based metadata when available, such as claimCount, lowConfidenceClaimCount, questionCount, or excludedClaimCount.

### FUNCTIONAL-014 — Document Sandbox Retention Reset SOP

- User Story: WO-016
- Objective: Validate functional behavior for "Document Sandbox Retention Reset SOP" against acceptance criteria.
- Expected: Story "Document Sandbox Retention Reset SOP" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: A repository runbook documents approved beta usage, Restricted data handling, prohibited external integrations, no-auth sandbox exposure risks, and the requirement to use only approved demo data or candidate-authorized pasted profile text.
- Check acceptance criterion 2: The runbook includes step-by-step Daytona startup, session operation, reset, restart, and post-reset verification procedures for the app running on port 3000.
- Check acceptance criterion 3: The runbook explicitly states that local JSON fixtures are demo data, mutable interview and audit state is in memory, and sandbox restart or reset clears volatile session data but does not provide production-grade retention compliance.

### FUNCTIONAL-015 — Validate Authorized Profile Intake API

- User Story: WO-015
- Objective: Validate functional behavior for "Validate Authorized Profile Intake API" against acceptance criteria.
- Expected: Story "Validate Authorized Profile Intake API" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Submitting a valid JSON request with authorizationAcknowledged set to true and profileText between the configured minimum and maximum lengths returns HTTP 200 with a structured JSON envelope containing data, errors, requestId, and meta.durationMs.
- Check acceptance criterion 2: Submitting a request without authorizationAcknowledged set to true returns HTTP 403 with an actionable error code and no extraction artifact is created or returned.
- Check acceptance criterion 3: Submitting empty, whitespace-only, too-short, oversized, or malformed profile text returns HTTP 400 with an actionable validation message and no raw profile text in the response.

### FUNCTIONAL-016 — Extract Deterministic Candidate Claims

- User Story: WO-019
- Objective: Validate functional behavior for "Extract Deterministic Candidate Claims" against acceptance criteria.
- Expected: Story "Extract Deterministic Candidate Claims" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Given a validated profile fixture containing known skills, roles, projects, and date ranges, the extraction service returns deterministic structured claims with stable claim IDs, normalized labels, categories, and source-derived text references.
- Check acceptance criterion 2: Repeated extraction of the same normalized profile text returns equivalent claims in a stable order without network calls, timers, random IDs, or environment-dependent behavior.
- Check acceptance criterion 3: The extraction service is framework-independent and can be invoked from unit tests without constructing a Next.js Request or Response object.

### FUNCTIONAL-017 — Build Authorized Paste Intake UI

- User Story: WO-021
- Objective: Validate functional behavior for "Build Authorized Paste Intake UI" against acceptance criteria.
- Expected: Story "Build Authorized Paste Intake UI" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: The intake UI displays a paste text area, mandatory authorization acknowledgment checkbox, authorized-use reminder, no-scraping guidance, and submit action in the Candidate Shortlist workflow.
- Check acceptance criterion 2: The submit action is disabled until the acknowledgment is checked and the pasted text meets the configured minimum client-side length hint.
- Check acceptance criterion 3: Submitting valid authorized text calls the versioned extraction API and displays a loading state followed by a successful extraction summary containing counts for claims, supported claims, and low-confidence claims.

### FUNCTIONAL-018 — Link Claims To Evidence Snippets

- User Story: WO-022
- Objective: Validate functional behavior for "Link Claims To Evidence Snippets" against acceptance criteria.
- Expected: Story "Link Claims To Evidence Snippets" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Each claim with source support includes at least one evidence object containing evidence ID, claim ID, snippet text, startOffset, endOffset, and sourceSection when the section can be identified.
- Check acceptance criterion 2: Evidence offsets are validated against the normalized profile text so slicing the text from startOffset to endOffset reproduces the evidence snippet or a documented normalized equivalent.
- Check acceptance criterion 3: Claims that cannot be tied to a concrete snippet remain in the response but are marked with an empty evidence reference list and an unsupported warning-ready signal.

### FUNCTIONAL-019 — Gate Claims By Confidence

- User Story: WO-024
- Objective: Validate functional behavior for "Gate Claims By Confidence" against acceptance criteria.
- Expected: Story "Gate Claims By Confidence" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Supported claims receive deterministic confidence values based on extraction signals and evidence quality, and unsupported claims receive confidence below 0.60 by default.
- Check acceptance criterion 2: Every claim in the extraction response includes confidence, confidenceLabel, rankingEligible, questionEligible, reviewRequired, and warningCodes fields.
- Check acceptance criterion 3: Claims with confidence below 0.60 or supportStatus set to UNSUPPORTED have rankingEligible false and questionEligible false unless a later human review capability explicitly changes eligibility.

### FUNCTIONAL-020 — Display Evidence Linked Claims

- User Story: WO-025
- Objective: Validate functional behavior for "Display Evidence Linked Claims" against acceptance criteria.
- Expected: Story "Display Evidence Linked Claims" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: After a successful extraction result, the UI renders every claim returned by the API with label, category, support status, confidence label, and eligibility indicators.
- Check acceptance criterion 2: Supported claims display their evidence snippets and source offset or source section references in a way recruiters can inspect without viewing the full raw pasted profile text.
- Check acceptance criterion 3: Unsupported or low-confidence claims display prominent non-color-only warning text and are clearly marked as requiring human review before ranking or question influence.

### FUNCTIONAL-021 — Enable Human Claim Review

- User Story: WO-027
- Objective: Validate functional behavior for "Enable Human Claim Review" against acceptance criteria.
- Expected: Story "Enable Human Claim Review" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: The claims UI provides an explicit review action for claims marked reviewRequired, with clear copy that review enables downstream consideration but does not verify or approve the candidate.
- Check acceptance criterion 2: A reviewed claim updates in session state with reviewedBy set to a redacted demo actor label, reviewedAt timestamp, reviewStatus, and updated rankingEligible and questionEligible values when policy allows.
- Check acceptance criterion 3: A low-confidence or unsupported claim cannot become eligible through implicit UI rendering, page load, or client-only state changes; the server-side review update path must apply the transition.

### FUNCTIONAL-022 — Define Team Graph Data Contracts

- User Story: WO-020
- Objective: Validate functional behavior for "Define Team Graph Data Contracts" against acceptance criteria.
- Expected: Story "Define Team Graph Data Contracts" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Unit tests are written and passing for schema validation, duplicate identifier detection, missing reference detection, and confidence eligibility rules across all graph-related fixture entities.
- Check acceptance criterion 2: System integration tests validate that the fixture loader and health/readiness boundary fail closed with structured errors when required local JSON data is missing or invalid.
- Check acceptance criterion 3: Mock data and fixtures are generated and committed for at least one team, one goal, multiple team members, skills, candidate claims, evidence snippets, and graph relationships without requiring external services.

### FUNCTIONAL-023 — Compute Team Goal Capability Gaps

- User Story: WO-026
- Objective: Validate functional behavior for "Compute Team Goal Capability Gaps" against acceptance criteria.
- Expected: Story "Compute Team Goal Capability Gaps" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Unit tests are written and passing for full coverage, partial coverage, no coverage, unknown goal, duplicate team skill evidence, and priority ordering scenarios.
- Check acceptance criterion 2: System integration tests validate the gap service through the fixture repository boundary using committed local demo data and no external dependencies.
- Check acceptance criterion 3: Mock data and fixtures are generated and committed to demonstrate at least one high-priority missing capability, one under-covered capability, and one already-covered capability.

### FUNCTIONAL-024 — Assemble Evidence Linked Knowledge Graph

- User Story: WO-028
- Objective: Validate functional behavior for "Assemble Evidence Linked Knowledge Graph" against acceptance criteria.
- Expected: Story "Assemble Evidence Linked Knowledge Graph" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Unit tests are written and passing for node normalization, edge normalization, evidence-link preservation, missing relationship handling, and low-confidence claim eligibility labeling.
- Check acceptance criterion 2: System integration tests validate graph assembly across fixture loader and gap service boundaries using committed local demo data.
- Check acceptance criterion 3: Mock data and fixtures are generated and committed so the graph includes team-to-goal, goal-to-skill, team-member-to-skill, candidate-to-claim, claim-to-evidence, and candidate-to-gap relationships.

### FUNCTIONAL-025 — Expose Gap And Graph APIs

- User Story: WO-031
- Objective: Validate functional behavior for "Expose Gap And Graph APIs" against acceptance criteria.
- Expected: Story "Expose Gap And Graph APIs" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Unit tests are written and passing for request validation, response mapping, structured error mapping, and service dependency injection at the route boundary.
- Check acceptance criterion 2: System integration tests validate successful and failing calls to the gap and graph endpoints using local fixture data and the real Next.js route handlers.
- Check acceptance criterion 3: Mock data and fixtures are generated and committed so API tests cover at least one valid team-goal scenario, one unknown goal, one unknown team, and one invalid request shape.

### FUNCTIONAL-026 — Add Team Goal Gap Panel

- User Story: WO-032
- Objective: Validate functional behavior for "Add Team Goal Gap Panel" against acceptance criteria.
- Expected: Story "Add Team Goal Gap Panel" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Unit tests are written and passing for the goal selector, gap panel rendering, severity label rendering, empty state rendering, loading state rendering, and error state rendering.
- Check acceptance criterion 2: System integration tests validate that selecting a team goal calls the gap API boundary and renders the returned prioritized gaps in the Candidate Shortlist workflow.
- Check acceptance criterion 3: Mock data and fixtures are generated and committed for selected goal, no selected goal, no gaps, API error, and under-covered capability scenarios.

### FUNCTIONAL-027 — Render Resilient Knowledge Graph

- User Story: WO-036
- Objective: Validate functional behavior for "Render Resilient Knowledge Graph" against acceptance criteria.
- Expected: Story "Render Resilient Knowledge Graph" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Unit tests are written and passing for graph panel state handling, fallback rendering, selected node details, graph data mapping, and error boundary behavior.
- Check acceptance criterion 2: System integration tests validate that the graph panel fetches graph data through the API boundary and renders either the Cytoscape visualization or the fallback list without SSR failures.
- Check acceptance criterion 3: Mock data and fixtures are generated and committed for normal graph rendering, empty graph, graph API error, browser visualization failure, and dense demo graph scenarios.

### FUNCTIONAL-028 — Configure Explainable Ranking Weights

- User Story: WO-023
- Objective: Validate functional behavior for "Configure Explainable Ranking Weights" against acceptance criteria.
- Expected: Story "Configure Explainable Ranking Weights" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: A typed ranking weight profile exists for team-gap relevance, evidence strength, confidence, recency, and priority coverage, and the total weighting is validated before scoring can run.
- Check acceptance criterion 2: Invalid weight profiles, including missing required keys, negative values, non-numeric values, and totals outside the accepted tolerance, return a structured validation failure without falling back to unsafe defaults.
- Check acceptance criterion 3: Unit tests are written and passing for valid profiles, malformed profiles, boundary totals, and default profile loading behavior.

### FUNCTIONAL-029 — Compute Team-Gap Fit Scores

- User Story: WO-029
- Objective: Validate functional behavior for "Compute Team-Gap Fit Scores" against acceptance criteria.
- Expected: Story "Compute Team-Gap Fit Scores" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Given a selected team goal and candidate set, the scoring service returns candidates ordered by descending team-gap fit score with deterministic tie handling.
- Check acceptance criterion 2: Low-confidence, unsupported, or unreviewed claims are visible in the response as excluded inputs and do not contribute to score calculations.
- Check acceptance criterion 3: Candidates that fill no selected team gap receive a safe low or zero score and an explicit no-gap-coverage indicator rather than being forced into a misleading recommendation.

### FUNCTIONAL-030 — Expose Evidence-Backed Ranking Reasons

- User Story: WO-033
- Objective: Validate functional behavior for "Expose Evidence-Backed Ranking Reasons" against acceptance criteria.
- Expected: Story "Expose Evidence-Backed Ranking Reasons" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Every recommendation reason for a scored candidate includes candidate ID, gap ID, claim ID, evidence ID or explicit unfilled-gap indicator, confidence, and a short human-readable rationale.
- Check acceptance criterion 2: A candidate result with no covered priority gaps includes an explicit unfilled or no-coverage reason instead of an empty explanation array.
- Check acceptance criterion 3: Reasons are derived only from eligible scoring inputs, and ineligible low-confidence claims appear only in exclusion rationale, not as positive recommendation reasons.

### FUNCTIONAL-031 — Render Ranked Shortlist Cards

- User Story: WO-037
- Objective: Validate functional behavior for "Render Ranked Shortlist Cards" against acceptance criteria.
- Expected: Story "Render Ranked Shortlist Cards" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: The Candidate Shortlist view renders candidates in the exact rank order returned by the shortlist service and displays score, rank, covered gaps, and reason summaries for each card.
- Check acceptance criterion 2: Each card provides an accessible way to inspect evidence-linked reason details without rendering raw HTML from candidate-provided text.
- Check acceptance criterion 3: Unfilled priority gaps are visible in the shortlist view when no candidate covers them, and the UI does not hide weak coverage scenarios.

### FUNCTIONAL-032 — Gate Low-Confidence Claim Influence

- User Story: WO-040
- Objective: Validate functional behavior for "Gate Low-Confidence Claim Influence" against acceptance criteria.
- Expected: Story "Gate Low-Confidence Claim Influence" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Low-confidence, unsupported, or unreviewed claims appear with warning badges and explanatory text that does not rely on color alone.
- Check acceptance criterion 2: Excluded claims are not included in positive score contributions or recommendation reasons until a user performs an explicit review action.
- Check acceptance criterion 3: A review action updates in-memory eligibility state for the current demo session and causes subsequent shortlist scoring to include the reviewed claim only when all required evidence references are present.

### FUNCTIONAL-033 — Capture Shortlist Human Sign-Off

- User Story: WO-041
- Objective: Validate functional behavior for "Capture Shortlist Human Sign-Off" against acceptance criteria.
- Expected: Story "Capture Shortlist Human Sign-Off" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: The Candidate Shortlist view provides an explicit human sign-off control with acknowledgment copy confirming the user reviewed ranking reasons, exclusions, and warnings.
- Check acceptance criterion 2: Submitting sign-off records shortlist session ID or context hash, actor label, timestamp, selected team goal, candidate result identifiers, and acknowledgment version in in-memory state.
- Check acceptance criterion 3: The UI shows signed and unsigned states distinctly and does not display ready-for-interview completion language until sign-off succeeds.

### FUNCTIONAL-034 — Collect Shortlist Usefulness Feedback

- User Story: WO-043
- Objective: Validate functional behavior for "Collect Shortlist Usefulness Feedback" against acceptance criteria.
- Expected: Story "Collect Shortlist Usefulness Feedback" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: After shortlist sign-off succeeds, the UI presents a feedback form with a required usefulness rating and optional comment using safe length limits.
- Check acceptance criterion 2: Feedback submissions record recommendation context reference, selected team goal, rating, optional comment, timestamp, and actor label in in-memory state without storing candidate profile text or evidence snippets.
- Check acceptance criterion 3: Feedback cannot be submitted for an unsigned shortlist context, and the user receives a clear message that sign-off is required first.

### FUNCTIONAL-035 — Manage Interview Claim Status

- User Story: WO-017
- Objective: Validate functional behavior for "Manage Interview Claim Status" against acceptance criteria.
- Expected: Story "Manage Interview Claim Status" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Given an interview session for a candidate with known claims, when a valid status update is submitted, then the in-memory session state stores the new status, updated timestamp, redacted actor label, and claim identifier.
- Check acceptance criterion 2: Given an invalid status value, unknown candidate, unknown claim, or claim that does not belong to the selected candidate, when a status update is attempted, then the service rejects it with a typed validation or domain error.
- Check acceptance criterion 3: Given multiple claim statuses in one session, when the session summary is requested, then it returns counts by status and identifies unresolved high-priority claims without making hiring recommendations.

### FUNCTIONAL-036 — Generate Traceable Interview Questions

- User Story: WO-030
- Objective: Validate functional behavior for "Generate Traceable Interview Questions" against acceptance criteria.
- Expected: Story "Generate Traceable Interview Questions" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Given supported or human-reviewed claims with evidence and matching team gaps, when the question generation service runs, then it returns at least one targeted verification question per eligible high-relevance claim with claim ID, evidence ID, gap ID, confidence, question type, and rationale.
- Check acceptance criterion 2: Given low-confidence or unsupported claims that have not been reviewed by a human, when the question generation service runs, then those claims remain visible in an excluded claims collection and no generated question is created from them.
- Check acceptance criterion 3: Given a claim with missing evidence, missing team gap mapping, or invalid seniority context, when the service evaluates it, then it produces a structured warning instead of silently generating an untraceable question.

### FUNCTIONAL-037 — Expose Questions API Contract

- User Story: WO-034
- Objective: Validate functional behavior for "Expose Questions API Contract" against acceptance criteria.
- Expected: Story "Expose Questions API Contract" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Given a valid request with known candidate ID, team goal ID, reviewed claim IDs, and seniority context, when the client posts to the questions endpoint, then the response uses the standard data, errors, requestId, and meta.durationMs envelope and includes traceable generated questions.
- Check acceptance criterion 2: Given malformed JSON, missing required fields, unknown candidate IDs, unknown claim IDs, or unknown team goal IDs, when the endpoint is called, then it returns the appropriate structured 400 or 404 response without stack traces or sensitive payload content.
- Check acceptance criterion 3: Given a request that includes unreviewed low-confidence claims, when the endpoint evaluates eligibility, then those claims are excluded from question generation and returned as warnings rather than influencing prompts.

### FUNCTIONAL-038 — Show Questions In Shortlist

- User Story: WO-042
- Objective: Validate functional behavior for "Show Questions In Shortlist" against acceptance criteria.
- Expected: Story "Show Questions In Shortlist" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Given a shortlisted candidate with eligible claims and a selected team goal, when the recruiter opens the candidate detail area, then targeted questions are fetched from the questions API and displayed with claim, evidence, gap, priority, and rationale context.
- Check acceptance criterion 2: Given the questions API returns excluded low-confidence claims, when questions are displayed, then the UI shows non-color-only warnings explaining that those claims require human review before they can influence prompts.
- Check acceptance criterion 3: Given the questions API returns no eligible questions, when the candidate detail area renders, then the UI shows an actionable empty state that allows the recruiter to continue reviewing evidence without implying a candidate should be rejected.

### FUNCTIONAL-039 — Build Interview Mode Workspace

- User Story: WO-044
- Objective: Validate functional behavior for "Build Interview Mode Workspace" against acceptance criteria.
- Expected: Story "Build Interview Mode Workspace" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Given a shortlisted candidate with generated questions, when the operator opens Interview Mode, then the workspace displays candidate context, claim-linked questions, evidence references, team gap relevance, and current claim status controls.
- Check acceptance criterion 2: Given the operator changes a claim status to Claimed, Needs Follow-up, Verified, or Not Verified, when the update succeeds, then the UI reflects the new status and refreshes summary counts without requiring a page reload.
- Check acceptance criterion 3: Given a low-confidence or excluded claim appears in interview context, when the workspace renders, then it shows a warning and does not present that claim as a generated prompt source unless it has been human-reviewed.

### FUNCTIONAL-040 — Flag Unresolved Priority Claims

- User Story: WO-045
- Objective: Validate functional behavior for "Flag Unresolved Priority Claims" against acceptance criteria.
- Expected: Story "Flag Unresolved Priority Claims" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Given an interview session with high-priority claim mappings, when one or more high-priority claims are Claimed or Needs Follow-up, then Interview Mode displays an unresolved priority prompt with claim labels, gap context, and recommended follow-up action text.
- Check acceptance criterion 2: Given all high-priority claims are Verified or Not Verified, when the summary refreshes, then the unresolved priority prompt is hidden and the session summary indicates no high-priority follow-ups remain.
- Check acceptance criterion 3: Given a claim has no high-priority team gap mapping, when it remains Claimed or Needs Follow-up, then it can appear in general summary counts but does not trigger the priority follow-up prompt.

### FUNCTIONAL-041 — Capture Interview Human Signoff

- User Story: WO-046
- Objective: Validate functional behavior for "Capture Interview Human Signoff" against acceptance criteria.
- Expected: Story "Capture Interview Human Signoff" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Given an interview session summary is visible, when the operator confirms required acknowledgements and signs off, then the in-memory session stores sign-off metadata and the UI shows the session as human-reviewed.
- Check acceptance criterion 2: Given unresolved high-priority claims remain, when the operator attempts sign-off, then the UI requires an explicit unresolved-follow-up acknowledgement before sign-off can succeed.
- Check acceptance criterion 3: Given required acknowledgement fields are missing, when sign-off is submitted, then the application returns or displays a structured validation error and does not mark the session complete.

### FUNCTIONAL-042 — Add deterministic CI quality gates

- User Story: WO-008
- Objective: Validate functional behavior for "Add deterministic CI quality gates" against acceptance criteria.
- Expected: Story "Add deterministic CI quality gates" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: A GitHub Actions workflow runs on pull_request and main branch push events and fails if dependency installation, linting, TypeScript checking, automated tests, or production build fail.
- Check acceptance criterion 2: The workflow uses npm ci or the repository equivalent lockfile-safe install command and does not require real secrets, external LinkedIn integrations, databases, or production infrastructure.
- Check acceptance criterion 3: Unit tests written and passing: N/A — this story wires existing and newly available unit test commands into CI rather than adding domain logic.

### FUNCTIONAL-043 — Automate dependency risk scanning

- User Story: WO-012
- Objective: Validate functional behavior for "Automate dependency risk scanning" against acceptance criteria.
- Expected: Story "Automate dependency risk scanning" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: A dependency update automation configuration is committed for the Node.js package ecosystem and, when supported, GitHub Actions workflow dependencies.
- Check acceptance criterion 2: A vulnerability scan runs on a scheduled basis or as part of CI and fails or reports according to an explicitly documented severity threshold appropriate for the MVP demo.
- Check acceptance criterion 3: Unit tests written and passing: N/A — this story adds dependency automation and security scanning configuration rather than new executable business logic.

### FUNCTIONAL-044 — Backfill domain service unit tests

- User Story: WO-035
- Objective: Validate functional behavior for "Backfill domain service unit tests" against acceptance criteria.
- Expected: Story "Backfill domain service unit tests" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Unit tests written and passing for profile text validation, evidence-linked claim extraction, low-confidence claim handling, team-gap analysis, ranking eligibility, question generation traceability, and interview status transitions where those modules exist.
- Check acceptance criterion 2: System integration tests validating service/API boundaries: N/A — this story targets pure domain unit coverage; API boundary validation is covered by the dedicated contract-test workstream.
- Check acceptance criterion 3: Mock data/fixtures generated and committed for supported claims, unsupported claims, low-confidence claims, unfilled team gaps, ranking inversion, and interview status transitions.

### FUNCTIONAL-045 — Validate internal API contracts

- User Story: WO-038
- Objective: Validate functional behavior for "Validate internal API contracts" against acceptance criteria.
- Expected: Story "Validate internal API contracts" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Contract tests validate successful and failure responses for extraction, graph, shortlist, questions, interview status, and health endpoints where implemented.
- Check acceptance criterion 2: Unit tests written and passing: N/A — this story targets HTTP/API contract behavior; pure business logic coverage is handled by the domain unit-test workstream.
- Check acceptance criterion 3: System integration tests validating service/API boundaries are written and passing using the Next.js route handlers or an in-process test server without external network dependencies.

### FUNCTIONAL-046 — Instrument redacted demo telemetry

- User Story: WO-039
- Objective: Validate functional behavior for "Instrument redacted demo telemetry" against acceptance criteria.
- Expected: Story "Instrument redacted demo telemetry" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: Structured logs are emitted for key API operations including extraction, graph retrieval, shortlist scoring, question generation, interview status updates, sign-off if implemented, feedback if implemented, and health checks.
- Check acceptance criterion 2: Logs include requestId, operation, result status, durationMs, redacted actor label, and relevant aggregate counts while excluding raw pasted profile text, evidence snippets, candidate names, and full candidate identifiers.
- Check acceptance criterion 3: Unit tests written and passing for log redaction helpers, request identifier generation or propagation, and duration metadata behavior where implemented as reusable utilities.

### FUNCTIONAL-047 — Automate scripted demo smoke test

- User Story: WO-047
- Objective: Validate functional behavior for "Automate scripted demo smoke test" against acceptance criteria.
- Expected: Story "Automate scripted demo smoke test" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: A Playwright smoke test runs against a local Next.js server on port 3000 and completes the scripted MVP workflow in under 90 seconds on CI for the committed deterministic fixture scenario.
- Check acceptance criterion 2: Unit tests written and passing: N/A — this story adds browser-level end-to-end validation rather than new pure business logic.
- Check acceptance criterion 3: System integration tests validating service/API boundaries are written and passing by exercising the real browser, Next.js routes, domain services, and local JSON fixtures together.

### FUNCTIONAL-048 — Publish Daytona demo runbook

- User Story: WO-048
- Objective: Validate functional behavior for "Publish Daytona demo runbook" against acceptance criteria.
- Expected: Story "Publish Daytona demo runbook" satisfies expected functional validation outcomes without critical issues.

**Steps**
- Check acceptance criterion 1: A committed runbook documents fresh Daytona setup, dependency installation, application startup on port 3000, health verification, smoke-test execution, fixture reset, and recovery from common demo failures.
- Check acceptance criterion 2: Unit tests written and passing: N/A — this story is operational documentation and does not add executable application logic.
- Check acceptance criterion 3: System integration tests validating service/API boundaries: N/A — the runbook references the automated integration and smoke-test commands created by other workstreams rather than implementing new tests.