from django.db import models

# Create your models here.
class Stu(models.Model) :
    id = models.AutoField("学号",primary_key=True)
    name = models.CharField("姓名",max_length=16)
    age = models.SmallIntegerField("年龄")
    sex = models.CharField("性别",max_length=1)
    classid = models.CharField("班级",max_length=8)

    def __str__(self):
        return "%d:%s:%d:%s:%s"%(self.id,self.name,self.age,self.sex,self.classid)

    class Meta:
        db_table="stu"
        verbose_name = '浏览学生信息'
        verbose_name_plural = '学生信息管理'