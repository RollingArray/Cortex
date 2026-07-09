/**
 * Cortex Application Bootstrap
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Bootstraps the Cortex Angular application
 * and registers the application's core
 * infrastructure providers.
 *
 * Responsibilities:
 * -----------------
 * - Bootstrap Angular
 * - Configure Ionic
 * - Configure Routing
 * - Configure HTTP Client
 * - Register Authentication
 */

/*------------------------------------------------------------------------------
 * Angular
 *----------------------------------------------------------------------------*/

import { bootstrapApplication } from '@angular/platform-browser';

import {
  RouteReuseStrategy,
  provideRouter,
  withPreloading,
  PreloadAllModules,
} from '@angular/router';

import { provideHttpClient, withInterceptors } from '@angular/common/http';

/*------------------------------------------------------------------------------
 * Ionic
 *----------------------------------------------------------------------------*/

import { IonicRouteStrategy, provideIonicAngular } from '@ionic/angular/standalone';

/*------------------------------------------------------------------------------
 * Application
 *----------------------------------------------------------------------------*/

import { AppComponent } from './app/app.component';

import { routes } from './app/app.routes';

/*------------------------------------------------------------------------------
 * Core
 *----------------------------------------------------------------------------*/

import { AUTH_SERVICE, MockAuthService } from './app/core/services';

import { authInterceptor } from './app/core/interceptors/auth.interceptor';

/*------------------------------------------------------------------------------
 * Bootstrap
 *----------------------------------------------------------------------------*/

bootstrapApplication(AppComponent, {
  providers: [
    {
      provide: RouteReuseStrategy,
      useClass: IonicRouteStrategy,
    },

    {
      provide: AUTH_SERVICE,
      useClass: MockAuthService,
    },

    provideIonicAngular(),

    provideHttpClient(withInterceptors([authInterceptor])),

    provideRouter(
      routes,

      withPreloading(PreloadAllModules),
    ),
  ],
});
