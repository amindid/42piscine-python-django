import { LoginPage } from './login.js';

export class HomePage extends HTMLElement {
	constructor() {
		super();
		this.innerHTML = `
						<div id="root" style="width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center;">
						<img src='../images/Pong.svg' alt="" class="logo">
						<img src='../images/Welcome_to_Pong.svg' alt="" class="title">
						<div class="buttonDiv">
							<a href="" class="homeAtag"><button class="homeButton">PLAY LOCAL</button></a>
							<a id="play-online" class="homeAtag"><button class="homeButton">PLAY ONLINE</button></a>
						</div>
						</div>`
	}
	
	connectedCallback() {
		
		this.querySelector('#play-online').addEventListener('click', redirect_login);
		function redirect_login() {
			const html_content = document.querySelector('home-page');
			html_content.remove();
		
			const login = document.createElement('login-page');
			document.body.appendChild(login);
		}
		function changebackground() {
			const body = document.body
				body.style.backgroundImage = "url('../images/homepageBackground.svg')";
		}
		changebackground();
	}
}

customElements.define("home-page", HomePage);
