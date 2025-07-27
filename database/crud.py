from models.utils import prompts


def create_prompt(**kwargs):
    return prompts.create(**kwargs)


def get_prompt_by_id(prompt_id):
    return prompts.get_or_none(prompts.id == prompt_id)


def update_prompt(prompt_id, **kwargs):
    query = prompts.update(**kwargs).where(prompts.id == prompt_id)
    return query.execute()


def delete_prompt(prompt_id):
    query = prompts.delete().where(prompts.id == prompt_id)
    return query.execute()