import { Component, ChangeDetectorRef, NgZone,  } from '@angular/core';
import { LayoutComponent } from '../../component/layout/layout.component';

import { MatGridListModule } from '@angular/material/grid-list';
import { CommonModule, NgFor } from '@angular/common';
import { Observable } from 'rxjs';
import { MatchAppnonent, Match, Color } from '../../services/data-models';
import { DataLoaderService } from '../../services/data-loader.service';

@Component({
  selector: 'app-index',
  standalone: true,
  imports: [LayoutComponent, MatGridListModule, CommonModule],
  templateUrl: './index.component.html',
  styleUrl: './index.component.css'
})
export class IndexComponent {
  
  colorData$: Observable<Color[]> | undefined;
  matchData$: Observable<Match[]> | undefined;

  constructor(
    private dataLoader: DataLoaderService,
    private cd: ChangeDetectorRef, // Inject ChangeDetectorRef
    private zone: NgZone // Inject NgZone
  ) {}

  ngOnInit() {
    this.loadData();
  }

  // loadData(): void {
  //   this.colorService.getData().subscribe((data: Color[]) => {
  //     console.log('Data loaded:', data);
  //     this.colors = [...data];
  //     console.log('Colors:', this.colors);
  //   });
  // }

  loadData(): void {
    this.colorData$ = this.dataLoader.getColorData();
    this.matchData$ = this.dataLoader.getMatchData();
    // this.colorService.getData().subscribe((data: Color[]) => {
    //   console.log('Data loaded:', data);
    //   this.colors = [...data];
    //   console.log('Colors:', this.colors);
    // });
  }


  videos = [
    { title: 'Video 1', channel: 'Channel 1', thumbnail: 'assets/video1.jpg' },
    { title: 'Video 2', channel: 'Channel 2', thumbnail: 'assets/video2.jpg' },
    { title: 'Video 3', channel: 'Channel 3', thumbnail: 'assets/video3.jpg' },
    { title: 'Video 4', channel: 'Channel 4', thumbnail: 'assets/video4.jpg' },
    { title: 'Video 5', channel: 'Channel 5', thumbnail: 'assets/video5.jpg' },
  ];
}
