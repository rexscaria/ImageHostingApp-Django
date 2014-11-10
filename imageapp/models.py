from django.db import models
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher
from django.core.files.storage import FileSystemStorage
from django.conf import  settings

# Create your models here.
file_system = FileSystemStorage(location=settings.FILE_SYSTEM)

class User(models.Model):
    email = models.EmailField(max_length=200, null=False, unique=True)
    first_name = models.CharField(max_length=60, null=False)
    second_name = models.CharField(max_length=60, null=False)
    password = models.CharField(max_length=60, null=False)

    def _get_password(self):
        return self._password

    def _set_password(self, value):
        hasher = BCryptSHA256PasswordHasher()
        self._password = hasher.encode(value,hasher.salt())

    def __unicode__(self):
        return "{0} {1}".format(self.first_name, self.second_name)

    def return_valid_user(self, email_address, raw_password):
        hasher = BCryptSHA256PasswordHasher()
        password = hasher.encode(raw_password, hasher.salt())
        user = self.objects.filter(email=email_address, _password=password)
        if user:
            return User
        return None


class Picture(models.Model):
    user = models.ForeignKey(User, null=False, related_name='pictures')
    photo = models.ImageField(storage=file_system)

    def __unicode__(self):
        return "{0} {1}".format(self.user, self.photo)

