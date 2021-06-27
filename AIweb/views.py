from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Sale
from .forms import  SalesSearchForm

# Create your views here.
def home_view(request):
    form=SalesSearchForm(request.POST or None)
    if request.method == 'POST':
        date_form=request.POST.get('date_form')
        date_to=request.POST.get('date_to')
        chart_type=request.POST.get('chart_type')
        print(date_form,date_to,chart_type)
    message="This is home view"

    qs=Sale.objects.filter(created=date_form)
    print(qs)
    context={
        'message':message,
        'form':form,
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