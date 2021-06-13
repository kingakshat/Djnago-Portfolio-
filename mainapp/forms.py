from django.forms import ModelForm
from .models import Feedback

class CustomerForm(ModelForm):
	class Meta:
		model = Feedback
		fields = '__all__'
		#print(fields, model)
		



