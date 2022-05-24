from django.urls import path
from . import views


app_name = 'housework'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
    path('housework_list/', views.HouseworkListView.as_view(), name="housework_list"),
]