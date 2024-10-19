from django.db import models

# Create your models here.
class Contato(models.Model):
    telefone = models.CharField(max_length=14)
    email = models.CharField(max_length=45,unique=True)

class User(models.Model):
    nome = models.CharField(max_length=50)
    contato = models.ForeignKey(Contato, models.PROTECT)

class Motorista(User):
    cpf = models.CharField(max_length=14)
    numero_CNH = models.IntegerField()
    categoria_CNH = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    
class Van(models.Model):
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE,related_name='vans_associadas')
    origem = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    ponto_parada = models.CharField(max_length=50)
    horario_saida = models.TimeField( auto_now=False, auto_now_add=False)
    contato = models.ForeignKey(Contato, models.PROTECT)
    duracao_percurso = models.TimeField(auto_now=False, auto_now_add=False)

class Reserva(models.Model):
    id_Van = models.ForeignKey(Van, on_delete=models.CASCADE)
    id_User = models.ForeignKey(User, on_delete=models.CASCADE)
    Destino = models.CharField(max_length=50)
    Acento = models.IntegerField()
