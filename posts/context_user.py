def picture(request):
    # user = request.user
    # print(user)
    # picture = user.socialaccount_set.filter(provider='github')[0].extra_data['avatar_url']
    picture = "https://github.com/mdo.png"
    # print(picture)
    return {'user_picture': picture}
