from django import forms
from .models import Prato

class FormPratoMenu(forms.ModelForm):
	class Meta:
		model = Prato
		fields = ('nome', 'ingredientes','preparo','pessoas','tempodepreparo',)
