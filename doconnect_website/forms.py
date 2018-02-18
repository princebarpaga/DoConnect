from django import forms

from .models import Post
from .models import Patient
from .models import Question

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class PatientSignUpForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ('username', 'password')

class AskQuestions(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('userid','userquestion', 'priorityid')

