import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import {
  IonApp,
  IonSplitPane,
  IonMenu,
  IonContent,
  IonList,
  IonListHeader,
  IonNote,
  IonMenuToggle,
  IonItem,
  IonIcon,
  IonLabel,
  IonRouterOutlet,
  IonRouterLink,
} from '@ionic/angular/standalone';
import { addIcons } from 'ionicons';
import {
  gridOutline,
  gridSharp,
  chatbubbleOutline,
  chatbubbleSharp,
  documentTextOutline,
  documentTextSharp,
  searchOutline,
  searchSharp,
  hardwareChipOutline,
  hardwareChipSharp,
  settingsOutline,
  settingsSharp,
} from 'ionicons/icons';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
  imports: [
    RouterLink,
    RouterLinkActive,
    IonApp,
    IonSplitPane,
    IonMenu,
    IonContent,
    IonList,
    IonListHeader,
    IonNote,
    IonMenuToggle,
    IonItem,
    IonIcon,
    IonLabel,
    IonRouterLink,
    IonRouterOutlet,
  ],
})
export class AppComponent {
  public appPages = [
    {
      title: 'Dashboard',
      url: '/dashboard',
      icon: 'grid',
    },
    {
      title: 'Ask Cortex',
      url: '/chat',
      icon: 'chatbubble',
    },
    {
      title: 'Documents',
      url: '/documents',
      icon: 'document-text',
    },
    {
      title: 'Search',
      url: '/search',
      icon: 'search',
    },
    {
      title: 'System',
      url: '/system',
      icon: 'hardware-chip',
    },
    {
      title: 'Settings',
      url: '/settings',
      icon: 'settings',
    },
  ];

  constructor() {
    addIcons({
      gridOutline,
      gridSharp,
      chatbubbleOutline,
      chatbubbleSharp,
      documentTextOutline,
      documentTextSharp,
      searchOutline,
      searchSharp,
      hardwareChipOutline,
      hardwareChipSharp,
      settingsOutline,
      settingsSharp,
    });
  }
}
