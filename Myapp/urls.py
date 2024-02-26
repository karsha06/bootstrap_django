from django.urls import path
from Myapp import views

urlpatterns = [
    path('',views.index,name='my_index'),
    path('about/',views.icons,name='my_icons'),
    path('contact/', views.contact, name='my_contact'),
    path('gallery/',views.portfolio,name ='my_portfolio'),
    path('gallery/', views.portfolio, name='my_portfolio')

]