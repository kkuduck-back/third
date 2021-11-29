from rest_framework import fields, serializers
from .models import Subscription, User, DefaultSubscription, Plan
from user_api import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class DefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultSubscription
        fields = "__all__"

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = (
            'plan_name',
            'plan_price',
            'cycle'
        )

class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"