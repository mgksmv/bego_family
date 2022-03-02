import os
from django.core.exceptions import ValidationError


def validate_file(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.pdf', '.docx', '.pptx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Вы можете загрузить только PDF, Word документ или файлы презентации.')


def validate_pdf(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Вы можете загрузить только PDF.')


def validate_video(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.mp4', '.mov', '.avi', '.webm', '.wmv', '.mkv', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.ogg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Вы можете загрузить только видео файлы.')
