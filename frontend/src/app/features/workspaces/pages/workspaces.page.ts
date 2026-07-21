/**
 * Workspaces Page
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Displays the list of workspaces available to
 * the current user.
 */

/*------------------------------------------------------------------------------
 * Angular
 *----------------------------------------------------------------------------*/

import { AsyncPipe } from '@angular/common';
import { Component, inject } from '@angular/core';
import { Router } from '@angular/router';

/*------------------------------------------------------------------------------
 * Ionic
 *----------------------------------------------------------------------------*/

import {
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonCardTitle,
  IonCol,
  IonContent,
  IonGrid,
  IonHeader,
  IonRow,
  IonTitle,
  IonToolbar,
} from '@ionic/angular/standalone';

/*------------------------------------------------------------------------------
 * RxJS
 *----------------------------------------------------------------------------*/

import { map } from 'rxjs/operators';

/*------------------------------------------------------------------------------
 * Services
 *----------------------------------------------------------------------------*/

import { WorkspaceService } from 'src/app/core/services';

/*------------------------------------------------------------------------------
 * Interfaces
 *----------------------------------------------------------------------------*/

import { WorkspaceSummary } from 'src/app/shared/interfaces';
import { tap } from 'rxjs/operators';
/*------------------------------------------------------------------------------
 * Component
 *----------------------------------------------------------------------------*/

@Component({
  selector: 'app-workspaces',
  standalone: true,
  templateUrl: './workspaces.page.html',
  styleUrls: ['./workspaces.page.scss'],
  imports: [
    AsyncPipe,

    IonHeader,
    IonToolbar,
    IonTitle,
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
export class WorkspacesPage {
  /*--------------------------------------------------------------------------
   * Dependencies
   *------------------------------------------------------------------------*/

  private readonly workspaceService = inject(WorkspaceService);

  private readonly router = inject(Router);

  /*--------------------------------------------------------------------------
   * View Model
   *------------------------------------------------------------------------*/

  protected readonly vm$ = this.workspaceService.getWorkspaces().pipe(
    tap((workspaces) => {
      console.log('Workspace API Response:', workspaces);
    }),
    map((workspaces) => ({
      workspaces,
      hasWorkspaces: workspaces.length > 0,
    })),
    tap((vm) => {
      console.log('ViewModel:', vm);
    }),
  );

  /*--------------------------------------------------------------------------
   * Public Methods
   *------------------------------------------------------------------------*/

  public async openWorkspace(workspace: WorkspaceSummary): Promise<void> {
    await this.router.navigate(['/workspaces', workspace.id, 'dashboard']);
  }
}
