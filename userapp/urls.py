from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index),
    path('reg',views.signup),
    path('log',views.login),
    path('pass',views.changepass),
    path('users',views.users),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('addpt',views.addpets),
    path('allpets',views.allpets),
    path('addtocart/<int:pid>',views.addtocart,name='cart'),
    path('viewcart',views.viewcart),
    path('cartdelete/<int:cid>',views.cartdelete,name='cartdelete'),
    path('mailing',views.sendmail),
    path('formview',views.formview),
    
]