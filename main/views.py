from django.shortcuts import render, redirect

from . models import Message
from . forms import MessageForm


def home(request):
    return render(request, 'main/home.html')

# def base(request):
#     return render(request, 'main/base.html')

def about(request):
    return render(request, 'main/about.html')
    
def projects(request):
    return render(request, 'main/projects.html')

def say_thanks(request):
    get_message = Message.objects.first()
    author_name = get_message.author_name

    return render(request, 'main/say_thanks.html', {"author_name" : author_name}) 

def contacts_test(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(**form.cleaned_data)
            return (redirect('say_thanks'))
    else:
        form = MessageForm()

    return render(request, 'main/contacts_test.html', {"form" : form})



# views for russian language
def home_ru(request):
    return render(request, 'main/language_ru/home_ru.html')

def about_ru(request):
    return render(request, 'main/language_ru/about_ru.html')
    
def projects_ru(request):
    return render(request, 'main/language_ru/projects_ru.html')

def say_thanks_ru(request):
    get_message = Message.objects.first()
    author_name = get_message.author_name

    return render(request, 'main/language_ru/say_thanks_ru.html', {"author_name" : author_name}) 

def contacts_test_ru(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(**form.cleaned_data)
            return (redirect('say_thanks_ru'))
    else:
        form = MessageForm()

    return render(request, 'main/language_ru/contacts_test_ru.html', {"form" : form})
# end views for russian language