from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import io

class News:
    def __init__(self, title, content):
        self.title = title
        self.content = content

news = News(title="ASfsafgafg", content="fsadftgfrfs")


class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=180)
    content = serializers.CharField()


def convert_to_json():
    serializer = NewsSerializer(news)
    
    json = JSONRenderer().render(serializer.data)
    print(json)


def json_to_python():
    json = b'{"title":"ASfsafgafg","content":"fsadftgfrfs"}'
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = NewsSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)



