import { Component } from '@angular/core';

import {
  IonApp,
  IonRouterOutlet,
  IonSplitPane,
  
} from '@ionic/angular/standalone';

import { SidebarComponent } from '../sidebar/sidebar.component';

@Component({
  selector: 'app-shell',
  standalone: true,
  templateUrl: './shell.component.html',
  styleUrls: ['./shell.component.scss'],
  imports: [
    IonApp,
    IonSplitPane,
    IonRouterOutlet,
    SidebarComponent
  ],
})
export class ShellComponent {}