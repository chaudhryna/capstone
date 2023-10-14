from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.utils import timezone

from helpdesk.decorators import it_staff_required

from accounts.models import User
from tickets.models import Ticket, TechNotes
from tickets.forms import CreateTicketForm, UpdateTicketForm, TechNotesForm

@login_required
def create_ticket(request):
    form = CreateTicketForm()
    
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
    
    if form.is_valid():
        new_ticket = form.save(commit=False)
        new_ticket.customer = request.user
        new_ticket.status = "OPEN" 
        new_ticket.save()
        
        messages.success(request, f'Your ticket has been submitted.')
        return redirect('profile')
    else:
        form = CreateTicketForm()
    
    context = {
            'form': form,
            }
    return render(request, "tickets/create_ticket.html", context)

    
@login_required
def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    
    context = {
        'ticket': ticket,
    }
    return render(request, "partials/_ticket_detail.html", context)

@it_staff_required
def update_ticket(request, ticket_id):
    # techs = User.objects.filter(groups__name='IT Support').order_by('last_name').values()
    ticket = Ticket.objects.get(pk=ticket_id)
    
    if request.method == 'POST':
        update_form = UpdateTicketForm(request.POST, instance=ticket)
        notes_form = TechNotesForm(request.POST)
    
        if update_form.is_valid():
                update_form.save()
                return redirect('it_dashboard')
        elif notes_form.is_valid:
            new_note = notes_form.save(commit=False)
            new_note.tech = request.user
            new_note.ticket = ticket
            new_note.save()
            messages.success(request, f'The ticket has been updated.')
            return redirect('it_dashboard')
    else:
        update_form = UpdateTicketForm(instance=ticket)
        notes_form = TechNotesForm()
        
    tech_notes = TechNotes.objects.filter(ticket=ticket).order_by('-created')
        
    context = {
        'ticket': ticket,
        'update_form': update_form,
        'notes_form': notes_form,
        'tech_notes': tech_notes
    }
   
    return render(request, "tickets/update_ticket.html", context)
    