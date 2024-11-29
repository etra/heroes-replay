import { Component, Input } from '@angular/core';
import { Match } from '../../services/data-models';
import { DataService } from '../../services/data.service';
import { VideoItemComponent } from '../../component/video-item/video-item.component';
import { CommonModule } from '@angular/common';
import { NzLayoutModule } from 'ng-zorro-antd/layout';
import { NzPageHeaderModule } from 'ng-zorro-antd/page-header';

@Component({
  selector: 'page-detail',
  standalone: true,
  imports: [VideoItemComponent, CommonModule, NzLayoutModule, NzPageHeaderModule],
  templateUrl: './detail.component.html',
  styleUrl: './detail.component.css'
})
export class DetailComponent {

  constructor(private dataService: DataService) {}

  match: Match | undefined = undefined;
  @Input()
  set id(video_id: string) {
    this.match = this.dataService.getItemByVideoId(video_id);
  }


  ngOnInit() {
    console.log(this.match)
    console.log('DetailComponent initialized');
  }
  
  onBack(): void {
    console.log('onBack');
  }
}
