from django.shortcuts import render
from .models import Farm, Sheep, Pig, Cow


def farm_list(request):
    farms = Farm.objects.all()
    return render(request, "farm/farm_list.html", {"farms": farms})


def farm_detail(request, farm_id):
    farm = Farm.objects.get(id=farm_id)
    return render(request, "farm/farm_detail.html", {"farm": farm})
