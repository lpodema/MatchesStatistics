from django.urls import path

from players.views import PlayerListRetrieveUpdateViewSet, PlayerCreateViewSet, \
    PlayerScoreViewSet, ProfileImageViewSet, PlayerReportViewSet

urlpatterns = [
    path('', PlayerListRetrieveUpdateViewSet.as_view({
        'get': 'list',
    }), name='player-list'),
    path('<uuid:UUID>', PlayerListRetrieveUpdateViewSet.as_view({
        'get': 'retrieve',
        # 'patch': 'partial_update,'
    }), name='player-retrieve-update'),
    path('create', PlayerCreateViewSet.as_view({
        'post': 'create'
    })),
    path('playerscore/', PlayerScoreViewSet.as_view({
        'get': 'list',
    }), name='player-create'),
    path('playerscore/<str:player>', PlayerScoreViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update,'
    }), name='playerscore-retrieve-update'),
    path('profileimage/', ProfileImageViewSet.as_view({
        'get': 'list',
    }), name='profileimage-list'),
    path('profileimage/<str:player>', ProfileImageViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update,'
    }), name='profileimage-retrieve-update'),
    path('report/', PlayerReportViewSet.as_view({
        'get': 'list',
    }), name='best-players-report'),

]
