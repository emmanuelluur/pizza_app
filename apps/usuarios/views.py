from django.shortcuts import render
from .forms import RegisterNewUserForm
# Create your views here.

def register_user(request):
	template = './register.html'
	context = {}
	if request.method == 'POST':
		form = RegisterNewUserForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, template, {"message": "User Saved", "clase": "alert-success text-center"})
		else:
			return render(request, template, {"message": "Error check all fields", "clase": "alert-danger text-center"})
	return render(request, template, context)
