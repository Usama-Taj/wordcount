from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    full_text = request.GET['words']
    no_of_words = full_text.split()
    occurance_of_each_word = {}
    for word in no_of_words:
        if word in occurance_of_each_word:
            occurance_of_each_word[word] += 1
        else:
            occurance_of_each_word[word] = 1

    sorted_occurances = sorted(
        occurance_of_each_word.items(), key=lambda item: item[1], reverse=True)
    return render(request, 'count.html', {
        'full_text': request.GET['words'],
        'no_of_words': len(no_of_words),
        'occurance_of_each_word': sorted_occurances,

    })
