import jsonfield
from django.db import models


default_story = {
    "0": {
        "que": "",
        "ans": [
            {
                "text": "",
                "redir": 1
            }
        ]
    }
}


class Story(models.Model):
    title = models.CharField(max_length=64,
                             verbose_name='Название истории',
                             unique=True)
    description = models.CharField(max_length=256,
                                   verbose_name='Описание истории',
                                   unique=True)
    data = jsonfield.JSONField(default=default_story)

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'

    def __str__(self):
        return self.title