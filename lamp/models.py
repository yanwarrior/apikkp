from django.db import models

class Lampu(models.Model):
	nama = models.CharField(max_length=30, unique=True)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.nama

	def nyala(self):
		self.status = True
		self.save()

	def mati(self):
		self.status = False
		self.save()


class Jadwal(models.Model):
	lampu = models.ForeignKey(Lampu)
	tanggal = models.DateField()
	jam = models.TimeField()
	state = models.BooleanField(default=False)
	# TODO: command 

	def __str__(self):
		return self.lampu.nama

	def state_nyala(self):
		self.state = True
		self.save()

	def state_mati(self):
		self.state = False
		self.save()


from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)