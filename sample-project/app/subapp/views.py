from django.shortcuts import render

def get_users(request):
    return render(request, "users_list.html")

def get_home(request):
    return render(request, "home.html")

def get_user_profile(request):
    return render(request, "user_profile.html")