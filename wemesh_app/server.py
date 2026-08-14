#!/usr/bin/env python3
"""WEMESH deterministic hackathon demo server.

Standard-library only so the same code runs locally and inside Daytona.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import time
from difflib import SequenceMatcher
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


APP_DIR = Path(__file__).resolve().parent
PROJECT_DIR = APP_DIR.parent
DATA_DIR = PROJECT_DIR / "data"
TEAM_DIR = DATA_DIR / "aws-team"

AUTHORIZED_PROFILE_URL = "https://www.linkedin.com/in/sehyeog-kim-5a1131265/"
TEAM_FILES = [
    "aws_engineer_a.json",
    "aws_engineer_b.json",
    "aws_engineer_c_sarath_krishnan_kg.json",
    "aws_engineer_d_sriharsha_ms_kg.json",
    "aws_engineer_e.json",
    "aws_engineer_f.json",
]

GAP_PROFILE = [
    {
        "id": "gap_multi_agent",
        "label": "Bedrock multi-agent orchestration and interoperability",
        "short": "Multi-agent orchestration",
        "priority": "Critical",
        "team_coverage": "Hiring priority · direct AWS evidence required",
        "direct_signals": ["amazon bedrock agentcore", "multi-agent systems", "agent-to-agent protocol", "model context protocol", "strands agents"],
        "transfer_signals": ["agentic workflows", "simulation pipeline automation", "n8n", "claude agent sdk"],
        "why": "The profile shows adjacent orchestration work, but no explicit Bedrock, A2A, MCP, or production multi-agent evidence.",
    },
    {
        "id": "gap_evaluation_observability",
        "label": "Agent evaluation, observability, and production operations",
        "short": "Evaluation & observability",
        "priority": "Critical",
        "team_coverage": "Hiring priority · direct AWS evidence required",
        "direct_signals": ["agent evaluation", "agent observability", "amazon cloudwatch", "agentops", "production monitoring"],
        "transfer_signals": ["mesh-independence studies", "simulation pipeline automation", "stress distribution analysis"],
        "why": "Simulation validation is transferable evidence, not proof of production AgentOps or CloudWatch experience.",
    },
    {
        "id": "gap_bedrock_delivery",
        "label": "Amazon Bedrock and AgentCore production delivery",
        "short": "Bedrock & AgentCore",
        "priority": "Critical",
        "team_coverage": "Hiring priority · no candidate evidence",
        "direct_signals": ["amazon bedrock", "amazon bedrock agentcore", "agentcore runtime"],
        "transfer_signals": [],
        "why": "No Amazon Bedrock or AgentCore claim appears in the authorized candidate profile snapshot.",
    },
    {
        "id": "gap_identity_security",
        "label": "Agent identity, security, and multi-tenant governance",
        "short": "Identity & security",
        "priority": "Critical",
        "team_coverage": "Hiring priority · no candidate evidence",
        "direct_signals": ["agentcore identity", "private key jwt", "tenant isolation", "resource-based policies", "secrets governance"],
        "transfer_signals": [],
        "why": "No agent identity, authorization, or multi-tenant security claim appears in the profile.",
    },
    {
        "id": "gap_enterprise_rag",
        "label": "Enterprise RAG and Bedrock Knowledge Bases",
        "short": "Enterprise RAG",
        "priority": "High",
        "team_coverage": "Hiring priority · no candidate evidence",
        "direct_signals": ["retrieval-augmented generation", "bedrock knowledge bases", "enterprise retrieval", "vector search"],
        "transfer_signals": [],
        "why": "The profile does not claim RAG, enterprise retrieval, or Bedrock Knowledge Bases work.",
    },
    {
        "id": "gap_resilience_gateway",
        "label": "LLM gateway resilience and production routing",
        "short": "Resilience & gateway",
        "priority": "High",
        "team_coverage": "Hiring priority · no candidate evidence",
        "direct_signals": ["llm gateway", "cross-region inference", "model fallback", "quota isolation", "request routing"],
        "transfer_signals": [],
        "why": "No LLM gateway, model routing, or AWS inference-resilience claim appears in the profile.",
    },
]

RUBRIC = [
    ("gap_coverage", "Direct AWS capability evidence", 0.35, "Explicit profile evidence for the Bedrock team’s required production capabilities."),
    ("semantic_alignment", "Transferable systems relevance", 0.25, "Adjacent knowledge that may transfer, without treating it as direct AWS expertise."),
    ("evidence_strength", "Claim evidence strength", 0.15, "Whether matched claims retain direct profile evidence and extraction confidence."),
    ("novel_contribution", "Novel contribution", 0.15, "Potentially useful knowledge that is not already explicit in the representative team graph."),
    ("verification_readiness", "Interview verifiability", 0.10, "Whether the fit can be tested through concrete, evidence-linked questions."),
]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def similarity(left: str, right: str) -> float:
    a, b = normalize(left), normalize(right)
    if not a or not b:
        return 0.0
    if a == b:
        return 0.98
    if len(a) >= 4 and len(b) >= 4 and (a in b or b in a):
        return 0.90
    a_tokens, b_tokens = set(a.split()), set(b.split())
    union = a_tokens | b_tokens
    jaccard = len(a_tokens & b_tokens) / len(union) if union else 0.0
    sequence = SequenceMatcher(None, a, b).ratio()
    return min(0.96, 0.68 * jaccard + 0.32 * sequence)


def team_payload() -> dict[str, Any]:
    agenda_doc = load_json(TEAM_DIR / "representative-aws-genai-team-agenda.json")
    members = []
    total_nodes = total_edges = total_evidence = 0
    for filename in TEAM_FILES:
        kg = load_json(TEAM_DIR / filename)
        real_name = str(kg.get("source", {}).get("real_name", "")).strip()
        alias = kg["person"]["name"]

        def public_excerpt(item: dict[str, Any]) -> str:
            excerpt = str(item.get("excerpt", ""))
            return excerpt.replace(real_name, alias) if real_name else excerpt

        clusters = []
        for cluster in kg.get("summary", {}).get("primary_clusters", []):
            clusters.append(
                {
                    "name": cluster.get("name") or cluster.get("label"),
                    "count": len(cluster.get("node_ids", [])),
                    "node_ids": cluster.get("node_ids", []),
                }
            )
        member = {
            "id": kg["person"]["id"],
            "alias": alias,
            "headline": kg["person"].get("headline", ""),
            "clusters": clusters,
            "node_count": len(kg.get("nodes", [])),
            "edge_count": len(kg.get("edges", [])),
            "evidence_count": len(kg.get("evidence", [])),
            "nodes": kg.get("nodes", []),
            "edges": kg.get("edges", []),
            "evidence": [
                {
                    "id": item.get("id"),
                    "section": item.get("section", "public professional evidence"),
                    "excerpt": public_excerpt(item),
                }
                for item in kg.get("evidence", [])
            ],
        }
        members.append(member)
        total_nodes += len(kg.get("nodes", []))
        total_edges += len(kg.get("edges", []))
        total_evidence += len(kg.get("evidence", []))
    return {
        "team": agenda_doc["team"],
        "agenda": agenda_doc["agenda"],
        "members": members,
        "gaps": GAP_PROFILE,
        "totals": {"nodes": total_nodes, "edges": total_edges, "evidence": total_evidence},
    }


def validate_linkedin_url(raw_url: str) -> str:
    value = raw_url.strip()
    parsed = urlparse(value)
    host = (parsed.hostname or "").lower()
    if parsed.scheme not in {"http", "https"} or host not in {"linkedin.com", "www.linkedin.com"}:
        raise ValueError("Enter a valid linkedin.com/in/ profile URL.")
    if not parsed.path.startswith("/in/"):
        raise ValueError("The URL must point to a LinkedIn public profile path (/in/...).")
    return value


def evidence_index(candidate: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["id"]: item for item in candidate.get("evidence", [])}


def score_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    nodes = candidate.get("nodes", [])
    evidence_by_id = evidence_index(candidate)
    gap_results = []
    matched_node_ids: set[str] = set()

    for gap in GAP_PROFILE:
        ranked = []
        for match_kind, signals in (("direct", gap["direct_signals"]), ("transferable", gap["transfer_signals"])):
            for node in nodes:
                node_label = normalize(node["label"])
                for signal in signals:
                    signal_label = normalize(signal)
                    if node_label == signal_label:
                        ranked.append((0.98, node, signal, match_kind))
                    elif len(signal_label) >= 4 and signal_label in node_label:
                        ranked.append((0.90, node, signal, match_kind))
        ranked.sort(key=lambda item: (item[3] != "direct", -item[0], item[1]["label"]))
        deduped = []
        seen_nodes = set()
        for item in ranked:
            if item[1]["id"] not in seen_nodes:
                deduped.append(item)
                seen_nodes.add(item[1]["id"])
        top = deduped[:3]
        direct_matches = [item for item in top if item[3] == "direct"]
        transferable_matches = [item for item in top if item[3] == "transferable"]
        if direct_matches:
            coverage = min(100, 85 + 5 * min(3, len(direct_matches)))
            status = "Direct evidence"
        elif transferable_matches:
            coverage = min(55, 45 + 5 * (len(transferable_matches) - 1))
            status = "Transferable only"
        else:
            coverage = 0
            status = "No explicit evidence"
        if top:
            matched_node_ids.update(item[1]["id"] for item in top)
        gap_results.append(
            {
                "id": gap["id"],
                "label": gap["label"],
                "short": gap["short"],
                "priority": gap["priority"],
                "team_coverage": gap["team_coverage"],
                "why": gap["why"],
                "fit": coverage,
                "status": status,
                "matches": [
                    {
                        "node_id": item[1]["id"],
                        "label": item[1]["label"],
                        "type": item[1]["type"],
                        "confidence": item[1].get("confidence", 0),
                        "signal": item[2],
                        "similarity": round(item[0] * 100),
                        "match_kind": item[3],
                        "evidence_ids": item[1].get("evidence_ids", []),
                    }
                    for item in top
                ],
            }
        )

    direct_scores = [item["fit"] for item in gap_results if item["status"] == "Direct evidence"]
    direct_coverage = round(sum(direct_scores) / len(GAP_PROFILE)) if direct_scores else 0
    transfer_scores = [item["fit"] for item in gap_results if item["status"] == "Transferable only"]
    semantic_alignment = round(sum(transfer_scores) / len(transfer_scores)) if transfer_scores else 0

    matched_nodes = [node for node in nodes if node["id"] in matched_node_ids]
    evidence_scores = []
    for node in matched_nodes:
        referenced = [evidence_by_id[eid] for eid in node.get("evidence_ids", []) if eid in evidence_by_id]
        confidence = float(node.get("confidence", 0.0))
        evidence_scores.append(confidence * (1.0 if referenced else 0.55))
    evidence_strength = round((sum(evidence_scores) / len(evidence_scores)) * 100) if evidence_scores else 0

    team = team_payload()
    team_labels = set()
    for filename in TEAM_FILES:
        kg = load_json(TEAM_DIR / filename)
        team_labels.update(normalize(node["label"]) for node in kg.get("nodes", []))
    novel = [node for node in matched_nodes if normalize(node["label"]) not in team_labels]
    novel_ratio = len(novel) / len(matched_nodes) if matched_nodes else 0
    novel_contribution = round(45 + novel_ratio * 20) if matched_nodes else 0

    connected_ids = {
        endpoint
        for edge in candidate.get("edges", [])
        for endpoint in (edge.get("source"), edge.get("target"))
        if endpoint
    }
    verifiable = [node for node in matched_nodes if node.get("evidence_ids") and node["id"] in connected_ids]
    verification_readiness = round(55 + 35 * len(verifiable) / len(matched_nodes)) if matched_nodes else 0

    scores = {
        "gap_coverage": direct_coverage,
        "semantic_alignment": semantic_alignment,
        "evidence_strength": evidence_strength,
        "novel_contribution": min(100, novel_contribution),
        "verification_readiness": min(100, verification_readiness),
    }
    rubric = [
        {
            "id": key,
            "label": label,
            "weight": round(weight * 100),
            "score": scores[key],
            "weighted_points": round(scores[key] * weight, 1),
            "description": description,
        }
        for key, label, weight, description in RUBRIC
    ]
    overall = round(sum(item["weighted_points"] for item in rubric))

    clusters = []
    for cluster in candidate.get("summary", {}).get("primary_clusters", []):
        clusters.append(
            {
                "name": cluster.get("name") or cluster.get("label"),
                "node_ids": cluster.get("node_ids", []),
            }
        )

    evidence_samples = {}
    for node in nodes:
        snippets = []
        for evidence_id in node.get("evidence_ids", []):
            record = evidence_by_id.get(evidence_id)
            if record:
                snippets.append(record.get("excerpt") or record.get("text") or record.get("content") or "")
        evidence_samples[node["id"]] = [snippet for snippet in snippets if snippet][:2]

    questions = []
    templates = [
        "Walk us through one concrete system where you personally used {claim}. What was the boundary of your ownership?",
        "If you had to reproduce your {claim} work inside Amazon Bedrock AgentCore, what are the first three implementation checks you would make?",
        "What failed or produced a misleading result when you applied {claim}, and how did you detect and correct it?",
        "Which alternative did you reject when using {claim}, and what evidence drove that decision?",
    ]
    question_types = ["Transfer test", "Reproduction", "Experience probe", "Security probe"]
    for index, gap in enumerate(gap_results):
        match = gap["matches"][0] if gap["matches"] else None
        if match:
            question = templates[index % 4].format(claim=match["label"])
            claim_id = match["node_id"]
            claim = match["label"]
            evidence_ids = match["evidence_ids"]
            question_type = question_types[index % len(question_types)]
        else:
            question = f"Your profile does not show direct {gap['short']} experience. What is the closest system you personally built, and what would you need to learn before owning this capability?"
            claim_id = None
            claim = "No explicit profile claim"
            evidence_ids = []
            question_type = question_types[index % len(question_types)]
        questions.append(
            {
                "id": f"question_{index + 1}",
                "gap_id": gap["id"],
                "gap": gap["short"],
                "claim_id": claim_id,
                "claim": claim,
                "evidence_ids": evidence_ids,
                "question_type": question_type,
                "question": question,
                "status": "Claimed",
            }
        )

    return {
        "candidate": {
            "id": candidate["person"]["id"],
            "display_name": "Candidate 01",
            "headline": candidate["person"].get("headline", ""),
            "knowledge_status": "Claimed",
            "nodes": nodes,
            "edges": candidate.get("edges", []),
            "clusters": clusters,
            "evidence_count": len(candidate.get("evidence", [])),
            "source_note": "Authorized stored LinkedIn KG snapshot; no live scraping or platform API.",
        },
        "fit": {
            "overall": overall,
            "label": "Strong direct evidence" if overall >= 75 else "Targeted verification required" if overall >= 40 else "Limited direct fit",
            "potential_fit": f"{sum(1 for gap in gap_results if gap['fit'] > 0)}/{len(gap_results)}",
            "verified_fit": f"0/{len(gap_results)}",
            "gap_results": gap_results,
            "rubric": rubric,
            "decision_guardrail": "No direct AWS Bedrock evidence was found. Transferable claims may justify targeted questions, but they are not verified AWS expertise and do not support an automated hiring decision.",
        },
        "questions": questions,
        "evidence_samples": evidence_samples,
        "team_totals": team["totals"],
    }


class WemeshHandler(SimpleHTTPRequestHandler):
    server_version = "WEMESH/1.0"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, directory=str(APP_DIR), **kwargs)

    def log_message(self, format: str, *args: Any) -> None:
        # Never log profile URLs or candidate payloads.
        if self.path.startswith("/api/analyze"):
            return
        super().log_message(format, *args)

    def end_headers(self) -> None:
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'self'",
        )
        super().end_headers()

    def send_json(self, payload: dict[str, Any], status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        started = time.perf_counter()
        if self.path == "/api/health":
            team = team_payload()
            self.send_json(
                {
                    "ok": True,
                    "data": {"status": "ready", "mode": "deterministic-demo", "fixtures": team["totals"]},
                    "meta": {"duration_ms": round((time.perf_counter() - started) * 1000, 2)},
                }
            )
            return
        if self.path == "/api/team":
            self.send_json({"ok": True, "data": team_payload()})
            return
        if self.path in {"/", "/index.html"}:
            self.path = "/index.html"
        super().do_GET()

    def do_POST(self) -> None:
        if self.path != "/api/analyze":
            self.send_json({"ok": False, "error": "Not found"}, HTTPStatus.NOT_FOUND)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > 8192:
                raise ValueError("Invalid request size.")
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            if payload.get("authorized") is not True:
                self.send_json(
                    {"ok": False, "error": "Confirm that this profile is authorized for recruiting review."},
                    HTTPStatus.FORBIDDEN,
                )
                return
            linkedin_url = validate_linkedin_url(str(payload.get("linkedin_url", "")))
            if normalize(linkedin_url.rstrip("/")) != normalize(AUTHORIZED_PROFILE_URL.rstrip("/")):
                self.send_json(
                    {
                        "ok": False,
                        "error": "This deterministic demo recognizes the pre-authorized Candidate 01 profile snapshot only. Use the demo URL shown in the field.",
                    },
                    HTTPStatus.UNPROCESSABLE_ENTITY,
                )
                return
            candidate = load_json(DATA_DIR / "sehyeog-kim-kg.json")
            self.send_json({"ok": True, "data": score_candidate(candidate)})
        except (ValueError, json.JSONDecodeError) as exc:
            self.send_json({"ok": False, "error": str(exc)}, HTTPStatus.BAD_REQUEST)
        except FileNotFoundError:
            self.send_json({"ok": False, "error": "Required KG fixture is unavailable."}, HTTPStatus.INTERNAL_SERVER_ERROR)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the WEMESH hackathon demo")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=3000)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), WemeshHandler)
    print(f"WEMESH ready at http://{args.host}:{args.port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
