/**
 * API Service
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Provides a centralized HTTP client for communicating
 * with the Cortex
 *
 * Responsibilities:
 * -----------------
 * - Build API URLs
 * - Execute HTTP requests
 * - Provide typed responses
 */

/*------------------------------------------------------------------------------
 * Angular
 *----------------------------------------------------------------------------*/

import { Injectable, inject } from '@angular/core';

import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';

import { Observable } from 'rxjs';

/*------------------------------------------------------------------------------
 * Environment
 *----------------------------------------------------------------------------*/

import { environment } from '../../../environments/environment';

/*------------------------------------------------------------------------------
 * Constants
 *----------------------------------------------------------------------------*/

import { API } from '../../shared/constants';

/*------------------------------------------------------------------------------
 * Service
 *----------------------------------------------------------------------------*/

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  /*--------------------------------------------------------------------------
   * Dependencies
   *--------------------------------------------------------------------------*/

  private readonly http = inject(HttpClient);

  /*--------------------------------------------------------------------------
   * Public Methods
   *--------------------------------------------------------------------------*/

  public get<T>(endpoint: string, params?: HttpParams, headers?: HttpHeaders): Observable<T> {
    return this.http.get<T>(this.buildUrl(endpoint), {
      params,
      headers,
    });
  }

  public post<T>(endpoint: string, body: unknown, headers?: HttpHeaders): Observable<T> {
    return this.http.post<T>(this.buildUrl(endpoint), body, {
      headers,
    });
  }

  public put<T>(endpoint: string, body: unknown, headers?: HttpHeaders): Observable<T> {
    return this.http.put<T>(this.buildUrl(endpoint), body, {
      headers,
    });
  }

  public patch<T>(endpoint: string, body: unknown, headers?: HttpHeaders): Observable<T> {
    return this.http.patch<T>(this.buildUrl(endpoint), body, {
      headers,
    });
  }

  public delete<T>(endpoint: string, headers?: HttpHeaders): Observable<T> {
    return this.http.delete<T>(this.buildUrl(endpoint), {
      headers,
    });
  }

  /*--------------------------------------------------------------------------
   * Private Methods
   *--------------------------------------------------------------------------*/

  private buildUrl(endpoint: string): string {
    return `${environment.apiUrl}${API.Version}${endpoint}`;
  }
}
