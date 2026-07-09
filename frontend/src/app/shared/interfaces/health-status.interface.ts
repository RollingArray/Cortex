/**
 * Health Status
 *
 * Project:
 * --------
 * Cortex
 *
 * Purpose:
 * --------
 * Represents the operational status of the Cortex platform
 * returned by the backend health endpoint.
 */

export interface HealthStatus {
  success: boolean;

  status: string;
}
