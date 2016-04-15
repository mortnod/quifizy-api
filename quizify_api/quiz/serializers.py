from rest_framework import serializers

from songs.models import Category, Song
from quiz.models import *
from accounts.serializers import PlayerSerializer


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'spotify_uri')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    songs = SongSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'songs')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    player = PlayerSerializer()

    class Meta:
        model = Score
        fields = ('player', 'answer_time', 'answered_correctly')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    correct_answer = SongSerializer()
    alternatives = SongSerializer(many=True)
    score_player1 = ScoreSerializer()
    score_player2 = ScoreSerializer()

    class Meta:
        model = Question
        fields = ('correct_answer', 'alternatives', 'score_player1', 'score_player2')


class RoundSerializer(serializers.HyperlinkedModelSerializer):
    whos_turn = PlayerSerializer()
    winner = PlayerSerializer()
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Round
        fields = ('id', 'status', 'whos_turn', 'winner', 'category', 'questions')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    player1 = PlayerSerializer()
    player2 = PlayerSerializer()
    rounds = RoundSerializer(many=True)

    class Meta:
        model = Game
        fields = ('id', 'player1', 'player2', 'invitation_status', 'rounds')