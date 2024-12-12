Steps to Setup a token based authentication 

1. install restframework (pip install djangorestframework)
2. include the rest_framework into the INSTALLED APPS in the settings.py file
3. include the rest_framework.authtoken to INSTALLED_APPS
4. run python manage.py migrate to create a table to store authentication tokens.
5. Configure Default Authentication in settings.py
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',
            ],
        }

6. create the token endpoint in the urls.py
    NB: Django REST Framework provides a built-in view for obtaining tokens. You can use this or create your own custom view.

    from django.urls import path
    from rest_framework.authtoken.views import obtain_auth_token

    urlpatterns = [
        ...
        path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    ]
7. Test with the token using POSTMAN
        Access the protected endpoint using the token as a Bearer token in the Authorization header: