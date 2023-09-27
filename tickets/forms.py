from django.forms import ModelForm, Textarea, TextInput, Select, DateInput

from tickets.models import Ticket
    

class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket 
        fields = ("title", "details", "type_of_issue")
        
        widgets = {
            'type_of_issue': Select(attrs={'class': 'form-control'}),
            'title': TextInput(attrs={'class': 'form-control'}),
            'details': Textarea(attrs={'class': 'form-control', 'cols': 40, 'rows': 3}),
        }
        
class UpdateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ("status", "due_date", "assigned_tech", )
        
        widgets = {
            'status': Select(attrs={'class': 'form-control'}),
            'due_date': DateInput(attrs={'type': 'date', 'placeholder': 'mm-dd-yyyy', 'class': 'form-control'}),
            'assigned_tech': Select(attrs={'class': 'form-control'})
        }