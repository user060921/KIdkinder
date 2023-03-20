from django.shortcuts import render, redirect
from .models import *


def home_page(request):
    context = {'home': 'active'}
    return render(request, 'home.html', context)


def about_page(request):
    about = About.objects.filter().first()
    context = {
        'about': about,
        'About': 'active'
    }
    return render(request, 'about.html', context)


def blog_page(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
        'blog': 'active'
    }

    return render(request, 'blog.html', context)


def class_page(request):
    classes = Class.objects.all()
    context = {
        'classes': classes
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        clases = Class2.objects.create(
            name=name,
            email=email,
            description=description,
        )
        clases.save()
        return redirect('class_page')
    return render(request, 'class.html', context)


def contact_page(request):
    context = {
        'contact': 'active'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        massage = request.POST.get('massage')
        Us = ContactUs.objects.create(
            name=name,
            email=email,
            massage=massage,
            subject=subject,
        )
        print(name, email, subject, massage)
    return render(request, 'contact.html', context)


def gallery_page(request):
    gallerys = Gallery.objects.all()
    context = {
        'gallerys': gallerys,
        'galler': 'active'
    }
    return render(request, 'gallery.html', context)


def single_page(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'single.html', context)


def team_page(request):
    teams = Teachers.objects.all()
    parents = Teacher.objects.all()
    context = {
        'teams': teams,
        'parents': parents
    }
    return render(request, 'team.html', context)


def blog_detail(request, cat_id):
    print(cat_id)
    blog = Blog.objects.all().get(id=cat_id)
    blog.save()
    context = {'blog': blog}
    return render(request, 'detail.html', context)
