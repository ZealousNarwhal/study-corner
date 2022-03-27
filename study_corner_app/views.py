from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
	'''homepage'''
	return render(request, 'study_corner_app/index.html')

def topic(request):
	'''topics page'''
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'study_corner_app/topic.html', context)
