/**
 * Shell Component
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Provides the primary application shell for
 * workspace-scoped pages.
 */

/*------------------------------------------------------------------------------
 * Imports
 *----------------------------------------------------------------------------*/

import { Component, DestroyRef, OnInit, inject } from '@angular/core';

import { ActivatedRoute } from '@angular/router';

import { IonRouterOutlet, IonSplitPane } from '@ionic/angular/standalone';

import { filter, map, distinctUntilChanged } from 'rxjs';

import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

import { SidebarComponent } from '../sidebar/sidebar.component';

import { WorkspaceContextService } from 'src/app/core/services';

/*------------------------------------------------------------------------------
 * Component
 *----------------------------------------------------------------------------*/

@Component({
  selector: 'app-shell',
  standalone: true,
  templateUrl: './shell.component.html',
  styleUrls: ['./shell.component.scss'],
  imports: [IonSplitPane, IonRouterOutlet, SidebarComponent],
})
export class ShellComponent implements OnInit {
  /*--------------------------------------------------------------------------
   * Dependencies
   *------------------------------------------------------------------------*/

  private readonly route = inject(ActivatedRoute);

  private readonly destroyRef = inject(DestroyRef);

  private readonly workspaceContext = inject(WorkspaceContextService);

  /*--------------------------------------------------------------------------
   * Lifecycle
   *------------------------------------------------------------------------*/

  public ngOnInit(): void {
    this.route.paramMap
      .pipe(
        map((params) => params.get('workspaceId')),
        filter((id): id is string => id !== null),
        distinctUntilChanged(),
        takeUntilDestroyed(this.destroyRef),
      )
      .subscribe(async (workspaceId) => {
        await this.workspaceContext.selectWorkspace(workspaceId);
      });
  }
}
