#SUMMARIZER
from django.shortcuts import render
from .apps import SummaryappConfig            
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView#APIView
from rest_framework.response import Response
from rest_framework import status

class call_model(APIView):

    def get(self,request):
        if request.method == 'GET':
            
            # sentence is the query we want to get the prediction for
            params =  request.GET.get('sentence')
            
            # predict method used to get the prediction
            #response = SummaryappConfig.summarizer(sentence) #nlp??
            
            print(params)
            
            # returning JSON response
            return Response({'key': 'value'}, status=status.HTTP_200_OK)
        
    def post(self,request):
        
        path = request.data
        #text = pdf_to_text(r'E:\stwork\iso OutPut\dec.pdf')
        sentence=path
        response = SummaryappConfig.summarizer(sentence) 
        #print(response)
        #return Response(response, status=status.HTTP_200_OK)  # this one is orignal - `working one      
        #return JsonResponse(response, status=status.HTTP_200_OK)
        return JsonResponse(response) # summarizer is giving a dic and here we convert it into json
        #return sentence
        
        #return HttpResponse(json.dumps(response_data), content_type="application/json")
'''
from django.http import JsonResponse
return JsonResponse({'foo':'bar'})
'''

'''
import json
blackjack_hand = ("asd asd asd asd assd asdasd asd asd sad asd afzgdfbsrber ")
encoded_hand = json.dumps(blackjack_hand)
print(encoded_hand)
decoded_hand = json.loads(encoded_hand)
print(decoded_hand)
'''

#return jsonify(summary)
'''
from django.shortcuts import render
from .apps import WebappConfig 

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .apps import WebappConfig

class call_model(APIView):

    def get(self,request):
        if request.method == 'GET':
            
            # sentence is the query we want to get the prediction for
            params =  request.GET.get('sentence')
            
            # predict method used to get the prediction
            response = WebappConfig.predictor.predict(sentence) #nlp??
            
            # returning JSON response
            return JsonResponse(response)
'''