
# Copy this file to github_settings.py (don't check it into github)

# Go to https://github.com/settings/developers

# Add a New OAuth2 App

# Using ngrok is hard because the url changes every time you start ngrok

# If you are running on localhost, here are some settings:

# Application name: ChuckList Local
# Homepage Url: http://localhost:8000
# Application Description: Whatever
# Authorization callback URL: http://127.0.0.1:8000/oauth/complete/github/


# Using PythonAnywhere here are some settings:

# Application name: ChuckList PythonAnywhere
# Homepage Url: https://drchuck.pythonanywhere.com
# Application Description: Whatever
# Authorization callback URL: https://drchuck.pythonanywhere.com/oauth/complete/github/

# Also on PythonAnywhere, go into the Web tab and enable "Force HTTPS"
# so you don't get a redirect URI mismatch.

# Then copy the client_key and secret to this file
# local
# SOCIAL_AUTH_GITHUB_KEY = '88910d8134b4a02a451b'
# SOCIAL_AUTH_GITHUB_SECRET = 'c377ce1c99e14501f7fc0be212fbee2ea7997f05'
# ngrok
SOCIAL_AUTH_GITHUB_KEY = 'c2e4dc16ddfafc048bab'
SOCIAL_AUTH_GITHUB_SECRET = '15f6c8902e23ca0b833a8520634de8d0b7c88a1d'

# For detail: https://readthedocs.org/projects/python-social-auth/downloads/pdf/latest/

