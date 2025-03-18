import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';

export const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    title: 'Home'
  },
  // {
  //   path: 'how-it-works',
  //   loadComponent: () => import('./how-it-works/how-it-works.component').then(m => m.HowItWorksComponent),
  //   title: 'How It Works'
  // },
  // {
  //   path: 'shopping-list',
  //   loadComponent: () => import('./shopping-list/shopping-list.component').then(m => m.ShoppingListComponent),
  //   title: 'Shopping List'
  // },
  // {
  //   path: 'about',
  //   loadComponent: () => import('./about/about.component').then(m => m.AboutComponent),
  //   title: 'About Us'
  // },
  // {
  //   path: 'results',
  //   loadComponent: () => import('./results/results.component').then(m => m.ResultsComponent),
  //   title: 'Search Results'
  // },
  {
    path: '**',
    redirectTo: '',
    pathMatch: 'full'
  }
];