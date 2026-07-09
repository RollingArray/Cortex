/**
 * Mock Authentication Service
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Provides a mock authentication implementation
 * for local development.
 *
 * Responsibilities:
 * -----------------
 * - Simulate authentication
 * - Provide a default authenticated user
 * - Enable frontend development without
 *   a backend authentication provider
 */

/*------------------------------------------------------------------------------
 * Angular
 *----------------------------------------------------------------------------*/

import { Injectable } from '@angular/core';

/*------------------------------------------------------------------------------
 * RxJS
 *----------------------------------------------------------------------------*/

import { BehaviorSubject, Observable } from 'rxjs';

/*------------------------------------------------------------------------------
 * Services
 *----------------------------------------------------------------------------*/

import { AuthService } from './auth.service';

/*------------------------------------------------------------------------------
 * Shared Interfaces
 *----------------------------------------------------------------------------*/

import { AuthSession, AuthToken, AuthUser } from '../../shared/interfaces';

/*------------------------------------------------------------------------------
 * Service
 *----------------------------------------------------------------------------*/

@Injectable({
  providedIn: 'root',
})
export class MockAuthService extends AuthService {
  private readonly session = new BehaviorSubject<AuthSession | null>(null);

  public async initialize(): Promise<void> {
    const user: AuthUser = {
      id: 'local-user',

      username: 'ranjoy',

      displayName: 'Ranjoy Sen',

      email: 'ranjoy@localhost',

      roles: ['Administrator'],
    };

    const token: AuthToken = {
      accessToken: 'mock-access-token',

      tokenType: 'Bearer',
    };

    this.session.next({
      authenticated: true,

      provider: 'Mock',

      user,

      token,
    });
  }

  public async login(): Promise<AuthSession> {
    return this.session.value!;
  }

  public async logout(): Promise<void> {
    this.session.next(null);
  }

  public getSession(): Observable<AuthSession | null> {
    return this.session.asObservable();
  }

  public getUser(): Observable<AuthUser | null> {
    return new Observable((subscriber) => {
      this.session.subscribe((session) => {
        subscriber.next(session?.user ?? null);
      });
    });
  }

  public getToken(): Observable<AuthToken | null> {
    return new Observable((subscriber) => {
      this.session.subscribe((session) => {
        subscriber.next(session?.token ?? null);
      });
    });
  }

  public isAuthenticated(): Observable<boolean> {
    return new Observable((subscriber) => {
      this.session.subscribe((session) => {
        subscriber.next(session?.authenticated ?? false);
      });
    });
  }
}
