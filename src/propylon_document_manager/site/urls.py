from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from ..file_versions.api.views import RegisterView

# API URLS
urlpatterns = [
    # API base url
    path("api/", include("propylon_document_manager.site.api_router")),
    # DRF auth token
    # path("api-auth/", include("rest_framework.urls")),
    # path("auth-token/", obtain_auth_token),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/register/", RegisterView.as_view()),
]

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
