from flask import current_app as app
from pathlib import Path
from h3.db import db
from h3.models import *
import json

"""
This is responsible for backing up and restoring data whitin the tables.
"""



def backup():
    backup_path = Path(app.config['BACKUP_PATH'])
    backup_path.mkdir(parents=True, exist_ok=True)

    models = {
        mapper.class_.__name__: mapper.class_
        for mapper in db.Model.registry.mappers
    }

    for model in models.values():
        if hasattr(model, '__tablename__') and hasattr(model, 'to_dict'):
            filename = backup_path / f"{model.__tablename__}.csv"
            with open(filename, 'w') as file:
                for row in model.query.all():
                    file.write(json.dumps(row.to_dict()) + '\n')

def _reorder_models(innput_models, restore_order):
    models = {
        name: innput_models[name]
            for name in restore_order if name in innput_models
        }
    
    remaining_models = {
        name: model 
            for name, model in innput_models.items() if name not in restore_order
        }
    
    models.update(remaining_models)
    return models

def restore():
    backup_path = Path(app.config['BACKUP_PATH'])
    restore_order = [
            "Player",
            "Town", "HeroClass", "Hero", 
            "Color", 
            "Template", "Tournament",
            # "Match",
            # "MatchOpponent"

        ]
    models = {
        mapper.class_.__name__: mapper.class_
        for mapper in db.Model.registry.mappers
    }

    models = _reorder_models(models, restore_order)

    for model in models.values():
        if hasattr(model, '__tablename__') and hasattr(model, 'from_dict'):
            filename = backup_path / f"{model.__tablename__}.csv"
            with open(filename, 'r') as file:
                for line in file:
                    data = json.loads(line)
                    item = model.from_dict(data)
                    db.session.add(item)
        db.session.commit()    