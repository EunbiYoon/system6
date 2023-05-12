from django.urls import path
from .views import home_view, detail_bom_view, detail_cost_view, category_bom_view, category_cost_view

urlpatterns = [
    # detail
    path('',home_view,name='home_url'),
    path('<slug:slug>/<int:pk>/bom/', detail_bom_view, name='detail_bom_url'),
    path('<slug:slug>/<int:pk>/cost/', detail_cost_view, name='detail_cost_url'),
    path('<slug:slug>/bom/', category_bom_view, name='category_bom_url'),
    path('<slug:slug>/cost/', category_cost_view, name='category_cost_url'),
]
