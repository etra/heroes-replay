export interface Match {
    [key: string]: any; 
    id: number;
    player_id: string;
    town_id: string;
    hero_id: string;
    color_id: string;
    link: string;
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
