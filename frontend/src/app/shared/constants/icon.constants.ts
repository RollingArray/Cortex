/**
 * Icon Constants
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Defines the application's centralized icon library.
 *
 * Responsibilities:
 * -----------------
 * - Provide application icons
 * - Ensure icon consistency
 * - Eliminate hardcoded icon names
 */

/*------------------------------------------------------------------------------
 * Ionicons
 *----------------------------------------------------------------------------*/

import {
  documentTextOutline,
  layersOutline,
  serverOutline,
  chatbubbleEllipsesOutline,
  searchOutline,
  settingsOutline,
  gridOutline,
  pulseOutline,
  cloudUploadOutline,
  cloudDownloadOutline,
  refreshOutline,
  playOutline,
  stopOutline,
  checkmarkCircleOutline,
  closeCircleOutline,
  warningOutline,
  informationCircleOutline,
} from 'ionicons/icons';

/*------------------------------------------------------------------------------
 * Icons
 *----------------------------------------------------------------------------*/

export const ICONS = {
  Navigation: {
    Dashboard: gridOutline,

    Chat: chatbubbleEllipsesOutline,

    Documents: documentTextOutline,

    Search: searchOutline,

    System: pulseOutline,

    Settings: settingsOutline,
  },

  Metrics: {
    Documents: documentTextOutline,

    Chunks: layersOutline,

    Backend: serverOutline,
  },

  Actions: {
    Upload: cloudUploadOutline,

    Download: cloudDownloadOutline,

    Refresh: refreshOutline,

    Start: playOutline,

    Stop: stopOutline,
  },

  Status: {
    Healthy: checkmarkCircleOutline,

    Error: closeCircleOutline,

    Warning: warningOutline,

    Information: informationCircleOutline,
  },
} as const;
