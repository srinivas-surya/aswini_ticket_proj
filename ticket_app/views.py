from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import TicketData
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
# Create your views here.

@csrf_exempt
def user_login(request):
    context = {}
    if request.method == "POST":
        '''getting user data from form'''
        username = request.POST['username']
        password = request.POST['password']
        ''' verifying user with the database'''
        user1 = authenticate(request, username=username, password=password)

        if user1:
            login(request, user1)
            '''redirecting to profile_data page'''
            return HttpResponseRedirect(reverse("ticket_view"))

        else:
            ''' user provide wrong credentials sending error msg'''
            context["error"] = "provide valid credentials"
            return render(request, "ticket_app/login.html", context)

    else:
        return render(request, "ticket_app/login.html")

@csrf_exempt
def ticket_create(request):
    if request.method == "POST":
        ''' getting data from user form'''
        name = request.POST['name']
        past_address = request.POST['past_address']
        current_address = request.POST['present_address']
        phone_number = request.POST['phone_number']
        print(name, past_address, current_address, phone_number)
        ''' storing data into database'''
        ticket_view = TicketData.objects.create(
            name=name,
            past_address=past_address,
            present_address=current_address,
            phone_number=phone_number,
            created_user = request.user
        )
        ticket_view.save()
        return HttpResponseRedirect(reverse("ticket_view"))
    else:
        return render(request, "ticket_app/ticket_create.html")


@csrf_exempt
def ticket_view(request):
    created_user_id = request.user.id
    '''filtering data based on user_login'''
    data = TicketData.objects.filter(created_user_id=created_user_id)
    return render(request, "ticket_app/ticket_view.html", {"data":data})


@csrf_exempt
def ticket_update(request,pk):
    if request.method == "POST":
        name = request.POST['username']
        past_address = request.POST['past']
        current_address = request.POST['address']
        phone_number = request.POST['phone']
        "updating profile user data"
        TicketData.objects.filter(pk=pk).update(name=name, past_address=past_address,
                                                 present_address=current_address, phone_number=phone_number)

        return HttpResponseRedirect(reverse("ticket_view"))

    else:
        "filter the data based on user selected value"
        data = TicketData.objects.get(pk=pk)
        return render(request, "ticket_app/ticket_update.html", {"data":data})


@csrf_exempt
def ticket_delete(request, pk):
    data = TicketData.objects.get(pk=pk)
    print("working")
    print(pk)
    data.delete()
    return HttpResponseRedirect(reverse("ticket_view"))

@csrf_exempt
def dashboard(request):
    return render(request, "ticket_app/dashboard.html")