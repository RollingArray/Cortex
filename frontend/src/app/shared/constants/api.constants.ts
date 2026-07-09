/**
 * API Constants
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Defines the Cortex backend API version and
 * endpoint definitions.
 */

export const API = {
  Version: '/api/v1',

  Health: {
    Status: '/health',
  },

  System: {
    Status: '/system',
  },

  Documents: {
    List: '/documents',

    Upload: '/documents/upload',

    Delete: '/documents',
  },

  Search: {
    Query: '/search',
  },

  Chat: {
    Message: '/chat',
  },
} as const;
