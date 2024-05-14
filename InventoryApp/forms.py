# forms.py
from django import forms

class RoleSelectionForm(forms.Form):
    ROLES = (
        ('admin', 'Admin'),
        ('cashier', 'Cashier'),
    )
    role = forms.ChoiceField(choices=ROLES, widget=forms.RadioSelect)
