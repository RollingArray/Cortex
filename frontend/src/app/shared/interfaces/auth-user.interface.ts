/**
 * Authentication User Interface
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Defines the authenticated user model used
 * throughout the Cortex platform.
 *
 * Responsibilities:
 * -----------------
 * - Represent the authenticated user
 * - Support future authentication providers
 * - Provide a provider-independent user model
 */

/*------------------------------------------------------------------------------
 * Authentication User
 *----------------------------------------------------------------------------*/

export interface AuthUser {
  readonly id: string;

  readonly username: string;

  readonly displayName: string;

  readonly email: string;

  readonly roles: readonly string[];
}
