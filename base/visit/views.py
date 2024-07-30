from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main.html', {'title': 'AI Planner'})


def sections(request):
    return render(request, 'sections.html', {'title': 'AI Planner'})

def design(request):
    return render(request, 'sections/design.html', {'title': 'AI Planner'})

def smart(request):
    return render(request, 'sections/smart.html', {'title': 'AI Planner'})

def video(request):
    return render(request, 'video.html', {'title': 'AI Planner'})