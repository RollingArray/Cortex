/**
 * Workspace Service
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Provides workspace API operations for the
 * Cortex platform.
 *
 * Responsibilities:
 * -----------------
 * - Retrieve workspace information
 * - Create workspaces
 * - Update workspaces
 * - Delete workspaces
 *
 * Note:
 * -----
 * This service is responsible only for communicating
 * with the backend API. It does not maintain application
 * state. Workspace state is managed by
 * WorkspaceContextService.
 */

/*------------------------------------------------------------------------------
 * Angular
 *----------------------------------------------------------------------------*/

import { inject, Injectable } from '@angular/core';

/*------------------------------------------------------------------------------
 * RxJS
 *----------------------------------------------------------------------------*/

import { Observable, of } from 'rxjs';

/*------------------------------------------------------------------------------
 * Shared Interfaces
 *----------------------------------------------------------------------------*/

import {
  WorkspaceCreateRequest,
  WorkspaceSummary,
  WorkspaceUpdateRequest,
} from '../../shared/interfaces';
import { WorkspaceHttpService } from '../http/workspace-http.service';

/*------------------------------------------------------------------------------
 * Shared Constants
 *----------------------------------------------------------------------------*/

/*------------------------------------------------------------------------------
 * Service
 *----------------------------------------------------------------------------*/

@Injectable({
  providedIn: 'root',
})
export class WorkspaceService {
  private readonly workspaceHttpService = inject(WorkspaceHttpService);

  getWorkspaces(): Observable<WorkspaceSummary[]> {
    return this.workspaceHttpService.getWorkspaces();
  }

  getWorkspace(workspaceId: string): Observable<WorkspaceSummary> {
    return this.workspaceHttpService.getWorkspace(workspaceId);
  }

  createWorkspace(request: WorkspaceCreateRequest): Observable<WorkspaceSummary> {
    return this.workspaceHttpService.createWorkspace(request);
  }

  updateWorkspace(
    workspaceId: string,
    request: WorkspaceUpdateRequest,
  ): Observable<WorkspaceSummary> {
    return this.workspaceHttpService.updateWorkspace(workspaceId, request);
  }

  deleteWorkspace(workspaceId: string): Observable<void> {
    return this.workspaceHttpService.deleteWorkspace(workspaceId);
  }
}
