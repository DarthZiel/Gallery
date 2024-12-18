from .models import ThreeDModel
# Register your models here.



from django.contrib import admin


class ThreeDModelAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        # Установить текущего пользователя как владельца записи
        if not change:  # Если это новое добавление
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        # Ограничить видимость записей только для текущего пользователя
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        # Разрешить изменять только свои записи
        if obj and obj.user != request.user:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        # Разрешить удалять только свои записи
        if obj and obj.user != request.user:
            return False
        return super().has_delete_permission(request, obj)

admin.site.register(ThreeDModel, ThreeDModelAdmin)