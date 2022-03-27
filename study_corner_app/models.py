from django.db import models

# Create your models here.
class Topic(models.Model):
	"""A container that stores a group of Questions"""
	title = models.CharField(max_length=64)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Model returns a string"""
		return self.title


class Question(models.Model):
	"""An element displaying a question or problem"""
	title = models.CharField(max_length=64)
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default="None")
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Model returns a string"""
		return self.title

class Answer(models.Model):
	"""An element displaying the answer to a question or problem"""
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Model returns a string"""
		return self.answer