/**
 * Status Indicator Component
 *
 * Project:
 * --------
 * Cortex
 *
 * Purpose:
 * --------
 * Displays a consistent visual representation of application,
 * backend and service status throughout the Cortex platform.
 *
 * Features:
 * ---------
 * - Status label
 * - Status color
 * - Reusable across the application
 */

/*------------------------------------------------------------------------------
 * Imports
 *----------------------------------------------------------------------------*/

import { Component, Input } from '@angular/core';

/*------------------------------------------------------------------------------
 * Component
 *----------------------------------------------------------------------------*/

@Component({
  selector: 'app-status-indicator',
  standalone: true,
  templateUrl: './status-indicator.component.html',
  styleUrls: ['./status-indicator.component.scss'],
})
export class StatusIndicatorComponent {
  /*--------------------------------------------------------------------------
   * Inputs
   *--------------------------------------------------------------------------*/

  @Input({ required: true })
  status!: string;
}
