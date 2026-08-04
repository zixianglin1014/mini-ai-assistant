class PromptTemplate:

    def __init__(self, template):

        self.template = template

    def format(self, **kwargs):

        return self.template.format(**kwargs)
