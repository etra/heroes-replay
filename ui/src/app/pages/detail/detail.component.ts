import { Component, Input } from '@angular/core';
import { Match } from '../../services/data-models';
import { DataService } from '../../services/data.service';
import { VideoItemComponent } from '../../component/video-item/video-item.component';
@Component({
  selector: 'app-detail',
  standalone: true,
  imports: [VideoItemComponent],
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

}
