from django.db import models


class Session(models.Model):
    chat_id = models.CharField(max_length=32)
    last_text = models.CharField(max_length=255, blank=True, null=True)
    menu_id = models.IntegerField()
    msg_id = models.CharField(max_length=32)
    is_closed = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Menus(models.Model):
    label = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    menu_type = models.CharField(max_length=32, choices=(('T','Tree'),('P','Param')))
    has_options = models.BooleanField(default=False)
    close_session = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.pk}. {self.label}'


class MenuOptions(models.Model):
    menu = models.ForeignKey(Menus, related_name='menus_menu_options', on_delete=models.CASCADE)
    label = models.CharField(max_length=32)
    data = models.CharField(max_length=32, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-created',)
