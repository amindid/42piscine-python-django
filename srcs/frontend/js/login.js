import {HomePage} from './homePage.js' ;
import {RegistrationPage} from './registration.js' ;

export class LoginPage extends HTMLElement {
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
								<form action="login" method="post" class="form-checkbox-container">
										<div class="inputdiv">
											<input type="text" id="username" name="username" placeholder="Enter your username" autocomplete="off" required>
										</div>
										<div class="inputdiv">
											<input type="password" id="password" name="password" placeholder="Enter your password" required>
											<span class="ayeIcon">
												<img src='../images/closed-eye.svg' id="eye-icon" alt="Show password" width="100%" height="100%">
											</span>
										</div>
										<div class="ckeckbox-fpass-container">
											<div class="checkbox-div">
												<label class="checkBoxContainer">
													<input type="checkbox">
													<svg viewBox="0 0 64 64" height="22px" width="21.52px">
														<path d="M 0 16 V 56 A 8 8 90 0 0 8 64 H 56 A 8 8 90 0 0 64 56 V 8 A 8 8 90 0 0 56 0 H 8 A 8 8 90 0 0 0 8 V 16 L 32 48 L 64 16 V 8 A 8 8 90 0 0 56 0 H 8 A 8 8 90 0 0 0 8 V 56 A 8 8 90 0 0 8 64 H 56 A 8 8 90 0 0 64 56 V 16" pathLength="575.0541381835938" class="path"></path>
													</svg>
												</label>
												<p class="rememberme">Remember Me</p>
											</div>
											<div class="fpass-div">
												<a style="text-decoration: none;" id="forgate_passwprd"><p class="text">Forget password?</p></a>
											</div>
										</div>
										<div style="width: 100%; display: flex; flex-direction: column; align-items: center;">
											<button type="submit" class="button" >LOGIN</button>
										</div>
								</form>
							<div class="separation">
								<hr color="white" width="80%" style="max-width: 700px;">
								<div class="orDiv">Or</div>
							</div>
							<div class="authcontainer">
								<button type="submit" value="facebookAuth" class="button2"  style="background-color: #0472FF;"><img src='../images/facebook.svg' alt=""></button>
								<button type="submit" value="42Auth" class="button2"  style="background-color: black;"><img src='../images/42.svg' alt=""></button>
								<button type="submit" id="google-auth-btn" value="googleAuth" class="button2" ><img src='../images/google.svg' alt=""></button>
							</div>
							<div class="signUpDiv">
								<p>New User? <a id="redirect-registration" >SIGN UP HERE</a></p>
							</div>
						</div>`

			document.getElementById('go-back').addEventListener('click', redirect_homepage);
			function redirect_homepage() {
				const html_content = document.querySelector('login-page');
				html_content.remove();
			
				const login = new HomePage;
				document.body.appendChild(login);
			}
			document.getElementById('redirect-registration').addEventListener('click', redirect_registration);
			function redirect_registration() {
				const html_content = document.querySelector('login-page');
				html_content.remove();
			
				const login = new RegistrationPage;
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

customElements.define("login-page", LoginPage);
