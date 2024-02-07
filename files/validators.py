from django.core.exceptions import ValidationError
import magic

mime = magic.Magic(mime=True)


def valid_file_types(file):
    allowed_types = ['image/jpeg', 'image/png', 'application/pdf', 'text/plain']
    file_type = mime.from_buffer(file.read(2048))

    if file_type not in allowed_types:
        raise ValidationError('Type not allowed')

    file.seek(0)
    return file
