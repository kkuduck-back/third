from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(null=False, primary_key=True)
    user_name = models.CharField(max_length=128, null=False, unique=True)
    
    class Meta:
        db_table = 'User'

class DefaultSubscription(models.Model):
    dsub_id = models.AutoField(null=False, primary_key=True)
    service_name = models.CharField(max_length=128, null=False)
    image_url = models.CharField(max_length=1024, null=True)
    
    class Meta:
        db_table = 'DefaultSubscription'

class Plan(models.Model):
    plan_name = models.CharField(max_length=128, null=False)
    plan_price = models.IntegerField(null=False)
    cycle = models.CharField(max_length=64, null=False)
    dsub_id = models.ForeignKey(DefaultSubscription, null=False, on_delete=models.CASCADE, db_column='dsub_id')

    class Meta:
        db_table = 'Plan'


class Subscription(models.Model):
    service_name = models.CharField(max_length=128, null=False)
    plan_name = models.CharField(max_length=128, null=False)
    plan_price = models.IntegerField(null=False)
    cycle = models.CharField(max_length=128, null=False)
    head_count = models.IntegerField(null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True)
    share_id = models.CharField(max_length=128, null=True)
    image_url = models.CharField(max_length=1024, null=True)
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE, db_column="user_id")

    class Meta:
        db_table = 'Subscription'