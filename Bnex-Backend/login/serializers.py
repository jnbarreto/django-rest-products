from rest_framework import serializers
from login.validators import validate_cpf
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'cpf',
            'password',
            'confirm_password',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        email = data.get('email')
        try:
            EmailValidator()(email)
        except ValidationError:
            raise serializers.ValidationError(
                {'email': 'Endereço de email inválido.'}
            )

        cpf = data.get('cpf')
        if not validate_cpf(cpf):
            raise serializers.ValidationError({'cpf': 'CPF inválido.'})

        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if len(password) < 6:
            raise serializers.ValidationError(
                {'password': 'Senha deve ter pelo menos 6 dígitos.'}
            )

        if password != confirm_password:
            raise serializers.ValidationError(
                {'confirm_password': 'As senhas não coincidem.'}
            )

        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)

        hashe = make_password(validated_data['password'])
        validated_data['password'] = hashe

        user = User(**validated_data)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(
            username=data['username'], password=data['password']
        )
        if user is None:
            raise serializers.ValidationError('Credenciais inválidas.')
        return user
