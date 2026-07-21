import { Routes } from '@angular/router';

export const routes: Routes = [
  /*--------------------------------------------------------------------------
   * Default
   *------------------------------------------------------------------------*/

  {
    path: '',
    pathMatch: 'full',
    redirectTo: 'workspaces',
  },

  /*--------------------------------------------------------------------------
   * Workspaces
   *------------------------------------------------------------------------*/

  {
    path: 'workspaces',
    loadComponent: () =>
      import('./features/workspaces/pages/workspaces.page').then((m) => m.WorkspacesPage),
  },

  /*--------------------------------------------------------------------------
   * Workspace Shell
   *------------------------------------------------------------------------*/

  {
    path: 'workspaces/:workspaceId',
    loadComponent: () => import('./layout/shell/shell.component').then((m) => m.ShellComponent),

    children: [
      {
        path: '',
        pathMatch: 'full',
        redirectTo: 'dashboard',
      },

      {
        path: 'dashboard',
        loadComponent: () =>
          import('./features/dashboard/pages/dashboard.page').then((m) => m.DashboardPage),
      },
    ],
  },

  /*--------------------------------------------------------------------------
   * Wildcard
   *------------------------------------------------------------------------*/

  {
    path: '**',
    redirectTo: 'workspaces',
  },
];
