from django.db import models


class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return "%s  -  %s " % (self.name, self.email)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'A lot of users'