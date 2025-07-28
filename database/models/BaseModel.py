import os
from peewee import Model, AutoField, DateTimeField, MySQLDatabase

from datetime import datetime

kindergarten_db = MySQLDatabase(
            'kindergarten',
            user=os.getenv('SQL_USER'),
            password=os.getenv('SQL_PASSWORD'),
            host=os.getenv('SQL_HOST'),
            port=int(os.getenv('SQL_PORT'))
        )


class BaseModel(Model):
    id = AutoField(primary_key=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)
    
    class Meta:
        database = kindergarten_db
        legacy_table_names = False  # 禁用旧式表名