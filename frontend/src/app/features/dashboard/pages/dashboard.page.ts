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

import { PageLayoutComponent } from 'src/app/layout/page-layout/page-layout.component';

import {
  MetricCardComponent,
  StatusIndicatorComponent,
  WorkspaceHeaderComponent,
} from 'src/app/shared/components';

import { ICONS } from 'src/app/shared/constants';

import { HealthService, WorkspaceContextService } from 'src/app/core/services';

import { HealthStatus } from 'src/app/shared/interfaces';

import { AsyncPipe } from '@angular/common';

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
    WorkspaceHeaderComponent,

    AsyncPipe,

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

  private readonly workspaceContext = inject(WorkspaceContextService);

  /*--------------------------------------------------------------------------
   * Properties
   *--------------------------------------------------------------------------*/

  protected healthStatus = 'Loading...';

  protected readonly currentWorkspace$ = this.workspaceContext.currentWorkspace$;

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
