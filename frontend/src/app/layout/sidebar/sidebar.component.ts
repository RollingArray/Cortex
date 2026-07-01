import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';

import {
  IonContent,
  IonIcon,
  IonItem,
  IonLabel,
  IonList,
  IonListHeader,
  IonMenu,
  IonMenuToggle,
  IonNote,
} from '@ionic/angular/standalone';

import { NAVIGATION } from '../../shared/constants/navigation.constants';
import { NavigationItemComponent } from 'src/app/shared/components/navigation-item/navigation-item.component';

@Component({
  selector: 'app-sidebar',
  standalone: true,
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss'],
  imports: [
    
    IonMenu,
    IonContent,
    IonList,
    IonListHeader,
    IonNote,
    IonMenuToggle,
    
    NavigationItemComponent
  ],
})
export class SidebarComponent {
  protected readonly navigation = NAVIGATION;
}
