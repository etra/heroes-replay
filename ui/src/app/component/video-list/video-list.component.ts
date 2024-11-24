import { Component, ChangeDetectorRef, NgZone,  OnInit, input, Input, OnChanges} from '@angular/core';
import { Match } from '../../services/data-models';
import { CommonModule } from '@angular/common';
import { NzListModule } from 'ng-zorro-antd/list';
import { NzGridModule } from 'ng-zorro-antd/grid';
import { VideoItemComponent } from '../video-item/video-item.component';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-video-list',
  standalone: true,
  imports: [CommonModule, NzGridModule, NzListModule, VideoItemComponent],

  templateUrl: './video-list.component.html',
  styleUrl: './video-list.component.css'
})

export class VideoListComponent {
  // matchData: Observable<Match[]> | undefined;
  @Input() inputMatches: Match[] | null = null;

  matches: Match[] = [];


  // @Input() matches: Match[] | undefined;
  ngOnInit() {
    if (this.inputMatches) {
        this.matches = this.inputMatches;
    }
  }
}
