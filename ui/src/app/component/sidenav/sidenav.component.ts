import { Component } from '@angular/core';
import { MatSidenav } from '@angular/material/sidenav';
import { MatNavList } from '@angular/material/list';
import { MatListItem } from '@angular/material/list';
import { MatDivider } from '@angular/material/divider';


@Component({
  selector: 'app-sidenav',
  standalone: true,
  imports: [MatSidenav, MatNavList, MatListItem, MatDivider],
  templateUrl: './sidenav.component.html',
  styleUrl: './sidenav.component.css'
})
export class SidenavComponent {

}
