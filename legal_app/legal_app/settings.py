# In legal_app/settings.py:

INSTALLED_APPS = [
    # ... other apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ... your apps
    'core',
    # If using django-allauth:
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
]

# ... other settings

# If using django-allauth, add these settings:
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )

# SITE_ID = 1  # Replace with your actual site ID if needed

# LOGIN_REDIRECT_URL = '/'  # Where to redirect after login
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # or 'optional'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
```

```python
# In legal_app/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # ... other URL patterns
    # If using django-allauth:
    # path('accounts/', include('allauth.urls')),
    # If using custom views (without allauth):
    path('accounts/', include('django.contrib.auth.urls')),  # Includes login, logout, password reset
]
```

```python
# Create a templates directory (legal_app/templates) and add a login template (legal_app/templates/registration/login.html):

# {% extends "base.html" %}  (Assuming you have a base template)

# {% block content %}
#   <h2>Login</h2>
#   <form method="post">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <button type="submit">Login</button>
#   </form>
# {% endblock %}

# (Adapt this template based on whether you're using django-allauth or built-in auth)