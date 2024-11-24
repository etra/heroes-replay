import { Component, ChangeDetectorRef, NgZone,  OnInit, input, Input, OnChanges, SimpleChanges} from '@angular/core';
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

export class VideoListComponent implements OnChanges{
  // matchData: Observable<Match[]> | undefined;
  @Input() inputMatches: Match[] | null = null;

  matches: Match[] = [];

  ngOnChanges(): void {
    if (this.inputMatches) {
      this.matches = this.inputMatches;
    }
  }
}
