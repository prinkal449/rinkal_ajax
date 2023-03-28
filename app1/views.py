from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.

def index(request):
    a = User.objects.all()
    return render(request, 'index.html', {'all_entries':a})


def create_row(request):
    User.objects.create(
        company = request.POST['company'],
        contact = request.POST['contact'],
        country = request.POST['country']
    )
    all_rows = list(User.objects.values())
    return JsonResponse({'msg' : 'successfully created !!', 'updated_data' :  all_rows}) 



def del_row(request):
    user_obj = User.objects.get(id= request.POST['pk'])
    user_obj.delete()
    all_rows = list(User.objects.values())
    return JsonResponse({'msg': 'row deleted !!', 'updated_data' :  all_rows})

