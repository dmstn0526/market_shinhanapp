from django.db import models

# Create your models here.

class Member(models.Model):
    user_id = models.CharField(max_length=128, unique=True, verbose_name='아이디')
    password = models.CharField(max_length=225, verbose_name='비밀번호')
    name = models.CharField(max_length=128, verbose_name='이름')
    age = models.IntegerField(verbose_name='나이')

    def __str__(self): # __로 감싸진 magic method: 함수를 직접 호출해서 사용하는 것이 아닌 자동으로 호출되는 로직
        return f'{self.name}: {self.age}세'

    class Meta:
        verbose_name='회원'
        verbose_name_plural = '회원' # 복수형 지칭