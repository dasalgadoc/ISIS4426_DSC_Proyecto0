""" User's application models """

from django.contrib.auth.models import User
from django.db import models


class PasswordRetrieval(models.Model):
    """" Proxy class from user to password retrieval """

    user = models.OneToOneField(User, on_delete = models.CASCADE)

    secret_question = models.CharField(max_length = 140, blank = True)
    secret_answer = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        """ To string method from Password Retrieval class """
        return "Question: {} -> Answer: {}".format(self.secret_question, self.secret_answer)

