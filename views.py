# i have created this file -


from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
#    return HttpResponse("""Hello World <a href = "https://youtu.be/zKj4KWEP970"> LearnDjangoWithMe </a>""")


def index(request):
    #Now I'm going to add a dictionary in this file and then adding it into our index.html file
    #ram = {'name':'Krishna','place':"Out of the universe"}
    #return render(request, 'index.html', ram)
    return render(request, 'index.html')
    #return HttpResponse("Home")
#def removepunc(request):
#    djtext = request.GET.get('text', 'default')
#    print(djtext)
#    return HttpResponse("remove punc <a href='/'>back</a>")
#def capfirst(request):
#    return HttpResponse("capitalize first")
#def newlineremove(request):
#    return HttpResponse("new line remove")
#def spaceremove(request):
#    return HttpResponse("space remove")
#def charcount(request):
#    return HttpResponse("character count")


#def exercise1(request):
#    a = '''<h2>Navigation Bar<br></h2> <a href="https://youtu.be/zKj4KWEP970">My Playlist</a><br>
#    <a href="https://youtube.com/">YouTube</a><br>
#    <a href="https://web.whatsapp.com/">Whatsapp Web</a><br>'''
#    return HttpResponse(a)


def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''@!%;:<>-[]{}( *+?.,^|]/&")'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        ram = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', ram)
    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        ram = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', ram)
    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        ram = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', ram)
    elif spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        ram = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', ram)
    elif charcounter == "on":
        analyzed = ""
        for char in djtext:
            analyzed=len(djtext)
        return render(request, 'analyze.html')
    else:
        return HttpResponse("Error")
