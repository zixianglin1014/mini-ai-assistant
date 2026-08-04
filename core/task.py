from core.prompts import QA_PROMPT, SUMMARY_PROMPT, TITLE_PROMPT

TASK_PROMPTS = {"summary": SUMMARY_PROMPT, "title": TITLE_PROMPT, "qa": QA_PROMPT}


TASK_REQUIREMENTS = {
    "summary": ["text"],
    "title": ["text"],
    "qa": ["context", "question"],
}


def get_prompt(task):

    if task not in TASK_PROMPTS:

        raise ValueError(f"不支持的任务类型:{task}")

    return TASK_PROMPTS[task]


def get_required_params(task):

    if task not in TASK_REQUIREMENTS:

        raise ValueError(f"未知任务:{task}")

    return TASK_REQUIREMENTS[task]
