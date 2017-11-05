from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Instrument

class InstrumentList(ListView):
    model = Instrument
    template_name= "instrument_list.html"

    #def productList(request):
        # product=Product.object.all()
        # template_name="product_list.html"
        # return render(request.template_name,{"object_list":product})


class InstrumentDetail(DetailView):
    model= Instrument

    def get_queryset(self):
        return Instrument.objects.values("title","exchange","symbol").all()

    def get_context_data(self, **kwargs):
        print(kwargs)
        template_name="instrument_detail.html"
        context = super(InstrumentDetail, self).get_context_data(**kwargs)
        print(context)
        return context

    def get_slug_field(self, **kwargs):
        print(kwargs)
        context= super(InstrumentDetail, self).get_slug_field(**kwargs)
        return context
