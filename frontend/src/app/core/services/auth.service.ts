/**
 * Authentication Service
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Defines the authentication service contract
 * for the Cortex platform.
 *
 * Responsibilities:
 * -----------------
 * - Initialize authentication
 * - Authenticate users
 * - Manage authentication sessions
 * - Provide a provider-independent API
 */

/*------------------------------------------------------------------------------
 * Imports
 *----------------------------------------------------------------------------*/

import { Observable } from 'rxjs';
import { AuthSession, AuthToken, AuthUser } from 'src/app/shared/interfaces';

/*------------------------------------------------------------------------------
 * Authentication Service
 *----------------------------------------------------------------------------*/

export abstract class AuthService {
  public abstract initialize(): Promise<void>;

  public abstract login(): Promise<AuthSession>;

  public abstract logout(): Promise<void>;

  public abstract getSession(): Observable<AuthSession | null>;

  public abstract getUser(): Observable<AuthUser | null>;

  public abstract getToken(): Observable<AuthToken | null>;

  public abstract isAuthenticated(): Observable<boolean>;
}
