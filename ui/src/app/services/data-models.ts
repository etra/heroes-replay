export interface Player {
    [key: string]: any; 
    player_id: string;
    name: string
    youtube: string;
    twitch: string;
    discord: string;
}

export interface Town {
    [key: string]: any; 
    id: string;
    name: string;
}

export interface Hero {
    [key: string]: any; 
    id: string;
    name: string;
}

export interface Match {
    [key: string]: any; 
    id: number;
    player_id: string;
    player: Player;
    town_id: string;
    town: Town;
    hero_id: string;
    hero: Hero;
    color_id: string;
    link: string;
    video_title: string
    thumbnail: string;
    video_id: string;
    opponents: MatchAppnonent[];
    created_time: string;
    updated_time: string;
}

export interface MatchAppnonent {
    id: number;
    match_id: number;
    player_id: string;
    town_id: string;
    hero_id: string;
    color_id: string;
}

export interface Color {
    id: string;
    name: string;
  }
