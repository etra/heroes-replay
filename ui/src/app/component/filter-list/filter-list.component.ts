import { Component } from '@angular/core';
import { NzSelectModule } from 'ng-zorro-antd/select';
import { FormsModule } from '@angular/forms';
import { SimpleChanges } from '@angular/core';
import { OnChanges } from '@angular/core';
import { Input } from '@angular/core';
import { DataService } from '../../services/data.service';
import { FilterItemComponent } from '../filter-item/filter-item.component';
@Component({
  selector: 'app-filter-list',
  standalone: true,
  imports: [FilterItemComponent],
  templateUrl: './filter-list.component.html',
  styleUrl: './filter-list.component.css'
})
export class FilterListComponent {
  listOfFilters: string[] = ['player_id', 'color_id']
  constructor(private dataService: DataService) {}

  // listOfOption = ['lexiav', 'stygianone'];
  
  // @Input() listOfSelected: string[] = [];

  ngOnInit() {
    this.listOfFilters = this.dataService.getAvailableFilters()
  }

  // ngOnChanges(changes: SimpleChanges): void {
  //   console.log('FilterListComponent ngOnChanges', this.listOfSelected);
  // }

  // onFilterChange(selected: string[], filter_key: string): void {
  //   console.log('Selected values:', selected);

  //   // Update the filters in DataService
  //   this.dataService.updateFilter(filter_key, selected); // Replace 'customFilter' with your filter key
  // }
  
}
