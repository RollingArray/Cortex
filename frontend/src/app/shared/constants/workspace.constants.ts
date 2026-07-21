/**
 * Workspace Constants
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Provides default workspace values used
 * throughout the Cortex platform.
 */

/*------------------------------------------------------------------------------
 * Shared Interfaces
 *----------------------------------------------------------------------------*/

import { WorkspaceSummary } from '../interfaces';

/*------------------------------------------------------------------------------
 * Default Workspace
 *----------------------------------------------------------------------------*/

export const DEFAULT_WORKSPACE: WorkspaceSummary = {
  id: 'personal',

  name: 'Personal Workspace',

  description: 'Your personal AI knowledge workspace.',

  documents: 0,

  knowledge: 0,

  conversations: 0,

  agents: 0,
};
