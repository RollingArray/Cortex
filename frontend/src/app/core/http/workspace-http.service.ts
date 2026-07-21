/**
 * Workspace API
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Provides HTTP operations for
 * Workspace resources.
 *
 * Features:
 * ---------
 * - List workspaces
 * - Retrieve workspace
 * - Create workspace
 * - Update workspace
 * - Delete workspace
 */

import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { ApiService } from '../services';
import {
  WorkspaceCreateRequest,
  WorkspaceSummary,
  WorkspaceUpdateRequest,
} from 'src/app/shared/interfaces';

@Injectable({
  providedIn: 'root',
})
export class WorkspaceHttpService {
  private readonly api = inject(ApiService);

  /**
   * Retrieve all workspaces.
   */
  getWorkspaces(): Observable<WorkspaceSummary[]> {
    return this.api.get<WorkspaceSummary[]>('/workspaces');
  }

  /**
   * Retrieve a workspace.
   */
  getWorkspace(workspaceId: string): Observable<WorkspaceSummary> {
    return this.api.get<WorkspaceSummary>(`/workspaces/${workspaceId}`);
  }

  /**
   * Create a workspace.
   */
  createWorkspace(request: WorkspaceCreateRequest): Observable<WorkspaceSummary> {
    return this.api.post<WorkspaceSummary>('/workspaces', request);
  }

  /**
   * Update a workspace.
   */
  updateWorkspace(
    workspaceId: string,
    request: WorkspaceUpdateRequest,
  ): Observable<WorkspaceSummary> {
    return this.api.patch<WorkspaceSummary>(`/workspaces/${workspaceId}`, request);
  }

  /**
   * Delete a workspace.
   */
  deleteWorkspace(workspaceId: string): Observable<void> {
    return this.api.delete<void>(`/workspaces/${workspaceId}`);
  }
}
