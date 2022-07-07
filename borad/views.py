from django.shortcuts import render
from django.http import HttpResponse
from  rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Boradserializers
from .models import Borad
# Create your views here
buffer = ['dgaggdg','gdsagg','dgasgsa']

@api_view(['GET'])
def getroutes(request):
    routes=[{
        'Endpoint':'/nots/',
         'method':'GET',
        'body':None,
        'description':'Returns an array of nots'
             },
        {
            'Endpoint':'/nots/id',
            'method':'GET',
            'body':None,
            'description':'Returns a single  note object'

        },
        {
            'Endpoint':'/nots/create/',
            'method':'POST',
            'body':{'body':""},
            'description':'create  one note with data sent in post req'
        },
        {
            'Endpoint':'/nots/id/update/',
            'method':'PUT',
            'body':{'body':""},
            'description':'create  an exiting note with data sent in post req'
        },
        {
            'Endpoint':'/nots/id/delete/',
            'method':'DELETE',
            'body':{'body':""},
            'description':'create  an exiting note with data sent in post req'
        }
    ]
    return Response(routes)
def home(requset):
    borads=Borad.objects.all()
    borads_names=[]
    for borad in borads:
        borads_names.append(borad.name)
    print(borads_names)
    return HttpResponse(borads_names) #render(requset,'home.html',{'buffer':buffer})




def socketio(request):
    socketio = request.environ['socketio']
    if socketio.on_connect():
        socketio.send({'buffer': buffer})
        socketio.broadcast({'announcement': socketio.session.session_id + ' connected'})

    while True:
        message = socketio.recv()

        if len(message) == 1:
            message = message[0]
            message = {'message': [socketio.session.session_id, message]}
            buffer.append(message)
            if len(buffer) > 15:
                del buffer[0]
            socketio.broadcast(message)
        else:
            if not socketio.connected():
                socketio.broadcast({'announcement': socketio.session.session_id + ' disconnected'})
                break

    return HttpResponse()


@api_view(['GET'])
def getBorads(request):
    borads=Borad.objects.all()
    serializer=Boradserializers(borads,many=True)
    return  Response(serializer.data)
@api_view(['GET'])
def getBorad(request,pk):
    borads=Borad.objects.get(id=pk)
    serializer=Boradserializers(borads,many=False)
    return  Response(serializer.data)

@api_view(['POST'])
def createBorad(request):
    data=request.data
    borads=Borad.objects.create(name=data['name'],description=data['description'])
    serializer=Boradserializers(borads,many=False)
    return  Response(serializer.data)
@api_view(['PUT'])
def updateBorad(request,pk):
    data=request.data
    borads=Borad.objects.get(id=pk)

    serializer=Boradserializers(borads,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return  Response(serializer.data)
@api_view(['DELETE'])
def deletBorad(request,pk):
    data=request.data
    borads=Borad.objects.get(id=pk)
    borads.delete()


    return  Response("was deleted")