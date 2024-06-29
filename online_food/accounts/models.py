from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db.models import OneToOneField
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
# # Create your models here



class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('User must have an email id')
        
        if not username:
            raise ValueError('User must have  an username')
        
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,email,username,password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):

    RESTRAUNT=1
    CUSTOMER=2

    ROLE_CHOICE=(
        (RESTRAUNT,'Restraunt'),
        (CUSTOMER,'Customer'),
    )
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=12,blank=True)
    role=models.PositiveSmallIntegerField(choices=ROLE_CHOICE,blank=True,null=True)

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    objects=UserManager()

    def __str__(self):
        return self.email

    def has_permsel(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True


class UserProfile(models.Model):
    user=OneToOneField (User,on_delete=models.CASCADE,blank=True,null=True)
    profile_picture=models.ImageField(upload_to="user/profile_picture",blank=True,null=True)
    cover_photo=models.ImageField(upload_to="user/cover_photo",blank=True,null=True)
    address_line1=models.CharField(max_length=50,blank=True,null=True)
    address_line2=models.CharField(max_length=50,blank=True,null=True)
    country=models.CharField(max_length=15,blank=True,null=True)
    state=models.CharField(max_length=15,blank=True,null=True)
    city=models.CharField(max_length=15,blank=True,null=True)
    pin_code=models.CharField(max_length=6,blank=True,null=True)
    latitude=models.CharField(max_length=20,blank=True,null=True)
    longitute=models.CharField(max_length=20,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
# # Create your models here




class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('User must have an email id')
        
        if not username:
            raise ValueError('User must have  an username')
        
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,email,username,password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):

    RESTRAUNT=1
    CUSTOMER=2

    ROLE_CHOICE=(
        (RESTRAUNT,'Restraunt'),
        (CUSTOMER,'Customer'),
    )
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=12,blank=True)
    role=models.PositiveSmallIntegerField(choices=ROLE_CHOICE,blank=True,null=True)

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    objects=UserManager()

    def __str__(self):
        return self.email

    def has_permsel(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True


class UserProfile(models.Model):
    user=OneToOneField (User,on_delete=models.CASCADE,blank=True,null=True)
    profile_picture=models.ImageField(upload_to="user/profile_picture",blank=True,null=True)
    cover_photo=models.ImageField(upload_to="user/cover_photo",blank=True,null=True)
    address_line1=models.CharField(max_length=50,blank=True,null=True)
    address_line2=models.CharField(max_length=50,blank=True,null=True)
    country=models.CharField(max_length=15,blank=True,null=True)
    state=models.CharField(max_length=15,blank=True,null=True)
    city=models.CharField(max_length=15,blank=True,null=True)
    pin_code=models.CharField(max_length=6,blank=True,null=True)
    latitude=models.CharField(max_length=20,blank=True,null=True)
    longitute=models.CharField(max_length=20,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    
@receiver(post_save,sender=User)
def post_save_create_profile_receiver(sender,instance,created,**kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('user profile is created')
    else:
        try:
            profile=UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # create the userprofile if not exist
            UserProfile.objects.create(user=instance)
            print('profile was not exist,but i created one ')
        print('user is updated')

@receiver(pre_save,sender=User)
def pre_save_profile_receiver(sender,instance,**kwargs):
    print(instance.username,'this user is being saved')
post_save.connect(post_save_create_profile_receiver,sender=User)