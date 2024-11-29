import { Component, OnChanges, SimpleChanges} from '@angular/core';
import { CommonModule } from '@angular/common';
import { Observable } from 'rxjs';
import { Match } from '../../services/data-models';
import { VideoListComponent } from '../../component/video-list/video-list.component';
import { FilterListComponent } from '../../component/filter-list/filter-list.component';
import { DataService } from '../../services/data.service';
import { NzLayoutModule } from 'ng-zorro-antd/layout';
import { OnInit } from '@angular/core';
import { NzIconModule } from 'ng-zorro-antd/icon';
import { ViewportRuler } from '@angular/cdk/scrolling';
import { NzMenuModule } from 'ng-zorro-antd/menu';
import { provideRouter } from '@angular/router';




@Component({
  selector: 'page-index',
  standalone: true,
  imports: [CommonModule, NzMenuModule, NzIconModule, VideoListComponent, FilterListComponent, NzLayoutModule],
  templateUrl: './index.component.html',
  styleUrl: './index.component.css'
})
export class IndexComponent {
  
  matchData: Observable<Match[]> | undefined;
  isCollapsed: boolean = true;
  constructor(
    private dataService: DataService,
    private viewportRuler: ViewportRuler
  ) {}

  ngOnInit() {
    
    this.matchData = this.dataService.getItems();
    this.viewportRuler.change(100).subscribe(() => {
      this.setInitialState();
    });
  }

  private setInitialState(): void {
    const viewportWidth = this.viewportRuler.getViewportSize().width;
    this.isCollapsed = viewportWidth < 768; // Example: Collapse on smaller screens
    console.log(this.viewportRuler.getViewportSize().width);
    console.log(this.isCollapsed);
  }

  loadData(): void {
    // this.dataService.filteredItems$.subscribe((filteredData) => {
    //   this.matchData = filteredData;
    // });
    
  }
}
