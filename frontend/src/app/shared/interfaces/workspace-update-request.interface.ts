/**
 * Update Workspace Request
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Defines the payload used to
 * update a workspace.
 */

export interface WorkspaceUpdateRequest {
  name?: string;

  description?: string;
}
