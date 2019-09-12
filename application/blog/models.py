from django.db import models
from tinymce import models as tinymce_models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



User = get_user_model()


class Author (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    pdp = models.ImageField(upload_to='blog/', null=True, max_length=255)
    anniv = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_author_profile(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)
    instance.author.save()


class Article(models.Model):
   
	titre = models.CharField(max_length=255, blank=False, default='')
	date = models.DateField(auto_now_add=True)
	image = models.ImageField(upload_to='blog/', null=True, max_length=255)
	# contenu = tinymce_models.HTMLField()
	contenu = RichTextField(blank=False, default='')
	customer = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='author_article_set')

	def __str__(self):
		return self.titre
		# +", publié par : "+self.customer.user.username
