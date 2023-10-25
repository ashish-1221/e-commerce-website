from django.db import models
from django.contrib.auth.models  import User

# Vendor Models
class Vendor(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField(null=True)
    
    def __str__(self):
        return self.user.username


# productCategory Model
class ProductCategory(models.Model):
    """A vendor/admin can define the category for the products
    The category table must have 2 fields
    1. Title of te product
    2 Detail of the product. The detail of the product can be null.
    Depends on the endor
    Args:
        models (_type_): _description_
    """
    user = models
    title = models.CharField(max_length=200)
    detail = models.CharField(null=True)
    
    def __str__(self):
        return self.title
    
## Product Models
class Product(models.Model):
    """ 
    Product Table contains the information of all the products i present in the ware
    house
    Fields required in the Product Table
    1. Name of the product
    2. Details of the product
    3. Price of the product

    Args:
        models (_type_): _description_
    """
    category = models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True,related_name="category_product")
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    price = models.FloatField()
    
    def __str__(self):
        return self.title


## Customer Model
class Customer(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.user.username


## Order Model
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)

    def __unicode_(self):
        return '%s' % (self.order_time)

## Order Items Model
class OrderItems(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="order_items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.title

## Customer Address Model
class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="customer_addresses")
    address = models.TextField()
    default_address  = models.BooleanField(default=False)
    def __str__(self):
        return self.address


## Product Rating and Reviews 
class ProductRating(models.Model):
    """
        User must be logged in
        1. Customer from the Customer Model; Customer who is viewing through his page
    """
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="rating_customers")
    # produc the customer is viewing
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="rating_products")
    # rating will vary between 1 to 5
    rating = models.IntegerField()
    reviews = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.rating}-{self.reviews}'
