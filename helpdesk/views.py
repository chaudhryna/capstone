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
    
