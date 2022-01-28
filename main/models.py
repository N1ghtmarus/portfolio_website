from django.db import models

class Message(models.Model):
    author_name = models.CharField('Имя автора', max_length=50)
    message_text = models.TextField('Текст сообщения')
    created_at = models.DateTimeField('Опубликовано', auto_now_add=True)
    
    def __str__(self):
        return self.message_text

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']