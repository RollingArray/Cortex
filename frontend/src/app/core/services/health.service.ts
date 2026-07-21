/**
 * Health Service
 *
 * Project:
 * --------
 * Cortex
 *
 * Purpose:
 * --------
 * Provides access to the Cortex backend health endpoint.
 *
 * Responsibilities:
 * -----------------
 * - Retrieve application health
 * - Retrieve platform status
 * - Abstract health endpoint from UI components
 */

/*------------------------------------------------------------------------------
 * Imports
 *----------------------------------------------------------------------------*/

import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { ApiService } from '../http/api.service';

import { HealthStatus } from '../../shared/interfaces/health-status.interface';
import { API } from 'src/app/shared/constants';

/*------------------------------------------------------------------------------
 * Service
 *----------------------------------------------------------------------------*/

@Injectable({
  providedIn: 'root',
})
export class HealthService {
  /*--------------------------------------------------------------------------
   * Dependencies
   *--------------------------------------------------------------------------*/

  private readonly apiService = inject(ApiService);

  /*--------------------------------------------------------------------------
   * Public Methods
   *--------------------------------------------------------------------------*/

  public getStatus(): Observable<HealthStatus> {
    return this.apiService.get<HealthStatus>(API.Health.Status);
  }
}
