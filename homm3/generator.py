from homm3.models import Repository

class Generator:

    repository: 'Repository'

    def __init__(self, repository: 'Repository') -> None:
        self.repository = repository

    def generate_index(self):
        
        flt = {
            'color_id': [],
            'player_id': [],
            'hero_id': [],
            'town_id': []
        }
        for match in self.repository.matches:
            flt['color_id'].append(match.color_id)
            flt['player_id'].append(match.player_id)
            flt['hero_id'].append(match.hero_id)
            flt['town_id'].append(match.town_id)


        flt['color_id'] = list(set(flt['color_id']))
        flt['player_id'] = list(set(flt['player_id']))
        flt['hero_id'] = list(set(flt['hero_id']))
        flt['town_id'] = list(set(flt['town_id']))




        return {
            "matches": [match.to_dict() for match in self.repository.matches],
            "filters": flt,
            "players": [player.to_dict() for player in self.repository.players.values()],
        }
    
    def generate_static(self):
        return {
            "templates": [template.to_dict() for template in self.repository.templates.values()],
            "tournaments": [tournament.to_dict() for tournament in self.repository.tournaments.values()],
            "players": [player.to_dict() for player in self.repository.players.values()],
            "towns": [town.to_dict() for town in self.repository.towns.values()],
            "heroes": [hero.to_dict() for hero in self.repository.heroes.values()],
            "colors": [color.to_dict() for color in self.repository.colors.values()],
        }