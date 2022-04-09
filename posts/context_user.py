# def picture(request):
#     user = request.user
#     picture = 'https://github.com/mdo.png'
#     if user.is_active:
#         for i in user.socialaccount_set.all():
#             if i.provider == 'github':
#                 picture = i.extra_data['avatar_url']
#             elif i.provider == 'google':
#                 picture = i.extra_data['picture']
#             else:
#                 picture = 'https://github.com/mdo.png'
#     return {'user_picture': picture}
