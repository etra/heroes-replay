import { Component, Input } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NzCardModule } from 'ng-zorro-antd/card';
import { NzAvatarModule } from 'ng-zorro-antd/avatar';
import { Player } from '../../services/data-models';
import { NgIf, CommonModule } from '@angular/common';


@Component({
  selector: 'app-player-card',
  standalone: true,
  imports: [RouterModule, NzCardModule, NzAvatarModule, NgIf, CommonModule],
  templateUrl: './player-card.component.html',
  styleUrl: './player-card.component.css'
})
export class PlayerCardComponent {
  @Input() player: Player | undefined = undefined;
}
