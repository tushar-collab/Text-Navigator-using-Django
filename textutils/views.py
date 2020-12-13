from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   # params={'name':'Tushar','soft':'django'}
    return render(request,'index.html')
    #return HttpResponse('''<h1>hello bhai</h1><br><a href="https://www.hackerrank.com/">Click here</a>''')

def about(request):
    return render(request,'aboutus.html')


def analyse(request):

    #collecting the text
    djtext=request.POST.get('text','default')

    # checking the checkboxes
    removepunc=request.POST.get('removepunc','off')
    capital=request.POST.get('caps','off')
    removenew=request.POST.get('rnew','off')
    extraspace=request.POST.get('exsp','off')
    countchar=request.POST.get('charcount','off')

    #print(djtext)
    if removepunc == "on":

        analysed=""
        punc='''!"#$%&'()*+,"-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punc:
                analysed=analysed+char
        djtext=analysed
        params={'purpose':'remove punctuations','analsed_text':analysed}
        #return render(request,'analyse.html',params)
    if capital == "on":

        analysed=""
        for ch in djtext:
            analysed=analysed + ch.upper()
        djtext=analysed
        params={'purpose':'Capitalize','analsed_text':analysed}
        #return render(request,'analyse.html',params)
    if removenew == "on":
        analysed=""
        for ch in djtext:
            if ch != "\n" and ch != "\r":
                analysed=analysed + ch
        djtext=analysed
        params={'purpose':'Remove new line','analsed_text':analysed}
        #return render(request,'analyse.html',params)
    if extraspace == "on":
        analysed=""
        for index,ch in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analysed=analysed + ch
        djtext=analysed
        params={'purpose':'Remove extra space','analsed_text':analysed}
        #return render(request,'analyse.html',params)
    if countchar == "on":
        analysed=0

        for ch in djtext:
            if ch!=" ":
                analysed=analysed+1
        djtext=analysed
    #params={'purpose':'counting characters','analsed_text':analysed}
    if(removepunc != "on" and removenew != "on" and extraspace != "on" and capital != "on"):
        return render(request,'error.html')
    return render(request,'analyse.html',params)





