# Imports
from rest_framework.views import APIView
from Sunify_Prediction import predictions
from  rest_framework.response import Response



class predictView(APIView):
    def get(self, request):
        predict = predictions.prediction()
        response_dict = {"Predicted_readings":predict}
        return Response(response_dict, status=200)

