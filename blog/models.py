from django.db import models
from django.conf import settings  

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs/')
    category = models.CharField(max_length=50, choices=[('Mental Health', 'Mental Health'), ('Heart Disease', 'Heart Disease'), ('Covid19', 'Covid19'), ('Immunization', 'Immunization')])
    summary = models.TextField()
    content = models.TextField()
    draft = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
