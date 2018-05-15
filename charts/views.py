from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from random import randint


User = get_user_model()

class HomeView(View):                                       #view for actual graph
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})



def get_data(request, *args, **kwargs):
    data = {
        "sales": 100, 
        "customers": 10,
    }
    return JsonResponse(data) # http response

colorid = round(randint(100000,900000)) #get a random color using color id
colorid = str(colorid)
print("#" + colorid)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ['Arkansas Nuclear 1\n', 'Arkansas Nuclear 2\n', 'Beaver Valley 1\n', 'Beaver Valley 2\n', 'Braidwood 1\n', 'Braidwood 2\n', 'Browns Ferry 1\n', 'Browns Ferry 2\n', 'Browns Ferry 3\n', 'Brunswick 1\n', 'Brunswick 2\n', 'Byron 1\n', 'Byron 2\n', 'Callaway\n', 'Calvert Cliffs 1\n', 'Calvert Cliffs 2\n', 'Catawba 1\n', 'Catawba 2\n', 'Clinton\n', 'Columbia Generating Station\n', 'Comanche Peak 1\n', 'Comanche Peak 2\n', 'Cooper\n', 'D.C. Cook 1\n', 'D.C. Cook 2\n', 'Davis-Besse\n', 'Diablo Canyon 1\n', 'Diablo Canyon 2\n', 'Dresden 2\n', 'Dresden 3\n', 'Duane Arnold\n', 'Farley 1\n',
'Farley 2\n', 'Fermi 2\n', 'FitzPatrick\n', 'Grand Gulf 1\n', 'Harris 1\n', 'Hatch 2\n', 'Hope Creek 1\n', 'Indian Point 2\n', 'Indian Point 3\n',
'LaSalle 1\n', 'Oconee 1\n', 'Oconee 2\n', 'Oconee 3\n', 'Quad Cities 1\n', 'Quad Cities 2\n', 'Susquehanna 2\n', 'Watts Bar 2']
        default_items = [qs_count, 1, 100, 55, 100, 92, 100, 100, 23, 87, 100, 100, 88, 100, 100, 100, 100, 100, 65, 1, 100, 100, 100, 100, 100, 12, 100, 100, 100, 100, 100, 100, 13, 100, 87, 100, 1, 30, 95, 6, 100, 100, 100, 100, 100, 1, 87, 98, 85]
        data = {   # using a dictionary for the data set 
                "labels": labels,
                "default": default_items,
        }
        return Response(data)
# changed power values of 0 to 1 for visibilty 

# def get(self, request, format=None):
#         qs_count = User.objects.all().count()
#         labels = ['Arkansas Nuclear 1\n', 'Arkansas Nuclear 2\n', 'Beaver Valley 1\n', 'Beaver Valley 2\n', 'Braidwood 1\n', 'Braidwood 2\n', 'Browns Ferry 1\n', 'Browns Ferry 2\n', 'Browns Ferry 3\n', 'Brunswick 1\n', 'Brunswick 2\n', 'Byron 1\n', 'Byron 2\n', 'Callaway\n', 'Calvert Cliffs 1\n', 'Calvert Cliffs 2\n', 'Catawba 1\n', 'Catawba 2\n', 'Clinton\n', 'Columbia Generating Station\n', 'Comanche Peak 1\n', 'Comanche Peak 2\n', 'Cooper\n', 'D.C. Cook 1\n', 'D.C. Cook 2\n', 'Davis-Besse\n', 'Diablo Canyon 1\n', 'Diablo Canyon 2\n', 'Dresden 2\n', 'Dresden 3\n', 'Duane Arnold\n', 'Farley 1\n',
# 'Farley 2\n', 'Fermi 2\n', 'FitzPatrick\n', 'Grand Gulf 1\n', 'Harris 1\n', 'Hatch 2\n', 'Hope Creek 1\n', 'Indian Point 2\n', 'Indian Point 3\n',
# 'LaSalle 1\n', 'Oconee 1\n', 'Oconee 2\n', 'Oconee 3\n', 'Quad Cities 1\n', 'Quad Cities 2\n', 'Susquehanna 2\n', 'Watts Bar 2']
#         default_items = [qs_count, 0, 100, 55, 100, 92, 100, 100, 23, 87, 100, 100, 88, 100, 100, 100, 100, 100, 65, 0, 100, 100, 100, 100, 100, 12, 100, 100, 100, 100, 100, 100, 13, 100, 87, 100, 0, 30, 95, 6, 100, 100, 100, 100, 100, 0, 87, 98, 85, 58]
#         data = {
#                 "labels": labels,
#                 "default": default_items,
#         }
#         return Response(data)

# Up to watts bar 