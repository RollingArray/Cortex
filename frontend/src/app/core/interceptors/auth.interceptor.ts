/**
 * Authentication Interceptor
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Intercepts outgoing HTTP requests and
 * attaches authentication credentials.
 *
 * Responsibilities:
 * -----------------
 * - Add Authorization header
 * - Skip public endpoints
 * - Prepare the HTTP pipeline for
 *   authenticated requests
 */

/*------------------------------------------------------------------------------
 * Angular
 *----------------------------------------------------------------------------*/

import { HttpInterceptorFn } from '@angular/common/http';

import { inject } from '@angular/core';

/*------------------------------------------------------------------------------
 * RxJS
 *----------------------------------------------------------------------------*/

import { switchMap, take } from 'rxjs/operators';

/*------------------------------------------------------------------------------
 * Services
 *----------------------------------------------------------------------------*/
import { AUTH_SERVICE } from '../services';

/*------------------------------------------------------------------------------
 * Interceptor
 *----------------------------------------------------------------------------*/

export const authInterceptor: HttpInterceptorFn = (
  request,

  next,
) => {
  const auth = inject(AUTH_SERVICE);

  return auth.getToken().pipe(
    take(1),

    switchMap((token) => {
      if (!token) {
        return next(request);
      }

      const authenticatedRequest = request.clone({
        setHeaders: {
          Authorization: `${token.tokenType} ${token.accessToken}`,
        },
      });

      return next(authenticatedRequest);
    }),
  );
};
