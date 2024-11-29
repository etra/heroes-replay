import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PlayerCardComponent } from '../../component/player-card/player-card.component';
import { NzLayoutModule } from 'ng-zorro-antd/layout';
import { DataService } from '../../services/data.service';
import { Match, Player } from '../../services/data-models';
import { VideoListComponent } from '../../component/video-list/video-list.component';
import { NzPageHeaderModule } from 'ng-zorro-antd/page-header';
@Component({
  selector: 'page-player',
  standalone: true,
  imports: [CommonModule, PlayerCardComponent, NzLayoutModule, VideoListComponent, NzPageHeaderModule],
  templateUrl: './player.component.html',
  styleUrl: './player.component.css'
})
export class PlayerComponent {
  
  constructor(private dataService: DataService) {}
  player: Player | undefined = undefined;
  matches: Match[] | undefined  = [];
  
  @Input()
  set id(player_id: string) {
    this.player = this.dataService.getPlayerById(player_id);
    this.matches = this.dataService.getPlayerMatches(player_id);
  }


  ngOnInit() {
    
    console.log(this.player)
    console.log(this.matches)
    console.log('DetailComponent initialized');
  }
}
