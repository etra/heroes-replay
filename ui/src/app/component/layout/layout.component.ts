import { Component } from '@angular/core';
import { HeaderComponent } from '../header/header.component';
import { SidenavComponent } from '../sidenav/sidenav.component';
import { MatSidenavContainer, MatSidenavContent } from '@angular/material/sidenav';

@Component({
  selector: 'app-layout',
  standalone: true,
  imports: [HeaderComponent, SidenavComponent, MatSidenavContainer, MatSidenavContent],
  templateUrl: './layout.component.html',
  styleUrl: './layout.component.css'
})
export class LayoutComponent {

}
