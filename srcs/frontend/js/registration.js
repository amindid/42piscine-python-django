import {HomePage} from './homePage.js' ;
import {LoginPage} from './login.js' ;

export class RegistrationPage extends HTMLElement {
	constructor() {
		super();
	}
	connectedCallback() {
		this.innerHTML = `
						<a id="go-back" ><img src='../images/arrow.svg' alt="" class="goBackArrow"></a>
						<div id="root" class="box">
							<div class="ponglogo">
								<img src='../images/Pong.svg'>
							</div>
							<div class="titleDecorationDiv">
								<hr color="white" width="80%" style="max-width: 700px;">
								<div class="regiTitle">
									<img src='../images/REGESTRATION.svg' alt="">
								</div>
							</div>
								<form action="registration" method="post" class="regi-form-container">
									<div class="regi-inputdiv">
										<input type="email" id="email" name="email" style="padding-left: 10px;" placeholder="Enter your email" autocomplete="off" required>
									</div>
									<div class="regi-inputdiv">
										<input type="text" id="username" name="username" style="padding-left: 10px;" placeholder="Enter your username" autocomplete="off" required>
									</div>
									<div class="regi-inputdiv">
										<input type="password" id="password" name="password" style="padding-left: 10px;" placeholder="Enter your password" required>
										<span class="ayeIcon">
											<img src='../images/closed-eye.svg' id="eye-icon" alt="Show password" width="100%" height="100%">
										</span>
									</div>
									<div class="regi-inputdiv">
										<input type="password" id="passwordConfirmation" name="passwordConfirmation" style="padding-left: 10px;" placeholder="Confirm your password" required>
									</div>
									<div class="regi-buttonDiv">
										<button  type="submit" class="button" >REGISTER</button>
									</div>
									</form>
							<div class="signUpDiv">
								<p><a id="redirect-login" >SIGN IN</a></p>
							</div>
						</div>`

		document.getElementById('go-back').addEventListener('click', redirect_homepage);
		function redirect_homepage() {
			const html_content = document.querySelector('registration-page');
			html_content.remove();
		
			const login = new HomePage;
			document.body.appendChild(login);
		}
		document.getElementById('redirect-login').addEventListener('click', redirect_login);
		function redirect_login() {
			const html_content = document.querySelector('registration-page');
			html_content.remove();
		
			const login = new LoginPage;
			document.body.appendChild(login);
		}
		document.getElementById('eye-icon').addEventListener("click", change_eye);
		function change_eye() {
			const passwordInput = document.getElementById('password');
			const eyeIcon = document.getElementById('eye-icon');
			
			const currentType = passwordInput.getAttribute('type');
			
			if (currentType === 'password') {
				passwordInput.setAttribute('type', 'text');
				eyeIcon.src = "../images/eye.svg";
				eyeIcon.alt = "Hide password";
			} else {
				passwordInput.setAttribute('type', 'password');
				eyeIcon.src = "../images/closed-eye.svg";
				eyeIcon.alt = "Show password";
			}
		}
		function changebackground() {
			const body = document.body
				body.style.backgroundImage = "url('../images/registrationBackground.svg')";
		}
		changebackground();
	}
}

customElements.define("registration-page", RegistrationPage);
