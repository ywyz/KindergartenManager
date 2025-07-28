from database.crud import create_prompt


def add_prompt(name, grade, subject, content, output_format):
    """
    添加新的提示词
    """
    result = create_prompt(name=name, grade=grade, subject=subject, content=content, output_format=output_format)
    return result