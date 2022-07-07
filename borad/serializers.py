from rest_framework.serializers import ModelSerializer
from .models import Borad
class Boradserializers(ModelSerializer):
    class Meta:
        model = Borad
        fields ='__all__'