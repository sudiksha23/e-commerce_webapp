from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
STATE_CHOICES = (
    ('New South Wales','New South Wales'),
    ('Queensland','Queensland'),
    ('South Australia','South Australia'),
    ('Tasmania','Tasmania'),
    ('Victoria','Victoria'),
    ('Western Australia','Western Australia'),
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    
    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES = (
    ('B','Beans'),
    ('D','Daal'),
    ('DS','Disposable Stuff'),
    ('DF', 'Dry Food'),
    ('FIW','Whole Fish'),
    ('CBF','Cleaned Block Fish'),
    ('K','keema'),
    ('DFS','Dry Fish'),
    ('F','Flour'),
    ('FF','Frozen Food'),
    ('G','Ghee'),
    ('M','Meat'),
    ('O','Oil'),
    ('R','Rice'),
    ('SW','Whole Spices'),
    ('SG','Ground Spice'),
    ('S','Sugar'),
    ('SD','Sundries'),
    ('V','Vegetable'),
    ('P','Pickle'),
    ('BS','Bangladeshi Snacks')
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    product_image = models.ImageField(upload_to='productimg')
    quantity_pr_price = models.CharField(max_length=30)
    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    @property
    def totalcost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class OderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')  
    @property
    def totalcost(self):
        return self.quantity * self.product.discounted_price

    