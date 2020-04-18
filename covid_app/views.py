from django.shortcuts import render
import requests
import json

def home(request):

    if request.method == 'POST':
        country = request.POST['country']
        url = 'https://corona.lmao.ninja/v2/countries/'+country
        response = requests.get(url)
        jres = json.loads(response.text)
        print(jres)
        # country = 
        # case = 
        data = {'Country':jres['country'],
                'Cases':str(jres['cases']),
                'Deaths':str(jres['deaths']),
                'Active':str(jres['active']),
                'Critical':str(jres['critical']),
                'TodaysDeath':str(jres['todayDeaths']),
                'TodayCases':str(jres['todayCases']),
        }

        print(data)
    else:
        data = {}
        
    return render(request,'home.html',data)
