from django.contrib import admin

from . import models

admin.site.register(models.Department)
admin.site.register(models.User)
admin.site.register(models.Admin)
admin.site.register(models.User_bookmark)
admin.site.register(models.Dissertation)
admin.site.register(models.Dissertation_authors)
admin.site.register(models.User_file)
admin.site.register(models.User_group)
admin.site.register(models.Group_bookmark)
admin.site.register(models.Folder)
admin.site.register(models.Site)
admin.site.register(models.User_access)
admin.site.register(models.Headers)
admin.site.register(models.Practice)
admin.site.register(models.Proxies)
