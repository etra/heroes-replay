from flask import current_app as app
from pathlib import Path
from h3.db import db
from h3.models import *
import json

def export_to_ui():
    path = Path(app.config['UI_EXPORT_PATH'])
    path.mkdir(parents=True, exist_ok=True)

    matches = Match.query.all()
    with open(path / f"matches.ndjson", "w") as f:
        for match in matches:
            match
            f.write(json.dumps(match.to_dict()))