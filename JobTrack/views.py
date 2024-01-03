from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, logout, get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Job
from django.contrib.auth.models import User


# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from .forms import CreateUserForm
from .forms import JobForm
from django.urls import reverse

# Create your views here.

def home(request):
    

   
    return render(request, 'home.html')


@login_required(login_url='login')
def addjob(request):
    form = JobForm()
    person = Person.objects.get(user=request.user)


    if request.method == 'POST':
        form = JobForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                
                person = Person.objects.get(user=request.user)
                job = form.save(commit=False)
                print(job)
                job.person = person
                job.save()
                print(job)

                messages.success(request, f"Job created successfully!")
                return redirect(reverse('alljob'))
            except IntegrityError:
                messages.error(request, 'A job with the same details already exists.')
        else:
            messages.error(request, 'Error occurred while creating the job! Please try again.')

    # Use logging instead of print
    print(request.user.id)  # Replace with proper logging

    context = {'form': form, 'person': person}
    return render(request, 'addjob.html', context)

@login_required(login_url='login')
def alljob(request):
    person = Person.objects.get(user=request.user)
    job = Job.objects.filter(person=person)   
    print(job)
    context = {'job': job, 'person': person}

    return render(request, 'alljob.html', context)


def chart_data(request):
    person = Person.objects.get(user=request.user)


    jobs = Job.objects.filter(person=person) 
    p_job = jobs.filter(status='pending').count()
    d_job = jobs.filter(status='declined').count()
    i_job = jobs.filter(status='Interview').count()
    # Fetch data from your models or any other source
    data = {
        'labels': ['Pending', 'Interview', 'Declined'],
        'data': [p_job, i_job, d_job],
    }
    return JsonResponse(data)






@login_required(login_url='login')
def stats(request):
    person = Person.objects.get(user=request.user)

    jobs = Job.objects.filter(person=person) 
    p_job = jobs.filter(status='pending').count()
    d_job = jobs.filter(status='declined').count()
    i_job = jobs.filter(status='Interview').count()

    context = {'p_job': p_job, 'd_job': d_job, 'i_job': i_job, 'person': person}

    return render(request, 'Stats.html', context)
@login_required(login_url='login')
def profile(request):

    person = Person.objects.get(user=request.user)
   
    new_fname = request.POST.get('fname')
    new_lname = request.POST.get('lname')
    new_email = request.POST.get('email')
    new_username = request.POST.get('username')
    user = request.user

    if request.method == 'POST': 
        try:

            if new_email:
                user.email = new_email
                user.save()
                person.email = new_email
                    
                person.save()
            if new_username:
                user.username = new_username
                user.save()
                person.username = new_username
            if new_fname:
                person.fname = new_fname
                user.first_name = new_fname
                user.save()
                person.save()
            if new_lname:
                person.lname = new_lname
                user.last_name = new_lname
                user.save()
                person.save()
                    
                person.save()
                messages.success(request, f"Profile updated successfully!")
            
            context = {'person': person, 'success_message': 'Profile updated successfully!'}
            return render(request, 'Profile.html', context)
            


        except IntegrityError as e:
            # Handle the error, for example, you can redirect the user to a form page with an error message.
            error_message = f"Error: {e}"
            context = {'person': person, 'error_message': error_message}
            return render(request, 'Profile.html', context)
    else:

        context = {'person': person}
        return render(request, 'Profile.html', context)
    
    
    

def register(request):
    if request.user.is_authenticated:
        return redirect('addjob')   
    else:
    
        form = CreateUserForm()

        if request.method == 'POST': 
            form = CreateUserForm(request.POST)

        
            if not request.POST.get('password1') == request.POST.get('password2'):
                messages.error(request, 'Passwords do not match.')

            elif form.is_valid():
                try:
                    user = form.save()
                    username = form.cleaned_data.get('username')
                    messages.success(request, f"{username} created successfully!")
                    # Redirect to home or profile page
                    return redirect('login')
                except IntegrityError as e:
                    messages.error(request, 'Username or email is already in use.')
            else:
                messages.error(request, "Username or email is already in use, or you're password is weak")

        context = {'form': form, 'error_message': messages.get_messages(request)}
        return render(request, 'register.html', context)
  
 



def user_login(request):  # Renamed from 'login' to avoid conflict
    if request.user.is_authenticated:
        return redirect('/addjob')
    else:
        if request.method == 'POST': 
            username = request.POST.get('username')
            password = request.POST.get('password')        
            user_model = get_user_model()  # Use get_user_model() to get the custom user model
            user = authenticate(request, username=username, password=password)
            

            if user is not None:
                auth_login(request, user)
                
                return redirect('/addjob')
            else:
                messages.info(request, 'Credentials error')
                messages.error(request, 'Error occurred while logging in!')
                context = {'error_message':'Credenrials error, please try again'}  # Move this line outside of the if statement
                return render(request, 'login.html', context)


        context = {}  # Move this line outside of the if statement
        return render(request, 'login.html', context)

@login_required(login_url='login')
def user_logout(request):  # Renamed from 'userLogout' to follow convention
    logout(request)
    return redirect('/')

@login_required(login_url='login')
def delete(request, id):
  job = Job.objects.get(id=id)
  job.delete()
  return redirect('/alljob')

def jobupdate(request, id):
    job = Job.objects.get(id=id)
    new_position = request.POST.get('position')
    new_company = request.POST.get('company')
    new_status = request.POST.get('status')
    new_location = request.POST.get('location')
    new_type = request.POST.get('job_type')
    print(request.POST)
    print(new_position, new_company, new_status)
    if request.method == 'POST':
        if new_position:
            job.position = new_position
        if new_company:
            job.company = new_company
        if new_status:
            job.status = new_status
        if new_location:
            job.job_location = new_location
        if new_type:
            job.job_type = new_type

        job.save()
        return redirect('/alljob')
    else:
        # Handle non-POST requests, e.g., display a form or redirect to an appropriate page
        return redirect('/alljob') 