# import requests
# from django.conf import settings
#
# class StackOverflowMiddleware(object):
#     def process_exception(self, request, exception):
#         if settings.DEBUG:
#             intitle = u'{}: {}'.format(exception.__class__.__name__,  exception.message)
#             print (intitle)
#
#             url = 'https://api.stackexchange.com/2.2/search'
#             headers = { 'User-Agent': 'github.com/vitorfs/users' }
#             params = {
#                 'order': 'desc',
#                 'sort': 'votes',
#                 'site': 'stackoverflow',
#                 'pagesize': 3,
#                 'tagged': 'python;django',
#                 'intitle': intitle
#             }
#
#             r = requests.get(url, params=params, headers=headers)
#             questions = r.json()
#
#             print ('')
#
#             for question in questions['items']:
#                 print (question['title'])
#                 print (question['link'])
#                 print ('')
#
#         return None
