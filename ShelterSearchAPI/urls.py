from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sheltersearchapi/', include('base.urls', namespace='base')),
    # User Management
    path('api/user/', include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Schema & Documentation
    path('api/docs/', include_docs_urls(title='ShelterSearchAPI')),
    path('/schema', get_schema_view(
        title="ShelterSearchAPI",
        description="API for the ShelterSearchAPI",
        version="1.0.0"
    ), name='openapi-schema'),

]
