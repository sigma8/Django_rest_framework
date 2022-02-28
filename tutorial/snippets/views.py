#from urllib import response
#from django.shortcuts import render
#from django.http import Http404, HttpResponse, JsonResponse 
#from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics #status, mixins, 
#from rest_framework.parsers import JSONParser
#from rest_framework.views import APIView
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnipperDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# Usando las clases serializadoras creamos las vistas de nuestra API

# El decorador @csrf_exempt se usa para poder hacer POST a la vista
# incluso si no se tiene csrf token
#@csrf_exempt

# El decorador @api_view se trabajar con vistas basadas en funciones
#@api_view(['GET', 'POST'])



#class SnippetList(mixins.ListModelMixin,
#                mixins.CreateModelMixin,
#                generics.GenericAPIView):
#    queryset = Snippet.objects.all()
#    serializer_class = SnippetSerializer


#class SnippetList(APIView):
#    def get(self, request, *args, **kwargs):
#        return self.list(request, *args, **kwargs)
#    def post(self, request,*args, **kwargs):
#        return self.create( request, *args, **kwargs)
#El uso de sufijos 'format' nos brinda un URL que se refieren explícitamente a un formato dado  
#def snippet_list(request, format=None):

    #Lista todos los codigos Snippets, o crear nuevo Snippet
    #def get(self, request, format=None):
        #if request.method == 'GET':
    #    snippets = Snippet.objects.all()
    #    serializer = SnippetSerializer(snippets, many=True)
        #return JsonResponse(serializer.data, safe=False)
        #Response renderiza al tipo de contenido solicitado por el cliente
    #    return Response(serializer.data)
    
    #def post(self, request, format=None):
    #elif request.method == 'POST':
        #data = JSONParser().parse(request)
        #request.data maneja data arbitraria y funciona para metodos PUT, POST, PATCH
        #serializer = SnippetSerializer(data=request.data) 
        #if serializer.is_valid():
        #    serializer.save()
            #return JsonResponse(serializer.data, status=201)
            #Usar los codigos de estatus de HTTP transmiten es estado de la solicitud de forma mas clara
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return JsonResponse(serializer.errors, status=400)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#class SnippetDetail(mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    generics.GenericAPIView):
#    queryset = Snippet.objects.all()
#    serializer_class = SnippetSerializer

#    def get(self, request, *args, **kwargs):
#        return self.retrieve(request, *args, **kwargs)

#    def put(self, request, *args, **kwargs):
#        return self.update(request, *args, **kwargs)

#    def delete(self, request, *args, **kwargs):
#        return self.destroy(request, *args, **kwargs)    
#class SnippetDetail(APIView):

#@api_view(['GET', 'PUT', 'DELETE'])
#def snippet_detail(request, pk, format=None):

#    def get_object(self, pk):
    #Retira, actualiza o borra codigo Snippet

#        try:
#            snippet = Snippet.objects.get(pk=pk)
#        except Snippet.DoesNotExist:
            #return HttpResponse(status=404)
            #return Response(status=status.HTTP_404_NOT_FOUND)
#            raise Http404

#    def get(self, request, pk, format=None):
    #if request.method == 'GET':
#        snippet = self.get_object(pk)
#        serializer = SnippetSerializer(snippet)
        #return JsonResponse(serializer.data)
#        return Response(serializer.data)

#    def put(self, request, pk, format=None):
    #elif request.method == 'PUT':
        #data = JSONParser().parse(request)
#        snippet = self.get_object(pk)
#        serializer = SnippetSerializer(snippet, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
            #return JsonResponse(serializer.data)
#            return Response(serializer.data)
        #return JsonResponse(serializer.errors, status=400)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#    def delete(self, request, pk, format=None):
    #elif request.method == 'DELETE':
#        snippet = self.get_object(pk) 
#        snippet.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)



