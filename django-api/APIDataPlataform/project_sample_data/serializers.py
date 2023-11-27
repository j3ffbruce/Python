from rest_framework import serializers

class CSVDataSerializer(serializers.Serializer):
    nm_cliente = serializers.CharField(max_length=200, required=True, allow_blank=False)
    nr_cpf = serializers.CharField(min_length=10, max_length=11, required=True, allow_blank=False)

