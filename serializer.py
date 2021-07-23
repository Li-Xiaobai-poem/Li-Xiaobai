from rest_framework import serializers

from app1.models import History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'