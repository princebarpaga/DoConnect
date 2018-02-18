from django.shortcuts import render,redirect
from .forms import PatientSignUpForm, AskQuestions
from .models import Patient, Question
from django.http import JsonResponse


# Create your views here.
def post_list(request):
	return render(request, 'doconnect_website/frontpage.html', {})


def patient(request):
	if request.method == 'POST':
		patientSignUpForm = PatientSignUpForm(request.POST)
		if patientSignUpForm.is_valid():
			print('valid')
			username=patientSignUpForm.cleaned_data.get('username')
			password=patientSignUpForm.cleaned_data.get('password')
			patient = Patient.objects.create(username = username, password = password)
			patient_id = patient.id
			return redirect('/patient_profile/' + str(patient_id) + '/')
		else:
			print('invalid') 
	else:
		patientSignUpForm = PatientSignUpForm(request.POST or None)
		context = {'patientSignUpForm': patientSignUpForm}
		return render(request, 'doconnect_website/patient_login.html',context)

def doctor(request):
	return render(request, 'doconnect_website/doctor_login.html',{})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def patient_login(request):
	return render(request, 'doconnect_website/patient_profile.html',{})

def validate_username(request):
	
	return render(request, 'doconnect_website/patient_profile.html',{})

def patient_profile(request, patient_id):
	patient = Patient.objects.get(id = patient_id)
	return render(request, 'doconnect_website/patient_profile.html',{})

def questions(request):
	return render(request, 'doconnect_website/question_page/index.html',{})


def questionsend(request):
	if request.method == 'POST':
		patientQuestionForm = AskQuestions(request.POST)
		if patientQuestionForm.is_valid():
			print('valid')
			userid=patientQuestionForm.cleaned_data.get('userid')
			userquestion=patientQuestionForm.cleaned_data.get('userquestion')
			priorityid=patientQuestionForm.cleaned_data.get('priorityid')
			qtion = Question.objects.create(userid = userid, userquestion = userquestion, priorityid= priorityid)
			patient_id = 0
			return redirect('patient_profilee/')
		else:
			print('invalid') 
	else:
		patientQuestionForm = AskQuestions(request.POST or None)
		context = {'patientQuestionForm':patientQuestionForm}
		return render(request, 'doconnect_website/question_page/index.html/',context)

def finalP(request):
	return render(request, 'doconnect_website/frontpage.html', {})