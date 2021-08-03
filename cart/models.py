from django.db import models
from store.models import product

class cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField( auto_now_add=True)


    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=False)



    def __str__(self):
        return self.product



