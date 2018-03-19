from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . views import CreateView
from . views import DetailsView
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'parentinfograph', views.ParentInfographViewSet)
#



urlpatterns = {
    # re_path(r'^api/', include(router.urls)),
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # re_path(r'^index/$', views.Index, name='index'),

    path(' ',views.InfographListView.as_view(),name='infograph_list'),

    path('parentinfograph/', CreateView.as_view(), name="create"),
    re_path(r'^parentinfograph/(?P<pk>[0-9]+)/$',
            DetailsView.as_view(), name="details"),

    path('infograph/', CreateView.as_view(), name="create"),
    re_path(r'^infograph/(?P<pk>[0-9]+)/$',
            DetailsView.as_view(), name="details"),
#
#     path('mastertopics/', CreateView.as_view(), name="create"),
#     re_path(r'^mastertopics/(?P<pk>[0-9]+)/$',
#             DetailsView.as_view(), name="details"),
#
#     path('topics/', CreateView.as_view(), name="create"),
#     re_path(r'^topics/(?P<pk>[0-9]+)/$',
#             DetailsView.as_view(), name="details"),
#
    path('infographcategory/', CreateView.as_view(), name="create"),
    re_path(r'^infographcategory/(?P<pk>[0-9]+)/$',
            DetailsView.as_view(), name="details"),


}

urlpatterns = format_suffix_patterns(urlpatterns)
