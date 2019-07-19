from django.db import models
from django.contrib.auth.models import AbstractUser

# 일반 유저
class CUser(AbstractUser):
    codeNum = models.IntegerField(blank=True, null=True, verbose_name="주민번호")                # 주민 번호
    phoneNum = models.IntegerField(
        blank=True, null=True, verbose_name= "전화번호")               # 핸드폰 번호
    # 직업
    job = models.ForeignKey('Job', on_delete=models.CASCADE, related_name='user_job', blank=True, null=True, verbose_name="직업ㄴ")
    license = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="자격증")    # 자격증
    # 레벨
    level = models.IntegerField(default=1)
    point = models.IntegerField(default=0)                              # 가지고 있는포인트
    area = models.ForeignKey('Area', on_delete=models.CASCADE,
                             related_name='user_area', blank=True, null=True, verbose_name="지역")  # 지역
    another = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="기타 특이사항")   # 비고
    image = models.ImageField(
        upload_to='images/', blank=True, null=True, verbose_name="사진")  # 이미지
    is_organ = models.BooleanField(default=False, verbose_name="")                       # 일반 회원인지, 기관 회원인지 확인
    organ = models.OneToOneField('Organ', on_delete=models.CASCADE, related_name='user_organ', blank=True, null=True)  # 기관에 대한 정보
    def __str(self):
        return self.username

# 기관 유저에 대해 이어줄 테이블 
class Organ(models.Model):
    crew = models.CharField(max_length=20, verbose_name="소속")                # 소속
    ead = models.CharField(max_length=20, verbose_name="책임자명")             # 책임자명
    url = models.CharField(max_length=500,default="", verbose_name="URL")     # 인터넷 주소
    def __str(self):
        return self.Cuser.username

# 봉사 활동 -> 일반 유저와 기관 유저와 연결
class Service(models.Model):
    name = models.CharField(max_length=40)          # 봉사활동명
    Essential = models.BooleanField(default=True)   # 필수 퀘스트인지의 여부
    Finish = models.BooleanField(default=False)     # 봉사활동의 등록 마감 여부
    point = models.IntegerField()                   # 봉사활동에 해당하는 포인트
    level = models.IntegerField()                   # 어느 레벨에서 열리는지의 레벨
    organ = models.ForeignKey('CUser', on_delete=models.CASCADE, related_name="service_organ")    # 기관
    user = models.ManyToManyField('CUser', related_name='service_user')    # 이에 대한 퀘스트를 할 유저
    number = models.IntegerField(default=15)        # 봉사활동에 참여할 수 있는 최대의 유저 _ 일반 유저가 참여할 때 마다 1씩 차감
    emergency = models.BooleanField(blank=False)    # 긴급 봉사인지의 여부
    image = models.ImageField(upload_to='images/', blank=True)  # 이미지
    def __str__(self):
        return self.name

# 지역
class Area(models.Model):
    area = models.CharField(max_length=20)  # 지역
    def __str__(self):
        return self.area

# 직업
class Job(models.Model):
    job = models.CharField(max_length=20)   # 직업
    def __str__(self):
        return self.name

# 상품
class Product(models.Model):
    name = models.CharField(max_length=30)  # 상품명
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE) # 상품의 브랜드
    point = models.IntegerField()           # 해당 상품의 포인트
    image = models.ImageField(upload_to='images/', blank=True)
    def __str__(self):
        return self.name

# 브랜드
class Brand(models.Model):
    name = models.CharField(max_length=20)  # 브랜드명
    image = models.ImageField(upload_to='images/', blank=True)  # 브랜드 이미지
    def __str__(self):
        return self.name

# Create your models here.
