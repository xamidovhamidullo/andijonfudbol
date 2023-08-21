from rest_framework import serializers
from .models import *


class NewCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewCategory
        fields = '__all__'


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'


class NewTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewTable
        fields = '__all__'


class NewPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewPlayer
        fields = '__all__'


class NewTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewTeam
        fields = '__all__'


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class TeamPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPlayer
        fields = '__all__'


class CompetitionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionCategory
        fields = '__all__'


class StroeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stroe
        fields = '__all__'


class StroeArenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StroeArena
        fields = '__all__'


class LeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'


class PrideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pride
        fields = '__all__'


class CeremonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceremony
        fields = '__all__'


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class BoburArenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoburArena
        fields = '__all__'


class ArenaImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArenaImg
        fields = '__all__'


class BoburSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bobur
        fields = '__all__'