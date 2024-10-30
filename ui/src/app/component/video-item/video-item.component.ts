import { Component } from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import {MatButtonModule} from '@angular/material/button';


@Component({
  selector: 'app-video-item',
  standalone: true,
  imports: [MatCardModule, MatButtonModule],
  templateUrl: './video-item.component.html',
  styleUrl: './video-item.component.css'
})

export class VideoItemComponent {

}
