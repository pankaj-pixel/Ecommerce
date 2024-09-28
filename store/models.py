from django.db import models
import datetime 
# Create your models here.

#categories of products
class Category (models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("categories")

    def __str__(self):
        return self.name

    ##def get_absolute_url(self):
     #   return reverse("_detail", kwargs={"pk": self.pk})


#customers
class  Customer(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    password =models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'  
    
#all products
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default =0,max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to='uploads/product/',null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    #add sales item
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,decimal_places=)
    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1) 
    address = models.CharField( max_length=100,default='',blank=True)
    phone = models.CharField(max_length=12,blank=True) 
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default = False)

    def __str__(self):
        return self.product
         