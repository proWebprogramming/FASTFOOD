from django.contrib import admin
from home.models import Aboutus, Chef, ContactMessage


class AboutusAdmin(admin.ModelAdmin):
    list_display = ['title','email', 'phone',]

class ChefAdmin(admin.ModelAdmin):
    list_display = ['title',]



class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'email', 'message', 'creat_at',]
    readonly_fields = ('name', 'surname', 'phone', 'email', 'message', 'creat_at',)
    list_filter = ['status']










admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Chef, ChefAdmin)
admin.site.register(Aboutus, AboutusAdmin)

