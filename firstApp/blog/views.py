from django.shortcuts import render


posts = [
    {
        'author': 'Ashish',
        'title': 'Blog Post 1',
        'content': 'This is my first django app', 
        'date_posted':'July 1'
    },
    {
        'author': 'Ashish',
        'title': 'Blog Post 2',
        'content': 'This is my second django app', 
        'date_posted':'July 2'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)


def about(request):
    return render(request,'blog/about.html', {'title': 'About'})
