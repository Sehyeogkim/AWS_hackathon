## Next.js MVP Foundation and Local Data Contracts

### [P0] Create Next.js MVP App Shell

Create the initial Next.js TypeScript application shell for WEMESH so the MVP has a reliable runtime foundation for the Candidate Shortlist and Interview Mode workflows. This change creates the app entry points, shared layout, base styling, package scripts, TypeScript configuration, and the first placeholder routes needed to prove the sandbox can boot consistently. The affected files include the project package manifest, Next.js configuration, TypeScript configuration, app router layout and page files, global styles, and baseline source directory structure. When complete, a developer or demo operator can install dependencies, start the app locally, and see a branded WEMESH landing surface that clearly states the MVP is human decision support and not an automated hiring system. This story does not implement profile extraction, ranking, question generation, persistence, authentication, LinkedIn scraping, or any production hosting beyond the local app foundation. It depends only on the selected Next.js and TypeScript runtime capability and establishes the base capability that later schema, fixture, API, and operational health work build on.

| Field | Value |
|---|---|
| Story Points | 3 |
| Hours | 30h |
| Priority | P0 |
| Labels | epic:foundation, nextjs, typescript, runtime, complexity:medium |

**Acceptance Criteria**
- The application is created with Next.js App Router and TypeScript strict mode enabled, and npm scripts exist for development, build, type checking, linting, and testing.
- The root page renders a WEMESH MVP shell with navigation affordances for Candidate Shortlist and Interview Mode placeholders, and includes visible copy that HR remains the final decision-maker.
- Unit tests written and passing: a basic render or component test verifies the shell page and layout render without runtime errors.
- System integration tests written and passing: a build or smoke test verifies the Next.js application starts and serves the root route successfully.
- Mock data and fixtures: N/A — domain fixtures are introduced in the dedicated local demo data story, and this story only establishes the runnable shell.

### [P0] Establish Quality Automation Baseline

Add the baseline engineering automation needed to keep the greenfield MVP operable, reviewable, and safe to change as domain contracts and APIs are introduced. This change configures linting, formatting, unit testing, test environment setup, and optional smoke-test wiring so platform and application engineers can catch type, style, and regression failures before demo runs. The affected files include ESLint configuration, test runner configuration, setup files, package scripts, and an initial CI workflow if the repository supports GitHub Actions. When complete, contributors can run one command sequence that validates type safety, lint rules, unit tests, and build readiness without external services or secrets. This story does not implement feature logic, fixture content, API routes, deployment infrastructure, or production monitoring. It depends on a runnable Next.js TypeScript app capability and provides the verification backbone that later schemas, repositories, and routes must use.

| Field | Value |
|---|---|
| Story Points | 3 |
| Hours | 30h |
| Priority | P0 |
| Labels | epic:foundation, automation, ci, testing, complexity:medium |

**Acceptance Criteria**
- Linting, formatting, type checking, unit testing, and build scripts are available from package.json and return non-zero exit codes on failure.
- The test runner is configured for TypeScript and React or Next.js components, with a committed setup file and at least one passing baseline test.
- Unit tests written and passing: the quality baseline includes a deliberately small test proving the runner, setup, and TypeScript transpilation are functional.
- System integration tests written and passing: the automated validation sequence runs type checking, linting, tests, and Next.js build as a single local quality gate.
- Mock data and fixtures: N/A — this story validates tooling only, while committed domain fixtures are created in the local demo data story.

**Depends on:** WO-001

### [P0] Define Shared Domain Schemas

Create the shared TypeScript and Zod contract layer that will govern local fixtures, API payloads, and downstream domain services for WEMESH. This change defines validated models for candidates, profile pastes, claims, evidence snippets, skills, teams, goals, gaps, ranking reasons, graph nodes and links, interview questions, interview statuses, sign-off records, and standardized API envelopes. The affected files include schema modules, inferred TypeScript type exports, schema test files, and shared constants for confidence thresholds and allowed status values. When complete, malformed local data or untrusted request payloads can be rejected at clear boundaries before they contaminate ranking, question generation, or graph rendering. This story does not implement the extraction algorithm, ranking formula, UI workflows, repository file loading, or API route handlers. It depends on the app and test harness capability and creates the typed foundation that fixture, repository, and API work must consume.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:foundation, zod, contracts, type-safety, complexity:medium |

**Acceptance Criteria**
- Zod schemas and inferred TypeScript types exist for all MVP fixture domains needed by candidate intake, evidence-linked claims, team gaps, shortlist ranking, questions, graph data, and interview status.
- Schemas enforce core guardrails including confidence range limits, valid claim status values, required evidence references where applicable, stable entity identifiers, and restricted data classification metadata where relevant.
- Unit tests written and passing: valid and invalid payload tests cover each major schema group, including low-confidence claims and malformed graph links.
- System integration tests written and passing: a contract test verifies that representative cross-domain objects can be composed into a graph-ready and API-ready structure without type or validation failures.
- Mock data and fixtures generated and committed: small schema test fixtures are committed under the test fixtures area so validation runs without external dependencies.

**Depends on:** WO-001

### [P0] Configure Daytona Port Runtime

Configure the MVP runtime so WEMESH starts predictably in a Daytona sandbox on port 3000 with no secrets, no database, and no external platform dependencies. This change adds port-aware scripts, documented environment defaults, a lightweight operator runbook, and any container or dev environment metadata needed to recreate the demo quickly after sandbox failure. The affected files include package scripts, environment example files, README or runbook documentation, and optional Docker or devcontainer configuration if appropriate for the repository. When complete, a demo operator can install dependencies, start the app on the required port, verify the root route is reachable, and recover by rebuilding the sandbox rather than debugging snowflake state. This story does not implement production hosting, managed infrastructure, authentication, certificate automation, persistent storage, or external CI/CD deployment. It depends on the runnable app shell capability and supports later health checks and demo smoke tests.

| Field | Value |
|---|---|
| Story Points | 2 |
| Hours | 20h |
| Priority | P0 |
| Labels | epic:foundation, daytona, runtime, runbook, complexity:low |

**Acceptance Criteria**
- The development start command binds the Next.js app to port 3000 by default and documents how to override only non-secret operational settings when needed.
- A sandbox runbook or README section explains install, start, validation, reset, and rollback-by-rebuild steps for Daytona demo operators.
- Unit tests written and passing: N/A — this story primarily configures runtime scripts and documentation, with no standalone business logic to unit test.
- System integration tests written and passing: a smoke command or documented validation step starts the app on port 3000 and verifies the root route responds successfully.
- Mock data and fixtures: N/A — domain fixture content is created in the local demo data story, while this story only controls runtime execution.

**Depends on:** WO-001

### [P0] Create Local Demo Fixtures

Create the local JSON demo dataset that will serve as the canonical MVP data source for teams, goals, candidates, skills, claims, evidence, questions, and graph relationships. This change gives the demo deterministic input data so Candidate Shortlist, team-gap discovery, ranking inversion, recommendation reasons, and Interview Mode can later run without a database or external integrations. The affected files include data directory JSON files, fixture validation tests, and any fixture index metadata needed for loaders. When complete, the repository contains realistic but synthetic demo data for at least the scripted MVP scenario, including supported and low-confidence claims that demonstrate the human review gate. This story does not implement extraction logic, scoring logic, UI rendering, API endpoints, or mutable interview state. It depends on shared schema capability so every committed fixture can be validated in automation before it is used by downstream services.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:foundation, fixtures, local-json, demo-data, complexity:medium |

**Acceptance Criteria**
- Local JSON files exist for candidates, teams, team goals, skills, claims, evidence snippets, questions, and graph relationships, and all files validate against the shared schemas.
- The fixture dataset supports at least one complete scripted demo path with multiple candidates, a team goal, under-covered capabilities, evidence-linked claims, low-confidence warnings, ranking-relevant claims, and targeted questions.
- Unit tests written and passing: fixture validation tests parse every committed JSON file and fail with actionable file-level errors if schema validation fails.
- System integration tests written and passing: a cross-fixture integrity test verifies references among candidates, claims, evidence, skills, goals, questions, and graph links resolve successfully.
- Mock data and fixtures generated and committed: all MVP demo data is committed as local synthetic JSON and requires no database, LinkedIn API, scraping, or external service.

**Depends on:** WO-003

### [P0] Standardize API Response Handling

Create the shared API response envelope, request ID handling, validation helpers, and centralized error mapper for internal Next.js API routes. This change ensures every future endpoint can return consistent structured JSON with duration metadata, actionable errors, proper HTTP status codes, and no unsafe stack traces or restricted candidate data leakage. The affected files include API utility modules, typed application error classes, logger helpers, validation wrappers, and tests for success and failure mapping. When complete, route authors can wrap domain service results in the same response format and fail closed for malformed input, missing authorization acknowledgment, unknown local IDs, invalid status transitions, and unexpected server errors. This story does not create feature endpoints for extraction, shortlist ranking, questions, feedback, or interview status. It depends on shared schema capability and the automated test baseline, and it provides the API boundary contract that health and later feature routes will use.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:foundation, api, error-handling, observability, complexity:medium |

**Acceptance Criteria**
- Shared API helpers produce success responses with data, requestId, and meta.durationMs, and error responses with errors, requestId, and meta.durationMs.
- Centralized error mapping supports expected status codes including 400 for bad input, 403 for missing workflow authorization, 404 for unknown local entities, 409 for invalid state transitions, 422 for unprocessable domain outcomes, and 500 for unexpected failures.
- Unit tests written and passing: response helpers and error mapper tests cover known application errors, Zod validation errors, unexpected exceptions, and redacted logging context.
- System integration tests written and passing: a test-only or minimal route handler exercise verifies the helpers emit the correct JSON envelope and HTTP status through the Next.js route boundary.
- Mock data and fixtures generated and committed: API utility tests include local request and error fixtures that run without external services.

**Depends on:** WO-002, WO-003

### [P0] Implement Read-Only Fixture Repositories

Implement read-only repository adapters that load and validate local JSON fixtures behind stable TypeScript interfaces so future domain services do not import raw files directly. This change improves reliability by centralizing fixture parsing, caching, immutability, and redacted error handling while preserving the no-database MVP constraint. The affected files include repository interfaces, JSON loader utilities, fixture-specific adapters, dependency injection exports, and repository tests. When complete, downstream extraction, graph, team-gap, ranking, question, and health capabilities can request validated domain data through a clean boundary instead of coupling to file paths. This story does not implement business scoring, question generation, mutable interview sessions, database persistence, or external data access. It depends on the shared schemas and committed local fixtures being available and valid.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:foundation, repository, local-json, dependency-injection, complexity:medium |

**Acceptance Criteria**
- Read-only repository interfaces and implementations exist for candidates, teams, goals, skills, claims, evidence, questions, and graph data using local JSON fixtures as the only data source.
- Repository methods return immutable validated data and provide clear not-found behavior for unknown identifiers without exposing raw fixture payloads.
- Unit tests written and passing: repository tests cover successful reads, unknown IDs, invalid fixture load behavior through test doubles, and immutability expectations.
- System integration tests written and passing: a repository composition test loads the full committed fixture dataset and verifies cross-domain queries needed by future graph and shortlist services.
- Mock data and fixtures generated and committed: repository tests use committed synthetic fixtures and targeted test fixtures without external dependencies.

**Depends on:** WO-003, WO-009

### [P0] Add Health Readiness Endpoint

Add an operational health and readiness endpoint that verifies the single-process MVP runtime is alive, fixture-backed data access is usable, and core configuration is sane for the Daytona demo. This change gives demo operators, CI smoke tests, and future route owners a fast diagnostic path before running the under-90-second workflow. The affected files include a Next.js API route for health, repository readiness checks, response-envelope usage, health tests, and runbook updates that explain expected results and remediation steps. When complete, a request to the health endpoint returns structured JSON with status, request ID, duration, app mode, fixture readiness, and safe counts while avoiding raw candidate names, evidence snippets, or pasted text. This story does not implement external monitoring, alerting platforms, production SLO dashboards, authentication, durable audit storage, or feature-specific extraction and ranking endpoints. It depends on local repositories, standardized API responses, and the configured port runtime being available.

| Field | Value |
|---|---|
| Story Points | 3 |
| Hours | 30h |
| Priority | P0 |
| Labels | epic:foundation, healthcheck, operability, readiness, complexity:medium |

**Acceptance Criteria**
- A GET health endpoint exists and returns a structured success envelope when the app is running and required local fixtures can be loaded through repositories.
- The health response includes safe operational metadata such as status, app mode, fixture readiness, fixture domain counts, requestId, and meta.durationMs, and excludes restricted candidate profile text, names, and evidence snippets.
- Unit tests written and passing: health readiness logic is tested for healthy fixture state, missing or invalid fixture state through test doubles, and redacted response content.
- System integration tests written and passing: an endpoint test calls the health route through the Next.js API boundary and verifies success and failure response envelopes and status codes.
- Mock data and fixtures generated and committed: health tests use committed synthetic fixtures and controlled invalid fixture doubles without external dependencies.

**Depends on:** WO-013, WO-010, WO-004

---

## Privacy Compliance and Responsible Decision Guardrails

### [P0] Add Authorized Profile Privacy Notices

Implement clear privacy and authorized-use notices wherever a recruiter can submit or review pasted profile text so users understand that only candidate-authorized LinkedIn profile text is permitted and that the product does not scrape or call external profile APIs. This change affects the Candidate Shortlist intake form, candidate analysis entry points, shared notice components, and any local demo copy fixtures that explain the workflow. When complete, users must see an authorization acknowledgment before processing, blocked submissions must explain the required consent signal, and the UI must consistently direct users back to manual paste instead of import or scraping language. This story does not implement authentication, signed consent storage, production legal policy management, LinkedIn integration, or durable retention automation. It depends on the existing profile intake capability, server-side intake validation, and safe text rendering patterns so the notice is not merely client-side decoration.

| Field | Value |
|---|---|
| Story Points | 3 |
| Hours | 30h |
| Priority | P0 |
| Labels | privacy, compliance, candidate-intake, complexity:medium |

**Acceptance Criteria**
- The Candidate Shortlist intake flow displays an authorized-use reminder, a no-scraping and no-platform-API statement, and an explicit acknowledgment control before profile text can be submitted.
- Submitting pasted profile text without the authorization acknowledgment returns a structured forbidden response and the UI shows an actionable message without creating or displaying a candidate analysis artifact.
- All visible intake copy uses manual paste language only and contains no wording that implies LinkedIn scraping, direct import, platform sync, automated hiring, or automated rejection.
- Unit tests written and passing for the intake validation behavior that requires authorization acknowledgment before analysis can proceed.
- System integration tests written and passing for the browser-to-API intake boundary, including authorized submission success and missing-acknowledgment rejection.
- Mock data and fixtures committed for authorized and unauthorized intake scenarios, including representative pasted text that contains no real candidate PII.

**Depends on:** WO-001

### [P0] Display Human Decision Guardrails

Add consistent guardrail copy and review gates wherever rankings, recommendation reasons, generated questions, claim statuses, or sign-off actions could be mistaken for automated hiring decisions. This change affects the Candidate Shortlist ranking display, recommendation reason cards, targeted question generation surfaces, Interview Mode headers, claim status controls, sign-off dialogs, and shared compliance copy. When complete, users see that WEMESH is decision support only, rankings are explainable prompts for human review, and the product never automatically hires or rejects candidates. This story does not change the scoring formula, generate new questions, implement legal approvals, add authentication, or create final hiring disposition workflows. It depends on shortlist ranking, question generation, interview status management, and sign-off capability so the guardrails appear at the points where users act on recommendations.

| Field | Value |
|---|---|
| Story Points | 3 |
| Hours | 30h |
| Priority | P0 |
| Labels | responsible-ai, human-review, ux-guardrails, compliance, complexity:medium |

**Acceptance Criteria**
- Candidate Shortlist displays a non-dismissive human-review guardrail near ranked results stating that recommendations support review and do not hire or reject candidates automatically.
- Recommendation reason cards avoid final-decision wording and include evidence or gap-trace context so users understand why the system surfaced a candidate without treating rank as an outcome.
- Interview Mode displays guardrail copy explaining that claim statuses are interviewer judgments for verification support, not automated employment decisions.
- Shortlist and interview sign-off actions require an explicit human acknowledgment before summaries can be marked complete in the UI.
- Unit tests written and passing for shared guardrail copy rendering and sign-off acknowledgment state where component logic applies.
- System integration tests written and passing for shortlist and Interview Mode flows verifying guardrail visibility and absence of automated hire or reject language.
- Mock data and fixtures committed or updated for ranking and interview scenarios that exercise guardrail displays without external dependencies.

**Depends on:** WO-001

### [P0] Enforce CSP And Safe Rendering

Add global browser security headers and safe-rendering utilities so untrusted pasted profile text, extracted evidence, and generated recruiting artifacts cannot execute script or unsafe markup in the demo application. This change affects Next.js middleware or configuration, shared text display components, evidence panels, candidate claim displays, shortlist reason rendering, and Interview Mode question or status surfaces. When complete, responses include a restrictive Content Security Policy, user-provided text is rendered as text rather than HTML, and hostile profile input displays harmlessly with clear validation behavior. This story does not add authentication, web application firewall rules, external vulnerability scanning services, or production network controls. It depends on the application shell and route structure being available so headers apply consistently across both primary views and API boundaries.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | security, xss, privacy, platform-hardening, complexity:medium |

**Acceptance Criteria**
- All application pages and relevant API responses include security headers with a restrictive Content Security Policy, X-Content-Type-Options, Referrer-Policy, and frame protection appropriate for the Next.js MVP.
- Pasted profile text, evidence snippets, extracted claims, recommendation reasons, and interview questions are rendered without dangerously setting HTML from user-controlled content.
- A hostile pasted-text fixture containing script tags, event-handler attributes, encoded markup, and malformed HTML is displayed inertly and never executes in Candidate Shortlist or Interview Mode.
- Unit tests written and passing for sanitization or text-normalization helpers and safe display components.
- System integration tests written and passing that verify CSP headers are present and that hostile content remains escaped during an end-to-end intake and review flow.
- Mock data and fixtures committed for hostile pasted profile text, hostile evidence snippets, and benign profile text so tests run without external dependencies.

**Depends on:** WO-001, WO-002

### [P1] Capture In-Memory Review Audit Events

Implement an MVP-scoped in-memory audit event service for human review actions so status changes and sign-off moments are visible, inspectable, and correlated during controlled demos without adding a database. This change affects Interview Mode claim status updates, shortlist and interview sign-off actions, feedback or review gates, API response metadata, and any operational audit panel or downloadable audit snapshot used by demo operators. When complete, every claim status transition and human sign-off action records actor label, timestamp, resource type, resource ID, previous value, new value, request ID, and sanitized metadata in volatile memory. This story does not provide immutable production audit retention, one-year storage, database persistence, user identity, or enterprise compliance exports. It depends on redacted structured logging and existing human review or sign-off capabilities so audit events can be captured without duplicating sensitive content.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P1 |
| Labels | audit, compliance, interview-mode, in-memory-state, complexity:medium |

**Acceptance Criteria**
- Changing an Interview Mode claim status creates an in-memory audit event containing timestamp, redacted actor label, requestId, resource identifiers, previous status, new status, and operation outcome.
- Submitting shortlist or interview human sign-off creates an in-memory audit event that distinguishes sign-off type, referenced candidate or shortlist resources, and sanitized decision-support context without hire or reject language.
- Audit events are retrievable through a demo-safe API or operator panel for the current process lifetime and are cleared when the server process restarts or an explicit sandbox reset action is invoked.
- Audit events never store raw pasted profile text, evidence snippets, candidate names, full interview notes, or unrestricted recommendation text.
- Unit tests written and passing for audit event creation, status transition capture, sign-off capture, redaction, and reset behavior.
- System integration tests written and passing across API boundaries for status update and sign-off flows, verifying response requestId correlation with captured audit events.
- Mock data and fixtures committed for claim status transitions, shortlist sign-off, interview sign-off, and redaction sentinel values.

**Depends on:** WO-003

### [P0] Implement Redacted Structured Logging

Add a shared structured logging layer for API and domain operations so engineers can troubleshoot demo reliability without exposing candidate profile text, evidence snippets, names, or other restricted recruiting data. This change affects Next.js API route handlers, request ID generation, error mapping, and domain-service instrumentation for extraction, shortlist ranking, question generation, interview status updates, sign-off, feedback, and health checks. When complete, every significant API operation emits operational metadata such as operation name, request ID, result status, duration, claim counts, low-confidence counts, and a redacted actor label while never logging raw payloads. This story does not implement external log shipping, SIEM integration, immutable one-year audit retention, production identity attribution, or database-backed audit storage. It depends on the API response convention and route boundary capability so logs can be correlated with user-visible request identifiers.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | observability, privacy, logging, sre, complexity:medium |

**Acceptance Criteria**
- Every API route under /api/v1 and the health endpoint emits a structured log event with requestId, operation, status, durationMs, and redacted actor context for success and failure paths.
- Log output never contains raw pasted profile text, candidate names, evidence snippets, full interview notes, authorization payloads, stack traces, or user-controlled HTML content.
- Extraction, ranking, question generation, status update, sign-off, and feedback operations include safe count-based metadata when available, such as claimCount, lowConfidenceClaimCount, questionCount, or excludedClaimCount.
- Unit tests written and passing for the redaction helper, logger wrapper, and representative error serialization paths.
- System integration tests written and passing that invoke representative API routes and assert logs are emitted with request correlation while sensitive fixture values are absent.
- Mock data and fixtures committed with sentinel sensitive strings specifically designed to fail tests if raw candidate text or evidence leaks to logs.

**Depends on:** WO-010

### [P1] Document Sandbox Retention Reset SOP

Create an operator-facing retention and sandbox reset standard operating procedure so DevOps, SRE, and demo operators can safely run controlled beta sessions despite the MVP having no authentication, no database, and volatile in-memory state. This change affects repository documentation, demo runbooks, README setup guidance, and any in-app operator link or compliance notice that points users to cleanup expectations after processing authorized pasted profile text. When complete, operators can follow a repeatable checklist to limit sandbox sharing, use approved demo or authorized pasted text, avoid persistent PII, reset in-memory state, restart the Daytona process, and verify cleanup through health or audit endpoints. This story does not implement production retention automation, cryptographic erasure, durable audit retention, RBAC, network allow-listing, or infrastructure provisioning. It depends on redacted logging, in-memory audit visibility, and human decision guardrails so the SOP accurately describes implemented controls and their limitations.

| Field | Value |
|---|---|
| Story Points | 2 |
| Hours | 20h |
| Priority | P1 |
| Labels | runbook, retention, sandbox-operations, compliance, complexity:low |

**Acceptance Criteria**
- A repository runbook documents approved beta usage, Restricted data handling, prohibited external integrations, no-auth sandbox exposure risks, and the requirement to use only approved demo data or candidate-authorized pasted profile text.
- The runbook includes step-by-step Daytona startup, session operation, reset, restart, and post-reset verification procedures for the app running on port 3000.
- The runbook explicitly states that local JSON fixtures are demo data, mutable interview and audit state is in memory, and sandbox restart or reset clears volatile session data but does not provide production-grade retention compliance.
- The README or demo operator guide links to the retention and reset SOP so it is discoverable before running a beta or demo session.
- Unit tests: N/A — this is a documentation and operational procedure story with no production code logic required.
- System integration tests: N/A — reset API behavior is validated in the audit capture story; this story verifies documented operator steps against available controls.
- Mock data and fixtures: N/A — the SOP references existing approved demo fixtures and does not require new executable test data.

**Depends on:** WO-004, WO-011

---

## Authorized Profile Intake and Evidence-Linked Claim Extraction

### [P0] Validate Authorized Profile Intake API

Implement a server-side intake endpoint that accepts only candidate-authorized pasted profile text, validates the request shape, sanitizes hostile input, enforces demo-safe length limits, and returns structured errors that recruiters can act on. This change is needed because candidate profile text is Restricted data and the product must block unauthorized or unusable intake before any downstream extraction, ranking, or interview workflow can be influenced. The affected areas are the Next.js API route layer, shared TypeScript request and response schemas, validation helpers, redacted structured logging, and API contract tests. When complete, a recruiter submission with an authorization acknowledgment and valid text receives a normalized response suitable for extraction, while missing authorization, empty text, too-short text, oversized payloads, and malformed JSON fail closed with consistent status codes. This story does not include claim extraction logic, evidence linking, confidence scoring, UI form work, database persistence, authentication, LinkedIn scraping, or LinkedIn API integration. It depends on the application having a Next.js API runtime, a shared error-response convention, and privacy-safe logging utilities or the ability to add them in the same code path.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:authorized-profile-intake, type:api, security:input-validation, privacy:restricted-data, complexity:medium |

**Acceptance Criteria**
- Submitting a valid JSON request with authorizationAcknowledged set to true and profileText between the configured minimum and maximum lengths returns HTTP 200 with a structured JSON envelope containing data, errors, requestId, and meta.durationMs.
- Submitting a request without authorizationAcknowledged set to true returns HTTP 403 with an actionable error code and no extraction artifact is created or returned.
- Submitting empty, whitespace-only, too-short, oversized, or malformed profile text returns HTTP 400 with an actionable validation message and no raw profile text in the response.
- Input containing script tags, HTML markup, control characters, or unusual Unicode whitespace is normalized or rejected safely, and no raw HTML is rendered or echoed by the API.
- Structured logs for successful and failed intake include operation name, request ID, duration, status, and redacted counts only; logs do not include candidate names, raw pasted text, or evidence snippets.
- Unit tests are written and passing for schema validation, authorization enforcement, length boundaries, normalization, and redaction behavior.
- System integration tests are written and passing for the API route using valid requests, missing authorization, invalid payloads, and oversized payloads.
- Mock data and fixtures are generated and committed for valid profile text, short profile text, malicious markup, and oversized payload scenarios so tests run without external dependencies.

**Depends on:** WO-010, WO-005, WO-007

### [P0] Extract Deterministic Candidate Claims

Build a pure TypeScript extraction service that converts validated pasted profile text into structured candidate claims using deterministic, fixture-backed rules rather than external AI services. This change is needed so the MVP can reliably demonstrate profile-to-claim extraction within the 90-second demo budget while preserving explainability and avoiding third-party dependencies. The affected areas are the extraction domain module, shared claim and skill types, local skill taxonomy fixtures, API dependency injection wiring, and unit tests for repeatable parsing behavior. When complete, the same accepted profile text always produces the same set of skill, project, role, date, and ownership-style claims with stable identifiers suitable for evidence linking. This story does not include UI rendering, confidence scoring thresholds, human review actions, team-gap ranking, question generation, database persistence, scraping, or LinkedIn API usage. It depends on validated and sanitized profile text being available from the intake capability and on shared TypeScript contracts for API-safe claim objects.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:authorized-profile-intake, type:domain-service, deterministic-extraction, privacy:restricted-data, complexity:medium |

**Acceptance Criteria**
- Given a validated profile fixture containing known skills, roles, projects, and date ranges, the extraction service returns deterministic structured claims with stable claim IDs, normalized labels, categories, and source-derived text references.
- Repeated extraction of the same normalized profile text returns equivalent claims in a stable order without network calls, timers, random IDs, or environment-dependent behavior.
- The extraction service is framework-independent and can be invoked from unit tests without constructing a Next.js Request or Response object.
- The extraction service does not call external APIs, does not use LinkedIn scraping, does not use LinkedIn API clients, and does not require secrets or credentials.
- The API route integrates the extraction service behind the validated intake path and returns extracted claims in the versioned JSON envelope for valid requests.
- Unit tests are written and passing for skill extraction, project phrase extraction, role or seniority extraction, date recognition, duplicate suppression, and deterministic ordering.
- System integration tests are written and passing for the intake-to-extraction route boundary with representative valid profile fixtures.
- Mock data and fixtures are generated and committed for at least three profile styles, including technical leadership, hands-on engineering, and ambiguous generic experience.

**Depends on:** WO-003, WO-009, WO-013

### [P0] Build Authorized Paste Intake UI

Create the recruiter-facing paste intake experience that requires an authorization acknowledgment before profile text can be submitted for analysis. This change is needed so the MVP provides a visible consent-centered workflow and prevents recruiters from accidentally processing unauthorized or incomplete LinkedIn profile text. The affected areas are the Candidate Shortlist page or intake section, profile paste form component, client-side validation, API client wrapper, accessibility-focused error rendering, and UI tests. When complete, a recruiter can paste authorized profile text, see clear privacy and no-scraping guidance, submit only after checking the acknowledgment, and receive inline validation or extraction status without a page reload. This story does not include claim card rendering, human review actions, ranking display, question generation, authentication, localStorage persistence, LinkedIn scraping, or LinkedIn API integration. It depends on a server-side intake and extraction API that enforces authorization, validation, evidence linking, and confidence metadata so the UI can display reliable results.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:authorized-profile-intake, type:ui, accessibility, privacy:restricted-data, complexity:medium |

**Acceptance Criteria**
- The intake UI displays a paste text area, mandatory authorization acknowledgment checkbox, authorized-use reminder, no-scraping guidance, and submit action in the Candidate Shortlist workflow.
- The submit action is disabled until the acknowledgment is checked and the pasted text meets the configured minimum client-side length hint.
- Submitting valid authorized text calls the versioned extraction API and displays a loading state followed by a successful extraction summary containing counts for claims, supported claims, and low-confidence claims.
- Server-side validation errors from the API are displayed inline with actionable messages and do not expose raw pasted profile text in the UI error area.
- The form is accessible by keyboard, has labels for controls, exposes validation messages through accessible semantics, and does not rely on color alone for required or error states.
- Unit tests are written and passing for form validation, disabled submit behavior, acknowledgment requirement, API client success handling, and API client error handling.
- System integration tests are written and passing for the browser intake flow from paste to extraction summary using mocked or test-server API responses.
- Mock data and fixtures are generated and committed for valid extraction success, missing authorization error, too-short text error, and low-confidence summary responses.

**Depends on:** WO-005, WO-015

### [P0] Link Claims To Evidence Snippets

Enhance extracted candidate claims with evidence snippets, source offsets, and provenance metadata so recruiters can see exactly which pasted text supports each claim. This change is needed because WEMESH must make candidate self-representation transparent and prevent downstream shortlist or interview workflows from relying on unsupported assertions. The affected areas are the evidence-linking domain module, claim and evidence shared types, extraction service enrichment path, API response contract, local fixtures, and tests for offset correctness. When complete, each supported claim includes at least one evidence reference with snippet text, start and end character offsets, and a clear relationship back to the original normalized profile text; unsupported claims remain visible with an explicit absence of evidence. This story does not include confidence scoring policy, human review promotion, UI evidence rendering, ranking formulas, question generation, database storage, or audit persistence. It depends on deterministic claims being extracted from validated text and on source text normalization producing stable positions.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:authorized-profile-intake, type:domain-service, evidence-linking, traceability, complexity:medium |

**Acceptance Criteria**
- Each claim with source support includes at least one evidence object containing evidence ID, claim ID, snippet text, startOffset, endOffset, and sourceSection when the section can be identified.
- Evidence offsets are validated against the normalized profile text so slicing the text from startOffset to endOffset reproduces the evidence snippet or a documented normalized equivalent.
- Claims that cannot be tied to a concrete snippet remain in the response but are marked with an empty evidence reference list and an unsupported warning-ready signal.
- Evidence snippet text is concise enough for UI display and does not exceed the configured maximum snippet length unless the source sentence itself is shorter.
- The API response includes evidence objects in a stable deterministic order and every evidence ID is unique within the extraction result.
- Unit tests are written and passing for evidence span discovery, offset validation, snippet trimming, unsupported claim handling, and duplicate evidence suppression.
- System integration tests are written and passing for the extraction API returning claims linked to evidence for representative profile fixtures.
- Mock data and fixtures are generated and committed for supported claims, duplicate skill mentions, claims with no direct support, and multi-line evidence snippets.

**Depends on:** WO-019

### [P0] Gate Claims By Confidence

Add confidence scoring and ranking eligibility metadata to evidence-linked claims so unsupported or ambiguous candidate statements remain visible but cannot influence shortlist ranking or interview prompts until explicitly reviewed by a human. This change is needed to reduce over-trust in polished profiles and enforce the product rule that low-confidence claims require review before downstream influence. The affected areas are the confidence domain module, claim contracts, extraction response enrichment, downstream eligibility contract helpers, fixtures, and tests for threshold behavior. When complete, supported claims receive deterministic confidence values, unsupported claims default below the low-confidence threshold, and every claim exposes rankingEligible and questionEligible fields with warning metadata that other services can enforce. This story does not include the actual ranking formula, question generation logic, UI warning rendering, human review action implementation, database persistence, or durable audit trails. It depends on deterministic claims being linked to evidence snippets and on shared claim status fields being available to downstream modules.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:authorized-profile-intake, type:domain-service, confidence-gating, human-review-gate, complexity:medium |

**Acceptance Criteria**
- Supported claims receive deterministic confidence values based on extraction signals and evidence quality, and unsupported claims receive confidence below 0.60 by default.
- Every claim in the extraction response includes confidence, confidenceLabel, rankingEligible, questionEligible, reviewRequired, and warningCodes fields.
- Claims with confidence below 0.60 or supportStatus set to UNSUPPORTED have rankingEligible false and questionEligible false unless a later human review capability explicitly changes eligibility.
- Eligibility helper functions are exported for downstream ranking and question modules so those modules do not reimplement confidence threshold logic.
- No claim is removed solely because it is low confidence; the API returns it with clear metadata for human review.
- Unit tests are written and passing for confidence calculation, threshold boundaries, unsupported claim defaults, eligibility helper behavior, and deterministic scoring.
- System integration tests are written and passing for the extraction API returning low-confidence warnings and false eligibility for ambiguous or unsupported fixture claims.
- Mock data and fixtures are generated and committed for high-confidence supported claims, medium-confidence partial evidence claims, and low-confidence unsupported claims.

**Depends on:** WO-022

### [P0] Display Evidence Linked Claims

Implement the extracted-claims display so recruiters can inspect each candidate claim alongside supporting evidence, confidence indicators, and warning states. This change is needed because the product value depends on making claims reviewable rather than presenting opaque profile summaries or unsupported ranking signals. The affected areas are the claims list component, evidence snippet component, confidence badge component, extraction result state wiring, accessibility semantics, fixture responses, and UI tests. When complete, successful profile extraction shows grouped claims with evidence snippets, source references, confidence labels, ranking and question eligibility, and clear low-confidence or unsupported warnings that do not rely on color alone. This story does not include the paste form itself, human review state changes, shortlist scoring, targeted question generation, database storage, authentication, or graph visualization. It depends on the intake UI receiving extraction responses that already include evidence-linked claims and confidence gating metadata.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:authorized-profile-intake, type:ui, evidence-review, accessibility, complexity:medium |

**Acceptance Criteria**
- After a successful extraction result, the UI renders every claim returned by the API with label, category, support status, confidence label, and eligibility indicators.
- Supported claims display their evidence snippets and source offset or source section references in a way recruiters can inspect without viewing the full raw pasted profile text.
- Unsupported or low-confidence claims display prominent non-color-only warning text and are clearly marked as requiring human review before ranking or question influence.
- Claims are grouped or ordered consistently by category and confidence so repeated demo runs produce stable visual output.
- The UI handles an extraction result with zero reliable claims by showing an actionable empty state instead of a blank panel or broken component.
- Unit tests are written and passing for claim grouping, confidence badge rendering, evidence snippet rendering, unsupported warning rendering, and empty state behavior.
- System integration tests are written and passing for the paste-to-claims display flow using committed extraction result fixtures.
- Mock data and fixtures are generated and committed for supported claims, unsupported claims, mixed confidence claims, multi-evidence claims, and no reliable claims.

**Depends on:** WO-024, WO-021

### [P0] Enable Human Claim Review

Implement an explicit human review action for extracted claims so a recruiter can acknowledge low-confidence or unsupported claims before they become eligible for downstream ranking or interview-question workflows. This change is needed because WEMESH must preserve human decision-making and prevent weak claims from silently influencing shortlist or interview outputs. The affected areas are the claim review state model, in-memory review service, API route for review updates, claims display controls, eligibility update logic, redacted mutation logging, and tests for safe state transitions. When complete, low-confidence claims remain in a review-required state until a user explicitly reviews them, after which the session state records the review decision and eligible downstream consumers can see the updated eligibility without a database. This story does not include durable audit retention, authentication, production RBAC, shortlist scoring implementation, question generation implementation, automatic hiring or rejection, or candidate-facing workflows. It depends on claims being displayed with confidence and eligibility metadata and on downstream components consuming eligibility fields rather than recalculating or bypassing review state.

| Field | Value |
|---|---|
| Story Points | 8 |
| Hours | 80h |
| Priority | P0 |
| Labels | epic:authorized-profile-intake, type:api, type:ui, human-review-gate, privacy:restricted-data, complexity:high |

**Acceptance Criteria**
- The claims UI provides an explicit review action for claims marked reviewRequired, with clear copy that review enables downstream consideration but does not verify or approve the candidate.
- A reviewed claim updates in session state with reviewedBy set to a redacted demo actor label, reviewedAt timestamp, reviewStatus, and updated rankingEligible and questionEligible values when policy allows.
- A low-confidence or unsupported claim cannot become eligible through implicit UI rendering, page load, or client-only state changes; the server-side review update path must apply the transition.
- The review update API rejects unknown claim IDs, missing review decisions, invalid eligibility transitions, and malformed requests with structured actionable errors.
- Redacted mutation logs include operation, request ID, claim ID, review status, timestamp, and result without raw profile text, evidence snippets, or candidate names.
- Unit tests are written and passing for review transition rules, eligibility promotion behavior, invalid transition rejection, and in-memory state updates.
- System integration tests are written and passing for the claims UI calling the review API and for downstream eligibility metadata changing only after explicit review.
- Mock data and fixtures are generated and committed for review-required claims, already eligible claims, invalid claim IDs, and reviewed claim session state.

**Depends on:** WO-011, WO-025

---

## Team Knowledge Graph and Goal Gap Discovery

### [P0] Define Team Graph Data Contracts

Implement strict TypeScript and runtime schemas for the local team knowledge graph data so gap discovery and graph assembly have a reliable, validated source of truth. This change is needed because the MVP has no database and depends on local JSON demo data, so fixture drift would otherwise create broken graphs, misleading gaps, or privacy-risking error output during a live demo. The affected areas are the local data fixtures, shared domain types, schema validation utilities, fixture loader, health-readiness checks, and tests around invalid demo data. When complete, the app can load teams, team members, goals, skills, claims, evidence snippets, gaps, and graph relationships deterministically, while rejecting malformed or internally inconsistent fixture data with safe structured diagnostics. This story does not include the gap computation algorithm, candidate ranking, question generation, graph visualization, persistent storage, authentication, or any external LinkedIn integration. It depends on the application already having a Next.js and TypeScript runtime, local JSON as the canonical data source, and a shared structured API error pattern available for reuse.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:team-knowledge-graph, area:data-contracts, area:fixtures, area:operability, complexity:medium |

**Acceptance Criteria**
- Unit tests are written and passing for schema validation, duplicate identifier detection, missing reference detection, and confidence eligibility rules across all graph-related fixture entities.
- System integration tests validate that the fixture loader and health/readiness boundary fail closed with structured errors when required local JSON data is missing or invalid.
- Mock data and fixtures are generated and committed for at least one team, one goal, multiple team members, skills, candidate claims, evidence snippets, and graph relationships without requiring external services.
- Invalid fixtures never cause raw candidate profile text, evidence snippet content, candidate names, stack traces, or filesystem internals to appear in user-facing errors or structured logs.
- All schema and type definitions compile under TypeScript strict mode without using broad untyped escape hatches for untrusted fixture input.

**Depends on:** WO-003, WO-009, WO-013

### [P0] Compute Team Goal Capability Gaps

Build a pure team gap analysis service that compares a selected team goal against validated team member capabilities and returns prioritized missing or under-covered capabilities. This is necessary so hiring managers can see which candidate skills actually matter for the current team objective instead of reviewing generic role keywords or static job descriptions. The affected components are the domain service layer, fixture repository interfaces, gap output types, test fixtures, and any shared scoring constants used for severity and coverage labels. When complete, the service returns deterministic gap records that include goal ID, required capability, current coverage, severity, priority, supporting team member evidence, and whether the gap remains unfilled. This story does not include candidate shortlist ranking, interview question generation, API route exposure, UI rendering, Cytoscape visualization, or persistent storage. It depends on validated local fixture contracts and a fixture loader that can provide typed teams, team members, goals, skills, claims, and evidence references.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:team-knowledge-graph, area:gap-analysis, area:domain-service, area:reliability, complexity:medium |

**Acceptance Criteria**
- Unit tests are written and passing for full coverage, partial coverage, no coverage, unknown goal, duplicate team skill evidence, and priority ordering scenarios.
- System integration tests validate the gap service through the fixture repository boundary using committed local demo data and no external dependencies.
- Mock data and fixtures are generated and committed to demonstrate at least one high-priority missing capability, one under-covered capability, and one already-covered capability.
- The service returns stable, explainable gap records with severity labels and coverage counts that can be consumed by later API and UI layers without additional business logic.
- Low-confidence or unsupported candidate claims are not used to reduce team gaps in this service unless the input explicitly represents a human-reviewed eligible capability.

**Depends on:** WO-024, WO-020

### [P0] Assemble Evidence Linked Knowledge Graph

Create a graph assembly service that turns validated fixture data and computed team gaps into a normalized node-and-edge model connecting teams, goals, skills, team members, candidates, claims, evidence, and unfilled gaps. This is needed because the knowledge graph must be an explainability layer showing why a capability is missing, which claims relate to it, and what evidence supports those relationships. The affected areas are the domain graph service, graph view-model types, fixture repository interfaces, gap service integration, and graph-focused tests. When complete, downstream APIs and UI components can consume a single graph structure with stable IDs, typed node categories, typed relationship categories, evidence references, confidence metadata, and blocked eligibility indicators. This story does not include API route implementation, Cytoscape rendering, candidate ranking, targeted question generation, or interview status mutation. It depends on validated fixture contracts and a team-goal gap computation capability that returns typed prioritized gaps.

| Field | Value |
|---|---|
| Story Points | 8 |
| Hours | 80h |
| Priority | P0 |
| Labels | epic:team-knowledge-graph, area:knowledge-graph, area:domain-service, area:evidence-linking, complexity:high |

**Acceptance Criteria**
- Unit tests are written and passing for node normalization, edge normalization, evidence-link preservation, missing relationship handling, and low-confidence claim eligibility labeling.
- System integration tests validate graph assembly across fixture loader and gap service boundaries using committed local demo data.
- Mock data and fixtures are generated and committed so the graph includes team-to-goal, goal-to-skill, team-member-to-skill, candidate-to-claim, claim-to-evidence, and candidate-to-gap relationships.
- The assembled graph contains no duplicate node IDs, no dangling edges, and no full raw pasted profile text in nodes, edges, errors, or operational metadata.
- Graph output includes explicit unfilled-gap nodes or edges when no current team member or candidate claim covers a required capability.

**Depends on:** WO-010, WO-026

### [P0] Expose Gap And Graph APIs

Add typed internal API routes that expose selected team-goal gaps and knowledge graph data to the browser using consistent versioned JSON contracts. This is required so the Candidate Shortlist and future Interview Mode surfaces can retrieve explainable team knowledge data through stable service boundaries instead of importing fixtures or domain services directly in components. The affected components are Next.js API route handlers, request schemas, response schemas, route-level error mapping, privacy-safe structured logging, integration tests, and API fixtures. When complete, clients can request gap results and graph results for known local demo teams and goals and receive structured success responses with request IDs, duration metadata, and safe actionable errors for malformed or unknown inputs. This story does not include UI components, Cytoscape rendering, candidate ranking, targeted question generation, authentication, persistent audit storage, or external platform integrations. It depends on validated local fixtures, team-gap computation, and graph assembly services being available as framework-independent capabilities.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:team-knowledge-graph, area:api, area:service-boundary, area:observability, complexity:medium |

**Acceptance Criteria**
- Unit tests are written and passing for request validation, response mapping, structured error mapping, and service dependency injection at the route boundary.
- System integration tests validate successful and failing calls to the gap and graph endpoints using local fixture data and the real Next.js route handlers.
- Mock data and fixtures are generated and committed so API tests cover at least one valid team-goal scenario, one unknown goal, one unknown team, and one invalid request shape.
- All API responses use a consistent envelope containing data, errors, requestId, and meta.durationMs, with no stack traces or Restricted raw content in errors.
- The endpoints return correct HTTP status codes for malformed input, unknown local fixture IDs, invalid fixture state, and unexpected server failures.

**Depends on:** WO-028

### [P1] Add Team Goal Gap Panel

Implement the Candidate Shortlist team-goal selection and prioritized knowledge-gap panel so hiring managers can see which current team capabilities are missing or under-covered before they review candidate fit. This improves decision quality by anchoring shortlist discussion to current team goals rather than generic candidate popularity or broad skill matching. The affected areas are the Candidate Shortlist view, goal selector component, gap panel component, client API hooks or server data loaders, loading and error states, accessibility labels, and component tests. When complete, the user can select a demo team goal, see prioritized gaps with severity and coverage details, understand when no goal is selected, and recover from API or empty-data failures without leaving the page. This story does not include graph visualization, ranking formula implementation, interview question generation, Interview Mode status updates, authentication, database persistence, or external integrations. It depends on reliable internal APIs for graph and gap retrieval and on local fixtures containing at least one realistic team-goal scenario.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P1 |
| Labels | epic:team-knowledge-graph, area:frontend, area:candidate-shortlist, area:accessibility, complexity:medium |

**Acceptance Criteria**
- Unit tests are written and passing for the goal selector, gap panel rendering, severity label rendering, empty state rendering, loading state rendering, and error state rendering.
- System integration tests validate that selecting a team goal calls the gap API boundary and renders the returned prioritized gaps in the Candidate Shortlist workflow.
- Mock data and fixtures are generated and committed for selected goal, no selected goal, no gaps, API error, and under-covered capability scenarios.
- The UI prompts the user to select or use a demo goal when no goal is selected and does not show misleading gap or candidate-fit conclusions.
- Gap warnings and severity indicators are accessible through text and labels and do not rely on color alone.

**Depends on:** WO-028

### [P1] Render Resilient Knowledge Graph

Implement the browser-only knowledge graph visualization with an SSR-safe Cytoscape wrapper and a first-class fallback view so the demo remains usable even if graph rendering fails. This is needed because the graph is a high-value explainability surface, but Cytoscape depends on browser APIs and must not break the Next.js server render or the under-90-second demo workflow. The affected areas are the graph panel component, dynamic Cytoscape client component, fallback table or relationship list, graph data hook, error boundary, accessibility labels, browser tests, and runbook-style troubleshooting notes. When complete, users can inspect nodes and relationships between team goals, gaps, skills, candidates, claims, and evidence references, and if the visualization cannot load they still see a readable relationship list with the same core information. This story does not include graph assembly logic, gap computation, API route contracts, ranking, question generation, authentication, database persistence, or new external data sources. It depends on a stable graph API and the Candidate Shortlist surface where goal selection and gap context are already available.

| Field | Value |
|---|---|
| Story Points | 8 |
| Hours | 80h |
| Priority | P1 |
| Labels | epic:team-knowledge-graph, area:frontend, area:visualization, area:resilience, complexity:high |

**Acceptance Criteria**
- Unit tests are written and passing for graph panel state handling, fallback rendering, selected node details, graph data mapping, and error boundary behavior.
- System integration tests validate that the graph panel fetches graph data through the API boundary and renders either the Cytoscape visualization or the fallback list without SSR failures.
- Mock data and fixtures are generated and committed for normal graph rendering, empty graph, graph API error, browser visualization failure, and dense demo graph scenarios.
- The Cytoscape implementation is dynamically loaded only on the client and does not access browser globals during server render or static build.
- The fallback view displays core nodes and relationships in accessible text form and includes recovery guidance when visualization initialization fails.

**Depends on:** WO-032

---

## Candidate Shortlist Ranking Reasons and Human Sign-Off

### [P0] Configure Explainable Ranking Weights

The shortlist ranking needs an explicit, deterministic weighting configuration so hiring managers can understand why one candidate is ranked above another and platform operators can reproduce demo outcomes reliably. This change introduces typed local configuration for team-gap relevance, evidence strength, claim confidence, recency, and priority gap coverage, with validation that prevents invalid or non-normalized weights from silently changing recommendations. It affects the ranking domain service, shared TypeScript schemas, local JSON demo configuration, health or fixture validation checks, and unit test fixtures. When complete, the app will load a validated default weight profile at startup, expose the active profile to the shortlist scoring flow, and fail closed with a structured error if the configuration is missing or malformed. This story does not implement candidate scoring, UI ranking cards, sign-off, feedback capture, authentication, database persistence, or configurable user-managed weights. It depends on the existing local fixture loading capability, shared runtime validation patterns, and the domain service boundary used by team-gap and candidate-claim processing.

| Field | Value |
|---|---|
| Story Points | 3 |
| Hours | 30h |
| Priority | P0 |
| Labels | epic:EPIC-005, feature:ranking, guardrail:explainability, complexity:medium |

**Acceptance Criteria**
- A typed ranking weight profile exists for team-gap relevance, evidence strength, confidence, recency, and priority coverage, and the total weighting is validated before scoring can run.
- Invalid weight profiles, including missing required keys, negative values, non-numeric values, and totals outside the accepted tolerance, return a structured validation failure without falling back to unsafe defaults.
- Unit tests are written and passing for valid profiles, malformed profiles, boundary totals, and default profile loading behavior.
- System integration tests validate that the shortlist API or service boundary receives the active validated weight profile and rejects scoring when the profile is invalid.
- Mock data and fixtures are generated and committed for at least one valid default profile and multiple invalid profile cases so tests run without external dependencies.

**Depends on:** WO-020

### [P0] Compute Team-Gap Fit Scores

The Candidate Shortlist needs a deterministic scoring service that ranks candidates by how well their eligible evidence-linked claims address current team knowledge gaps, because recruiters and hiring managers need transparent prioritization rather than a generic candidate list. This change implements the core team-gap fit computation using the validated ranking weight profile, existing candidate claims, evidence metadata, and team-gap priorities from local JSON fixtures. It affects the ranking domain service, shortlist API route or server action, shared response schemas, local test fixtures, and structured logging around scoring operations. When complete, the service will return ordered candidate results with numeric scores, factor breakdowns, excluded claim summaries, and stable handling for candidates who do not fill any gap. This story does not build the visual shortlist cards, generate natural-language recommendation reason copy, implement human sign-off, persist scores, or add any automated hire or reject decision. It depends on validated ranking weights, evidence-linked candidate claim extraction, team-gap discovery, and low-confidence eligibility metadata being available to the scoring layer.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:EPIC-005, feature:shortlist-scoring, guardrail:low-confidence-gating, complexity:medium |

**Acceptance Criteria**
- Given a selected team goal and candidate set, the scoring service returns candidates ordered by descending team-gap fit score with deterministic tie handling.
- Low-confidence, unsupported, or unreviewed claims are visible in the response as excluded inputs and do not contribute to score calculations.
- Candidates that fill no selected team gap receive a safe low or zero score and an explicit no-gap-coverage indicator rather than being forced into a misleading recommendation.
- Unit tests are written and passing for score factor math, exclusion of ineligible claims, tie ordering, missing gaps, and empty candidate lists.
- System integration tests validate the shortlist service or API boundary using local team, gap, candidate, claim, evidence, and weight fixtures.
- Mock data and fixtures are generated and committed for ranked candidates, tied candidates, excluded low-confidence claims, and candidates with no gap coverage.

**Depends on:** WO-010, WO-024, WO-027, WO-020, WO-023

### [P0] Expose Evidence-Backed Ranking Reasons

Ranked candidates need structured recommendation reasons that explain which team gaps they cover and which evidence supports each claim, because hiring stakeholders must be able to audit the recommendation before trusting it. This change turns raw score outputs into traceable reason payloads that include gap references, claim references, evidence references, confidence indicators, and unfilled-gap explanations when no candidate covers a priority need. It affects the ranking reason domain service, shortlist API response contract, shared schemas, local demo fixtures, and tests that validate provenance. When complete, every ranked result will include machine-readable reasons suitable for UI rendering and compliance review, and no reason will be emitted without either evidence linkage or an explicit unfilled-gap rationale. This story does not implement the final visual presentation, sign-off workflow, interview question generation, persistent audit storage, or changes to extraction logic. It depends on deterministic team-gap scoring, evidence-linked claims, and stable identifiers for candidates, claims, gaps, and evidence snippets.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:EPIC-005, feature:recommendation-reasons, guardrail:traceability, complexity:medium |

**Acceptance Criteria**
- Every recommendation reason for a scored candidate includes candidate ID, gap ID, claim ID, evidence ID or explicit unfilled-gap indicator, confidence, and a short human-readable rationale.
- A candidate result with no covered priority gaps includes an explicit unfilled or no-coverage reason instead of an empty explanation array.
- Reasons are derived only from eligible scoring inputs, and ineligible low-confidence claims appear only in exclusion rationale, not as positive recommendation reasons.
- Unit tests are written and passing for evidence-backed reasons, unfilled-gap reasons, excluded-claim rationale, and missing-reference failures.
- System integration tests validate that the shortlist response includes structured reasons for top-ranked, low-ranked, and no-coverage candidates.
- Mock data and fixtures are generated and committed for evidence-backed coverage, unsupported claim exclusion, and unfilled priority gaps.

**Depends on:** WO-029

### [P0] Render Ranked Shortlist Cards

Recruiters and hiring managers need a Candidate Shortlist view that presents rank order, fit score, coverage of team gaps, and recommendation reasons in a compact reviewable format, because the MVP demo must show transparent shortlist prioritization quickly. This change builds or updates the shortlist UI components to consume the structured shortlist response and render ranked candidate cards with score breakdowns, evidence-linked reasons, covered and unfilled gaps, and clear non-decisional copy. It affects the Candidate Shortlist page, candidate card components, API client helpers, shared UI status components, local demo fixtures, and browser-level tests. When complete, users can open the shortlist, select or use a demo team goal, see ranked candidates, inspect why each candidate ranked where they did, and observe that the UI never displays auto-hire or auto-reject language. This story does not implement scoring math, reason generation, low-confidence review actions, human sign-off submission, interview mode question generation, or persistent state. It depends on the shortlist scoring API returning ordered candidates with evidence-backed reasons and unfilled-gap metadata.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:EPIC-005, feature:candidate-shortlist-ui, accessibility:wcag-core, complexity:medium |

**Acceptance Criteria**
- The Candidate Shortlist view renders candidates in the exact rank order returned by the shortlist service and displays score, rank, covered gaps, and reason summaries for each card.
- Each card provides an accessible way to inspect evidence-linked reason details without rendering raw HTML from candidate-provided text.
- Unfilled priority gaps are visible in the shortlist view when no candidate covers them, and the UI does not hide weak coverage scenarios.
- The UI includes explicit decision-support copy stating that rankings are recommendations for human review and are not hiring or rejection decisions.
- Unit tests are written and passing for shortlist card rendering, reason detail rendering, empty states, and non-decisional copy.
- System integration tests validate the browser-to-shortlist API flow with local fixtures and confirm ranked cards render within the demo workflow.
- Mock data and fixtures are generated and committed for a normal ranked shortlist, no-gap coverage, and reason detail expansion.

**Depends on:** WO-031, WO-033

### [P0] Gate Low-Confidence Claim Influence

The shortlist workflow must show unsupported or low-confidence claims without allowing them to influence ranking or interview prompts until a human explicitly reviews them, because recruiters need transparency without accidental automation bias. This change adds visible warning states, review actions, and eligibility updates for low-confidence claims in the Candidate Shortlist workflow, using in-memory session state and local fixtures rather than a database. It affects the shortlist UI warning components, review-state service, shortlist request assembly, API contract for reviewed claims, shared schemas, and tests that prove excluded claims stay out of scoring until reviewed. When complete, users can see which claims were excluded, understand why, mark a claim as reviewed for demo purposes, and re-run or refresh the shortlist so eligible reviewed claims can contribute according to scoring rules. This story does not implement durable audit storage, authentication, interview-mode status management, question generation, or changes to extraction confidence calculations. It depends on shortlist scoring support for excluded claims and the UI card experience that displays those exclusions.

| Field | Value |
|---|---|
| Story Points | 8 |
| Hours | 80h |
| Priority | P0 |
| Labels | epic:EPIC-005, feature:human-review-gate, guardrail:low-confidence-gating, complexity:high |

**Acceptance Criteria**
- Low-confidence, unsupported, or unreviewed claims appear with warning badges and explanatory text that does not rely on color alone.
- Excluded claims are not included in positive score contributions or recommendation reasons until a user performs an explicit review action.
- A review action updates in-memory eligibility state for the current demo session and causes subsequent shortlist scoring to include the reviewed claim only when all required evidence references are present.
- The UI shows a clear distinction between system confidence, human review state, and final hiring judgment so users do not confuse review with approval for hiring.
- Unit tests are written and passing for eligibility state transitions, review validation, and scoring exclusion before review.
- System integration tests validate the end-to-end flow from viewing an excluded claim, marking it reviewed, re-running shortlist scoring, and observing changed eligibility at the service boundary.
- Mock data and fixtures are generated and committed for low-confidence claims, unsupported claims, reviewed claims, and claims blocked by missing evidence.

**Depends on:** WO-027, WO-037

### [P0] Capture Shortlist Human Sign-Off

Every shortlist recommendation output needs explicit human sign-off before it can be treated as ready for interview preparation, because WEMESH must keep HR and hiring stakeholders as final decision-makers and prevent automated hiring conclusions. This change adds a sign-off workflow for shortlist results that records the reviewed recommendation context, actor label, timestamp, acknowledgment text, and current session state in memory, with structured redacted logging for operational traceability. It affects the Candidate Shortlist page, sign-off UI component, sign-off domain service, API route, shared schemas, and integration tests. When complete, the shortlist view will clearly show unsigned versus signed states, block downstream ready-for-interview completion messaging until sign-off exists, and display a human-reviewed confirmation without implying hire or reject decisions. This story does not add authentication, durable audit persistence, database tables, legal e-signature capability, or final hiring disposition tracking. It depends on ranked shortlist cards, recommendation reasons, and low-confidence review gating so the signer can see what they are acknowledging.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:EPIC-005, feature:human-signoff, governance:human-in-loop, complexity:medium |

**Acceptance Criteria**
- The Candidate Shortlist view provides an explicit human sign-off control with acknowledgment copy confirming the user reviewed ranking reasons, exclusions, and warnings.
- Submitting sign-off records shortlist session ID or context hash, actor label, timestamp, selected team goal, candidate result identifiers, and acknowledgment version in in-memory state.
- The UI shows signed and unsigned states distinctly and does not display ready-for-interview completion language until sign-off succeeds.
- Sign-off cannot succeed when required low-confidence claim review warnings remain unresolved for the selected shortlist policy state, and the user receives actionable guidance.
- Unit tests are written and passing for sign-off validation, missing acknowledgment, blocked sign-off, and successful in-memory recording.
- System integration tests validate shortlist rendering, sign-off API submission, signed-state refresh, and blocked submission when warnings remain unresolved.
- Mock data and fixtures are generated and committed for unsigned shortlist, signed shortlist, unresolved warning state, and acknowledgment versioning.

**Depends on:** WO-011, WO-006, WO-037

### [P1] Collect Shortlist Usefulness Feedback

The limited beta needs lightweight feedback capture on shortlist usefulness so product and hiring stakeholders can evaluate whether top recommendations improve candidate-team fit without adding external survey tools or storing unnecessary restricted data. This change adds an in-app feedback form after human sign-off that captures usefulness rating, optional safe comment, selected role context, recommendation context reference, and timestamp in in-memory state or downloadable demo-safe JSON. It affects the Candidate Shortlist page, feedback UI component, feedback domain service, API route, shared schemas, local fixtures, and tests. When complete, signed shortlist sessions can collect structured beta feedback, operators can inspect or export aggregate demo-safe feedback, and the workflow remains privacy-conscious with no candidate profile text or evidence snippets stored in feedback records. This story does not implement production analytics, durable database storage, authentication, external form integrations, hiring disposition capture, or automatic model tuning. It depends on shortlist human sign-off and the existing recommendation context so feedback is tied to reviewed outputs rather than raw rankings.

| Field | Value |
|---|---|
| Story Points | 3 |
| Hours | 30h |
| Priority | P1 |
| Labels | epic:EPIC-005, feature:beta-feedback, operability:demo-metrics, complexity:medium |

**Acceptance Criteria**
- After shortlist sign-off succeeds, the UI presents a feedback form with a required usefulness rating and optional comment using safe length limits.
- Feedback submissions record recommendation context reference, selected team goal, rating, optional comment, timestamp, and actor label in in-memory state without storing candidate profile text or evidence snippets.
- Feedback cannot be submitted for an unsigned shortlist context, and the user receives a clear message that sign-off is required first.
- An operator-accessible feedback summary or demo-safe JSON export shows aggregate counts and submitted ratings without exposing restricted candidate text.
- Unit tests are written and passing for feedback schema validation, unsigned-context blocking, comment sanitization, and aggregate summary generation.
- System integration tests validate the signed shortlist to feedback submission flow through the API boundary and verify unsigned submission is rejected.
- Mock data and fixtures are generated and committed for valid feedback, missing rating, overlong comment, unsigned context, and aggregate summary output.

**Depends on:** WO-011, WO-041

---

## Targeted Interview Questions and Interview Mode

### [P0] Manage Interview Claim Status

Implement the in-memory Interview Mode session capability that tracks per-claim verification status so HR interview operators can record human judgment during candidate conversations without introducing database persistence. The change should affect the interview session domain service, status transition validation, shared schemas, volatile server state, privacy-safe mutation logging, and service tests. When complete, claims can transition among Claimed, Needs Follow-up, Verified, and Not Verified according to explicit validation rules, and each mutation returns updated session state plus unresolved status summaries. This story does not include building the Interview Mode page, rendering controls, generating questions, capturing final sign-off, durable audit storage, or authentication. It depends on the availability of candidate claim identifiers, eligibility metadata, and local fixture data, and it must remain compatible with the no-database MVP constraint.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:interview-mode, domain:session-state, data:in-memory, privacy:restricted-data, complexity:medium |

**Acceptance Criteria**
- Given an interview session for a candidate with known claims, when a valid status update is submitted, then the in-memory session state stores the new status, updated timestamp, redacted actor label, and claim identifier.
- Given an invalid status value, unknown candidate, unknown claim, or claim that does not belong to the selected candidate, when a status update is attempted, then the service rejects it with a typed validation or domain error.
- Given multiple claim statuses in one session, when the session summary is requested, then it returns counts by status and identifies unresolved high-priority claims without making hiring recommendations.
- Unit tests are written and passing for all allowed statuses, invalid status rejection, claim ownership validation, session summary counts, and in-memory state reset initialization.
- System integration tests are N/A — this story implements the domain state service only and does not expose an API or UI boundary.
- Mock data and fixtures are generated and committed for sessions with all statuses, unknown claims, claim ownership mismatch, and unresolved high-priority claims.

**Depends on:** WO-003, WO-011

### [P0] Generate Traceable Interview Questions

Build a deterministic question generation capability that converts supported or human-reviewed candidate claims into targeted interview verification questions so recruiters and HR interview operators can test ownership, depth, and relevance without relying on generic prompts. The change should affect the domain service layer, shared TypeScript types, validation schemas, and local demo fixtures for candidates, claims, evidence, team gaps, and seniority context. When complete, each generated question will be linked to a claim, evidence snippet, team gap, confidence score, and rationale that explains why the question matters to the selected team goal. This story does not include the HTTP API route, Candidate Shortlist rendering, Interview Mode UI, durable persistence, external LLM calls, LinkedIn integrations, or automated hire and reject recommendations. It depends on the existing capability to produce evidence-linked claims, confidence metadata, team gap identifiers, and human review eligibility state from local JSON demo data.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:targeted-interview, domain:question-generation, data:local-json, guardrail:human-review, complexity:medium |

**Acceptance Criteria**
- Given supported or human-reviewed claims with evidence and matching team gaps, when the question generation service runs, then it returns at least one targeted verification question per eligible high-relevance claim with claim ID, evidence ID, gap ID, confidence, question type, and rationale.
- Given low-confidence or unsupported claims that have not been reviewed by a human, when the question generation service runs, then those claims remain visible in an excluded claims collection and no generated question is created from them.
- Given a claim with missing evidence, missing team gap mapping, or invalid seniority context, when the service evaluates it, then it produces a structured warning instead of silently generating an untraceable question.
- Unit tests are written and passing for eligibility filtering, question template selection, evidence and gap traceability, seniority-aware phrasing, and excluded-claim warning behavior.
- System integration tests are N/A — this story implements pure domain logic only and does not expose an HTTP or UI boundary.
- Mock data and fixtures are generated and committed for eligible claims, excluded low-confidence claims, missing evidence, multiple seniority levels, and high-priority team gaps.

**Depends on:** WO-024, WO-027, WO-020

### [P0] Expose Questions API Contract

Add a typed internal API endpoint for targeted interview question generation so the Candidate Shortlist and Interview Mode views can request consistent question packets through a stable service boundary. The change should affect the Next.js API route layer, shared request and response schemas, structured error mapping, privacy-safe logging, and integration tests that exercise the question service through HTTP semantics. When complete, clients can post candidate, reviewed claim, team goal, and seniority context identifiers and receive structured questions, excluded claim warnings, request metadata, and duration metrics. This story does not include building the UI, managing interview status transitions, storing sessions durably, adding authentication, or integrating with external AI providers. It depends on the domain capability to generate deterministic, evidence-linked questions and on existing local fixture repositories for candidates, claims, evidence, and team gaps.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:targeted-interview, api:v1, observability:redacted-logs, security:input-validation, complexity:medium |

**Acceptance Criteria**
- Given a valid request with known candidate ID, team goal ID, reviewed claim IDs, and seniority context, when the client posts to the questions endpoint, then the response uses the standard data, errors, requestId, and meta.durationMs envelope and includes traceable generated questions.
- Given malformed JSON, missing required fields, unknown candidate IDs, unknown claim IDs, or unknown team goal IDs, when the endpoint is called, then it returns the appropriate structured 400 or 404 response without stack traces or sensitive payload content.
- Given a request that includes unreviewed low-confidence claims, when the endpoint evaluates eligibility, then those claims are excluded from question generation and returned as warnings rather than influencing prompts.
- Unit tests are written and passing for request schema validation, response envelope construction, error mapping, and redacted log event construction.
- System integration tests are written and passing for successful question generation, malformed input, unknown IDs, and low-confidence exclusion through the actual API route boundary.
- Mock data and fixtures are generated and committed for successful API calls, invalid identifiers, malformed requests, and excluded claim scenarios.

**Depends on:** WO-010, WO-030

### [P0] Show Questions In Shortlist

Add targeted interview question visibility to the Candidate Shortlist experience so recruiters can move from evidence-backed ranking reasons into interview preparation without switching tools or losing provenance. The change should affect shortlist page components, candidate detail panels, client-side API integration, UI state for loading and warnings, and local demo fixtures used for scripted demos. When complete, a recruiter selecting a shortlisted candidate can see generated questions grouped by claim or team gap, along with evidence references, low-confidence exclusions, and clear human-review messaging. This story does not include implementing the question generation service, designing Interview Mode status controls, capturing sign-off, creating a database, or adding authentication. It depends on the questions API capability and on existing shortlist data that identifies candidates, reviewed claims, ranking reasons, and selected team goals.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:targeted-interview, view:candidate-shortlist, ux:evidence-traceability, accessibility:wcag-aa, complexity:medium |

**Acceptance Criteria**
- Given a shortlisted candidate with eligible claims and a selected team goal, when the recruiter opens the candidate detail area, then targeted questions are fetched from the questions API and displayed with claim, evidence, gap, priority, and rationale context.
- Given the questions API returns excluded low-confidence claims, when questions are displayed, then the UI shows non-color-only warnings explaining that those claims require human review before they can influence prompts.
- Given the questions API returns no eligible questions, when the candidate detail area renders, then the UI shows an actionable empty state that allows the recruiter to continue reviewing evidence without implying a candidate should be rejected.
- Unit tests are written and passing for question panel rendering, warning states, loading states, empty states, and accessibility labels for status indicators.
- System integration tests are written and passing for the Candidate Shortlist to questions API flow using a mocked or test API boundary with fixture-backed responses.
- Mock data and fixtures are generated and committed for candidates with multiple questions, excluded claims, no eligible questions, and API error states.

**Depends on:** WO-037, WO-034

### [P0] Build Interview Mode Workspace

Create the Interview Mode workspace so HR interview operators can review targeted questions, inspect evidence-linked claims, and update claim verification statuses during a live candidate conversation. The change should affect the Interview Mode page or route, question display components, claim status controls, client integration with question and session APIs or server actions, accessibility states, and demo fixtures for interview scenarios. When complete, an operator can open a shortlisted candidate, see interview-ready questions and evidence context, mark each claim as Claimed, Needs Follow-up, Verified, or Not Verified, and observe session summaries update immediately. This story does not include implementing the question generation service, adding durable persistence, introducing authentication, capturing final sign-off, or building candidate-facing interview assistance. It depends on the targeted questions API and the in-memory status management capability being available through callable application boundaries.

| Field | Value |
|---|---|
| Story Points | 8 |
| Hours | 80h |
| Priority | P0 |
| Labels | epic:interview-mode, view:interview-mode, ux:status-management, accessibility:keyboard-navigation, complexity:high |

**Acceptance Criteria**
- Given a shortlisted candidate with generated questions, when the operator opens Interview Mode, then the workspace displays candidate context, claim-linked questions, evidence references, team gap relevance, and current claim status controls.
- Given the operator changes a claim status to Claimed, Needs Follow-up, Verified, or Not Verified, when the update succeeds, then the UI reflects the new status and refreshes summary counts without requiring a page reload.
- Given a low-confidence or excluded claim appears in interview context, when the workspace renders, then it shows a warning and does not present that claim as a generated prompt source unless it has been human-reviewed.
- Unit tests are written and passing for workspace rendering, status control state changes, warning presentation, summary count updates, and accessible labels for all statuses.
- System integration tests are written and passing for opening Interview Mode, fetching questions, updating claim status through the application boundary, and rendering updated session summaries.
- Mock data and fixtures are generated and committed for candidates with multiple questions, all four statuses, excluded claims, API failure states, and empty interviewable claim sets.

**Depends on:** WO-042, WO-017

### [P1] Flag Unresolved Priority Claims

Add unresolved priority claim detection and prompting inside Interview Mode so HR interview operators can see which high-value claims still need verification or follow-up before closing an interview. The change should affect the interview session summary logic, high-priority gap mapping, UI prompt component, application boundary responses, and fixture coverage for unresolved sessions. When complete, claims connected to high-priority team gaps that remain Claimed or Needs Follow-up are surfaced in a clear follow-up prompt, while Verified and Not Verified claims are treated as resolved for session completeness purposes. This story does not include final sign-off capture, ranking formula changes, new team-gap discovery logic, durable persistence, or automated hiring decisions. It depends on interview status management, targeted question traceability, and existing priority metadata for team gaps or recommendation reasons.

| Field | Value |
|---|---|
| Story Points | 3 |
| Hours | 30h |
| Priority | P1 |
| Labels | epic:interview-mode, guardrail:follow-up, domain:session-summary, ux:operator-guidance, complexity:medium |

**Acceptance Criteria**
- Given an interview session with high-priority claim mappings, when one or more high-priority claims are Claimed or Needs Follow-up, then Interview Mode displays an unresolved priority prompt with claim labels, gap context, and recommended follow-up action text.
- Given all high-priority claims are Verified or Not Verified, when the summary refreshes, then the unresolved priority prompt is hidden and the session summary indicates no high-priority follow-ups remain.
- Given a claim has no high-priority team gap mapping, when it remains Claimed or Needs Follow-up, then it can appear in general summary counts but does not trigger the priority follow-up prompt.
- Unit tests are written and passing for unresolved priority detection, resolved status handling, non-priority exclusion, and prompt rendering rules.
- System integration tests are written and passing for status changes that make the unresolved priority prompt appear, update, and disappear through the Interview Mode boundary.
- Mock data and fixtures are generated and committed for unresolved high-priority claims, resolved high-priority claims, non-priority unresolved claims, and sessions with no gap mappings.

**Depends on:** WO-044

### [P0] Capture Interview Human Signoff

Implement human sign-off for Interview Mode so interview outputs cannot be treated as complete until an HR operator explicitly acknowledges unresolved items, human decision ownership, and the absence of automated hire or reject behavior. The change should affect the sign-off domain logic, in-memory interview session state, API or server action boundary, Interview Mode UI, structured mutation logging, and demo fixtures for complete and incomplete sessions. When complete, the operator can sign off only after reviewing the session summary, and the resulting in-memory session record includes sign-off timestamp, redacted actor label, unresolved priority count, and acknowledgement fields. This story does not include production audit persistence, authentication, retention automation, ATS export, automatic decisioning, or broader compliance approvals outside the MVP application behavior. It depends on Interview Mode status management, unresolved priority claim detection, and the workspace UI that presents session summaries.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:interview-mode, guardrail:human-signoff, compliance:soc2-style, observability:audit-like-events, complexity:medium |

**Acceptance Criteria**
- Given an interview session summary is visible, when the operator confirms required acknowledgements and signs off, then the in-memory session stores sign-off metadata and the UI shows the session as human-reviewed.
- Given unresolved high-priority claims remain, when the operator attempts sign-off, then the UI requires an explicit unresolved-follow-up acknowledgement before sign-off can succeed.
- Given required acknowledgement fields are missing, when sign-off is submitted, then the application returns or displays a structured validation error and does not mark the session complete.
- Unit tests are written and passing for sign-off validation, unresolved-priority acknowledgement requirements, session metadata updates, and prevention of automated decision fields.
- System integration tests are written and passing for the Interview Mode sign-off flow, missing acknowledgement rejection, unresolved priority acknowledgement, and completed session display.
- Mock data and fixtures are generated and committed for complete sessions, unresolved priority sessions, missing acknowledgement submissions, and already signed-off sessions.

**Depends on:** WO-006, WO-044, WO-045

---

## CI/CD Observability and Demo Validation

### [P0] Add deterministic CI quality gates

Add a GitHub Actions continuous integration workflow that validates the Next.js and TypeScript application on every pull request and main branch update so regressions are caught before they can break the Daytona demo. The change affects repository automation under .github/workflows, package scripts in package.json, dependency installation through the lockfile, and the existing lint, typecheck, test, and build commands used by the application. When complete, reviewers can see a single required CI status that installs dependencies reproducibly, checks formatting or lint rules, verifies TypeScript, runs automated tests, and produces a production build without relying on external services or secrets. This story does not include deployment to a hosted production environment, authentication setup, database provisioning, or changes to recruiting product behavior. It depends on the application having reproducible local install and validation commands and on the Daytona runtime expectation that the app can run as a single process on port 3000.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:ci-cd-observability, ci, automation, daytona, complexity:medium |

**Acceptance Criteria**
- A GitHub Actions workflow runs on pull_request and main branch push events and fails if dependency installation, linting, TypeScript checking, automated tests, or production build fail.
- The workflow uses npm ci or the repository equivalent lockfile-safe install command and does not require real secrets, external LinkedIn integrations, databases, or production infrastructure.
- Unit tests written and passing: N/A — this story wires existing and newly available unit test commands into CI rather than adding domain logic.
- System integration tests validating service/API boundaries are invoked by the workflow when the repository exposes an integration test script, and the workflow clearly skips only when no such script exists.
- Mock data/fixtures generated and committed: N/A — this story consumes committed test fixtures from the application and does not create new recruiting scenario data.
- CI output includes separate, readable steps for install, lint, typecheck, test, and build so an engineer can identify the failing quality gate within one job log.
- The workflow documents or enforces Node.js version selection so local, Daytona, and CI environments use a consistent runtime baseline.

**Depends on:** WO-001, WO-002

### [P1] Automate dependency risk scanning

Add dependency vulnerability scanning and automated update configuration so the platform team can detect risky packages early without relying on manual package audits before demos. The change affects GitHub security configuration, repository dependency update configuration such as .github/dependabot.yml or equivalent, package manifests, and CI security steps that inspect the Node.js dependency graph. When complete, dependency risk is visible in pull requests or scheduled checks, update pull requests are opened automatically for eligible package ecosystems, and high-severity issues can be remediated without hand-crafted version discovery. This story does not include replacing major framework libraries, changing application architecture, adding paid security platforms, or resolving every vulnerability that may already exist in the dependency tree. It depends on lockfile-based dependency management and a working CI validation capability so automated update pull requests can be tested before merge.

| Field | Value |
|---|---|
| Story Points | 2 |
| Hours | 20h |
| Priority | P1 |
| Labels | epic:ci-cd-observability, security, dependencies, automation, complexity:low |

**Acceptance Criteria**
- A dependency update automation configuration is committed for the Node.js package ecosystem and, when supported, GitHub Actions workflow dependencies.
- A vulnerability scan runs on a scheduled basis or as part of CI and fails or reports according to an explicitly documented severity threshold appropriate for the MVP demo.
- Unit tests written and passing: N/A — this story adds dependency automation and security scanning configuration rather than new executable business logic.
- System integration tests validating service/API boundaries: N/A — dependency scanning does not exercise service boundaries, but automated update pull requests must be validated by the CI workflow.
- Mock data/fixtures generated and committed: N/A — dependency risk scanning does not require recruiting demo data or test fixtures.
- The scanning setup does not require real secrets, production credentials, LinkedIn access, a database, or any external runtime integration.
- Automated update pull requests are grouped or limited to reduce operational noise and avoid flooding maintainers during demo preparation.

**Depends on:** WO-008

### [P0] Backfill domain service unit tests

Add focused unit tests for the deterministic recruiting domain services so confidence, eligibility, ranking, question generation, and interview status behavior remain stable as the demo evolves. The change affects test files near or under the extraction, team-gap, ranking, question, interview session, fixture-loading, and shared schema modules, plus committed fixtures needed to exercise normal and failure paths. When complete, developers can run a local unit test command and see deterministic coverage for supported evidence-linked claims, low-confidence claim exclusion, recommendation reason generation, targeted question traceability, and allowed interview status transitions. This story does not include rewriting the domain services, changing the ranking formula beyond what existing product behavior requires, creating a database, or adding browser end-to-end tests. It depends on the core domain capabilities already existing behind testable TypeScript functions or services that can be imported without starting the full Next.js server.

| Field | Value |
|---|---|
| Story Points | 8 |
| Hours | 80h |
| Priority | P0 |
| Labels | epic:ci-cd-observability, unit-tests, quality, domain-services, complexity:high |

**Acceptance Criteria**
- Unit tests written and passing for profile text validation, evidence-linked claim extraction, low-confidence claim handling, team-gap analysis, ranking eligibility, question generation traceability, and interview status transitions where those modules exist.
- System integration tests validating service/API boundaries: N/A — this story targets pure domain unit coverage; API boundary validation is covered by the dedicated contract-test workstream.
- Mock data/fixtures generated and committed for supported claims, unsupported claims, low-confidence claims, unfilled team gaps, ranking inversion, and interview status transitions.
- Tests assert that unsupported or low-confidence claims have confidence below the configured threshold and are not ranking eligible until explicitly reviewed.
- Tests assert generated verification questions include traceability to claim, evidence, and team gap identifiers when reliable inputs are available.
- Tests assert recommendation reasons include at least one evidence reference or a clear unfilled-gap reason and never express automatic hire or reject decisions.
- The unit test command is wired into package.json if missing and can be executed without network access, LinkedIn access, authentication, or a database.

**Depends on:** WO-019, WO-020, WO-023, WO-030, WO-017

### [P0] Validate internal API contracts

Add API contract tests for the internal Next.js endpoints that support the demo workflow so browser-to-server boundaries remain predictable and safe under valid and invalid requests. The change affects test suites for routes such as extraction, graph retrieval, shortlist scoring, question generation, interview status updates, sign-off if present, feedback if present, and health checks, plus shared response schemas and synthetic request fixtures. When complete, contract tests verify response envelopes, status codes, request identifiers, duration metadata, structured errors, validation failures, and guardrail behavior without calling external services. This story does not include adding new product endpoints, changing the route naming strategy, introducing authentication, creating durable persistence, or implementing third-party integrations. It depends on the internal API routes and shared domain services being available and on deterministic fixture data for candidates, teams, goals, claims, evidence, and questions.

| Field | Value |
|---|---|
| Story Points | 5 |
| Hours | 50h |
| Priority | P0 |
| Labels | epic:ci-cd-observability, api-contracts, integration-tests, reliability, complexity:medium |

**Acceptance Criteria**
- Contract tests validate successful and failure responses for extraction, graph, shortlist, questions, interview status, and health endpoints where implemented.
- Unit tests written and passing: N/A — this story targets HTTP/API contract behavior; pure business logic coverage is handled by the domain unit-test workstream.
- System integration tests validating service/API boundaries are written and passing using the Next.js route handlers or an in-process test server without external network dependencies.
- Mock data/fixtures generated and committed for authorized profile input, too-short profile input, missing authorization acknowledgment, unknown candidate or goal IDs, low-confidence claims, and reliable question inputs.
- Tests assert HTTP 400 for malformed or too-short input, HTTP 403 for missing authorization acknowledgment, HTTP 404 for unknown fixture IDs, HTTP 409 or equivalent conflict behavior for invalid status transitions, and safe HTTP 500 handling without stack traces for unexpected errors.
- Tests assert every endpoint response follows the structured envelope with data or errors, requestId, and meta.durationMs where the application contract requires it.
- Tests assert raw pasted text, evidence snippets, and candidate names are not emitted in error responses or operational logs captured during contract tests.

**Depends on:** WO-015, WO-028, WO-029, WO-034

### [P0] Instrument redacted demo telemetry

Add lightweight observability for the synchronous demo pipeline so operators can understand health, latency, failures, and privacy-safe workflow progress without exposing restricted candidate data. The change affects shared logging utilities, API route middleware or wrappers, health endpoint behavior, domain service timing calls, and optional client-side demo step timing for Candidate Shortlist and Interview Mode. When complete, API calls emit structured redacted events with request identifiers, operation names, status, duration, counts such as number of claims and low-confidence claims, and a redacted actor label suitable for Daytona demo troubleshooting. This story does not include durable audit storage, centralized log shipping, production APM vendor integration, user identity tracking, or retention automation because the MVP has no authentication and no database. It depends on the internal API routes and demo workflow being implemented and on privacy-safe response contracts that avoid leaking raw pasted profile text, evidence snippets, or candidate names.

| Field | Value |
|---|---|
| Story Points | 8 |
| Hours | 80h |
| Priority | P0 |
| Labels | epic:ci-cd-observability, observability, structured-logging, privacy, complexity:high |

**Acceptance Criteria**
- Structured logs are emitted for key API operations including extraction, graph retrieval, shortlist scoring, question generation, interview status updates, sign-off if implemented, feedback if implemented, and health checks.
- Logs include requestId, operation, result status, durationMs, redacted actor label, and relevant aggregate counts while excluding raw pasted profile text, evidence snippets, candidate names, and full candidate identifiers.
- Unit tests written and passing for log redaction helpers, request identifier generation or propagation, and duration metadata behavior where implemented as reusable utilities.
- System integration tests validating service/API boundaries assert representative endpoint calls produce structured redacted telemetry and response meta.durationMs without leaking restricted input.
- Mock data/fixtures generated and committed for telemetry tests with synthetic candidate text designed to catch accidental PII leakage.
- The health endpoint reports readiness for the local fixture-backed application and returns within the documented target under normal local conditions.
- Client-side demo step timing is captured in a privacy-safe way when implemented, using aggregate step names and durations rather than pasted text or interview content.

**Depends on:** WO-014, WO-015, WO-028, WO-029, WO-034

### [P0] Automate scripted demo smoke test

Add a Playwright smoke test that exercises the critical WEMESH demo path end to end so the team can prove the product still completes the recruiting workflow within the required time budget. The change affects Playwright configuration, browser test fixtures, stable UI selectors in Candidate Shortlist and Interview Mode, seeded local JSON scenarios, and CI wiring to start the Next.js app on port 3000 before running the smoke test. When complete, the test launches the app, performs authorized profile paste, verifies evidence-linked extraction, observes team-gap discovery, checks shortlist recommendation reasons, generates targeted interview questions, enters Interview Mode, and completes status updates within the operational demo threshold. This story does not include manual demo sign-off, visual redesign, production hosting, load testing beyond the scripted scenario, or support for external profile imports. It depends on the core UI flow, internal APIs, deterministic fixtures, and API contract behavior being stable enough for browser automation.

| Field | Value |
|---|---|
| Story Points | 8 |
| Hours | 80h |
| Priority | P0 |
| Labels | epic:ci-cd-observability, playwright, smoke-test, demo-validation, complexity:high |

**Acceptance Criteria**
- A Playwright smoke test runs against a local Next.js server on port 3000 and completes the scripted MVP workflow in under 90 seconds on CI for the committed deterministic fixture scenario.
- Unit tests written and passing: N/A — this story adds browser-level end-to-end validation rather than new pure business logic.
- System integration tests validating service/API boundaries are written and passing by exercising the real browser, Next.js routes, domain services, and local JSON fixtures together.
- Mock data/fixtures generated and committed for the scripted demo candidate, team goal, team gaps, ranking inversion, recommendation reasons, low-confidence warning, and targeted questions.
- The smoke test asserts the app accepts authorized pasted profile text and rejects or displays an actionable warning when low-confidence or unsupported claims appear.
- The smoke test asserts shortlist recommendation reasons include evidence references or unfilled-gap reasons and do not display automatic hire or reject decisions.
- The smoke test asserts Interview Mode shows targeted verification questions and supports the human-entered claim statuses Claimed, Needs Follow-up, Verified, and Not Verified or a representative subset required by the scripted path.
- The Playwright command is wired into CI with trace or screenshot collection on failure to support rapid operational triage.

**Depends on:** WO-037, WO-044, WO-046

### [P1] Publish Daytona demo runbook

Create an operations runbook that lets a demo operator reliably start, validate, recover, and reset the WEMESH MVP in a Daytona sandbox on port 3000. The change affects repository documentation under docs or the project root, package script references, health-check instructions, fixture reset guidance, CI status interpretation, Playwright smoke-test usage, and troubleshooting steps for in-memory state loss. When complete, an engineer can follow the runbook from a fresh sandbox to a ready demo, verify the health endpoint, run the automated smoke test, recover from a failed start or browser flow, and explain known limitations such as local JSON data and non-durable interview state. This story does not include stakeholder approval, live production deployment, access-control rollout, database backup and restore, centralized monitoring setup, or manual QA sign-off. It depends on CI validation, dependency scanning, automated tests, smoke testing, and telemetry capabilities being available so the runbook can reference real commands and observable signals.

| Field | Value |
|---|---|
| Story Points | 2 |
| Hours | 20h |
| Priority | P1 |
| Labels | epic:ci-cd-observability, runbook, daytona, documentation, complexity:low |

**Acceptance Criteria**
- A committed runbook documents fresh Daytona setup, dependency installation, application startup on port 3000, health verification, smoke-test execution, fixture reset, and recovery from common demo failures.
- Unit tests written and passing: N/A — this story is operational documentation and does not add executable application logic.
- System integration tests validating service/API boundaries: N/A — the runbook references the automated integration and smoke-test commands created by other workstreams rather than implementing new tests.
- Mock data/fixtures generated and committed: N/A — the runbook documents how to use existing committed demo fixtures and does not create new data.
- The runbook includes a privacy-safe operating procedure that reminds operators to use authorized pasted profile text only, avoid real secrets, avoid public exposure, and restart or reset the sandbox after sessions involving real candidate text.
- The runbook includes troubleshooting steps for failed npm install, port 3000 conflicts, health endpoint failures, Playwright smoke failures, stale in-memory interview state, and missing local fixture data.
- The runbook includes expected operational targets for startup, health check latency, extraction latency, view rendering, and under-90-second demo completion so operators know when to stop and investigate.

**Depends on:** WO-004, WO-018, WO-047