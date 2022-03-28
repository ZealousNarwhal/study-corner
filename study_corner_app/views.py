from django.shortcuts import render, redirect

from .models import Topic, Question

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
		questions = Question.objects.order_by('date_added')
		if Topic.objects.filter(title=topic).exists():
			context = 	{'topic': topic,
						'questions': questions,
						}
			return render(request, 'study_corner_app/questions.html', context)
		else:
			return redirect('/topics')

