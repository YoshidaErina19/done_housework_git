from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Grocery
# Create your views here.


class GroceryListView(LoginRequiredMixin, generic.ListView):
    model = Grocery
    template_name = 'grocery_list.html'

    def get_queryset(self):
        return Grocery.objects.filter(user=self.request.user)


"""
# 関数ベースビューで記述したもの
def index(request):
    context = {
        'checkbox_list': CheckBox.objects.all(),
    }
    return render(request, 'grocery/grocery_list.html', context)
"""
