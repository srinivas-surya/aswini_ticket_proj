from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import TicketData, CompletedTicketData
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
import time
# Create your views here.


@login_required
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
            '''redirecting to ticket_details page'''
            return HttpResponseRedirect(reverse("ticket_view"))

        else:
            ''' user provide wrong credentials sending error msg'''
            context["error"] = "provide valid credentials"
            return render(request, "ticket_app/login.html", context)

    else:
        return render(request, "ticket_app/login.html")


@login_required
@csrf_exempt
def ticket_create(request):
    if request.method == "POST":
        ''' getting data from user form'''
        topic = request.POST['topic']
        tower = request.POST['tower']
        dc = request.POST['dc']
        action_item = request.POST['item']
        severity = request.POST['severity']
        action_history = request.POST['history']
        action_history = (str(datetime.now())[0:11]) + " " + str(action_history)
        owner = request.POST['owner']
        eta = request.POST['eta']
        status_value = request.POST['status_value']
        print(status_value)
        ''' storing data into database'''
        ticket_data_create = TicketData.objects.create(
            topic=topic,
            tower=tower,
            dc=dc,
            action_item=action_item,
            severity=severity,
            action_history=action_history,
            owner=owner,
            status=status_value,
            eta=eta,
            updated_at=None
        )
        ticket_data_create.save()
        return HttpResponseRedirect(reverse("ticket_view"))
    else:
        return render(request, "ticket_app/ticket_create.html")


@login_required
@csrf_exempt
def ticket_view(request):
    '''render all tickets to the front end'''
    data = TicketData.objects.all()
    return render(request, "ticket_app/ticket_view.html", {"data": data})


@login_required
@csrf_exempt
def ticket_update(request, pk):
    if request.method == "POST":
        action_history = request.POST['history']
        status_val = request.POST['drop1']
        if status_val == "Completed":
            ticket_delete(pk, action_history)
            return HttpResponseRedirect(reverse("ticket_view"))
        else:

            "updating profile user data"
            data = TicketData.objects.get(pk=pk)
            old_action = str(data.action_history)
            new_action = str(date.today()) + " " + str(action_history)
            new_action = (old_action + "\n" + new_action)
            updated_at = datetime.now()
            TicketData.objects.filter(pk=pk).update(action_history=new_action,
                                                    status=status_val, updated_at=updated_at)
            return HttpResponseRedirect(reverse("ticket_view"))

    else:
        "filter the data based on user selected value"
        print(pk)
        data = TicketData.objects.get(pk=pk)
        return render(request, "ticket_app/ticket_update.html", {"data": None})


def ticket_delete(pk, action_history):
    data = TicketData.objects.get(pk=pk)
    old_action = str(data.action_history)
    new_action = str(date.today()) + " " + str(action_history)
    new_action = (old_action + "\n" + new_action)

    ''' storing data completed into database'''
    completed_ticket_create = CompletedTicketData.objects.create(
        topic=data.topic,
        tower=data.tower,
        dc=data.dc,
        action_item=data.action_item,
        severity=data.severity,
        action_history=new_action,
        owner=data.owner,
        status="Completed",
        eta=data.eta,
        created_at=data.created_at
    )
    completed_ticket_create.save()
    time.sleep(1)
    '''after updating into completed table deleting record from ticket table'''
    data.delete()


@login_required
@csrf_exempt
def dashboard(request):
    return render(request, "ticket_app/dashboard.html")