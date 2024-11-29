from flask import current_app as app
from pathlib import Path
from h3.db import db
from h3.models import *
import json
from typing import List

def export_to_ui():
    matches: List[Match] = Match.query.all()
    filters = {
        'color_id': [],
        'player_id': [],
        'hero_id': [],
        'town_id': []
    }
    for match in matches:
        filters['color_id'].append(match.color_id)
        filters['player_id'].append(match.player_id)
        filters['hero_id'].append(match.hero_id)
        filters['town_id'].append(match.town_id)


    filters['color_id'] = list(set(filters['color_id']))
    filters['player_id'] = list(set(filters['player_id']))
    filters['hero_id'] = list(set(filters['hero_id']))
    filters['town_id'] = list(set(filters['town_id']))

    data = {
        "matches": [match.to_dict() for match in Match.query.all()],
        "filters": filters,
        "players": [player.to_dict() for player in Player.query.all()],
    }
    path = Path(app.config['UI_EXPORT_PATH'])
    path.mkdir(parents=True, exist_ok=True)

    with open(path / f"index.json", "w") as f:
        json.dump(data, f)