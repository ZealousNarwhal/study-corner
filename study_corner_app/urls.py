'''URL pattern definitions for study_corner_app'''

from django.urls import path

from . import views

app_name = "study_corner_app"
urlpatterns = [
	# Home Page
	path('', views.index, name='index'),
	path('topics', views.topics, name='topics'),
	path('questions', views.questions, name='questions')
]