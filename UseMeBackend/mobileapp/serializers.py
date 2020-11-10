from rest_framework import serializers
from .models import Customer
from .models import Shop
from .models import Dperson

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id',
                'url',
                'user_name',
                'password',
                'confirm_password',
                'email_address',
                'home_address',
                'account_number',
                'mobile_number')
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id',
                'url',
                'user_name',
                'password',
                'confirm_password',
                'owner_email_address',
                'shop_address',
                'shop_number',
                'mobile_number')
class DpersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dperson
        fields = ('id',
                'url',
                'user_name',
                'password',
                'confirm_password',
                'email_address',
                'home_address',
                'vehicle_type',
                'vehicle_number',
                'mobile_number',
                'licens',
                'photo')