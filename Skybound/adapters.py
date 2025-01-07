from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_email
from django.contrib.auth import get_user_model

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # If the user is already logged in, skip
        if sociallogin.is_existing:
            return

        # Get the email from the social account
        email = user_email(sociallogin.account.user)
        if email:
            # Check if an account with this email exists
            User = get_user_model()
            try:
                existing_user = User.objects.get(email=email)
                sociallogin.connect(request, existing_user)
            except User.DoesNotExist:
                # Create a new user if it doesn't exist
                user = User(email=email, username=email.split('@')[0])
                user.save()
                sociallogin.account.user = user
                sociallogin.account.save()
                sociallogin.connect(request, user)
        else:
            print("Email not found in social account")
