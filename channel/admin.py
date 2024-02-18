from django.contrib import admin

from channel.models import MenuOptions, Menus, Session

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('chat_id','menu_id','msg_id','last_text','is_closed','updated')


@admin.register(Menus)
class MenuAdmin(admin.ModelAdmin):
    pass

@admin.register(MenuOptions)
class MenuOptionsAdmin(admin.ModelAdmin):
    list_display = ('label', 'menu','created')
