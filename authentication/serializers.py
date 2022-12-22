from rest_framework import serializers 
from authentication.models import User
 
 
class Usererializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('username',
                  'email',)