from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Sale

# Create your views here.
def home_view(request):
    message= "You're viewing AI based website front page"
    return render(request,'AIweb/home.html',context={'message':message})


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