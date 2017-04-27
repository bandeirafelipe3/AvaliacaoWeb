from django.db import models
from django.utils import timezone
# Create your models here.

class Prato(models.Model):
	autor = models.ForeignKey('auth.User')
	nome = models.CharField(max_length=45)
	ingredientes = models.TextField()
	preparo = models.TextField()
	pessoas = models.IntegerField()
	tempodepreparo = models.IntegerField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publicar(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nome



