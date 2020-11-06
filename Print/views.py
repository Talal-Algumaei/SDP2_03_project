from django.shortcuts import render, redirect
from .forms import NewPrintForm
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PrintFile
from django.core.files.storage import FileSystemStorage
from .serializers import PrintFileSerializer
import time



class NewPrintView(View):
    form_class = NewPrintForm
    template_name = 'create_new_print.html'
    
    def get(self,request):
        form = self.form_class
        context = {'form':form}
        return render(request,self.template_name,context)

    def post(self,request):
        form = self.form_class(request.POST , request.FILES)
        Upload_file = False
        if form.is_valid():
            File_name = str(form.cleaned_data.get("print_file")).split(".")[-1]
            print(form.cleaned_data.get("print_file"))
            if form.cleaned_data.get("is_print_3d") == True and form.cleaned_data.get("is_print_cnc") == True: 
                messages.error(request, "Please select only one process")
            elif not(form.cleaned_data.get("is_print_3d")) and not( form.cleaned_data.get("is_print_cnc")):
                messages.error(request, "Please select ANY Process")
            elif not(form.cleaned_data.get("is_print_file_gcode") == True and form.cleaned_data.get("is_tool_installed") == True):
                if form.cleaned_data.get("is_print_file_gcode") != True:
                    messages.error(request, "Please Convert the file to Gcode and try again")
                if form.cleaned_data.get("is_tool_installed") != True:
                    messages.error(request, "Please Install the required tool and try again")
            elif form.cleaned_data.get("is_print_file_gcode") == True:
                if File_name[0] == 'g' or File_name[0] == 'G' or File_name[0] == 'n':
                    Upload_file = True
                else:
                    messages.error(request, "Please Upload a gcode file")
        print(Upload_file)
        if  Upload_file == True:
            request_file = request.FILES['print_file'] if 'print_file' in request.FILES else None
            if request_file: 
                # save attatched file 
    
                # create a new instance of FileSystemStorage 
                fs = FileSystemStorage() 
                file = fs.save(request_file.name, request_file) 
                # the fileurl variable now contains the url to the file. This can be used to serve the file when needed. 
                fileurl = fs.url(file) 
                form.save()
                form = self.form_class
                time.sleep(3)
                return redirect("start-new-print")  

        return render(request,self.template_name,{'form': form})




@api_view(['GET'])
def print_file_view(request):
    serializer = PrintFileSerializer(PrintFile.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def print_details_view(request, pk):
    obj = PrintFile.objects.get(id=pk)
    serializer = PrintFileSerializer(obj, many=False)
    return Response(serializer.data)

#nice
@api_view(['POST'])
def print_create_view(request):
    serializer = PrintFileSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def print_update_view(request, pk):
    obj = PrintFile.objects.get(id=pk)
    serializer = PrintFileSerializer(instance=obj, data=request.data)
    if serializer.is_valid():
        print(serializer.data)
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def print_delete_view(request, pk):
    obj = PrintFile.objects.get(id=pk)
    obj.delete()
    return Response("Item successfuly deleted")