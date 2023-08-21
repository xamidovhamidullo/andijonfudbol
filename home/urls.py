from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('New/', New_view),
    path('NewTable/', NewTable_view),
    path('NewPlayer/', NewPlayer_view),
    path('NewTeam/', NewTeam_view),

    path('TeamPlayer/', TeamPlayer_view),

    path('Stroe/', Stroe_view),
    path('StroeArena/', StroeArena_view),

    path('Leadership/', Leadership_view),

    path('Trainer/', Trainer_view),

    path('Pride/', Pride_view),

    path('Ceremony/', Ceremony_view),
    path('Reference/', Reference_view),
    path('Training/', Training_view),

    path('Banner/', Banner_view),

    path('BoburArena/', BoburArena_view),
    path('ArenaImg/', ArenaImg_view),
    path('Bobur/', Bobur_view),
]
