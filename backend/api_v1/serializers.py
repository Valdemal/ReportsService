from rest_framework import serializers

from api_v1.models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class ReportPrintSerializer(serializers.Serializer):
    data = serializers.JSONField()
