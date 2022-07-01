from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Disbursements,Merchant,Order


# Create your views here.

def MerchantListView (request):
	#Lectura pararametros llamada
	week_sent=request.GET.get('week','')
	merchant_sent=request.GET.get('merchant','')

	#Verificar si tenemos el vendedor
	if merchant_sent:
		obj=Disbursements.objects.filter(merchant_id = merchant_sent,week=week_sent)
	else:
		obj=Disbursements.objects.filter(week=week_sent)
	
	context ={
		"object_list": obj
	}
	if not obj:
		return render(request, "merchant_unknown.html",{'week': week_sent}) #sino existen datos
	else:
		return render(request, "merchant_list.html",context)



def CreateData(request):
	#inicializacion listas
	listado_index=[]
	listado_values=[]
	
	#Lectura pararametros llamada
	week_sent=request.GET.get('week','1')
	
	order_objects=Order.objects.filter(Completed__week=week_sent)
	#order_test=order_objects[:5]
	#calculo de la comision
	for order_object in order_objects:
		if order_object.Amount > 300:
			fee=float (order_object.Amount)*0.0085
		elif order_object.Amount >= 50:
			fee=float (order_object.Amount)*0.0095
		else :
			fee=float(order_object.Amount)*0.01

		#Crear una lista de los vendedores y el total de la comision
		if order_object.merchant.id in listado_index:
			listado_values[listado_index.index(order_object.merchant.id)]+=fee
		else:
			listado_index.append(order_object.merchant.id)
			listado_values.append(fee)
	
	i=0
	#Guardar los datos en la base de datos
	while i<len(listado_index):
		Disbursements.objects.create(merchant=Merchant.objects.get(id=listado_index[i]),week=week_sent,disbursement=round(listado_values[i],2))
		i += 1
	return render(request, "data_created.html",{'week': week_sent})
