import { Component } from '@angular/core';

import { ShellComponent } from './layout/shell/shell.component';

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  imports: [
    ShellComponent,
  ],
})
export class AppComponent {}