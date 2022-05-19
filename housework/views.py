from django.shortcuts import render

import logging

from django.urls import reverse_lazy

from django.views import generic

from .forms import InquiryForm

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

    def get_queryset(self):
        houseworks = Housework.objects.filter(user=self.request.user).order_by('-created_at')
        return houseworks