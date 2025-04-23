from django.contrib import admin
from .models import About, Client, Recentwork, Service

# Register all models
admin.site.register(About)
admin.site.register(Client)
admin.site.register(Recentwork)
admin.site.register(Service)
