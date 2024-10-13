import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-detail',
  standalone: true,
  imports: [],
  templateUrl: './detail.component.html',
  styleUrl: './detail.component.css'
})
export class DetailComponent {
  resultId: number = 0;

  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    const resultId = this.route.snapshot.paramMap.get('id');
    this.resultId = resultId? +resultId : 0;
    // // Access the route parameter 'id' and store it
    // this.route.paramMap.subscribe(params => {
    //   this.resultId = +params.get('id');  // Convert 'id' to a number
    // });
  }
}
