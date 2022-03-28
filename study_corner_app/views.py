from django.shortcuts import render, redirect

from .models import Topic

# Create your views here.
def index(request):
	'''homepage'''
	return render(request, 'study_corner_app/index.html')

def topics(request):
	'''topics display page'''
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'study_corner_app/topics.html', context)

def questions(request):
	'''questions display page'''
	if request.method == 'GET':
		topic = request.GET.get('topic', '')
		if Topic.objects.filter(title=topic).exists():
			context = {'topic': topic}
			return render(request, 'study_corner_app/questions.html', context)
		else:
			return redirect('/topics')

