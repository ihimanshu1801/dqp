from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . views import CreateView
from . views import DetailsView
from . import views


urlpatterns = {
    path('parentinfograph/', CreateView.as_view(), name="create"),
    re_path(r'^parentinfograph/(?P<pk>[0-9]+)/$',
            DetailsView.as_view(), name="details"),

    # path('address/', views.address, name='address'),
    path('infograph/', CreateView.as_view(), name="create"),
    re_path(r'^infograph/(?P<pk>[0-9]+)/$',
            DetailsView.as_view(), name="details"),

    path('mastertopics/', CreateView.as_view(), name="create"),
    re_path(r'^mastertopics/(?P<pk>[0-9]+)/$',
            DetailsView.as_view(), name="details"),

    path('topics/', CreateView.as_view(), name="create"),
    re_path(r'^topics/(?P<pk>[0-9]+)/$',
            DetailsView.as_view(), name="details"),

    path('infographcategory/', CreateView.as_view(), name="create"),
    re_path(r'^infographcategory/(?P<pk>[0-9]+)/$',
            DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
