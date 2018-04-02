from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . views import ParentInfographCreateView, InfographCreateView,TopicsCreateView
from . views import ParentInfographDetailsView, InfographDetailsView,TopicsDetailsView
from . import views
from rest_framework import routers
from rest_framework_jwt.views import refresh_jwt_token

# router = routers.DefaultRouter()
# router.register(r'parentinfograph', views.ParentInfographViewSet)
#



urlpatterns = {
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('refresh-token/', refresh_jwt_token),
    # path('homepage', views.homepage, name = 'homepage'),
    # re_path(r'^infographs/(?P<pk>\d+)/$', views.board_topics, name = "board_topics"),
    # re_path(r'^infographs/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    # path(' ',views.InfographListView.as_view(),name='infograph_list'),

    path('parentinfograph/', ParentInfographCreateView.as_view(), name="create"),
    re_path(r'^parentinfograph/(?P<pk>[0-9]+)/$',
            ParentInfographDetailsView.as_view(), name="details"),

    path('parentinfograph/infograph/', InfographCreateView.as_view(), name="create"),
    re_path(r'^parentinfograph/infograph/(?P<pk>[0-9]+)/$',
             InfographDetailsView.as_view(), name="details"),

    path('topics/', TopicsCreateView.as_view(), name="create"),
    re_path(r'^topics/(?P<pk>[0-9]+)/$',
             TopicsDetailsView.as_view(), name="details"),

    # path('infographs/', InfographListView.as_view(), name="create"),
    # re_path(r'^infograph/(?P<pk>[0-9]+)/$',
    #          InfographDetailsView.as_view(), name="details"),
#
#     path('mastertopics/', CreateView.as_view(), name="create"),
#     re_path(r'^mastertopics/(?P<pk>[0-9]+)/$',
#             DetailsView.as_view(), name="details"),
#
#     path('topics/', CreateView.as_view(), name="create"),
#     re_path(r'^topics/(?P<pk>[0-9]+)/$',
#             DetailsView.as_view(), name="details"),
#
    # path('infographcategory/', CreateView.as_view(), name="create"),
    # re_path(r'^infographcategory/(?P<pk>[0-9]+)/$',
    #         DetailsView.as_view(), name="details"),


}

urlpatterns = format_suffix_patterns(urlpatterns)
