/**
 * Workspace Summary Interface
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Defines the summary information displayed
 * for the active workspace.
 *
 * Responsibilities:
 * -----------------
 * - Represent workspace metadata
 * - Provide workspace statistics
 * - Support dashboard presentation
 */

/*------------------------------------------------------------------------------
 * Workspace Summary
 *----------------------------------------------------------------------------*/

export interface WorkspaceSummary {
  readonly id: string;

  readonly name: string;

  readonly description: string;

  readonly documents: number;

  readonly knowledge: number;

  readonly conversations: number;

  readonly agents: number;
}
