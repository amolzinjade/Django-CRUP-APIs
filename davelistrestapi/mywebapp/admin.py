from django.contrib import admin
from .models import listing
from .models import Image
from .models import Message

admin.site.register(listing)
admin.site.register(Image)
admin.site.register(Message)
# Register your models here.
