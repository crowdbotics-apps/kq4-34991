from django.contrib import admin
from .models import Quests, Standings, User_Quest_Join

admin.site.register(Quests)
admin.site.register(Standings)
admin.site.register(User_Quest_Join)

# Register your models here.
