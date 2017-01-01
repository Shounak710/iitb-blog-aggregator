# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Items(models.Model):
    link = models.TextField(unique=True)
    feed = models.TextField()
    title = models.TextField()
    summary = models.TextField(blank=True, null=True)
    author_email = models.TextField(blank=True, null=True)
    author_name = models.TextField(blank=True, null=True)
    hash = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'items'

    def get_author(self):
        author = ""
        if self.author_name:
            author = "By " + self.author_name
        return author

    def get_summary(self):
        rsummary = self.summary
        if len(self.summary) > 30:
            rsummary = rsummary[:100]
        rsummary = rsummary + '...'
        return rsummary