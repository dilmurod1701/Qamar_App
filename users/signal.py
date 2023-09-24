from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete, post_delete
from django.contrib.auth.models import User

from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.crete(user=instance)
        instance.save()
        subject = 'Assalomu alekum'
        message = "Tabriklayman bugundan boshlab siz bizning foydalanuvchimiz qatoriga qo'shildingiz"
        from_mail = 'backendchi.bollar.no1@gmail.com'
        to = 'absoluteomon999@gmail.com'
        send_mail(subject=subject, message=message,from_email=from_mail, recipient_list=[to])

@receiver(pre_delete, sender=User)
def delete_profile(sender, instance, **kwargs):
    instance.profile.delete()
    print("Profile deleted")

