import { RouterModule, Routes } from '@angular/router';
import { IndexComponent } from './pages/index/index.component';
import { DetailComponent } from './pages/detail/detail.component';
import { PlayerComponent } from './pages/player/player.component';
import { CreatePlayerComponent } from './pages/create-player/create-player.component';
import { CreateMatchComponent } from './pages/create-match/create-match.component';
// import { ResultComponent } from './pages/result/result.component';
// import { DetailComponent } from './pages/detail/detail.component';

export const routes: Routes = [
  
  { path: '', component: IndexComponent },
  { path: 'match/:id', component: DetailComponent },
  { path: 'player/:id', component: PlayerComponent },
  { path: 'create-player', component: CreatePlayerComponent },
  { path: 'create-match', component: CreateMatchComponent },
];
