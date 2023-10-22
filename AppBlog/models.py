from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = models.CharField(max_length=1200)
    date = models.DateTimeField(auto_now_add=True)
    
    image = models.ImageField(upload_to='media/blog/', null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

class Comentario(models.Model):
    comentario = models.ForeignKey(Blog, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)