from django.urls import path, include
from .views import PropertyViewSet, PropertySearchView, BlogPostView, AgentView
from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static

app_name = 'base'

router = routers.DefaultRouter()
router.register('properties', PropertyViewSet, basename='properties')
router.register('blogposts', BlogPostView, basename='blogs')
router.register('agents', AgentView, basename='agents')


urlpatterns = [
    path('', include(router.urls)),
    path('posts/by-category/', BlogPostView.as_view({'get': 'list_by_category'}), name='posts-by-category'),
    path('properties/search/custom/', PropertySearchView.as_view(), name='property-search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
