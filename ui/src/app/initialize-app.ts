import { APP_INITIALIZER } from '@angular/core';
import { DataService } from './services/data.service';
import { lastValueFrom } from 'rxjs';

export function initializeApp(dataService: DataService) {
  return () => lastValueFrom(dataService.loadDatabase('database/index.json'));
}