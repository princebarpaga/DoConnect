from django.shortcuts import render

# Create your views here.
def post_list(request):
	return render(request, 'doconnect_website/frontpage.html', {})
def patient(request):
	return render(request, 'doconnect_website/patient_login.html',{})

def doctor(request):
	return render(request, 'doconnect_website/doctor_login.html',{})