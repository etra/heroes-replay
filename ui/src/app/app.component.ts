import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { TownsListComponent } from './towns-list/towns-list.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, TownsListComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'ui';
}

