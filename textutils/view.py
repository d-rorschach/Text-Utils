from django.http import HttpResponse
from django.shortcuts import render

def homepage(rq):
    return render(rq,'home.html')

def analyze(rq):
    txt=rq.POST.get('txt','default')
    punc=rq.POST.get('punc','off')
    caps=rq.POST.get('caps','off')
    newlineremover=rq.POST.get('newlineremover','off')
    extraspaceremover=rq.POST.get('extraspaceremover','off')
    res=""

    if (caps=="on"):
        for c in txt:
            res=res+c.upper()
        txt=res
        res=""
    
    if(newlineremover=="on"):
        for c in txt:
            if (c!='\n') or (c!='\r'):
                res+=c
        txt=res
        res=""

    if(extraspaceremover=="on"):
        res=txt[0]
        for i in range(1,len(txt)):
            if (txt[i-1]!=' ') or (txt[i]!=' '):
                res+=txt[i]
        txt=res
        res=""

    if(punc=="on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for c in txt:
            if c not in punctuations:
                res+=c
        txt=res
        res=""

    param={'answer':txt}
    return render(rq,'analyze.html',param)