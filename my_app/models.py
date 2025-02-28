from django.db import models

class wifi(models.Model):
    wifi_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500)
    sub_category = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.wifi_name


class dth(models.Model):
    dth_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    channels = models.CharField(max_length=50, default="")
    validity = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.dth_name


class prepaid(models.Model):
    prepaid_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500)
    validity = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.prepaid_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"


class postpaid(models.Model):
    price = models.CharField(max_length=50)
    data_rollover = models.CharField(max_length=50)
    sms_per_day = models.CharField(max_length=50)
    calls = models.CharField(max_length=50, default="")
    entertainment_apps = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.price


class CustomerDetails(models.Model):
    customer_id = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.customer_id


class CreateOrderRequest(models.Model):
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_currency = models.CharField(max_length=10)
    customer_details = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order for {self.customer_details.customer_id} with amount {self.order_amount}"
