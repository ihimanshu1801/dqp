from django.shortcuts import render

from rest_framework import generics
from . serializers import ParentInfographSerializer,InfographSerializer,InfographCategorySerializer,MasterTopicsSerializer,TopicsSerializer
from . models import ParentInfograph, Infograph,InfographCategory, MasterTopics,Topics
from django.contrib.auth.models import User
import requests



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


class CreateView(generics.ListCreateAPIView):
    queryset = InfographCategory.objects.all()
    serializer_class = InfographCategorySerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Infograph.objects.all()
    serializer_class = InfographSerializer


class CreateView(generics.ListCreateAPIView):
    queryset = MasterTopics.objects.all()
    serializer_class = MasterTopicsSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = MasterTopics.objects.all()
    serializer_class = MasterTopicsSerializer



class CreateView(generics.ListCreateAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer

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
#
#
# def home(request):
#     response = requests.get('http://freegeoip.net/json/')
#     geodata = response.json()
#     return render(request, 'home.html', {
#         'ip': geodata['ip'],
#         'country': geodata['country_name']
    # })
