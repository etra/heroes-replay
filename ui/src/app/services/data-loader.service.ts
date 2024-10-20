import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { of } from 'rxjs';
import { MatchAppnonent, Match, Color } from './data-models';

@Injectable({
  providedIn: 'root'
})
export class DataLoaderService {

  constructor(private http: HttpClient) {}

  getColorData(): Observable<Color[]> {
    return this._getData('database/colors.ndjson');
  }

  getMatchData(): Observable<Match[]> {
    return this._getData('database/matches.ndjson');
  }

  // Fetch and process JSON-ND data
  _getData(dataUrl: string): Observable<any[]> {
    return this.http.get(dataUrl, { responseType: 'text' }).pipe(
      map((data: string) => {
        // Split by newline to handle JSON-ND
        const items: any[] = data.split('\n').filter(line => line.trim() !== '').map(line => {
          try {
            return JSON.parse(line);
          } catch (e) {
            console.error('Invalid JSON on line:', line);
            return null;
          }
        }).filter(item => item !== null);
        return items;
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

}
