/**
 * Create Workspace Request
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Defines the payload used to
 * create a workspace.
 */

export interface WorkspaceCreateRequest {
  name: string;

  description: string;

  workspaceType: string;
}
