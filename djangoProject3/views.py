from django.http import HttpResponse
from django.shortcuts import render


def indexr(request):
    # return HttpResponse('<h1> Stupid person in the world</h1> <a target="_blank" href = '
    #                     '"https://getbootstrap.com/docs/4.4/getting-started/introduction/"> FREAK</a>')
    # params = {'name': 'harry', 'place': 'islamabaad'}
    return render(request, 'index.html')  # to use params should call first


def ex1(request):
    return HttpResponse(
        '<h1> Peaky BLINDER </h1> <a style="font-size:32px;" href = ''"https://htmlcheatsheet.com/"> FREAK</a>'
        '<br><a style="font-size:32px;" href="https://www.youtube.com/watch?v=lkhJ7OCOCIc&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12">new</a> '
        '')
    # return render(request, 'ex1.html')


def about(request):
    # to get the text we use Get.get function
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('about', 'off')
    fullcapital = request.POST.get('fullcapital', 'off')
    newline = request.POST.get('newline', 'off')
    removespace = request.POST.get('RemoveSpace', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    # remove punctuation
    if removepunc == 'on':
        punctuation = '''.'!)(}{][,?;:`"-_/@*%^&$#\|><'''
        # return HttpResponse('<h1> GHOST RIDER </h1>')
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        params = {"purpose": "Remove Punctuation", "analyzed_text": analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    # writing in uppercase formate
    if fullcapital == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {"purpose": "SHOW IN UPPERCASE", "analyzed_text": analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newline == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {"purpose": "Remove NEWLINE", "analyzed_text": analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    if removespace == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {"purpose": "Remove SPACES", "analyzed_text": analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if charcounter == 'on':
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1

        params = {"purpose": "Char counter", "analyzed_text": analyzed}
        # return render(request, 'analyze.html', params)
    if removepunc != 'on' and fullcapital != 'on' and newline != 'on' and removespace != 'on' and charcounter != 'on':
        return HttpResponse('<h1 style="text-align: center; margin-top: 286px;"> GAME IS OVER <h1>')

    return render(request, 'analyze.html', params)

    #


# def newline(request):
#     return HttpResponse("waiting for the new line <a href='/'>back</a>")
#
#
# def new(request):
#     return HttpResponse('i am new here')
#
#
# def noo(request):
#     return HttpResponse('so my answer is NOOOOO')
''
