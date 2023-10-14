from django.shortcuts import render

from helpdesk.decorators import it_staff_required

from tickets.models import Ticket

@it_staff_required
def it_dashboard(request):
    tech_id = request.user.id
    if Ticket.objects.exists():
        all_tickets = Ticket.objects.all().order_by('-created_date')
        tickets_by_tech = Ticket.objects.filter(assigned_tech=tech_id).order_by('-created_date')
        context = {
            'tickets': all_tickets,
            'tech_tickets': tickets_by_tech,
        }
    else:
        return render(request, 'helpdesk/it_dashboard.html')
    return render(request, 'helpdesk/it_dashboard.html', context)

