# i have created this file - OM


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
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('spaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        rams = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        rams = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        rams = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        rams = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', rams)
