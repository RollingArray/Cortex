/**
 * Authentication Service Token
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Defines the dependency injection token used
 * to resolve the application's authentication
 * service implementation.
 *
 * Responsibilities:
 * -----------------
 * - Decouple consumers from implementations
 * - Enable pluggable authentication services
 * - Support multiple authentication providers
 */

/*------------------------------------------------------------------------------
 * Angular
 *----------------------------------------------------------------------------*/

import { InjectionToken } from '@angular/core';

/*------------------------------------------------------------------------------
 * Services
 *----------------------------------------------------------------------------*/
import { AuthService } from './auth.service';

/*------------------------------------------------------------------------------
 * Injection Token
 *----------------------------------------------------------------------------*/

export const AUTH_SERVICE = new InjectionToken<AuthService>('AUTH_SERVICE');
