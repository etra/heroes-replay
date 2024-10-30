import { Component, ChangeDetectorRef, NgZone,  } from '@angular/core';
import { CommonModule, NgFor } from '@angular/common';
import { Observable } from 'rxjs';
import { MatchAppnonent, Match, Color } from '../../services/data-models';
import { DataLoaderService } from '../../services/data-loader.service';
import { VideoListComponent } from '../../component/video-list/video-list.component';

@Component({
  selector: 'app-index',
  standalone: true,
  imports: [CommonModule, VideoListComponent],
  templateUrl: './index.component.html',
  styleUrl: './index.component.css'
})
export class IndexComponent {
  
  matchData: Observable<Match[]> | undefined;

  constructor(
    private dataLoader: DataLoaderService,
  ) {}

  ngOnInit() {
    this.loadData();
  }

  loadData(): void {
    this.matchData = this.dataLoader.getMatchData();
  }

}
