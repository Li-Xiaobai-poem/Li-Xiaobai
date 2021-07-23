from django.contrib import admin

# Register your models here.
from app1.models import Release
from app1.models import Comments
from app1.models import User
from app1.models import Collections
admin.site.register(Release )
admin.site.register(Comments)
admin.site.register(User)
admin.site.register( Collections)