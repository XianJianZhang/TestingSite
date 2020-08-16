from django.shortcuts import render, redirect
from .forms import TestingSiteUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserChangeForm

# Create your views here.
def register(request):
  if request.method == "POST":
    register_form = TestingSiteUserForm(request.POST)
    print(request.POST)
    if register_form.is_valid():
      register_form.save()
      messages.success(request, "Profile successfully created")
      return redirect('blog-home')
  else:
    register_form = TestingSiteUserForm()
  return render(request, "user/register.html", {"form":register_form})

@login_required
def profile(request):
  if (request.method == 'POST'):
    u_form = UserChangeForm(request.POST, instance=request.user)
    p_form = ProfileForm(request.POST, instance=request.user.profile)
    if(u_form.is_valid() and p_form.is_valid()):
      u_form.save()
      p_form.save()
      messages.success(request, "Profile updated!")
      return redirect('user-profile')
  else:
    u_form = UserChangeForm(instance=request.user)
    p_form = ProfileForm(instance=request.user)
  return render(request, 'user/profile.html', {'p_form':p_form, 'u_form': u_form})

