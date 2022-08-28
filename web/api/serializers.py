from rest_framework import serializers

from dashboard.models import News

class NewsSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    text = serializers.CharField()
    url = serializers.CharField()
    tags = serializers.SerializerMethodField()
    
    class Meta:
        fields = '__all__'
        model = News

    def get_tags(self, obj):
        return obj.tags.split('|')