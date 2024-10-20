export interface Match {
    id: number;
    player_id: string;
    town_id: string;
    hero_id: string;
    color_id: string;
    link: string;
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
