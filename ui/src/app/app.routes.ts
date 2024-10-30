import { Routes } from '@angular/router';
import { WelcomeComponent } from './pages/welcome/welcome.component';
import { IndexComponent } from './pages/index/index.component';
// import { ResultComponent } from './pages/result/result.component';
// import { DetailComponent } from './pages/detail/detail.component';

export const routes: Routes = [
  
  { path: '', component: IndexComponent },
  { path: 'welcome', component: WelcomeComponent },
];
