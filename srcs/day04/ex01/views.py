from django.shortcuts import render

# Create your views here.
def django_framework_web(request):
	context = {
		'title' : 'Ex01: Django, framework web.'
	}
	return render(request,'ex01/base.html',context)
	
def display_process(request):
    context = {
        'title' : 'Ex01: Display process of a static page.'
	}
    return (render(request, 'ex01/display.html',context))

def template_engine(request):
    context = {
        'title' : 'Ex01: Template engine.'
	}
    return (render(request, 'ex01/templates.html',context))