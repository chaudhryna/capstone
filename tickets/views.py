from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from tickets.forms import CreateTicketForm

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

