from rest_framework import serializers
from .models import *


class SendCreateFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

    def validate_price(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError()
        return value