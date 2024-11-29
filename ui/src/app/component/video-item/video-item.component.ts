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
import { NzTableModule } from 'ng-zorro-antd/table';
import { NzImageModule } from 'ng-zorro-antd/image';
import { RouterLink, RouterModule } from '@angular/router';



interface ItemData extends Match {
  vide_url: SafeResourceUrl;
}

@Component({
  selector: 'app-video-item',
  standalone: true,
  imports: [NzCardModule, NgIf, NzTableModule, NzImageModule, RouterModule],
  templateUrl: './video-item.component.html',
  styleUrl: './video-item.component.css'
})

export class VideoItemComponent{
  @Input() inputMatch: Match | undefined = undefined;
  @Input() detailPage: boolean = false;

  match: ItemData | undefined = undefined;
  loading: boolean = true;
  constructor(private sanitizer: DomSanitizer) {}

  ngOnInit(): void {
    if (this.inputMatch) {
      this.loading = true;
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
