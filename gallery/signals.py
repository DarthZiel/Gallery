from django.contrib.auth.models import Group, User
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:  # Только для новых пользователей
        group, _ = Group.objects.get_or_create(name='gallery')  # Убедитесь, что группа существует
        instance.groups.add(group)  # Добавляем пользователя в группу

@receiver(m2m_changed, sender=User.groups.through)
def set_is_staff_for_group(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":  # Когда пользователь добавляется в группу
        default_group = Group.objects.get(name="gallery")  # Убедитесь, что группа существует
        if default_group.pk in pk_set:
            instance.is_staff = True  # Даем доступ к админке
            instance.save()
