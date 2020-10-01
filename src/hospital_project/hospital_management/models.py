from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
   """Helps django work with our custom user model."""
   def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        if not email:
           raise ValueError('Users must have an email address.')


        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user


   def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""
        user = self.create_user(email, name, password)
        user.is_superuser = True


        user.is_staff = True
        user.save(using=self._db)


        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a "user profile" inside our system."""

    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """Used to get a users full name."""

        return self.name


    def get_short_name(self):
           """Used to get users short name."""

           return self.name


    def __str__(self):
          """Django uses this when it needs to convert the object to string."""
          return self.email
