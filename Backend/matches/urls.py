from django.urls import path

from matches.views import MatchListRetrieveViewSet, MatchCreateViewSet, \
    MatchUpdateViewset, MatchFinishViewSet, MatchScoreListViewSet, MatchScoreRetrieveUpdateViewSet, \
    MatchScoreCreateViewSet, MatchPlayScriptAPI

urlpatterns = [
    path('', MatchListRetrieveViewSet.as_view({
        'get': 'list',
    }), name='match-list'),
    path('<uuid:UUID>', MatchListRetrieveViewSet.as_view({
        'get': 'retrieve',
    }), name='match-retrieve'),
    path('create', MatchCreateViewSet.as_view({
        'post': 'create'
    }), name='match-create'),
    path('<uuid:UUID>/join', MatchUpdateViewset.as_view({
        'patch': 'update'
    }), name='match-create'),
    path('<uuid:UUID>/finish', MatchFinishViewSet.as_view({'put': 'update'}, name='match-finish')),
    path('matchscore/', MatchScoreListViewSet.as_view({
        'get': 'list',
    }), name='matchscore-list'),
    path('matchscore/<str:match>/', MatchScoreRetrieveUpdateViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update,'
    }), name='matchscore-retrieve-update'),
    path('matchscore/create', MatchScoreCreateViewSet.as_view({
        'post': 'create'
    }), name='matchscore-create'),
    path('matchscript/create', MatchPlayScriptAPI.as_view()),
]
