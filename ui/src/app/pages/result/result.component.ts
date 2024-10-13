import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-result',
  standalone: true,
  imports: [],
  templateUrl: './result.component.html',
  styleUrl: './result.component.css'
})
export class ResultComponent {
  constructor(private router: Router) {}

  goToResult(id: number) {
    // Navigate to the result page and pass the id
    this.router.navigate(['/detail', id]);
  }
}
