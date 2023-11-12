from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request, 'learning.html')

def analyse(request):
	mytext=request.GET.get('text', 'No Text Entered')
	chec1=request.GET.get('removepun', 'off')
	chec2=request.GET.get('capitalize', 'off')
	chec3=request.GET.get('newLineRemover', 'off')
	chec4=request.GET.get('spaceremover', 'off')
	chec5=request.GET.get('extraspaceremover', 'off')

	if chec1=="on":
		punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
		analzed=""
		for i in mytext:
			if i not in punc:
				analzed=analzed+i

		parameter={'purpose':'Purpose Is to remove Punctuation from String', 'analyse_text':analzed}
		return render(request, 'textanalyse.html', parameter)

	elif chec2=="on":
		uppercase=mytext.upper()
		parameter={'purpose':'Purpose Is to uppercase String', 'analyse_text':uppercase}
		return render(request, 'textanalyse.html', parameter)

	elif chec3=="on":
		analzed=""
		for i in mytext:
			if i != "\n" and i != "\r":
				analzed=analzed+i
		parameter={'purpose':'Purpose Is to uppercase String', 'analyse_text':analzed}
		return render(request, 'textanalyse.html', parameter)

	elif chec4=="on":
		analzed=""
		for i in mytext:
			if i != " ":
				analzed=analzed+i
		parameter={'purpose':'Purpose Is to uppercase String', 'analyse_text':analzed}
		return render(request, 'textanalyse.html', parameter)

	elif chec5=="on":
		analzed=""
		for index, i in enumerate(mytext,0):
			if mytext[index] == " " and mytext[index+1] == " ":
				pass
			else:
				analzed=analzed+i
		parameter={'purpose':'Purpose Is to uppercase String', 'analyse_text':analzed}
		return render(request, 'textanalyse.html', parameter)

	else:
		return HttpResponse("Please Check The Checkbox")

def analysePost(request):
	mytext=request.POST.get('text2', 'No Text Entered')
	chec1=request.POST.get('removepun2', 'off')
	if chec1=="on":
		return HttpResponse(chec1)
	else:
		return HttpResponse(chec1)