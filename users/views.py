from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
# from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import requests

# Create your views here.


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# def github(request):
#     search_result = {}
#     if 'username' in request.GET:
#         username = request.GET['username']
#         url = 'https://api.github.com/users/%s' % username
#         response = requests.get(url)
#         search_was_successful = (response.status_code == 200)  # 200 = SUCCESS
#         search_result = response.json()
#         search_result['success'] = search_was_successful
#         search_result['rate'] = {
#             'limit': response.headers['X-RateLimit-Limit'],
#             'remaining': response.headers['X-RateLimit-Remaining'],
#         }
#     return render(request, 'core/github.html', {'search_result': search_result})
#
#
# def github_client(request):
#     search_result = {}
#     if 'username' in request.GET:
#         username = request.GET['username']
#         client = Github()
#
#         try:
#             user = client.get_user(username)
#             search_result['name'] = user.name
#             search_result['login'] = user.login
#             search_result['public_repos'] = user.public_repos
#             search_result['success'] = True
#         except GithubException as ge:
#             search_result['message'] = ge.data['message']
#             search_result['success'] = False
#
#         rate_limit = client.get_rate_limit()
#         search_result['rate'] = {
#             'limit': rate_limit.rate.limit,
#             'remaining': rate_limit.rate.remaining,
#         }
#
#     return render(request, 'core/github.html', {'search_result': search_result})
