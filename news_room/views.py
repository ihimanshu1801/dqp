from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters,generics,viewsets

from . serializers import (ParentInfographSerializer,InfographSerializer,
                           TopicsSerializer,UsersSerializer)#InfographCategorySerializer#,MasterTopicsSerializer,

from . models import (ParentInfograph, Infograph,InfographCategory,
                      MasterTopics,Topics,Users)

from django.contrib.auth.models import User
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from rest_framework import permissions

import django_filters.rest_framework
import django_filters
import requests

# def homepage(request):
#     infographs = Infograph.objects.all()
#     return render(request, 'homepage.html', {'infographs': infographs})
#
# def board_topics(request, pk):
#     infograph = get_object_or_404(Infograph, pk=pk)
#     return render(request, 'topics.html', {'infographs': infographs})
#
# def new_topic(request, pk):
#     infograph = get_object_or_404(Board, pk=pk)
#     return render(request, 'new_topic.html', {'infographs': infographs})
# class Index(TemplateView):
#     template_name = "index.html"
#     def get_context_data(self):
#         context = super(Index, self).get_context_data()
#         return context

# class ParentInfographViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = ParentInfograph.objects.all().order_by('title')
#     serializer_class = ParentInfographSerializer


# class IsAuthenticatedOrReadOnly(permissions.BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         # Read permission - always allow for GET request
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         # Write permissions - only if authenticated
#         return request.user and request.user.is_authenticated()
#
# @permission_classes((IsAuthenticatedOrReadOnly, ))
class ParentInfographCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ParentInfograph.objects.all()
    serializer_class = ParentInfographSerializer
    filter_backends = (filters.SearchFilter,django_filters.rest_framework.DjangoFilterBackend,)
    search_fields = ('name', 'description',)
    filter_fields = ('name', 'description',)


    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class ParentInfographDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = ParentInfograph.objects.all()
    serializer_class = ParentInfographSerializer


# class InfographListView(generics.ListAPIView):
#     queryset = Infograph.objects.all()
#     serializer_class = InfographSerializer
#     filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

# class InfographList(generics.ListAPIView):
#     queryset = Infograph.objects.all()
#     serializer_class = InfographSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filter_fields = ('name', 'description',"external_url")

#
# class InfographFilter(django_filters.FilterSet):
#     latest = django_filters.NumberFilter(name="latest", lookup_type='gte')
#     trending = django_filters.NumberFilter(name="trending", lookup_type='lte')
#     class Meta:
#         model = Infograph
#         fields = ['name', 'description', 'external_url','i_id']
#

class InfographCreateView(generics.ListCreateAPIView):
    queryset = Infograph.objects.all()
    serializer_class = InfographSerializer
    filter_backends = (filters.SearchFilter,django_filters.rest_framework.DjangoFilterBackend,
                      filters.OrderingFilter,)#filters.DjangoObjectPermissionsFilter,)
    search_fields = ('name', 'description',)
    filter_fields = ('name', 'description',"external_url",)
    ordering_fields = ("date_created","likes",)
    # permission_classes = (news_room.permissions.CustomObjectPermissions,)
    ordering = ("date_created",)


    def perform_create(self, serializer):
        serializer.save()


class InfographDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Infograph.objects.all()
    serializer_class = InfographSerializer

class InfographListView(generics.ListAPIView):
    queryset = Infograph.objects.all()
    serializer = InfographSerializer
    filter_backends = (filters.SearchFilter,)
#
# class InfographListView(ListView):
#     model = Infograph
#
#     def get_queryset(self):
#         return Infograph.objects.filter(date_created__lte=timezone.now()).order_by('-date_created')
# ========================================================
class TopicsCreateView(generics.ListCreateAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ( 'topic_description')

    def perform_create(self, serializer):
        serializer.save()


class TopicsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer


class TopicsListView(ListView):
    model = Topics

    def get_queryset(self):
        return Infograph.objects.filter(date_created__lte=timezone.now()).order_by('-date_created')

class UsersCreateView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name')


class UsersDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


# class CreateView(generics.ListCreateAPIView):
#     queryset = InfographCategory.objects.all()
#     serializer_class = InfographCategorySerializer
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#
# class DetailsView(generics.RetrieveUpdateDestroyAPIView):
#
#     queryset = InfographCategory.objects.all()
#     serializer_class = InfographCategorySerializer

#
# class CreateView(generics.ListCreateAPIView):
#     queryset = MasterTopics.objects.all()
#     serializer_class = MasterTopicsSerializer
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#
# class DetailsView(generics.RetrieveUpdateDestroyAPIView):
#
#     queryset = MasterTopics.objects.all()
#     serializer_class = MasterTopicsSerializer
#
#
#
# class CreateView(generics.ListCreateAPIView):
#     queryset = Topics.objects.all()
#     serializer_class = TopicsSerializer
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#
# class DetailsView(generics.RetrieveUpdateDestroyAPIView):
#
#     queryset = Topics.objects.all()
#     serializer_class = TopicsSerializer
# #
# class UserView(generics.ListAPIView):
#     """View to list the user queryset."""
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetailsView(generics.RetrieveAPIView):
#     """View to retrieve a user instance."""
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer


# def home(request):
#     response = requests.get('http://freegeoip.net/json/')
#     geodata = response.json()
#     return render(request, 'home.html', {
#         'ip': geodata['ip'],
#         'country': geodata['country_name']
#     })
