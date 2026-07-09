/**
 * Dashboard Component
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Provides the Cortex dashboard and displays
 * platform health and summary information.
 *
 * Features:
 * ---------
 * - Backend health
 * - Platform overview
 * - System metrics
 */

/*------------------------------------------------------------------------------
 * Imports
 *----------------------------------------------------------------------------*/

import { Component, OnInit, inject } from '@angular/core';

import {
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonCardTitle,
  IonCol,
  IonContent,
  IonGrid,
  IonRow,
} from '@ionic/angular/standalone';

import { TopbarComponent } from '../../../layout/topbar/topbar.component';
import { FooterComponent } from '../../../layout/footer/footer.component';
import { PageLayoutComponent } from '../../../layout/page-layout/page-layout.component';
import { MetricCardComponent, StatusIndicatorComponent } from 'src/app/shared/components';
import { ICONS } from 'src/app/shared/constants';
import { HealthService } from 'src/app/core/services';
import { HealthStatus } from 'src/app/shared/interfaces';

/*------------------------------------------------------------------------------
 * Component
 *----------------------------------------------------------------------------*/

@Component({
  selector: 'app-dashboard',
  standalone: true,
  templateUrl: './dashboard.page.html',
  styleUrls: ['./dashboard.page.scss'],
  imports: [
    PageLayoutComponent,
    MetricCardComponent,
    StatusIndicatorComponent,

    IonContent,
    IonGrid,
    IonRow,
    IonCol,
    IonCard,
    IonCardHeader,
    IonCardTitle,
    IonCardContent,
  ],
})
export class DashboardPage implements OnInit {
  /*--------------------------------------------------------------------------
   * Dependencies
   *--------------------------------------------------------------------------*/

  protected readonly icons = ICONS;

  private readonly healthService = inject(HealthService);

  /*--------------------------------------------------------------------------
   * Properties
   *--------------------------------------------------------------------------*/

  protected healthStatus = 'Loading...';

  /*--------------------------------------------------------------------------
   * Lifecycle
   *--------------------------------------------------------------------------*/

  public ngOnInit(): void {
    this.loadHealth();
  }

  /*--------------------------------------------------------------------------
   * Private Methods
   *--------------------------------------------------------------------------*/

  private loadHealth(): void {
    this.healthService.getStatus().subscribe({
      next: (response: HealthStatus) => {
        this.healthStatus = response.status;
      },

      error: () => {
        this.healthStatus = 'Offline';
      },
    });
  }
}
