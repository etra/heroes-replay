import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { of } from 'rxjs';

export interface Color {
  id: string;
  name: string;
}

@Injectable({
  providedIn: 'root'
})
export class ColorService {

  private dataUrl = 'database/colors.json';

  constructor(private http: HttpClient) {}

  getData(): Observable<Color[]> {
    return this.http.get<any>(this.dataUrl);
  }
  // Fetch and process JSON-ND data
  // getData(): Observable<Color[]> {
  //   return this.http.get(this.dataUrl, { responseType: 'text' }).pipe(
  //     map((data: string) => {
  //       // Split by newline to handle JSON-ND
  //       const colors: Color[] = data.split('\n').filter(line => line.trim() !== '').map(line => {
  //         try {
  //           return JSON.parse(line);
  //         } catch (e) {
  //           console.error('Invalid JSON on line:', line);
  //           return null;
  //         }
  //       }).filter(color => color !== null); // Filter out null values from invalid JSON lines
  //       return colors;
  //     }),
  //     catchError(this.handleError<Color[]>('getData', []))
  //   );
  // }

  // Handle HTTP errors
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(`${operation} failed: ${error.message}`);
      return of(result as T);
    };
  }
}
