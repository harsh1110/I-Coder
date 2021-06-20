from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField()
    image = models.ImageField(upload_to="static/shop_img", null=True, blank=True)
    catagory = models.CharField(max_length=100, blank=True, null=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    discount = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.name
    
class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.product.name 

class placeOrder(models.Model):
    placedOrder_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order = models.TextField()
    address = models.TextField()
    zipcode = models.PositiveIntegerField(null=True, blank=True)
    total = models.PositiveIntegerField(null=True, blank=True)
    phone = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.placedOrder_id)

class orderStatus(models.Model):
    order_id = models.ForeignKey(placeOrder, on_delete=models.CASCADE, null=True, blank=True)
    process = models.CharField(max_length=10,default='done', blank=True, null=True)
    shipped = models.CharField(max_length=10,default='todo', blank=True, null=True)
    inRoute = models.CharField(max_length=10,default='todo', blank=True, null=True)
    arrived = models.CharField(max_length=10,default='todo', blank=True, null=True)
    estimatedDate = models.DateField(auto_now_add=True,blank=True, null=True)
    facilityNo = models.PositiveIntegerField(default=151, null=True, blank=True)
    comment = models.TextField(default='Your Order is Confirmed...')

    def __str__(self):
        return str(self.order_id)

class review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    review = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(null=True, blank=True)
    star1 = models.CharField(null=True, blank=True, max_length=10)
    star2 = models.CharField(null=True, blank=True, max_length=10)
    star3 = models.CharField(null=True, blank=True, max_length=10)
    star4 = models.CharField(null=True, blank=True, max_length=10)
    star5 = models.CharField(null=True, blank=True, max_length=10)

    def __str__(self):
        return str(self.user) +' '+ str(self.product)
    

    






 


