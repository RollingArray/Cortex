import { Input, Component } from '@angular/core';

import { RouterLink, RouterLinkActive } from '@angular/router';

import { IonIcon, IonItem, IonLabel, IonMenuToggle } from '@ionic/angular/standalone';

import { AppNavigationItem } from '../../interfaces/app-navigation-item.interface';

@Component({
  selector: 'app-navigation-item',
  standalone: true,
  templateUrl: './navigation-item.component.html',
  styleUrls: ['./navigation-item.component.scss'],
  imports: [RouterLink, RouterLinkActive, IonMenuToggle, IonItem, IonIcon, IonLabel],
})
export class NavigationItemComponent {
  @Input({
    required: true,
  })
  item!: AppNavigationItem;
}
