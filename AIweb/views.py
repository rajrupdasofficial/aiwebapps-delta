from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Sale
from .forms import  SalesSearchForm
from reports.forms import ReportForm
import pandas as pd
from .utils import *
from pandas.core.frame import DataFrame

# Create your views here.
def home_view(request):
    sales_df=None
    positions_df=None
    merged_df=None
    df=None
    chart=None
    search_form=SalesSearchForm(request.POST or None)
    report_form=ReportForm()
    if request.method == 'POST':
        date_from=request.POST.get('date_form')
        date_to=request.POST.get('date_to')
        chart_type=request.POST.get('chart_type')
        results_by=request.POST.get('results_by')
        #print(date_from,date_to,chart_type)
        sale_qs=Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if len(sale_qs)>0:
            sales_df=pd.DataFrame(sale_qs.values())
            sales_df['customer_id']=sales_df['customer_id'].apply(get_customer_from_id)
            sales_df['salesman_id']=sales_df['salesman_id'].apply(get_salesman_from_id)
            sales_df['created']=sales_df['created'].apply(lambda x: x.strftime('%Y-%m-%d'))
            sales_df.rename({'customer_id':'customer','salesman_id':'salesman','id':'sales_id'},axis=1,inplace=True)
            #sales_df['sales_id']=sales_df['id']
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
            
            positions_df=pd.DataFrame(positions_data)
            merged_df=pd.merge(sales_df,positions_df,on='sales_id')    
            df=merged_df.groupby('transaction_id',as_index=False)['price'].agg('sum') 
            chart=get_chart(chart_type,sales_df,results_by)
            sales_df=sales_df.to_html()            
            positions_df=positions_df.to_html() 
            merged_df=merged_df.to_html()
            df=df.to_html()
        else:
            print("There is no data")



    context={
        'search_form':search_form,
        'sales_df':sales_df,
        'positions_df':positions_df,
        'merged_df':merged_df,
        'df':df,
        'chart':chart,
        'report_form':report_form,
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