from django import forms
from .models import Subscription, Provider, Frequency


class SubscriptionForm(forms.ModelForm):
	class Meta:
		model = Subscription
		fields = ['provider', 'amount', 'frequency']

	provider 	= forms.ModelChoiceField(
						required=True,
						queryset=Provider.objects.all().order_by('name'),
						widget=forms.Select(attrs={'class': 'form-control form-resize mx-auto my-2'}) 
				)
	amount		= forms.DecimalField(
       			 		required=True,
						max_digits=10,
        				decimal_places=2,
						widget=forms.NumberInput(attrs={'class': 'form-control form-resize mx-auto my-2', 'placeholder': 'Enter Amount'})

    			)
	frequency		= forms.ModelChoiceField(
						required=True, 
						queryset=Frequency.objects.all(),
						widget=forms.Select(attrs={'class': 'form-control form-resize mx-auto my-2'}) 
				)
