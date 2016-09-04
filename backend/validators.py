import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.json',]
    if not ext in valid_extensions:
        raise ValidationError('Extensión de archivo no soportada.')

def validate_phone_format(value):
    if(len(value) != 10 or not value.isdigit()):
        raise ValidationError('Pofavor ingrese un numero de telefono válido.')
