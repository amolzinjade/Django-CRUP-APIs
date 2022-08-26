from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from unicodedata import category
from rest_framework import parsers
from mywebapp import helpers
from django.contrib.auth import get_user_model
from .models import Image, Message, listing
from .serializers import MessageSerializer, listingserializer
from .serializers import ImageSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

# @api_view(['GET'])
# def list_public_listing(request):
#   if request.method =='GET':  
#     try:
#             listing1=listing.objects.all()
#             #checkCategory = listing1.values('categories')
#             #print(checkCategory)
#             # if checkCategory['categories'] == 'PUBLIC':
#             serializer=listingserializer(listing1,many=True)
#             return JsonResponse(serializer.data,safe=False)
#     except: listing.DoesNotExist

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })    

# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)    

# Create Listing API
@csrf_exempt
@api_view(['POST'])
def CreateListing(request):
        if request.method== 'POST':
            data = JSONParser().parse(request)
            serializer=listingserializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['PUT'])
def updateListing(request, pk):
        getId = listing.objects.filter(pk=pk).first()
        if request.method== 'PUT':
            data = JSONParser().parse(request)
            print("\n",getId)
            serializer = listingserializer(getId, data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=200)
            return Response(serializer.errors, status=400)

@csrf_exempt
@api_view(['DELETE'])
def deleteListing(request,pk):
    if request.method== 'DELETE':
        getId = listing.objects.filter(pk=pk)
        getId.delete()
        return Response("Record Deleted Successfully",status=204)

class ImageView(APIView):
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)

    def get(self, request):
        all_images = Image.objects.all()
        serializer = ImageSerializer(all_images, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        property_id = request.data['property_id']

        # converts querydict to original dict
        images = dict((request.data).lists())['image']
        flag = 1
        arr = []
        for img_name in images:
            modified_data = helpers.modify_input_for_multiple_files(property_id,
                                                            img_name)
            file_serializer = ImageSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                flag = 0

        if flag == 1:
            return Response(arr, status=201)
        else:
            return Response(arr, status=400)

@csrf_exempt
class SendMessageView(APIView):
    
    def post(self, request, *args, **kwargs):
        receiver_id = request.data['receiver']
        print("receiver="+receiver_id)
        message = request.data['message']
        print("message="+message)
        Message.objects.create(sender=request.user, receiver__id=receiver_id, message_text=message)
        return Response(status=200)