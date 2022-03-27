from django.shortcuts import render

# Create your views here.
def index(request):
	'''homepage'''
	return render(request, 'study_corner_app/index.html')
