/**
 * Authentication Constants
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Provides mock authentication data used during
 * local development.
 */

/*------------------------------------------------------------------------------
 * Shared Interfaces
 *----------------------------------------------------------------------------*/

import { AuthSession } from '../interfaces';

/*------------------------------------------------------------------------------
 * Mock Authentication
 *----------------------------------------------------------------------------*/

export const MOCK_AUTH_SESSION: AuthSession = {
  authenticated: true,

  provider: 'Mock',

  user: {
    id: 'local-user',

    username: 'ranjoy',

    displayName: 'Ranjoy Sen',

    email: 'ranjoy@localhost',

    roles: ['Administrator'],
  },

  token: {
    accessToken: 'mock-access-token',

    tokenType: 'Bearer',
  },
};
