from django.shortcuts import render

from helpdesk.decorators import it_staff_required

from tickets.models import Ticket

@it_staff_required
def it_dashboard(request):
    if Ticket.objects.exists():
        all_tickets = Ticket.objects.all()
        context = {
            'tickets': all_tickets
        }
    else:
        return render(request, 'helpdesk/it_dashboard.html')
    return render(request, 'helpdesk/it_dashboard.html', context)

@it_staff_required
def tech_tickets(request):
    tech_id = request.user.id
    if Ticket.objects.exists():
        tickets_by_tech = Ticket.objects.filter(assigned_tech=tech_id)
        
        context = {
        'tickets': tickets_by_tech
        }   
    else:
        return render(request, 'helpdesk/it_dashboard.html')
    return render(request, 'helpdesk/it_dashboard.html', context)
