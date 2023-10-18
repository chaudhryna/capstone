from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count


from helpdesk.decorators import it_staff_required

from tickets.models import Ticket

def chart_data(request):
    data = Ticket.objects.values('type_of_issue').annotate(total=Count('type_of_issue'))

    labels = [item["type_of_issue"] for item in data]
    values = [item["total"] for item in data]
    
    chart_data = {
        'labels': labels,
        'values': values,
        'chart_type': 'pie'
    }
    return JsonResponse(chart_data)

def tech_chart(request):
    data = Ticket.objects.values('assigned_tech__last_name').annotate(total_tickets=Count('assigned_tech'))

    labels = [item["assigned_tech__last_name"] for item in data]
    values = [item["total_tickets"] for item in data]

    tech_chart = {
        'labels': labels,
        'values': values,
        'chart_type': 'doughnut'
    }
    return JsonResponse(tech_chart)

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

