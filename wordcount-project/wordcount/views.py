from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'hithere':'This is me..'})

def count(request):
    fulltext = request.GET['fulltext'] # to get the entered text from url
    
    wordList = fulltext.split()

    worddictionary = {}
    for word in wordList:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)
    
    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordList),'sortedwords':sortedwords})

def aboutus(request):
    return render(request, 'aboutus.html')