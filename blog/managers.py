from django.db import models


class CatalogRecordQuerySet(models.QuerySet):
    def display(self):
        return self.active()

    def active(self):
        return self.exclude(published_date__year=
            2018,
        )

    def published(self):
        '''
        Filters the Catalog records whose state is 'published'
        '''
        return self.filter(state='published')


PostManager = models.Manager.from_queryset(CatalogRecordQuerySet)
