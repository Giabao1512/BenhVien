from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'NgaySinh', 'avatar', 'DiaChi']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # **validated_data : chuyen toan bo k can chuyen tung fields
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LichKhamSerializer(ModelSerializer):
    class Meta:
        model = LichKham
        fields = ['MaBN', 'MaBS', 'MaPK', 'NgayKham']


class ToaThuocSerializer(ModelSerializer):
    class Meta:
        model = ToaThuoc
        fields = '__all__'


class BenhAnSerializer(ModelSerializer):
    class Meta:
        model = BenhAn
        fields = '__all__'
