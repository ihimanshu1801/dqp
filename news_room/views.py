from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import TemplateView
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required

from rest_framework import generics
from . serializers import ParentInfographSerializer,InfographSerializer#InfographCategorySerializer#,MasterTopicsSerializer,TopicsSerializer
from . models import ParentInfograph, Infograph,InfographCategory, MasterTopics,Topics
from django.contrib.auth.models import User
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
# from . models import Infograph
# from django.http import HttpResponse
# from django.http import Http404

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



class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ParentInfograph.objects.all()
    serializer_class = ParentInfographSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = ParentInfograph.objects.all()
    serializer_class = ParentInfographSerializer


class CreateView(generics.ListCreateAPIView):
    queryset = Infograph.objects.all()
    serializer_class = InfographSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Infograph.objects.all()
    serializer_class = InfographSerializer


class InfographListView(ListView):
    model = Infograph

    def get_queryset(self):
        return Infograph.objects.filter(date_created__lte=timezone.now()).order_by('-date_created')



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
