from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm

@login_required
def profil_views(request):
    template_name = 'profiles/profil.html'
    return render(request, template_name)

def home(request):
    return render(request, 'home.html')

def signup_views(request):
    template_name = 'registration/signup.html'
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, template_name, {
		'form':form
	})


def logout_views(request):
    template_name = 'registration/logout.html'
    return render(request, template_name)



