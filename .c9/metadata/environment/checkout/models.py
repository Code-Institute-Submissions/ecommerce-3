{"filter":false,"title":"models.py","tooltip":"/checkout/models.py","ace":{"folds":[],"scrolltop":334.75,"scrollleft":0,"selection":{"start":{"row":26,"column":65},"end":{"row":26,"column":65},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"3624fec0fed85fb0efbb25dcc91fd0737921b075","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":1},"end":{"row":3,"column":0},"action":"remove","lines":["rom django.db import models","","# Create your models here.",""],"id":2},{"start":{"row":0,"column":1},"end":{"row":26,"column":65},"action":"insert","lines":["from django.db import models","from products.models import Product","","# Create your models here.","class Order(models.Model):","    full_name = models.CharField(max_length=50, blank=False)","    phone_number = models.CharField(max_length=20, blank=False)","    country = models.CharField(max_length=40, blank=False)","    postcode = models.CharField(max_length=20, blank=True)","    town_or_city = models.CharField(max_length=40, blank=False)","    street_address1 = models.CharField(max_length=40, blank=False)","    street_address2 = models.CharField(max_length=40, blank=False)","    county = models.CharField(max_length=40, blank=False)","    date = models.DateField()","","    def __str__(self):","        return \"{0}-{1}-{2}\".format(self.id, self.date, self.full_name)","","","class OrderLineItem(models.Model):","    order = models.ForeignKey(Order, null=False)","    product = models.ForeignKey(Product, null=False)","    quantity = models.IntegerField(blank=False)","","    def __str__(self):","        return \"{0} {1} @ {2}\".format(","            self.quantity, self.product.name, self.product.price)"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["f"],"id":3}]]},"timestamp":1567337040378}