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
        "name": "Rampart",
        "heroes": [
            {
                "name": "Clancy",
                "hero_class": "Ranger",
            },
            {
                "name": "Ivor",
                "hero_class": "Ranger",
            },
            {
                "name": "Jenova",
                "hero_class": "Ranger",
            },
            {
                "name": "Kyrre",
                "hero_class": "Ranger",
            },
            {
                "name": "Mephala",
                "hero_class": "Ranger",
            },
            {
                "name": "Ryland",
                "hero_class": "Ranger",
            },
            {
                "name": "Thorgrim",
                "hero_class": "Ranger",
            },
            {
                "name": "Ufretin",
                "hero_class": "Ranger",
            },
            {
                "name": "Gelu",
                "hero_class": "Ranger",
            },
            {
                "name": "Giselle",
                "hero_class": "Ranger",
            },
            {
                "name": "Aeris",
                "hero_class": "Druid",
            },
            {
                "name": "Alagar",
                "hero_class": "Druid",
            },
            {
                "name": "Coronius",
                "hero_class": "Druid",
            },
            {
                "name": "Elleshar",
                "hero_class": "Druid",
            },
            {
                "name": "Gem",
                "hero_class": "Druid",
            },
            {
                "name": "Malcom",
                "hero_class": "Druid",
            },
            {
                "name": "Melodia",
                "hero_class": "Druid",
            },
            {
                "name": "Uland",
                "hero_class": "Druid",
            }
        ]
    },
    {
        "name": "Tower",
        "heroes": [
            {
                "name": "Fafner",
                "hero_class": "Alchemist",
            },
            {
                "name": "Iona",
                "hero_class": "Alchemist",
            },
            {
                "name": "Josephine",
                "hero_class": "Alchemist",
            },
            {
                "name": "Neela",
                "hero_class": "Alchemist",
            },
            {
                "name": "Piquedram",
                "hero_class": "Alchemist",
            },
            {
                "name": "Rissa",
                "hero_class": "Alchemist",
            },
            {
                "name": "Thane",
                "hero_class": "Alchemist",
            },
            {
                "name": "Torosar",
                "hero_class": "Alchemist",
            },
            {
                "name": "Aine",
                "hero_class": "Wizard",
            },
            {
                "name": "Astral",
                "hero_class": "Wizard",
            },
            {
                "name": "Cyra",
                "hero_class": "Wizard",
            },
            {
                "name": "Daremyth",
                "hero_class": "Wizard",
            },
            {
                "name": "Halon",
                "hero_class": "Wizard",
            },
            {
                "name": "Serena",
                "hero_class": "Wizard",
            },
            {
                "name": "Solmyr",
                "hero_class": "Wizard",
            },
            {
                "name": "Theodorus",
                "hero_class": "Wizard",
            },
            {
                "name": "Dracon",
                "hero_class": "Wizard",
            }
        ]
    },
    {
        "name": "Inferno",
        "heroes": [
            {
                "name": "Calh",
                "hero_class": "Demoniac",
            },
            {
                "name": "Fiona",
                "hero_class": "Demoniac",
            },
            {
                "name": "Ignatius",
                "hero_class": "Demoniac",
            },
            {
                "name": "Marius",
                "hero_class": "Demoniac",
            },
            {
                "name": "Nymus",
                "hero_class": "Demoniac",
            },
            {
                "name": "Octavia",
                "hero_class": "Demoniac",
            },
            {
                "name": "Pyre",
                "hero_class": "Demoniac",
            },
            {
                "name": "Rashka",
                "hero_class": "Demoniac",
            },
            {
                "name": "Xeron",
                "hero_class": "Demoniac",
            },
            {
                "name": "Ash",
                "hero_class": "Heretic",
            },
            {
                "name": "Axsis",
                "hero_class": "Heretic",
            },
            {
                "name": "Ayden",
                "hero_class": "Heretic",
            },
            {
                "name": "Calid",
                "hero_class": "Heretic",
            },
            {
                "name": "Olema",
                "hero_class": "Heretic",
            },
            {
                "name": "Xarfax",
                "hero_class": "Heretic",
            },
            {
                "name": "Xyron",
                "hero_class": "Heretic",
            },
            {
                "name": "Zydar",
                "hero_class": "Heretic",
            }
        ]
    },
    {
        "name": "Necropolis",
        "heroes": [
            {
                "name": "Charna",
                "hero_class": "Death Knight",
            },
            {
                "name": "Clavius",
                "hero_class": "Death Knight",
            },
            {
                "name": "Galthran",
                "hero_class": "Death Knight",
            },
            {
                "name": "Isra",
                "hero_class": "Death Knight",
            },
            {
                "name": "Moandor",
                "hero_class": "Death Knight",
            },
            {
                "name": "Straker",
                "hero_class": "Death Knight",
            },
            {
                "name": "Tamika",
                "hero_class": "Death Knight",
            },
            {
                "name": "Vokial",
                "hero_class": "Death Knight",
            },
            {
                "name": "Haart Lich",
                "hero_class": "Death Knight",
            },
            {
                "name": "Ranloo",
                "hero_class": "Death Knight",
            },
            {
                "name": "Aislinn",
                "hero_class": "Necromancer",
            },
            {
                "name": "Nagash",
                "hero_class": "Necromancer",
            },
            {
                "name": "Nimbus",
                "hero_class": "Necromancer",
            },
            {
                "name": "Sandro",
                "hero_class": "Necromancer",
            },
            {
                "name": "Septienna",
                "hero_class": "Necromancer",
            },
            {
                "name": "Thant",
                "hero_class": "Necromancer",
            },
            {
                "name": "Vidomina",
                "hero_class": "Necromancer",
            },
            {
                "name": "Xsi",
                "hero_class": "Necromancer",
            }
        ]
    },
    {
        "name": "Dungeon",
        "heroes": [
            {
                "name": "Ajit",
                "hero_class": "Overlord",
            },
            {
                "name": "Arlach",
                "hero_class": "Overlord",
            },
            {
                "name": "Dace",
                "hero_class": "Overlord",
            },
            {
                "name": "Damacon",
                "hero_class": "Overlord",
            },
            {
                "name": "Gunnar",
                "hero_class": "Overlord",
            },
            {
                "name": "Lorelei",
                "hero_class": "Overlord",
            },
            {
                "name": "Shakti",
                "hero_class": "Overlord",
            },
            {
                "name": "Synca",
                "hero_class": "Overlord",
            },
            {
                "name": "Mutare",
                "hero_class": "Overlord",
            },
            {
                "name": "Mutare Drake",
                "hero_class": "Overlord",
            },
            {
                "name": "Alamar",
                "hero_class": "Warlock",
            },
            {
                "name": "Darkstorn",
                "hero_class": "Warlock",
            },
            {
                "name": "Deemer",
                "hero_class": "Warlock",
            },
            {
                "name": "Geon",
                "hero_class": "Warlock",
            },
            {
                "name": "Jaegar",
                "hero_class": "Warlock",
            },
            {
                "name": "Jeddite",
                "hero_class": "Warlock",
            },
            {
                "name": "Malekith",
                "hero_class": "Warlock",
            },
            {
                "name": "Sephinroth",
                "hero_class": "Warlock",
            }
        ]
    },
    {
        "name": "Stronghold",
        "heroes": [
            {
                "name": "Crag Hack",
                "hero_class": "Barbarian",
            },
            {
                "name": "Gretchin",
                "hero_class": "Barbarian",
            },
            {
                "name": "Gurnisson",
                "hero_class": "Barbarian",
            },
            {
                "name": "Jabarkas",
                "hero_class": "Barbarian",
            },
            {
                "name": "Krellion",
                "hero_class": "Barbarian",
            },
            {
                "name": "Shiva",
                "hero_class": "Barbarian",
            },
            {
                "name": "Tyraxor",
                "hero_class": "Barbarian",
            },
            {
                "name": "Yog",
                "hero_class": "Barbarian",
            },
            {
                "name": "Boragus",
                "hero_class": "Barbarian",
            },
            {
                "name": "Kilgor",
                "hero_class": "Barbarian",
            },
            {
                "name": "Dessa",
                "hero_class": "Battle Mage",
            },
            {
                "name": "Gird",
                "hero_class": "Battle Mage",
            },
            {
                "name": "Gundula",
                "hero_class": "Battle Mage",
            },
            {
                "name": "Oris",
                "hero_class": "Battle Mage",
            },
            {
                "name": "Saurug",
                "hero_class": "Battle Mage",
            },
            {
                "name": "Terek",
                "hero_class": "Battle Mage",
            },
            {
                "name": "Vey",
                "hero_class": "Battle Mage",
            },
            {
                "name": "Zubin",
                "hero_class": "Battle Mage",
            }
        ]

    },
    {
        "name": "Fortress",
        "heroes": [
            {
                "name": "Alkin",
                "hero_class": "Beastmaster",
            },
            {
                "name": "Broghild",
                "hero_class": "Beastmaster",
            },
            {
                "name": "Bron",
                "hero_class": "Beastmaster",
            },
            {
                "name": "Drakon",
                "hero_class": "Beastmaster",
            },
            {
                "name": "Gerwulf",
                "hero_class": "Beastmaster",
            },
            {
                "name": "Korbac",
                "hero_class": "Beastmaster",
            },
            {
                "name": "Tazar",
                "hero_class": "Beastmaster",
            },
            {
                "name": "Wystan",
                "hero_class": "Beastmaster",
            },
            {
                "name": "Andra",
                "hero_class": "Witch",
            },
            {
                "name": "Merist",
                "hero_class": "Witch",
            },
            {
                "name": "Mirlanda",
                "hero_class": "Witch",
            },
            {
                "name": "Rosic",
                "hero_class": "Witch",
            },
            {
                "name": "Styg",
                "hero_class": "Witch",
            },
            {
                "name": "Tiva",
                "hero_class": "Witch",
            },
            {
                "name": "Verdish",
                "hero_class": "Witch",
            },
            {
                "name": "Voy",
                "hero_class": "Witch",
            },
            {
                "name": "Adrienne",
                "hero_class": "Witch",
            },
            {
                "name": "Kinkeria",
                "hero_class": "Witch",
            }
        ]
    },
    {
        "name": "Conflux",
        "heroes": [
            {
                "name": "Erdamon",
                "hero_class": "Planeswalker",
            },
            {
                "name": "Fiur",
                "hero_class": "Planeswalker",
            },
            {
                "name": "Ignissa",
                "hero_class": "Planeswalker",
            },
            {
                "name": "Lacus",
                "hero_class": "Planeswalker",
            },
            {
                "name": "Kalt",
                "hero_class": "Planeswalker",
            },
            {
                "name": "Monere",
                "hero_class": "Planeswalker",
            },
            {
                "name": "Pasis",
                "hero_class": "Planeswalker",
            },
            {
                "name": "Thunar",
                "hero_class": "Planeswalker",
            },
            {
                "name": "Aenain",
                "hero_class": "Elementalist",
            },
            {
                "name": "Brissa",
                "hero_class": "Elementalist",
            },
            {
                "name": "Ciele",
                "hero_class": "Elementalist",
            },
            {
                "name": "Gelare",
                "hero_class": "Elementalist",
            },
            {
                "name": "Grindan",
                "hero_class": "Elementalist",
            },
            {
                "name": "Inteus",
                "hero_class": "Elementalist",
            },
            {
                "name": "Labetha",
                "hero_class": "Elementalist",
            },
            {
                "name": "Luna",
                "hero_class": "Elementalist",
            }
        ]
    },
    {
        "name": "Cove",
        "heroes": [
            {
                "name": "Anabel",
                "hero_class": "Captain",
            },
            {
                "name": "Cassiopeia",
                "hero_class": "Captain",
            },
            {
                "name": "Corkes",
                "hero_class": "Captain",
            },
            {
                "name": "Derek",
                "hero_class": "Captain",
            },
            {
                "name": "Elmore",
                "hero_class": "Captain",
            },
            {
                "name": "Illor",
                "hero_class": "Captain",
            },
            {
                "name": "Jeremy",
                "hero_class": "Captain",
            },
            {
                "name": "Leena",
                "hero_class": "Captain",
            },
            {
                "name": "Miriam",
                "hero_class": "Captain",
            },
            {
                "name": "Bidley",
                "hero_class": "Captain",
            },
            {
                "name": "Tark",
                "hero_class": "Captain",
            },
            {
                "name": "Andal",
                "hero_class": "Navigator",
            },
            {
                "name": "Astra",
                "hero_class": "Navigator",
            },
            {
                "name": "Casmetra",
                "hero_class": "Navigator",
            },
            {
                "name": "Dargem",
                "hero_class": "Navigator",
            },
            {
                "name": "Eovacius",
                "hero_class": "Navigator",
            },
            {
                "name": "Manfred",
                "hero_class": "Navigator",
            },
            {
                "name": "Spint",
                "hero_class": "Navigator",
            },
            {
                "name": "Zilare",
                "hero_class": "Navigator",
            }
        ]
    },
    {
        "name": "Factory",
        "heroes": [
            {
                "name": "Henrietta",
                "hero_class": "Mercenary",
            },
            {
                "name": "Sam",
                "hero_class": "Mercenary",
            },
            {
                "name": "Tancred",
                "hero_class": "Mercenary",
            },
            {
                "name": "Melchior",
                "hero_class": "Mercenary",
            },
            {
                "name": "Floribert",
                "hero_class": "Mercenary",
            },
            {
                "name": "Wynona",
                "hero_class": "Mercenary",
            },
            {
                "name": "Dury",
                "hero_class": "Mercenary",
            },
            {
                "name": "Morton",
                "hero_class": "Mercenary",
            },
            {
                "name": "Tavin",
                "hero_class": "Mercenary",
            },
            {
                "name": "Murdoch",
                "hero_class": "Mercenary",
            },
            {
                "name": "Celestine",
                "hero_class": "Artificer",
            },
            {
                "name": "Todd",
                "hero_class": "Artificer",
            },
            {
                "name": "Agar",
                "hero_class": "Artificer",
            },
            {
                "name": "Bertram",
                "hero_class": "Artificer",
            },
            {
                "name": "Wrathmont",
                "hero_class": "Artificer",
            },
            {
                "name": "Ziph",
                "hero_class": "Artificer",
            },
            {
                "name": "Victoria",
                "hero_class": "Artificer",
            },
            {
                "name": "Eanswythe",
                "hero_class": "Artificer",
            },
            {
                "name": "Frederick",
                "hero_class": "Artificer",
            }
        ]
    }
]
templates = [
    {
        "name": "Duel",
        "website": "https://www.h3templates.com/mkc/duel"
    },
    {
        "name": "Basic",
        "website": "https://www.h3templates.com/mkc/basic"
    },
    {
        "name": "Jebus Outcast",
        "website": "https://www.h3templates.com/mkc/jebus-outcast"
    },
    {
        "name": "mt_JO",
        "website": "https://www.h3templates.com/mkc/mt-jo"
    },
    {
        "name": "mt_SM",
        "website": "https://www.h3templates.com/mkc/mt-sm"
    },
    {
        "name": "Shadow Economy",
        "website": "https://www.h3templates.com/mkc/shadow-economy"
    },
    {
        "name": "Jerusalem Cross",
        "website": "https://www.h3templates.com/mkc/jerusalem-cross"
    },
    {
        "name": "Souverain",
        "website": "https://www.h3templates.com/mkc/souverain"
    },
    {
        "name": "[1 Hero] 6lm10a",
        "website": "https://www.h3templates.com/mkc/1-hero-6lm10a"
    },
    {
        "name": "h3dm1",
        "website": "https://h3hota.com/en/templates#mirror-templates/h3dm1"
    },
    {
        "name": "mt_Diamond",
        "website": "https://h3hota.com/en/templates#mirror-templates/mt_diamond"
    },
    {
        "name": "mt_Jebus",
        "website": "https://h3hota.com/en/templates#mirror-templates/mt_jebus"
    },
    {
        "name": "mt_TeamJebus",
        "website": "https://h3hota.com/en/templates#mirror-templates/mt_teamjebus"
    },
    {
        "name": "mt_Andromeda",
        "website": "https://h3hota.com/en/templates#mirror-templates/mt_andromeda"
    },
    {
        "name": "mt_Antares",
        "website": "https://h3hota.com/en/templates#mirror-templates/mt_antares"
    },
    {
        "name": "mt_Firewalk",
        "website": "https://h3hota.com/en/templates#mirror-templates/mt_firewalk"
    },
    {
        "name": "6lm10a",
        "website": "https://h3hota.com/en/templates#xl-u-templates/6lm10a"
    },
    {
        "name": "8mm6a",
        "website": "https://h3hota.com/en/templates#xl-u-templates/8mm6a"
    },
    {
        "name": "8xm12a",
        "website": "https://h3hota.com/en/templates#xl-u-templates/8xm12a"
    },
    {
        "name": "Spider",
        "website": "https://h3hota.com/en/templates#xl-u-templates/spider"
    },
    {
        "name": "Nostalgia",
        "website": "https://h3hota.com/en/templates#xl-u-templates/nostalgia"
    },
    {
        "name": "Kerberos",
        "website": "https://h3hota.com/en/templates#xl-u-templates/kerberos"
    },
    {
        "name": "Clash of Dragons",
        "website": "https://h3hota.com/en/templates#xl-u-templates/clash-of-dragons"
    },
    {
        "name": "Firewalk",
        "website": "https://h3hota.com/en/templates#xl-u-templates/firewalk"
    },
    {
        "name": "Jebus Cross",
        "website": "https://h3hota.com/en/templates#xl-u-templates/jebus-cross"
    },
    {
        "name": "2sm4d(3)",
        "website": "https://h3hota.com/en/templates#l-u-templates/2sm4d3"
    },
    {
        "name": "Mini-Nostalgia",
        "website": "https://h3hota.com/en/templates#l-u-templates/mini-nostalgia"
    },
    {
        "name": "Diamond",
        "website": "https://h3hota.com/en/templates#l-u-templates/diamond"
    },
    {
        "name": "Boomerang",
        "website": "https://h3hota.com/en/templates#l-u-templates/boomerang"
    },
    {
        "name": "Apocalypse",
        "website": "https://h3hota.com/en/templates#l-u-templates/apocalypse"
    },
    {
        "name": "Anarchy",
        "website": "https://h3hota.com/en/templates#l-u-templates/anarchy"
    },
    {
        "name": "Black’n’Blue",
        "website": "https://h3hota.com/en/templates#l-u-templates/blacknblue"
    },
    {
        "name": "2sm2c(2)",
        "website": "https://h3hota.com/en/templates#m200-templates/2sm2c2"
    },
    {
        "name": "Skirmish(M)",
        "website": "https://h3hota.com/en/templates#m200-templates/skirmishm"
    },
    {
        "name": "Nine-day Wonder",
        "website": "https://h3hota.com/en/templates#m200-templates/nine-day-wonder"
    }
]
colors = [
    "Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Teal", "Pink"
]
match_types = ["pvp", "pve", 'casting']

players = [
    {
        "name": "Lexiav",
        "youtube": "https://www.youtube.com/@Lexiav",
        "twitch": "https://www.twitch.tv/lexiav",
    },
    {
        "name": "StygianOne",
        "youtube": "https://www.youtube.com/@StygianOne",
        "twitch": "https://www.twitch.tv/stygianone",
    },
]

def generate_static_data():
    """Generating Heroes of Might and Magic III towns"""
    for match_type in match_types:
        db.session.add(MatchType.create_item(match_type))
    db.session.commit()

    for color in colors:
        db.session.add(Color.create_item(color))
    db.session.commit()

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

    for template_data in templates:
        template = Template.create_item(template_data["name"], template_data["website"])
        db.session.add(template)
    db.session.commit()
        # ... add other objects

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
    