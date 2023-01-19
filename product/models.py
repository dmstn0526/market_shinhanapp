from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='회원')
    title = models.CharField(max_length=128, verbose_name="상품명")
    content = models.TextField(verbose_name="상품내용")
    price = models.IntegerField(verbose_name="가격")
    location = models.CharField(max_length=256, verbose_name="위치")
    image = models.FileField(null=True, blank=True,verbose_name="이미지")

    def __str__(self): # __로 감싸진 magic method: 함수를 직접 호출해서 사용하는 것이 아닌 자동으로 호출되는 로직
        return f'상품명: {self.title}, 가격: {self.price}원, 위치: {self.location}'

    class Meta:
        db_table = 'shinhan_product'
        verbose_name='상품'
        verbose_name_plural = '상품' # 복수형 지칭