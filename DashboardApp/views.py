from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def hi(request):
    x = requests.get('https://covid-19india-api.herokuapp.com/v2.0/state_data')
    y = requests.get('https://covid-19india-api.herokuapp.com/v2.0/country_data')
    # data = json.loads(x.json)
    data = x.json()
    data1 = y.json()
    print('#############################################################')
    print(data1)
    # import  pdb; pdb.set_trace()
    data = {'state_data': data[1]['state_data'],
            'country_data': data1[1]
            }
    return render(request,'DashboardApp/hi.html', data)

def country_data(request):
    x = requests.get('https://covid-19india-api.herokuapp.com/v2.0/country_data')
    data = json.load(x)
    print('############################################################')
    print(data)
    # country_data = {
    #     'active_cases' : '',
    #     'confirmed_cases' : '',
    #     'recovered_cases' : '',
    #     'death_cases' : '',
    #     'migrated_cases' : '',
    # }
    return render(request,'Dashboard/hi.html', data)

def state_data(request):
    x = request.get('https://covid-19india-api.herokuapp.com/v2.0/state_data')
    print('############################################################')
    data = json.load(x)
    print(data)
    return render(request,'Dashboard/hello.html', data)

def helpline_numbers(request):
    x = request.get('https://covid-19india-api.herokuapp.com/v2.0/helpline_numbers')
    print('############################################################')
    data = json.load(x)
    print(data)
    return render(request,'Dashboard/index.html', data)
