/**
 * Metric Card Component
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Provides a reusable dashboard card for presenting
 * platform metrics and summary information.
 *
 * Features:
 * ---------
 * - Card title
 * - Optional icon
 * - Content projection
 * - Consistent dashboard styling
 */

/*------------------------------------------------------------------------------
 * Angular
 *----------------------------------------------------------------------------*/

import { Component, Input } from '@angular/core';

/*------------------------------------------------------------------------------
 * Ionic
 *----------------------------------------------------------------------------*/

import {
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonCardTitle,
  IonIcon,
} from '@ionic/angular/standalone';

/*------------------------------------------------------------------------------
 * Component
 *----------------------------------------------------------------------------*/

@Component({
  selector: 'app-metric-card',
  standalone: true,
  templateUrl: './metric-card.component.html',
  styleUrls: ['./metric-card.component.scss'],
  imports: [IonCard, IonCardHeader, IonCardTitle, IonCardContent, IonIcon],
})
export class MetricCardComponent {
  /*--------------------------------------------------------------------------
   * Inputs
   *--------------------------------------------------------------------------*/

  @Input({ required: true })
  title!: string;

  @Input()
  icon?: string;

  @Input()
  subtitle?: string;
}
