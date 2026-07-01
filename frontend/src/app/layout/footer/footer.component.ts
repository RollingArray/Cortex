import { Component } from '@angular/core';

import {
	IonFooter,
	IonToolbar,
	IonText,
} from '@ionic/angular/standalone';

@Component({
	selector: 'app-footer',
	standalone: true,
	templateUrl: './footer.component.html',
	styleUrls: ['./footer.component.scss'],
	imports: [
		IonFooter,
		IonToolbar,
		IonText,
	],
})
export class FooterComponent {}