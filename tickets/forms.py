from django.forms import ModelForm, Textarea, TextInput, Select

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