/**
 * API Configuration
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Defines the Cortex backend API configuration
 * and endpoint definitions.
 */

/*------------------------------------------------------------------------------
 * Environment
 *----------------------------------------------------------------------------*/

import { environment } from '../../../environments/environment';

/*------------------------------------------------------------------------------
 * API Configuration
 *----------------------------------------------------------------------------*/

export const API = {
  BaseUrl: environment.apiUrl,

  Version: '/api/v1',

  Endpoints: {
    Health: '/health',

    System: '/system',

    Documents: '/documents',

    Chat: '/chat',

    Search: '/search',
  },
} as const;
