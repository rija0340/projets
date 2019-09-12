from django.db import models

#table pour blog

class Personne(models.Model):

    nom = models.CharField(max_length=70, blank=False, default='')
    # date = models.DateField(auto_now_add=True)
    # image = models.CharField(max_length=70, blank=False, default='')
    # owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE, null= True, blank=True )
    
    # comment declaer un champ basé sur un foreingkey
    # def auteur(self):
    #     return self.utilisateur.username

    def __str__(self):
    	return self.nom





