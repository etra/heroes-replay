import json
from glob import glob
from dataclasses import dataclass
from typing import Dict, List, Union
from pathlib import Path
COLORS_PATH = 'database/static/colors.json'
HEROES_PATH = 'database/static/heroes.json'
TOWNS_PATH = 'database/static/towns.json'
TEMPLATES_PATH = 'database/static/templates.json'
TOURNAMENTS_PATH = 'database/static/tournaments.json'

PLAYER_DIR = 'database/players'
MATCHES_DIR = 'database/matches'

@dataclass(init=False)
class Repository:
    towns: Dict[str, 'Town']
    colors: Dict[str, 'Color']
    heroes: Dict[str, 'Hero']
    players: Dict[str, 'Player']
    
    templates: Dict[str, 'Template']
    tournaments: Dict[str, 'Tournament']

    matches: List['Match']

    def lookup_player(self, player_id: str) -> Union['Player']:
        return self.players.get(player_id, Player.empty(player_id))
    
    def lookup_hero(self, hero_id: str) -> Union['Hero']:
        return self.heroes.get(hero_id, Hero.empty(hero_id))
    
    def lookup_town(self, town_id: str) -> Union['Town']:
        return self.towns.get(town_id, Town.empty(town_id))
    
    def lookup_color(self, color_id: str) -> Union['Color']:
        return self.colors.get(color_id, Color.empty(color_id))
    
    def lookup_template(self, template_id: str) -> Union['Template']:
        return self.templates.get(template_id, Template.empty(template_id))
    
    def lookup_tournament(self, tournament_id: str) -> Union['Tournament']:
        return self.tournaments.get(tournament_id, Tournament.empty(tournament_id))
    
    @staticmethod
    def default():
        item = Repository()
        item.towns = Town.load_items(item)
        item.colors = Color.load_items(item)
        item.heroes = Hero.load_items(item)
        item.players = Player.load_items(item)
        item.templates = Template.load_items(item)
        item.tournaments = Tournament.load_items(item)
        item.matches = Match.load_items(item)
        return item


@dataclass
class RepositoryItem:
    repository: 'Repository'

    @staticmethod
    def load_items(repository: 'Repository') -> Union[Dict[str, 'RepositoryItem'], List['RepositoryItem']]:
        raise NotImplementedError
    
    @staticmethod
    def empty(item_id) -> 'RepositoryItem':
        raise NotImplementedError

    def to_dict(self):
        raise NotImplementedError

@dataclass(kw_only=True)
class Color(RepositoryItem):
    id: str
    name: str

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }
    
    @staticmethod
    def empty(color_id) -> 'Color':
        return Color(None, id=color_id, name=color_id)

    @staticmethod
    def load_items(repository: 'Repository') -> Dict[str, 'Color']:
        response = {}
        with open(COLORS_PATH, 'r') as f:
            colors = json.load(f)
            for color in colors:
                response[color['id']] = Color(repository, **color)
        return response
    

@dataclass(kw_only=True)
class Template(RepositoryItem):
    id: str
    name: str

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }
    
    @staticmethod
    def empty(template_id) -> 'Template':
        return Template(None, id=template_id, name=template_id)
    
    @staticmethod
    def load_items(repository: 'Repository') -> Dict[str, 'Template']:
        response = {}
        with open(TEMPLATES_PATH, 'r') as f:
            templates = json.load(f)
            for template in templates:
                response[template['id']] = Template(repository, **template)
        return response

@dataclass(kw_only=True)
class Tournament(RepositoryItem):
    id: str
    name: str

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }
    
    @staticmethod
    def empty(tournament_id) -> 'Tournament':
        return Tournament(None, id=tournament_id, name=tournament_id)

    @staticmethod
    def load_items(repository: 'Repository') -> Dict[str, 'Tournament']:
        response = {}
        with open(TOURNAMENTS_PATH, 'r') as f:
            tournaments = json.load(f)
            for tournament in tournaments:
                response[tournament['id']] = Tournament(repository, **tournament)
        return response

@dataclass(kw_only=True)
class Hero(RepositoryItem):
    id: str
    name: str
    hero_class_id: str
    town_id: str

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }
    
    @staticmethod
    def empty(hero_id) -> 'Hero':
        return Hero(None, id=hero_id, name=hero_id, hero_class_id='', town_id='')

    @staticmethod
    def load_items(repository: 'Repository') -> Dict[str, 'Hero']:
        response = {}
        with open(HEROES_PATH, 'r') as f:
            heroes = json.load(f)
            for hero in heroes:
                response[hero['id']] = Hero(repository, **hero)
        return response

@dataclass(kw_only=True)
class Town(RepositoryItem):
    id: str
    name: str

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }
    
    @staticmethod
    def empty(town_id) -> 'Town':
        return Town(None, id=town_id, name=town_id)

    @staticmethod
    def load_items(repository: 'Repository') -> Dict[str, 'Town']:
        response = {}
        with open(TOWNS_PATH, 'r') as f:
            towns = json.load(f)
            for town in towns:
                response[town['id']] = Town(repository, **town)
        return response

@dataclass(kw_only=True)
class Player(RepositoryItem):
    id: str
    name: str
    youtube: str;
    twitch: str;
    discord: str;
   
    def to_dict(self):
        return {
            'player_id': self.id,
            'name': self.name,
            'youtube': self.youtube,
            'twitch': self.twitch,
            'discord': self.discord
        }

    @staticmethod
    def empty(player_id) -> 'Player':
        return Player(None, id=player_id, name=player_id, youtube='', twitch='', discord='')

    @staticmethod
    def load_items(repository: 'Repository') -> List['Player']:
        response = {}
        for file in glob(f'{PLAYER_DIR}/*.json'):
            with open(file, 'r') as f:
                player = json.load(f)
                player_id = Path(file).name.replace('.json', '')
                player['id'] = player_id
                response[player['id']] = Player(repository, **player)
        return response

@dataclass(kw_only=True)
class Opponent(RepositoryItem):
    player_id: str
    town_id: str
    hero_id: str
    color_id: str

    def to_dict(self):
        return {
            'player_id': self.player_id,
            'town_id': self.town_id,
            'hero_id': self.hero_id,
            'color_id': self.color_id,

            'player': self.repository.lookup_player(self.player_id).to_dict(),
            'town': self.repository.lookup_town(self.town_id).to_dict(),
            'hero': self.repository.lookup_hero(self.hero_id).to_dict(),
            'color': self.repository.lookup_color(self.color_id).to_dict(),
            
            
            # 'player': if self.player_id in generator.players:
            #     generator.players[self.player_id].to_dict(),
        }

@dataclass(kw_only=True)
class Match(RepositoryItem):
    youtube_video_id: str
    youtube_vide_title: str

    template_id: str
    tournament_id: str

    player_id: str;
    town_id: str;
    hero_id: str;
    color_id: str;


    opponents: List[Opponent]

    def __post_init__(self):
        # Convert opponents from dicts to Opponent objects
        self.opponents = [
            Opponent(self.repository, **opponent) if isinstance(opponent, dict) else opponent 
            for opponent in self.opponents
            ]

    def to_dict(self):
        return {
            
            'thumbnail': f'https://i.ytimg.com/vi_webp/{self.youtube_video_id}/sddefault.webp',
            'video_id': self.youtube_video_id,
            'youtube_video_id': self.youtube_video_id,
            'youtube_vide_title': self.youtube_vide_title,
            'template_id': self.template_id,
            'tournament_id': self.tournament_id,

            'template': self.repository.lookup_template(self.template_id).to_dict(),
            'tournament': self.repository.lookup_tournament(self.tournament_id).to_dict(),

            'player_id': self.player_id,
            'town_id': self.town_id,
            'hero_id': self.hero_id,
            'color_id': self.color_id,
            
            'player': self.repository.lookup_player(self.player_id).to_dict(),
            'town': self.repository.lookup_town(self.town_id).to_dict(),
            'hero': self.repository.lookup_hero(self.hero_id).to_dict(),
            'color': self.repository.lookup_color(self.color_id).to_dict(),


            'opponents': [opponent.to_dict() for opponent in self.opponents]
        }

    @staticmethod
    def load_items(repository: 'Repository') -> List['Match']:
        response = []
        for file in glob(f'{MATCHES_DIR}/*.json'):
            with open(file, 'r') as f:
                match = json.load(f)
                if type(match) == dict:
                    response.append(Match(repository, **match))
                elif type(match) == list:
                    for match in match:
                        response.append(Match(repository, **match))
        return response

