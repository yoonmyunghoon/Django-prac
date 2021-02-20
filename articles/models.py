from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail
from django.conf import settings

# 이미지 업로드 경로 커스텀
# instance -> Article 모델의 인스턴스 객체
# filename -> 사용자가 업로드한 파일의 이름
# 처음 생성할 때는 pk가 안들어가서 none값이 들어감
def articles_image_path(instance, filename):
    return f"articles/{instance.pk}번글/images/{filename}"


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    # image_thumbnail = ImageSpecField(
    #     source="image",
    #     processors=[Thumbnail(200, 300)],
    #     format="JPEG",
    #     options={"quality": 90},
    # )
    image = ProcessedImageField(
        processors=[Thumbnail(200, 300)],
        format="JPEG",
        options={"quality": 90},
        upload_to=articles_image_path,  # MEDIA_ROOT(media)/articles/images
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles", blank=True)

    class Meta:
        ordering = ("-pk",)

    def __str__(self):
        return f"{self.id}번글 - {self.title}: {self.content}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-pk",)

    def __str__(self):
        return f"<Article({self.article_id}): Comment({self.pk} - {self.content})>"
