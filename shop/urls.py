from django.urls import path
from . import views


urlpatterns = [
    path('', views.shopHome, name="shophome"),
    path('<int:id>', views.productDetail, name="productDetail"),
    path('<int:id>/review', views.feedback,name="feedback"),
    path('add/<int:id>', views.addCart, name="addToCart"),
    path('delete/<int:id>', views.deleteCart, name="delFromCart"),
    path('clear', views.clearCart, name="clearCart"),
    path('checkout', views.checkout, name="checkout"),
    path('placeOrder', views.placeOrderDetial, name="placeOrder"),
    path('trackorder/<int:id>', views.trackorder, name="trackorder"),
    path('orders', views.orders, name="orders"),
    path('thanks', views.thanks, name="thankyou"),
]