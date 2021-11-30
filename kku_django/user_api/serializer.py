from rest_framework import fields, serializers
from .models import Subscription, User, DefaultSubscription, Plan
from user_api import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class PlanSerializer(serializers.ModelSerializer): # planserializer 가 반드시 default 보다 위에 있어야함
    class Meta:
        model = Plan 
        fields = (
            'plan_name',
            'plan_price',
            'cycle'
        )

class DefaultSerializer(serializers.ModelSerializer):

    plans = PlanSerializer(many=True, read_only=True) # model 에서 related_named 로 설정했던 거와 같은 이름인 plans 이어야 함
    class Meta:
        model = DefaultSubscription
        fields = (
            'service_name',
            'image_url',
            'plans'
        )

class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = (
            'user_id',
            'id',
            'service_name',
            'plan_name',
            'plan_price',
            'cycle',
            'head_count',
            'start_date',
            'end_date',
            'share_id',
            'image_url'
        )