from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . views import (ParentInfographCreateView, InfographCreateView,
                    TopicsCreateView, UsersCreateView)

from . views import (ParentInfographDetailsView, InfographDetailsView,
                    TopicsDetailsView,UsersDetailsView,InfographListView)
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

    path('topics/parentinfograph/', ParentInfographCreateView.as_view(), name="parentinfograph_list"),
    re_path(r'^topics/parentinfograph/(?P<pk>[0-9]+)/$',
            ParentInfographDetailsView.as_view(), name="parentinfograph_details"),

    path('topics/infograph/', InfographCreateView.as_view(), name="infograph_list"),
    re_path(r'^topics/infograph/(?P<pk>[0-9]+)/$',
             InfographDetailsView.as_view(), name="infograph_details"),

    path('infograph/', InfographListView.as_view(), name="list"),

    path('topics/', TopicsCreateView.as_view(), name="topic_list"),
    re_path(r'^topics/(?P<pk>[0-9]+)/$',
             TopicsDetailsView.as_view(), name="topic_details"),

    path('users/', UsersCreateView.as_view(), name="users_create"),
    re_path(r'^users/(?P<pk>[0-9]+)/$',
             UsersDetailsView.as_view(), name="user_details"),

    # path('mastertopics/', CreateView.as_view(), name="create"),
    # re_path(r'^mastertopics/(?P<pk>[0-9]+)/$',
    #         DetailsView.as_view(), name="details"),
    #
    # path('infographcategory/', CreateView.as_view(), name="create"),
    # re_path(r'^infographcategory/(?P<pk>[0-9]+)/$',
    #         DetailsView.as_view(), name="details"),


}

urlpatterns = format_suffix_patterns(urlpatterns)
