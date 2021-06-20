from django.shortcuts import render, redirect
from .models import *
from math import ceil
from django.contrib import messages
# Create your views here.


def shopHome(request):
    if request.user.is_authenticated:
        user = request.user
        print(user.id)
        cart = order.objects.filter(user=request.user)
        total = 0
        for item in cart:
            total += int(item.product.price)

        item = product.objects.all()
        n = len(item)
        nRow = n//2 + ceil((n/2)-(n//2))
        param = {'nRow': nRow, 'range': range(
            1, nRow), 'item': item, 'cart': cart, 'bill': total}
        return render(request, 'shop/home.html', param)
    else:
        return redirect('basehome')


def productDetail(request, id):
    if request.user.is_authenticated:
        item = product.objects.get(product_id=id)
        feedback = review.objects.filter(product=item)
        param = {'item': item, 'feedback':feedback}
        return render(request, 'shop/prod_detial.html', param)
    else:
        return redirect('basehome')


def addCart(request, id):
    if request.user.is_authenticated:
        user = request.user
        item = product.objects.get(product_id=id)
        quantity = 1
        orderplc = order.objects.create(
            user=user, product=item, quantity=quantity)
        orderplc.save()
        return redirect('shophome')
    else:
        return redirect('basehome')


def deleteCart(request, id):
    if request.user.is_authenticated:
        item = order.objects.get(order_id=id).delete()
        return redirect('/shop')
    else:
        return redirect('basehome')


def clearCart(request):
    if request.user.is_authenticated:
        item = order.objects.filter(user=request.user).delete()
        return redirect('/shop')
    else:
        return redirect('basehome')


def checkout(request):
    if request.user.is_authenticated:
        cart = order.objects.filter(user=request.user)
        total = 0
        for item in cart:
            total += int(item.product.price)
        param = {'cart': cart, 'bill': total}
        return render(request, 'shop/checkout.html', param)
    else:
        return redirect('basehome')


def placeOrderDetial(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            address1 = request.POST['address1']
            address2 = request.POST['address2']
            total = request.POST['total']
            user = request.user
            orderDetail = order.objects.filter(user=user)
            placedorderdetail = '   '
            for item in range (0,orderDetail.count()):
                hello = str(orderDetail[item])
                placedorderdetail += str(item + 1)+'. ' +hello + '  <br>   '
            print(placedorderdetail)
            zipcode = request.POST['zipcode']
            phone = request.POST['phone']
            detail = placeOrder.objects.create(user=user, order=placedorderdetail,zipcode= zipcode, total=total, address=address1+', '+address2, phone=phone)
            detail.save()
            clearCart(request)
            return redirect('thankyou')
    else:
        return redirect('basehome')

def thanks(request): 
    if request.user.is_authenticated:
        item = placeOrder.objects.filter(user=request.user)
        add_order = item.last()
        add_id = add_order

        status = orderStatus.objects.create(order_id=add_id)
        status.save()
        return render(request, 'shop/thanks.html')
    else:
        return redirect('basehome')


def trackorder(request,id):
    if request.user.is_authenticated:
        status = orderStatus.objects.get(order_id=id)
        param = {'status':status}
        return render(request, 'shop/trackorder.html',param)
    else:
        return redirect('basehome')



def orders(request):
    if request.user.is_authenticated:
        item = placeOrder.objects.filter(user=request.user)
        param ={'orders':item}
        return render(request, 'shop/orders.html',param)
    else:
        return redirect('basehome')



def feedback(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment = request.POST['review']
            user = request.user
            item = product.objects.get(product_id = id)
            rating = int(request.POST['rate'])
            if rating == '0':
                star1 = ''
                star2 = ''
                star3 = ''
                star4 = ''
                star5 = ''
            if rating == 1:
                star1 = 'checked'
                star2 = ''
                star3 = ''
                star4 = ''
                star5 = ''
            elif rating == 2:
                star1 = 'checked'
                star2 = 'checked'
                star3 = ''
                star4 = ''
                star5 = ''
            elif rating == 3:
                star1 = 'checked'
                star2 = 'checked'
                star3 = 'checked'
                star4 = ''
                star5 = ''
            elif rating == 4:
                star1 = 'checked'
                star2 = 'checked'
                star3 = 'checked'
                star4 = 'checked'
                star5 = ''
            else:
                star1 = 'checked'
                star2 = 'checked'
                star3 = 'checked'
                star4 = 'checked'
                star5 = 'checked'
            feedback = review.objects.create(user=user, product=item, review=comment, rating=rating, star1=star1, star2=star2,star3=star3,star4=star4,star5=star5)
            feedback.save()
            return redirect('/shop')
    else:
        return redirect('basehome')