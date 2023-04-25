from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # 유효성 검사에서는 제외시키고, 데이터 조회시에는 제공 (읽기 전용 속성)
        read_only_fields = ('article',)



class ArticleSerializer(serializers.ModelSerializer):

    class MyCommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)

    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = MyCommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        # comment_set은 Article 모델에 물리적 필드가 아니기 때문에 아래처럼 작성 불가능
        # read_only_fields = ('comment_set',)
