import { Component, ChangeDetectorRef, NgZone,  OnInit, input, Input, OnChanges} from '@angular/core';
import { Match } from '../../services/data-models';
import { CommonModule, NgFor } from '@angular/common';
import { NzListModule } from 'ng-zorro-antd/list';
import { NzIconModule } from 'ng-zorro-antd/icon';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';

interface ItemData {
  href: string;
  title: string;
  match: Match;
  thumbnail: string;
  avatar: string;
  video_id: string;
  vide_url: SafeResourceUrl;
  description: string;
  content: string;
}

@Component({
  selector: 'app-video-list',
  standalone: true,
  imports: [CommonModule, NzListModule, NzIconModule],
  templateUrl: './video-list.component.html',
  styleUrl: './video-list.component.css'
})

export class VideoListComponent implements OnChanges {

  @Input() matches: Match[] | null = [];

  data: ItemData[] = [];

  constructor(private sanitizer: DomSanitizer) {}

  ngOnChanges(): void {
    this.loadData();
  }

  loadData(): void {
    if (this.matches) {  // Check if matches is not null
      this.data = this.matches.map((match) => ({
        href: '#',
        match: match,
        title: `${match.player.name} as ${match.hero.name} of ${match.town.name}`,
        thumbnail: match.thumbnail,
        vide_url: this.sanitizer.bypassSecurityTrustResourceUrl("https://www.youtube.com/embed/" + match.video_id),
        video_id: match.video_id,
        avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
        description: "desciprtion",
        content: "content"
      }));
    } else {
      this.data = [];
    }

    // this.data = new Array(5).fill({}).map((_, index) => ({
    //   href: '#',
    //   title: `ant design part ${index} (page: ${pi})`,
    //   avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
    //   description: 'Ant Design, a design language for background applications, is refined by Ant UED Team.',
    //   content:
    //     'We supply a series of design principles, practical patterns and high quality design resources ' +
    //     '(Sketch and Axure), to help people create their product prototypes beautifully and efficiently.'
    // }));
  }

  // openModal(item: any): void {
  //   this.modal.create({
  //     nzTitle: item.title,
  //     nzContent: ModalContentComponent,
  //     nzComponentParams: {
  //       title: item.title,
  //       description: item.description,
  //       content: item.content
  //     },
  //     nzFooter: null
  //   });
  // }

}
