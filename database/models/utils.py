from .BaseModel import BaseModel
from peewee import AutoField, CharField, TextField, DateTimeField, SQL


class prompts(BaseModel):
    """
    提示词表
    """
    id = AutoField(primary_key=True, verbose_name="ID")
    name = CharField(max_length=100, verbose_name="提示词名称")
    grade = CharField(max_length=50, verbose_name="适用年级")
    subject = TextField(verbose_name="提示词主题")
    content = TextField(verbose_name="提示词内容")
    output_format = TextField(verbose_name="输出格式")
    created_at = DateTimeField(
        constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')],
        verbose_name="创建时间"
    )
    updated_at = DateTimeField(
        constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], verbose_name="更新时间")


