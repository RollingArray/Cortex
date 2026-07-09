/**
 * Authentication Token Interface
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Defines the authentication token model used
 * throughout the Cortex platform.
 *
 * Responsibilities:
 * -----------------
 * - Represent authentication tokens
 * - Support token expiration
 * - Support refresh tokens
 * - Remain provider independent
 */

/*------------------------------------------------------------------------------
 * Authentication Token
 *----------------------------------------------------------------------------*/

export interface AuthToken {
  readonly accessToken: string;

  readonly refreshToken?: string;

  readonly tokenType: string;

  readonly expiresAt?: Date;
}
