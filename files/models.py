from django.db import models
from .validators import valid_file_types


class File(models.Model):
    file = models.FileField(upload_to='uploads/', validators=[valid_file_types])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.file.name}'
