from django.shortcuts import render

import logging

from django.urls import reverse_lazy

from django.views import generic

from .forms import InquiryForm, HouseworkCreateForm

from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Housework

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('housework:inquiry')

    def form_valid(self, form):
        form.send_email()
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class HouseworkListView(LoginRequiredMixin, generic.ListView):
    model = Housework
    template_name = 'housework_list.html'
    paginate_by = 2

    def get_queryset(self):
        houseworks = Housework.objects.filter(user=self.request.user).order_by('-created_at')
        return houseworks

class HouseworkDetailView(LoginRequiredMixin, generic.DetailView):
    model = Housework
    template_name = 'housework_detail.html'

class HouseworkCreateView(LoginRequiredMixin, generic.CreateView):
    model = Housework
    template_name = 'housework_create.html'
    form_class = HouseworkCreateForm
    success_url = reverse_lazy('housework:housework_list')

    def form_valid(self, form):
        housework = form.save(commit=False)
        housework.user = self.request.user
        housework.save()
        messages.success(self.request, '家事を記録しました。お疲れ様でした！')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '家事の記録に失敗しました。')
        return super().form_invalid(form)

class HouseworkUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Housework
    template_name = 'housework_update.html'
    form_class = HouseworkCreateForm

    def get_success_url(self):
        return reverse_lazy('housework:housework_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '家事記録を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '家事記録の更新に失敗しました。')
        return super().form_invalid(form)

class HouseworkDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Housework
    template_name = 'housework_delete.html'
    success_url = reverse_lazy('housework:housework_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "家事記録を削除しました。")
        return super().delete(request, *args, **kwargs)