/**
 * System Status Interface
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Defines the system information returned by the
 * Cortex
 */

export interface SystemStatus {
  version: string;

  environment: string;

  aiProvider: string;

  vectorStore: string;

  status: string;
}
