import csv
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CSVDataSerializer
from rest_framework import status


class read_csv_file(APIView):
    def get(self, response):
        data = []
        with open('./project_sample_data/teste.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            for row in csv_reader:
                data.append(row)
        serializer = CSVDataSerializer(data=data, many=True)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            error = [item for item in serializer.errors if item]
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        
