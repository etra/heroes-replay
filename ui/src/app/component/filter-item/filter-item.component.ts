import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';
import { DataService } from '../../services/data.service';
import { NzSelectModule } from 'ng-zorro-antd/select';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-filter-item',
  standalone: true,
  imports: [NzSelectModule, FormsModule],
  templateUrl: './filter-item.component.html',
  styleUrl: './filter-item.component.css'
})
export class FilterItemComponent implements OnChanges {
  
  constructor(private dataService: DataService) {}

  listOfOption: string[] = [];
  @Input() filter_key: string = '';
  @Input() listOfSelected: string[] = [];

  ngOnInit() {
    this.listOfOption = this.dataService.getFilterOptions(this.filter_key);
    
    //TODO: Pull options from this.listOfOption = DataService.getFilterOptions(this.filter_key);
  }

  ngOnChanges(changes: SimpleChanges): void {
    // console.log('FilterListComponent ngOnChanges', this.listOfSelected);
  }

  onFilterChange(values: string[], key: string): void {
    this.dataService.updateFilter(key, values);
  }

}
