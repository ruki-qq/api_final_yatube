from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    CommentModelViewSet,
    FollowModelViewSet,
    GroupModelViewSet,
    PostModelViewSet,
)

router_v1 = DefaultRouter()
router_v1.register('groups', GroupModelViewSet, basename='group')
router_v1.register('posts', PostModelViewSet, basename='post')
router_v1.register('follow', FollowModelViewSet, basename='follow')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentModelViewSet, basename='comment'
)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
