from django.urls import path
from . import views


app_name = 'housework'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
    path('housework_list/', views.HouseworkListView.as_view(), name="housework_list"),
    path('housework_detail/<int:pk>/', views.HouseworkDetailView.as_view(), name="housework_detail"),
    path('housework_create/', views.HouseworkCreateView.as_view(), name="housework_create"),
    path('housework_update/<int:pk>/', views.HouseworkUpdateView.as_view(), name="housework_update"),
    path('housework_delete/<int:pk>/', views.HouseworkDeleteView.as_view(),name="housework_delete"),
]