# WEMESH Daytona Demo

## Local run

From the repository root:

```bash
.venv/bin/python wemesh_app/server.py --host 0.0.0.0 --port 3000
```

Open `http://localhost:3000` and confirm `http://localhost:3000/api/health` returns `status: ready`.

## Daytona deploy

Rotate the old hardcoded credential first, then provide the replacement only through the environment:

```bash
export DAYTONA_API_KEY="..."
.venv/bin/python Daytona_main.py
```

The launcher creates a private, ephemeral Python sandbox, uploads the HTML/server and local KG fixtures, runs the app on port `3000`, verifies `/api/health`, and prints a three-hour signed preview URL. The sandbox auto-deletes after 180 minutes.

To remove it early:

```bash
.venv/bin/python deploy_daytona.py --delete SANDBOX_ID
```

## Demo sequence

1. Confirm the pre-authorized Candidate 01 LinkedIn URL.
2. Select **Build KG & Evaluate Fit**.
3. Open the **Representative AWS GenAI Team** explorer: Group overview → Engineer A–F. Show that the six actual member KGs total 135 nodes and 123 semantic relations.
4. Show the Team KG → Hiring Priorities → Candidate KG schematic.
5. Open the **Actual Candidate Knowledge Graph**. Start with the 5 transferable-evidence nodes, switch to **All knowledge (38)**, and click a node to reveal its evidence and semantic relation count.
6. Explain the corrected assessment: `46/100`, direct AWS evidence `0`, transferable evidence for `2/6` capabilities, and no explicit evidence for the other four.
7. Open the five-part rubric and six capability-level evidence traces.
8. Enter **Interview Mode** and change claims from `Claimed` to `Verified`, `Needs Follow-up`, or `Not Verified`.
9. Confirm human sign-off.

The URL resolves to the already-extracted authorized KG snapshot. The demo does not scrape LinkedIn or call a LinkedIn API. All candidate knowledge remains claimed until interview verification.
