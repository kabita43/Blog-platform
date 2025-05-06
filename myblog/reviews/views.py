
from django.shortcuts import render
from rest_framework.views import APIView
from .models import WatchList,Review
from .serializers import WatchListSerializer,ReviewSerializer
# from rest_framewrok import mixins

from rest_framework.response import Response
from rest_framework import generics


class ReviewList(generics.ListCreateAPIView):
    serializer_class= ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


# class WatchListAV(APIView):
#     def get(self, request):
#         movies= WatchList.objects.all()
#         serializer= WatchListSerializer(movies, many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer=WatchListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        

# # class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,
# #                 generics.GenericsAPIView):
# #     queryset= Review.objects.all()  
# #     serializer_class= ReviewSerializer
# #     def get(self,request, *args, **kwargs):
# #         return self.list(request,*args,**kwargs)
    
# #     def post(self,request, *args, **kwargs):
# #         return self.create(request,*args,**kwargs)
        