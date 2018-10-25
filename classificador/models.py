from django.db import models

class Dominio(models.Model):
	url = models.CharField(max_length=100)
	restrict = models.BooleanField()

class Pagina(models.Model):
	url = models.CharField(max_length=200)
	domain = models.ForeignKey(Dominio, on_delete=models.CASCADE)
	restrict = models.BooleanField()

class Motivo(models.Model):
	nome = models.CharField(max_length=100)

class DominioRestritoPor(models.Model):
	id_d = models.ForeignKey(Dominio, on_delete=models.CASCADE)
	nome_m = models.ForeignKey(Motivo, on_delete=models.CASCADE)

class PaginaRestritoPor(models.Model):
	id_p = models.ForeignKey(Pagina, on_delete=models.CASCADE)
	nome_m = models.ForeignKey(Motivo, on_delete=models.CASCADE)