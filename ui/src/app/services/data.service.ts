import { tap } from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { ActivatedRoute, Router } from '@angular/router';
import { map, catchError } from 'rxjs/operators';
import { of } from 'rxjs';
import { MatchAppnonent, Match, Color } from './data-models';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  private database: any;
  private filters: { [key: string]: any } = {
    player_id: 'stygianone',
  }; // Filters by key-value pairs

  // BehaviorSubject to hold filtered items
  private filteredItemsSubject = new BehaviorSubject<any[]>([]);

  filteredItems$: Observable<any[]> = this.filteredItemsSubject.asObservable();

  constructor(private http: HttpClient, private router: Router, private route: ActivatedRoute) {
    this.route.queryParamMap.subscribe((params) => {
      this.filters = {}; // Reset filters
      params.keys.forEach((key) => {
        const values = params.getAll(key); // Get all values for the key
        if (values.length) {
          this.filters[key] = values;
        }
      });
      this.applyFilters(); // Apply filters when query parameters change
    });
  }


  loadDatabase(dataUrl: string): Observable<any[]> {
    return this.http.get<any[]>(dataUrl).pipe(
      tap((response) => {
        this.database = response;
        this.applyFilters(); // Apply filters immediately
        console.log('Database loaded', this.database);
      }),
      catchError(this.handleError<any[]>('getData', []))
    );
  }

  // Handle HTTP errors
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(`${operation} failed: ${error.message}`);
      return of(result as T);
    };
  }

    getDatabase(): any {
        return this.database;
    }


    updateFilter(key: string, values: string[]): void {
      this.filters[key] = values; // Update filter for the specific key
      this.applyFilters();
      this.updateUrlParams(); // Sync with the URL
    }

  // Apply filters to items
  private applyFilters(): void {
    if (!this.database) {
      return;
    }
    let filteredItems: Match[] = this.database.matches;

    // Apply each filter with OR logic
    for (const key of Object.keys(this.filters)) {
      const filterValues = this.filters[key];
      filteredItems = filteredItems.filter((item) =>
        filterValues.includes(item[key])
      );
    }

    this.filteredItemsSubject.next(filteredItems); // Emit the filtered items
  }

  // Sync filters with URL query parameters
  private updateUrlParams(): void {
    const queryParams: { [key: string]: string[] } = {};

    // Flatten the filters for the URL
    Object.keys(this.filters).forEach((key) => {
      queryParams[key] = this.filters[key];
    });

    this.router.navigate([], {
      relativeTo: this.route,
      queryParams,
      queryParamsHandling: 'merge', // Merge with existing params
    });
  }


// Get current filters
getFilters(): { [key: string]: any } {
  return this.filters;
}

  getItems(): Observable<any[]> {
    return this.filteredItems$;
  }
    
  getFilterOptions(filter_key: string): string[] {
    return this.database.filters[filter_key];
  }

  getAvailableFilters(): string[] {
    return Object.keys(this.database.filters);
  }

}
