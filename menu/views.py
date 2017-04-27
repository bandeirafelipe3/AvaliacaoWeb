from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Prato
from .forms import FormPratoMenu

# Create your views here.

def publicaprato(request):
	pratos = Prato.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'menu/publicaprato.html', {'pratos': pratos})
'''
def adicionaprato(request):
	if request.method == 'POST':
		form = FormPratoMenu(request.POST, request.FILES)
		if form.is_valid():
			dados = form.cleaned_data
			item = Prato(data=dados['data'], nome=dados['nome'],ingredientes=dados['ingredientes'],
				preparo=dados['preparo'], pessoas=dados['pessoas'], tempodepreparo=dados['tempodepreparo'])
			item.save()
			return render_to_response("salvo.html", {})

		else:
			form = FormItemPrato()
		return render_to_response("adiciona.html", {'form': form}, context_instance=RequestContext(request))
'''
def receita_detalhe(request, pk):
	prato = get_object_or_404(Prato, pk=pk)
	return render(request, 'menu/receita_detalhe.html', {'prato': prato})

def nova_receita(request):
	if request.method == "POST":
		form = FormPratoMenu(request.POST)
		if form.is_valid():
			prato = form.save(commit=False)
			prato.autor = request.User
			prato.published_date = timezone.now()
			prato.save()
			return redirect('receita_detalhe', pk=prato.pk)
	else:
		form = FormPratoMenu()
	return render(request, 'menu/editar_receita.html', {'form': form})

def editar_receita(request, pk):
	prato = get_object_or_404(Prato, pk=pk)
	if request.method == "POST":
		form = FormPratoMenu(request.POST, instance=prato)
		if form.is_valid():
			prato = form.save(commit=False)
			prato.autor = request.User
			prato.published_date = timezone.now()
			prato.save()
			return redirect('receita_detalhe', pk=prato.pk)
	else:
		form = FormPratoMenu(instance=prato)
	return render(request, 'menu/editar_receita.html', {'form': form})


