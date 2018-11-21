from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import MyUser

class MyUserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('url', 'id', 'email', 'phone')

class MyUserDetailSerializer(serializers.ModelSerializer):
    myprojects = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='cp_detail'
    )

    class Meta:
        model = MyUser
        fields = ('url', 'id', 'email', 'phone', 'user_name', 'hospital', 'address', 'myprojects')

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(help_text=u'旧密码',required=True)
    new_password = serializers.CharField(help_text=u'新密码',required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value