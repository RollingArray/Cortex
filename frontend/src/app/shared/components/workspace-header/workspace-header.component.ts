/**
 * Workspace Header Component
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Displays the active workspace context.
 *
 * Responsibilities:
 * -----------------
 * - Display workspace name
 * - Display workspace description
 *
 * Note:
 * -----
 * This is a presentation-only component.
 * It does not communicate with services
 * or perform navigation.
 */

/*------------------------------------------------------------------------------
 * Imports
 *----------------------------------------------------------------------------*/

import { Component, Input } from '@angular/core';

import {
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonCardSubtitle,
  IonCardTitle,
} from '@ionic/angular/standalone';

import { WorkspaceSummary } from '../../interfaces';

/*------------------------------------------------------------------------------
 * Component
 *----------------------------------------------------------------------------*/

@Component({
  selector: 'app-workspace-header',
  standalone: true,
  templateUrl: './workspace-header.component.html',
  styleUrls: ['./workspace-header.component.scss'],
  imports: [IonCard, IonCardHeader, IonCardTitle, IonCardSubtitle, IonCardContent],
})
export class WorkspaceHeaderComponent {
  /*--------------------------------------------------------------------------
   * Inputs
   *------------------------------------------------------------------------*/

  @Input({ required: true })
  public workspace!: WorkspaceSummary;
}
