import json
from pathlib import Path

from dependency_updater.src.maintenance import DependencyUpdater
import os

if not os.environ.get("SLACK_CHANNEL"):
    os.environ["SLACK_CHANNEL"] = "my-team-dependency-updater"
projects_json_path = Path(__file__).parent / "projects.json"
workdir = Path(__file__).parent / "workdir"

with open(projects_json_path, "r") as f:
    updater = DependencyUpdater(
        projects_json=json.load(f),
        workdir=workdir,
    )
    updater.run()
