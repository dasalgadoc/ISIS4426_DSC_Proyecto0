""" Event's module for models """

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """ Event's Category: four by default (Conferencia, Seminario, Congreso, Cursos) """
    
    category_description = models.CharField(max_length = 100, blank = False)

    def __str__(self):
        """ To String method from Category class """
        return "Category: {}".format(self.category_description)


class EventType(models.Model):
    """ Event's type: two by default (Presencial, Virtual) """

    event_type_description = models.CharField(max_length = 100, blank = False)

    def __str__(self):
        """ To String method from Event Type class """
        return "Event Type: {}".format(self.event_type_description)


class Event(models.Model):
    """ Event class, allows to storage any event """

    # Own fields
    event_name = models.CharField(max_length = 140, blank = False)
    event_site = models.CharField(max_length = 140, blank = True)
    event_address = models.CharField(max_length = 200, blank = True)
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    event_create_date = models.DateTimeField(auto_now_add=True)

    # Relationship
    event_category = models.ForeignKey(Category, on_delete = models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete = models.CASCADE)
    event_creator = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        """ To String method from Event class """
        return "Event: {} -> {} -> {}. By: {}".format(self.event_name, 
            self.event_category.__str__(), 
            self.event_type.__str__(),
            self.event_creator.__str__())
