from django.contrib.auth.tokens import PasswordResetTokenGenerator

class EmailConfirmationTokenGenerator(PasswordResetTokenGenerator):
	def _make_hash_value(self, user, timestamp):
		return f"{user.pk}{timestamp}{user.is_email_confirmed}"


email_confirmation_token = EmailConfirmationTokenGenerator()