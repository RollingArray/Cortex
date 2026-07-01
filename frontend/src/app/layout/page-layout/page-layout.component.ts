import { Component, Input } from '@angular/core';

import { TopbarComponent } from '../topbar/topbar.component';
import { FooterComponent } from '../footer/footer.component';

@Component({
	selector: 'app-page-layout',
	standalone: true,
	templateUrl: './page-layout.component.html',
	styleUrls: ['./page-layout.component.scss'],
	imports: [
		TopbarComponent,
		FooterComponent,
	],
})
export class PageLayoutComponent {

	@Input({ required: true })
	pageTitle!: string;

}