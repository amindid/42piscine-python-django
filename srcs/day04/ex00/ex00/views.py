from django.shortcuts import render

# Create your views here.

def markdown_cheatsheet(request):
    context = {
        'title' : 'Ex00: Markdown Cheatsheet.'
	}
    return (render(request, 'ex00/index.html',context))