from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
  if request.method == "POST":
    register_form = UserCreationForm(request.POST)
    if register_form.is_valid() == True:
      register_form.save()
      messages.add_message(request, messages.SUCCESS, "Created profile")
      return redirect('blog-home')
  else:
    register_form = UserCreationForm()
  return render(request, 'user/register.html', {"form": register_form})