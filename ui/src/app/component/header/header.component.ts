import { Component } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';
import { MatToolbar } from '@angular/material/toolbar';
import { MatButton } from '@angular/material/button';
import { MatFormField } from '@angular/material/form-field';
import { filter } from 'rxjs/operators';
import { NgIf } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [MatButton, MatToolbar, MatFormField, NgIf, RouterModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})

export class HeaderComponent {
  isIndexPage: boolean = true;
  constructor(private router: Router) {
    this.router.events.pipe(
      filter(event => event instanceof NavigationEnd)
    ).subscribe((event: NavigationEnd) => {
      this.isIndexPage = event.urlAfterRedirects === '/';
    });
  }
}
