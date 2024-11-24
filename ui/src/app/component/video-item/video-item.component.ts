import { Component, Input, OnChanges } from '@angular/core';
import { NzCardModule } from 'ng-zorro-antd/card';
import { NzListModule } from 'ng-zorro-antd/list';
import { NzGridModule } from 'ng-zorro-antd/grid';
import { NzIconModule } from 'ng-zorro-antd/icon';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';
import { NzAvatarModule } from 'ng-zorro-antd/avatar';
import { Match } from '../../services/data-models';
import { NgIf } from '@angular/common';
import { Observable } from 'rxjs';

interface ItemData extends Match {
  vide_url: SafeResourceUrl;
}

@Component({
  selector: 'app-video-item',
  standalone: true,
  imports: [NzCardModule, NgIf],
  templateUrl: './video-item.component.html',
  styleUrl: './video-item.component.css'
})

export class VideoItemComponent{
  @Input() inputMatch: Match | undefined = undefined;

  match: ItemData | undefined = undefined;
  
  constructor(private sanitizer: DomSanitizer) {}

  ngOnInit(): void {
    if (this.inputMatch) {
      this.match = {
        ...this.inputMatch,
        vide_url: this.sanitizer.bypassSecurityTrustResourceUrl("https://www.youtube.com/embed/" + this.inputMatch.video_id)
      };
    }
    // if (this.inputData) {  
    //   this.inputData.subscribe((data: Match) => {
    //     this.match = {
    //       ...data,
    //       vide_url: this.sanitizer.bypassSecurityTrustResourceUrl("https://www.youtube.com/embed/" + data.video_id)
    //     };
    //   });
    // }
  }
}
