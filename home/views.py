from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


@api_view(['GET'])
def NewCategory_view(request):
    category = NewCategory.objects.all()
    query = NewCategorySerializer(category, many=True).data
    return Response(query)


@api_view(['GET'])
def New_view(request):
    new = New.objects.all()
    query = NewSerializer(new, many=True).data
    return Response(query)


@api_view(['GET'])
def NewTable_view(request):
    table = NewTable.objects.all()
    query = NewTableSerializer(table, many=True).data
    return Response(query)


@api_view(['GET'])
def NewPlayer_view(request):
    player = NewPlayer.objects.all()
    query = NewPlayerSerializer(player, many=True).data
    return Response(query)


@api_view(['GET'])
def NewTeam_view(request):
    team = NewTeam.objects.all()
    query = NewTeamSerializer(team, many=True).data
    return Response(query)


@api_view(['GET'])
def Information_view(request):
    info = Information.objects.last()
    query = InformationSerializer(info).data
    return Response(query)


@api_view(['GET'])
def TeamPlayer_view(request):
    category = TeamPlayer.objects.all()
    query = TeamPlayerSerializer(category, many=True).data
    return Response(query)


@api_view(['GET'])
def CompetitionCategory_view(request):
    competition = CompetitionCategory.objects.all()
    query = CompetitionCategorySerializer(competition, many=True).data
    return Response(query)


@api_view(['GET'])
def Stroe_view(request):
    stroe = Stroe.objects.all()
    query = StroeSerializer(stroe, many=True).data
    return Response(query)


@api_view(['GET'])
def StroeArena_view(request):
    arena = StroeArena.objects.all()
    query = StroeArenaSerializer(arena, many=True).data
    return Response(query)


@api_view(['GET'])
def Leadership_view(request):
    leader = Leadership.objects.last()
    query = LeadershipSerializer(leader).data
    return Response(query)


@api_view(['GET'])
def Trainer_view(request):
    trainer = Trainer.objects.all()
    query = TrainerSerializer(trainer, many=True).data
    return Response(query)


@api_view(['GET'])
def Pride_view(request):
    pride = Pride.objects.all()
    query = PrideSerializer(pride, many=True).data
    return Response(query)


@api_view(['GET'])
def Ceremony_view(request):
    ceremony = Ceremony.objects.all()
    query = CeremonySerializer(ceremony, many=True).data
    return Response(query)


@api_view(['GET'])
def Reference_view(request):
    reference = Reference.objects.all()
    query = ReferenceSerializer(reference, many=True).data
    return Response(query)


@api_view(['GET'])
def Training_view(request):
    train = Training.objects.all()
    query = TrainerSerializer(train, many=True).data
    return Response(query)


@api_view(['GET'])
def Banner_view(request):
    banner = Banner.objects.all()
    query = BannerSerializer(banner, many=True).data
    return Response(query)


@api_view(['GET'])
def BoburArena_view(request):
    boburarena = BoburArena.objects.all()
    query = ReferenceSerializer(boburarena, many=True).data
    return Response(query)


@api_view(['GET'])
def ArenaImg_view(request):
    arena_img = ArenaImg.objects.last()
    query = ReferenceSerializer(arena_img).data
    return Response(query)


@api_view(['GET'])
def Bobur_view(request):
    bobur = Bobur.objects.all()
    query = BoburSerializer(bobur, many=True).data
    return Response(query)
