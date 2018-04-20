# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['name']) < 5:
            errors["name"] = "Name has to be more than 5 characters"
        print len(postData['desc'])
        if len(postData['desc']) < 10:
            errors['desc'] = "Description has to be more than 10 characters"
        return errors

class Courses(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = CourseManager()

    def __repr__(self):
        return "< name {}, description {} >".format(self.name, self.desc)



