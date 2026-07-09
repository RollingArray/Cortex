/**
 * Authentication Session Interface
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Defines the authenticated session for the
 * current user.
 *
 * Responsibilities:
 * -----------------
 * - Represent the authenticated session
 * - Combine user and authentication token
 * - Remain provider independent
 */

/*------------------------------------------------------------------------------
 * Imports
 *----------------------------------------------------------------------------*/

import { AuthToken } from './auth-token.interface';

import { AuthUser } from './auth-user.interface';

/*------------------------------------------------------------------------------
 * Authentication Session
 *----------------------------------------------------------------------------*/

export interface AuthSession {
  readonly authenticated: boolean;

  readonly provider: string;

  readonly user?: AuthUser;

  readonly token?: AuthToken;
}
