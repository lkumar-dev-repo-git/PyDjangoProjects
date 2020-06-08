
from django.shortcuts import render

def showIndex(req):
    emp = {
        "idno": 101,
        "name": "Ravi",
        "salary": 125000.00
    }
    return render(req,"index.html",{"data":emp})