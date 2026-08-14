#!/usr/bin/env python3
"""Deploy the standard-library WEMESH demo to a private Daytona sandbox."""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

from daytona import (
    CreateSandboxFromSnapshotParams,
    Daytona,
    FileUpload,
    SessionExecuteRequest,
)


ROOT = Path(__file__).resolve().parent
FILES = [
    ROOT / "wemesh_app" / "server.py",
    ROOT / "wemesh_app" / "index.html",
    ROOT / "data" / "sehyeog-kim-kg.json",
    ROOT / "data" / "aws-team" / "aws_engineer_a.json",
    ROOT / "data" / "aws-team" / "aws_engineer_b.json",
    ROOT / "data" / "aws-team" / "aws_engineer_c_sarath_krishnan_kg.json",
    ROOT / "data" / "aws-team" / "aws_engineer_d_sriharsha_ms_kg.json",
    ROOT / "data" / "aws-team" / "aws_engineer_e.json",
    ROOT / "data" / "aws-team" / "aws_engineer_f.json",
    ROOT / "data" / "aws-team" / "representative-aws-genai-team-agenda.json",
]


def require_files() -> None:
    missing = [str(path.relative_to(ROOT)) for path in FILES if not path.exists()]
    if missing:
        raise SystemExit(f"Missing deployment files: {', '.join(missing)}")


def output_url(preview: object) -> str:
    for attribute in ("url", "preview_url", "signed_url"):
        value = getattr(preview, attribute, None)
        if value:
            return str(value)
    if hasattr(preview, "model_dump"):
        dumped = preview.model_dump()
        for key in ("url", "preview_url", "signed_url"):
            if dumped.get(key):
                return str(dumped[key])
    return str(preview)


def deploy(ttl_minutes: int, preview_seconds: int) -> None:
    if not os.getenv("DAYTONA_API_KEY"):
        raise SystemExit("Set DAYTONA_API_KEY in the environment before deploying.")
    require_files()
    client = Daytona()
    sandbox = client.create(
        CreateSandboxFromSnapshotParams(
            name=f"wemesh-demo-{int(time.time())}",
            language="python",
            public=False,
            ephemeral=True,
            ttl_minutes=ttl_minutes,
            labels={"project": "wemesh", "purpose": "hackathon-demo"},
        ),
        timeout=120,
    )
    work_dir = sandbox.get_work_dir()
    remote_root = f"{work_dir}/wemesh"
    sandbox.process.exec(
        f"mkdir -p '{remote_root}/wemesh_app' '{remote_root}/data/aws-team'",
        timeout=30,
    )
    uploads = []
    for local_path in FILES:
        relative = local_path.relative_to(ROOT).as_posix()
        uploads.append(FileUpload(source=str(local_path), destination=f"{remote_root}/{relative}"))
    sandbox.fs.upload_files(uploads)

    session_id = "wemesh-server"
    sandbox.process.create_session(session_id)
    launch = sandbox.process.execute_session_command(
        session_id,
        SessionExecuteRequest(
            command=f"cd '{remote_root}' && python3 wemesh_app/server.py --host 0.0.0.0 --port 3000",
            run_async=True,
        ),
        timeout=30,
    )
    time.sleep(2)
    health = sandbox.process.exec(
        "python3 -c \"import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:3000/api/health').read().decode())\"",
        cwd=remote_root,
        timeout=20,
    )
    if health.exit_code != 0:
        raise RuntimeError(f"WEMESH health check failed: {health.result}")
    preview = sandbox.create_signed_preview_url(3000, expires_in_seconds=preview_seconds)
    result = {
        "sandbox_id": sandbox.id,
        "session_id": session_id,
        "command_id": getattr(launch, "cmd_id", None) or getattr(launch, "command_id", None),
        "preview_url": output_url(preview),
        "health": json.loads(health.result),
        "ttl_minutes": ttl_minutes,
    }
    print(json.dumps(result, indent=2))


def delete(sandbox_id: str) -> None:
    if not os.getenv("DAYTONA_API_KEY"):
        raise SystemExit("Set DAYTONA_API_KEY in the environment before deleting.")
    client = Daytona()
    sandbox = client.get(sandbox_id)
    client.delete(sandbox, wait=True)
    print(f"Deleted Daytona sandbox {sandbox_id}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Deploy or clean up the WEMESH Daytona demo")
    parser.add_argument("--ttl-minutes", type=int, default=180)
    parser.add_argument("--preview-seconds", type=int, default=10_800)
    parser.add_argument("--delete", metavar="SANDBOX_ID")
    args = parser.parse_args()
    if args.delete:
        delete(args.delete)
    else:
        deploy(args.ttl_minutes, args.preview_seconds)


if __name__ == "__main__":
    main()
