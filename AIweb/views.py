from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Sale
from .forms import  SalesSearchForm
import pandas as pd
# Create your views here.
def home_view(request):
    sales_df=None
    positions_df=None
    form=SalesSearchForm(request.POST or None)
    if request.method == 'POST':
        date_from=request.POST.get('date_form')
        date_to=request.POST.get('date_to')
        chart_type=request.POST.get('chart_type')
        print(date_from,date_to,chart_type)
        sale_qs=Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if len(sale_qs)>0:
            sales_df=pd.DataFrame(sale_qs.values())
            positions_data=[]
            for sale in sale_qs:
                for pos in sale.get_positions():
                    obj={
                        'position':pos.id,
                        'product':pos.product.name,
                        'quantity':pos.quantity,
                        'price':pos.price,
                        'sales_id':pos.get_sales_id()
                    }
                    positions_data.append(obj)       
            sales_df=sales_df.to_html()
            positions_df=pd.DataFrame(positions_data)
            positions_df=positions_df.to_html()
        else:
            print("There is no data")



    context={
        'form':form,
        'sales_df':sales_df,
        'positions_df':positions_df,
    }
    return render(request,'AIweb/home.html',context)


class SalesListView(ListView):
    model=Sale
    #qs=Sale.objects.all()
    template_name='Aiweb/main.html'
    #context_object_list="object_list"
    
    #return render(request,'Aiweb/main.html, context={})

class SaleDetailView(DetailView):
        model=Sale
        #obj=Sale.objects.get(pk=pk)
        template_name='Aiweb/detail.html'
        #return render(request,'Aiweb/detail.html',{'object':obj})