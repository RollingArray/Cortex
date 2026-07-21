/**
 * Workspace Context Service
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Maintains the active workspace context
 * for the current user session.
 *
 * Responsibilities:
 * -----------------
 * - Initialize workspace context
 * - Maintain active workspace
 * - Switch active workspace
 * - Clear workspace context
 */

/*------------------------------------------------------------------------------
 * Angular
 *----------------------------------------------------------------------------*/

import { Injectable, inject } from '@angular/core';

/*------------------------------------------------------------------------------
 * RxJS
 *----------------------------------------------------------------------------*/

import { BehaviorSubject, firstValueFrom } from 'rxjs';

/*------------------------------------------------------------------------------
 * Shared Interfaces
 *----------------------------------------------------------------------------*/

import { WorkspaceSummary } from 'src/app/shared/interfaces';

/*------------------------------------------------------------------------------
 * Services
 *----------------------------------------------------------------------------*/

import { WorkspaceService } from './workspace.service';

/*------------------------------------------------------------------------------
 * Service
 *----------------------------------------------------------------------------*/

@Injectable({
  providedIn: 'root',
})
export class WorkspaceContextService {
  /*--------------------------------------------------------------------------
   * Dependencies
   *--------------------------------------------------------------------------*/

  private readonly workspaceService = inject(WorkspaceService);

  /*--------------------------------------------------------------------------
   * State
   *--------------------------------------------------------------------------*/

  private readonly workspaceSubject = new BehaviorSubject<WorkspaceSummary | null>(null);

  /*--------------------------------------------------------------------------
   * Observables
   *--------------------------------------------------------------------------*/

  public readonly currentWorkspace$ = this.workspaceSubject.asObservable();

  /*--------------------------------------------------------------------------
   * Public Methods
   *--------------------------------------------------------------------------*/

  /**
   * Initializes the workspace context.
   *
   * Loads all available workspaces and selects
   * the first workspace as the active workspace.
   */
  public async initialize(): Promise<void> {
    console.log('a');
    const workspaces = await firstValueFrom(this.workspaceService.getWorkspaces());

    if (workspaces.length === 0) {
      this.clear();

      return;
    }

    this.setWorkspace(workspaces[0]);
  }

  /**
   * Selects the active workspace.
   */
  public async selectWorkspace(workspaceId: string): Promise<void> {
    const workspace = await firstValueFrom(this.workspaceService.getWorkspace(workspaceId));

    this.setWorkspace(workspace);
  }

  /**
   * Returns the current workspace.
   */
  public get currentWorkspace(): WorkspaceSummary | null {
    return this.workspaceSubject.value;
  }

  /**
   * Sets the current workspace.
   */
  public setWorkspace(workspace: WorkspaceSummary): void {
    this.workspaceSubject.next(workspace);
  }

  /**
   * Clears the current workspace.
   */
  public clear(): void {
    this.workspaceSubject.next(null);
  }
}
