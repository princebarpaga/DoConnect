from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def post_list(request):
	return render(request, 'doconnect_website/frontpage.html', {})
def patient(request):
	return render(request, 'doconnect_website/patient_login.html',{})

def doctor(request):
	return render(request, 'doconnect_website/doctor_login.html',{})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def patient_login(request):
	return render(request, 'doconnect_website/patient_profile.html',{})