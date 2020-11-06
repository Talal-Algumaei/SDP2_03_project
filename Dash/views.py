from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DashPanelData, PrintTrackData
from .serializers import DashPanelDataSerializer, PrintTrackDataSerializer
from rest_framework import mixins
from rest_framework import generics



@login_required(login_url='login')
def home_page_view(request):
    queryset = DashPanelData.objects.all()
    trackdata = PrintTrackData.objects.get(id=1)
    context = {
        'object_list': reversed(queryset),
        'track_list': trackdata,
    }
    
    return render(request, 'admin_panel.html', context)


@login_required(login_url='login')
def camera_view(request):
    return redirect("http://192.168.1.234:8000/index.html")


@api_view(['GET'])
def dash_panel_view(request):
    serializer = DashPanelDataSerializer(DashPanelData.objects.all(), many=True)
    return Response(serializer.data)



class PrintTrackDataDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = PrintTrackData.objects.all()
    serializer_class = PrintTrackDataSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class DashPanelDataDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = DashPanelData.objects.all()
    serializer_class = DashPanelDataSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)