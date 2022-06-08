from django.shortcuts import render
from .models import CheckBox
# Create your views here.

def index(request):
    context = {
        'checkbox_list': CheckBox.objects.all(),
    }
    return render(request, 'grocery/grocery.html', context)

# class IndexView(generic.TemplateView):
    # template_name = 'index.html'