from django.shortcuts import render
from .forms import ProductForm, TransactionForm
from .models import Product, Transaction

def index(request):
	if request.method == 'POST':
		if request.POST.get('item', '') == 'item':
			t = Transaction()
			form = request.POST
			t.who = form.get('who', '')
			paid = form.get('paid', '')
			if paid == 'on':
				t.paid = True
			else:
				t.paid = False
			t.product = Product.objects.get(pk=int(form.get('product', '')))
			t.save()

	context = {
		'form':TransactionForm(),
		'items': Product.objects.all()
	}
	return render(request, 'index.html', context)

def item(request):
	if request.method == 'POST':
		if request.POST.get('item', '') == 'item':
			p = Product()
			form = request.POST
			p.name = form.get('name', '')
			p.cost = form.get('cost', '')
			p.price = form.get('price', '')
			p.save()
		if request.POST.get('delete', '') != '':
			p = Product.objects.get(pk=int(request.POST.get('delete', ''))) 
			p.delete()
	context = {
	'form': ProductForm(),
	'items': Product.objects.all(),
	'check': len(Product.objects.all())
	}
	return render(request, 'item.html', context)

def record(request):
	context = {
	'debts': Transaction.objects.filter(paid=False),
	'delivers': Transaction.objects.filter(recieved=False),
	'history': Transaction.objects.all()
	}
	return render(request, 'record.html', context)
