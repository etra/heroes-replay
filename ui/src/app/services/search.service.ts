import { Injectable } from '@angular/core';
// import * as lunr from 'lunr';
import Fuse from 'fuse.js';
import { Match } from './data-models';

@Injectable({
  providedIn: 'root'
})
export class SearchService {
  
  private index: Fuse<any> | null = null;

  // private index: lunr.Index | null = null;

  constructor() {}

  initializeIndex(matches: Match[] = []): void {
    this.index = new Fuse(matches, 
  }

  search(query: string): lunr.Index.Result[] {
    if (!this.index) {
      throw new Error('Index is not initialized.');
    }
    return this.index.search(query);
  }
}
