import {
  chatbubbleOutline,
  documentTextOutline,
  gridOutline,
  hardwareChipOutline,
  searchOutline,
  settingsOutline,
} from 'ionicons/icons';

import { AppNavigationItem } from '../interfaces/app-navigation-item.interface';

export const NAVIGATION: readonly AppNavigationItem[] = [
  {
    title: 'Dashboard',
    path: '/dashboard',
    icon: gridOutline,
  },
  {
    title: 'Ask Cortex',
    path: '/chat',
    icon: chatbubbleOutline,
  },
  {
    title: 'Documents',
    path: '/documents',
    icon: documentTextOutline,
  },
  {
    title: 'Search',
    path: '/search',
    icon: searchOutline,
  },
  {
    title: 'System',
    path: '/system',
    icon: hardwareChipOutline,
  },
  {
    title: 'Settings',
    path: '/settings',
    icon: settingsOutline,
  },
] as const;
