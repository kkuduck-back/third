from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from user_api import models

#default 랑 plan 이랑 합치려고
from itertools import chain

from user_api.models import User, DefaultSubscription, Plan, Subscription
from user_api.serializer import DefaultSerializer, PlanSerializer, UserSerializer, SubSerializer

# Create your views here.
class UserView(APIView):
    # def get(self, requset):
    #     return Response("get ok", status=200)

    def get(self, request,  **kwargs):
        if kwargs.get('uid') is None:
            user_queryset = User.objects.all() #모든 User의 정보를 불러온다.
            user_serializer = UserSerializer(user_queryset, many=True)
            return Response({'count': user_queryset.count(), 'data': user_serializer.data}, status = status.HTTP_200_OK)
        else:
            uid = kwargs.get('uid')
            user_serializer = UserSerializer(User.objects.get(user_id=uid)) #id에 해당하는 User의 정보를 불러온다
            # 등록한 sub 종류
            sub = Subscription.objects.filter(user_id = uid)
            sub_serializer = SubSerializer(sub, many=True)
            return Response({'user':user_serializer.data, 'subscriptions':sub_serializer.data}, status=status.HTTP_200_OK)  

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'result':'success', 'data':user_serializer.data}, status=status.HTTP_200_OK)
        else :
            return Response({'result':'fail', 'data':user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# 만약 dsub_serializer.data.get('service_name') == plan_serializer.data.get('service_name') 이라면
#    둘을 합치고 sorted 한 뒤 중복된 값을 뺴라


class DefaultSubView(APIView):
    def get(self, request,  **kwargs):
        if kwargs.get('uid') is None:
            dsub_queryset = DefaultSubscription.objects.all()
            dsub_serializer = DefaultSerializer(dsub_queryset, many=True)
            return Response({'count': dsub_queryset.count(), 'data': dsub_serializer.data}, status = status.HTTP_200_OK)
        else:
            uid = kwargs.get('uid')
            dsub_serializer = DefaultSerializer(DefaultSubscription.objects.get(dsub_id=uid))
            # 등록한 plan 종류
            plans = Plan.objects.filter(dsub_id=uid)
            plan_serializer = PlanSerializer(plans, many=True)
            return Response({'service_name':dsub_serializer.data.get('service_name'), 'image_url':dsub_serializer.data.get('image_url'), 'plans':plan_serializer.data}, status=status.HTTP_200_OK)   





# class DefaultSubView(APIView):
#     def get(self, request,  **kwargs):
#         if kwargs.get('uid') is None:
#             dsub_queryset = DefaultSubscription.objects.all()
#             dsub_serializer = DefaultSerializer(dsub_queryset, many=True)
#             return Response({'count': dsub_queryset.count(), 'data': dsub_serializer.data}, status = status.HTTP_200_OK)
#         else:
#             uid = kwargs.get('uid')
#             dsub_serializer = DefaultSerializer(DefaultSubscription.objects.get(dsub_id=uid))
#             # 등록한 plan 종류
#             plans = Plan.objects.filter(dsub_id=uid)
#             plan_serializer = PlanSerializer(plans, many=True)
#             return Response({'service_name':dsub_serializer.data.get('service_name'), 'image_url':dsub_serializer.data.get('image_url'), 'plans':plan_serializer.data}, status=status.HTTP_200_OK)   






    # def post(self, request):
    #     dsub_serializer = DefaultSerializer(data=request.data)
    #     if dsub_serializer.is_valid():
    #         dsub_serializer.save()
    #         return Response({'result':'success', 'data':dsub_serializer.data}, status=status.HTTP_200_OK)
    #     else :
    #         return Response({'result':'fail', 'data':dsub_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# class PlanView(APIView):
#     def post(self, request):
#         plan_serializer = PlanSerializer(data=request.data)
#         if plan_serializer.is_valid():
#             plan_serializer.save()
#             return Response({'result':'success', 'data':plan_serializer.data}, status=status.HTTP_200_OK)
#         else :
#             return Response({'result':'fail', 'data':plan_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SubView(APIView):
    def get(self, request,  **kwargs):
        if kwargs.get('uid') is None:
            sub_queryset = Subscription.objects.all()
            sub_serializer = SubSerializer(sub_queryset, many=True)
            return Response({'data': sub_serializer.data}, status = status.HTTP_200_OK)
        else:
            uid = kwargs.get('uid')
            sub_serializer = SubSerializer(Subscription.objects.get(id=uid))
            return Response(sub_serializer.data, status=status.HTTP_200_OK)  
            
    def post(self, request):
        sub_serializer = SubSerializer(data=request.data)
        if sub_serializer.is_valid():
            sub_serializer.save()
            return Response({'result':'success', 'data':sub_serializer.data}, status=status.HTTP_200_OK)
        else :
            return Response({'result':'fail', 'data':sub_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        if kwargs.get('uid') is None:
            return Response("uid required", status = status.HTTP_400_BAD_REQUEST)
        else:
            uid = kwargs.get('uid')
            sub_object = Subscription.objects.get(id=uid)
            sub_serializer = SubSerializer(sub_object, data=request.data)
            if sub_serializer.is_valid():
                sub_serializer.save()
                return Response({'result':'success', 'data':sub_serializer.data},status=status.HTTP_200_OK)
            else:
                return Response("error", status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, **kwargs):
        if kwargs.get('uid') is None:
            return Response("uid required", status = status.HTTP_400_BAD_REQUEST)
        else:
            uid = kwargs.get('uid')
            sub_object = Subscription.objects.get(id=uid)
            sub_object.delete()
            return Response({"result":"success"}, status= status.HTTP_200_OK)
