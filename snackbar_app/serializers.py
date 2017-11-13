from rest_framework import serializers
from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    """ A serializer of UserProfile model"""

    class Meta:
        model = models.UserProfile
        fields = ('first_name','last_name','email', 'password','avatar')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        instance = self.instance

        # this means it's an update
        if instance is not None:
            originalName = instance.name
            originalEmail = instance.email

            # if 'dataOwner' is not None it means they're trying to update the owner field
            dataName = data.get('name')
            dataEmail = data.get('email')

            if dataName is not None and (originalName != dataName):
                raise serializers.ValidationError('Cannot update name')
                # data.update({'name': originalOwner})
            if dataEmail is not None and (originalEmail != dataEmail):
                raise serializers.ValidationError('Cannot update email')
                # data.update({'name': originalOwner})
        return data

    def create(self, data):
        """ Create and return a new user"""
        user = models.UserProfile(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            avatar=data['avatar']
        )
        user.set_password(data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        models.UserProfile.objects.filter(pk=instance.id).update(**validated_data)
        user = models.UserProfile.objects.get(pk=instance.id)
        return user

