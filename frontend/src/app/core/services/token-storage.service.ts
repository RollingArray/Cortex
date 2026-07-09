/**
 * Token Storage Service
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Provides persistent storage for authentication
 * tokens used by the Cortex platform.
 *
 * Responsibilities:
 * -----------------
 * - Store authentication tokens
 * - Retrieve authentication tokens
 * - Remove authentication tokens
 * - Abstract browser storage
 */

/*------------------------------------------------------------------------------
 * Angular
 *----------------------------------------------------------------------------*/

import { Injectable } from '@angular/core';

/*------------------------------------------------------------------------------
 * Shared Interfaces
 *----------------------------------------------------------------------------*/
import { AuthToken } from 'src/app/shared/interfaces';

/*------------------------------------------------------------------------------
 * Constants
 *----------------------------------------------------------------------------*/

const STORAGE_KEY = 'cortex.auth.token';

/*------------------------------------------------------------------------------
 * Service
 *----------------------------------------------------------------------------*/

@Injectable({
  providedIn: 'root',
})
export class TokenStorageService {
  public get(): AuthToken | null {
    const value = localStorage.getItem(STORAGE_KEY);

    if (!value) {
      return null;
    }

    return JSON.parse(value) as AuthToken;
  }

  public save(token: AuthToken): void {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(token));
  }

  public clear(): void {
    localStorage.removeItem(STORAGE_KEY);
  }
}
