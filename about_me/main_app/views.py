from django.shortcuts import render
import about_me.settings

# Create your views here.

def main_controller(request):
    return render(request,"main.html",{'base_dir': about_me.settings.BASE_DIR})


def about_controller(request):
    return render(request,"about.html")


def works_controller(request):
    return render(request,"works.html")
