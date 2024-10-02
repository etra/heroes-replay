from h3.db import db, session
from h3.models import *

hero_classes = [
    {
        "name": "Knight"
    },
    {
        "name": "Cleric"
    },
    {
        "name": "Ranger"
    },
    {
        "name": "Druid"
    },
    {
        "name": "Alchemist"
    },
    {
        "name": "Wizard"
    },
    {
        "name": "Demoniac"
    },
    {
        "name": "Heretic"
    },
    {
        "name": "Death Knight"
    },
    {
        "name": "Necromancer"
    },
    {
        "name": "Overlord"
    },
    {
        "name": "Warlock"
    },
    {
        "name": "Barbarian"
    },
    {
        "name": "Battle Mage"
    },
    {
        "name": "Beastmaster"
    },
    {
        "name": "Witch"
    },
    {
        "name": "Planeswalker"
    },
    {
        "name": "Elementalist"
    },
    {
        "name": "Captain"
    },
    {
        "name": "Navigator"
    },
    {
        "name": "Mercenary"
    },
    {
        "name": "Artificer"
    }
]
towns = [
    {
        "name": "Castle",
        "heroes": [
            {
                "name": "Christian",
                "hero_class": "Knight",
            },
            {
                "name": "Edric",
                "hero_class": "Knight",
            },
            {
                "name": "Lord Haart",
                "hero_class": "Knight",
            },
            {
                "name": "Orrin",
                "hero_class": "Knight",
            },
            {
                "name": "Sorsha",
                "hero_class": "Knight",
            },
            {
                "name": "Sylvia",
                "hero_class": "Knight",
            },
            {
                "name": "Tyris",
                "hero_class": "Knight",
            },
            {
                "name": "Valeska",
                "hero_class": "Knight",
            },
            {
                "name": "Catherine",
                "hero_class": "Knight",
            },
            {
                "name": "Roland",
                "hero_class": "Knight",
            },
            {
                "name": "Sir Mullich",
                "hero_class": "Knight",
            },
            {
                "name": "Beatrice",
                "hero_class": "Knight",
            },
            {
                "name": "Adela",
                "hero_class": "Cleric",
            },
            {
                "name": "Adelaide",
                "hero_class": "Cleric",
            },
            {
                "name": "Caitlin",
                "hero_class": "Cleric",
            },
            {
                "name": "Cuthbert",
                "hero_class": "Cleric",
            },
            {
                "name": "Ingham",
                "hero_class": "Cleric",
            },
            {
                "name": "Loynis",
                "hero_class": "Cleric",
            },
            {
                "name": "Sanya",
                "hero_class": "Cleric",
            },
            {
                "name": "Rion",
                "hero_class": "Cleric",
            }
        ]
    },
    {
        "name": "Rampart"
    },
    {
        "name": "Tower"
    },
    {
        "name": "Inferno"
    },
    {
        "name": "Necropolis"
    },
    {
        "name": "Dungeon"
    },
    {
        "name": "Stronghold"
    },
    {
        "name": "Fortress"
    },
    {
        "name": "Conflux"
    },
    {
        "name": "Cove"
    },
    {
        "name": "Factory"
    }
]

def generate_static_data():
    """Generating Heroes of Might and Magic III towns"""
    for hero_class_data in hero_classes:
        hero_class = HeroClass.create_item(hero_class_data["name"])
        db.session.add(hero_class)
        db.session.commit()

    for town_data in towns:
        town = Town.create_town(town_data['name'])
        db.session.add(town)
        db.session.commit()
        if "heroes" in town_data:
            for hero_data in town_data["heroes"]:
                hero = Hero.create_item(
                    name=hero_data["name"], 
                    hero_class_name=hero_data["hero_class"], 
                    town_name=town_data["name"])
                
                db.session.add(hero)
        # ... add other objects
        db.session.commit()

    # town = Town.create_town("Castle")
    


    # db.session.add(town)

    # db.session.add(Town(name="Rampart"))
    # db.session.add(Town(name="Tower"))
    # db.session.add(Town(name="Inferno"))
    # db.session.add(Town(name="Necropolis"))
    # db.session.add(Town(name="Dungeon"))
    # db.session.add(Town(name="Stronghold"))
    # db.session.add(Town(name="Fortress"))
    # db.session.add(Town(name="Conflux"))
    # db.session.add(Town(name="Cove"))
    # db.session.add(Town(name="Factory"))
    