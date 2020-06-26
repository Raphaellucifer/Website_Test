from django.shortcuts import render
from Crazy_Minion.models import Post


# Create your views here.
def home(request):
    obj = Post.objects.get(title='Python Data Structures')
    post = {"post_title": obj.title, 'author': obj.author, 'date_added': 'March 16',
            'short_description': obj.text}
    return render(request, 'index.html', context=post)


def tutorials(request):
    return render(request, 'tutorials.html')


def about_us(request):
    return render(request, 'about-us.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def get_to_us(request):
    return render(request, 'get_to_us.html')


def tutorial_post(request):
    return render(request, 'tutorial_post.html')
