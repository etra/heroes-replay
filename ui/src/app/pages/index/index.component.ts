import { Component} from '@angular/core';
import { CommonModule } from '@angular/common';
import { Observable } from 'rxjs';
import { Match } from '../../services/data-models';
import { VideoListComponent } from '../../component/video-list/video-list.component';
import { FilterListComponent } from '../../component/filter-list/filter-list.component';
import { DataService } from '../../services/data.service';
import { NzLayoutModule } from 'ng-zorro-antd/layout';


@Component({
  selector: 'app-index',
  standalone: true,
  imports: [CommonModule, VideoListComponent, FilterListComponent, NzLayoutModule],
  templateUrl: './index.component.html',
  styleUrl: './index.component.css'
})
export class IndexComponent {
  
  matchData: Observable<Match[]> | undefined;

  constructor(
    private dataService: DataService
  ) {}

  ngOnInit() {
    this.matchData = this.dataService.getItems();
  }
}
