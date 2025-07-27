from models.utils import prompts

Models = [prompts]


def initialize_database():
    for model in Models:
        if not model.table_exists():
            model.create_table()
            print(f"已创建表: {model.__name__}")
        else:
            print(f"表已存在，跳过: {model.__name__}")

