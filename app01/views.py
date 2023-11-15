from django.shortcuts import render
from django.http import JsonResponse
from app01 import models
# Create your views here.
#def test(request):
 #   clubs = Club.objects.filter(players = Player.objects.get(id = 6))
  #  print("##############")
   # print(clubs)
    #print("##############")
#def test2(request):
 #   clubs = Club.objects.filter(players__in = [Player.objects.get(id = 6),Player.objects.get(id = 4)])
  #  print("##############")
   # print(clubs)
    #print("##############")
def search(request):
    return render(request,"index.html")
def players_get_all(request):
    players=models.Player.objects.all()
    pls=[]
    for player in players:
        pls.append({"id":player.id,
                     "name":player.name,
                     "family":player.family
        })
    return JsonResponse({"players":pls})
def clubs_search(request):
    players=request.POST.getlist("players[]")
    pls=[]
    for player in players:
#        pls.append(models.Player.objects.get(id=player))
    clubs = models.Club.objects.filter(players__in = pls)
    cls=[]
    for club in clubs:
        pls1=[]
        for player in club.players.all():
            pls1.append(player.name + " " + player.family)
        cls.append({
            "id":club.id,
            "name":club.name,
            "year":club.year,
            "players":pls1
        })
    return JsonResponse({"clubs":cls})