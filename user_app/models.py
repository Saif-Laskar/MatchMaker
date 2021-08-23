import uuid

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):

        if not email:
            raise ValueError("Email Address is Mandatory")
        if not name:
            raise ValueError("User Must have a name")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        # self.set_isCompany(s)
        user.is_company = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_weddingPlanner(self, email, name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.is_company = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):
    email = models.CharField(max_length=300, unique=True)
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    is_company = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_table):
        return True

    def set_isCompany(self):
        self.is_company = True


class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    nid = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    current_address = models.CharField(max_length=200, null=True, blank=True)
    district = models.CharField(max_length=15, null=True, blank=True)
    permanent_address = models.CharField(max_length=200, null=True, blank=True)
    blood_group = models.CharField(max_length=3, null=True, blank=True)
    relation_status = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    religion = models.CharField(max_length=20, null=True, blank=True)


class InterestModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    interest_religion = models.CharField(max_length=20, null=True, blank=True)
    interest_district = models.CharField(max_length=15, null=True, blank=True)
    interest_gender = models.CharField(max_length=10, null=True, blank=True)
    interest_max_height = models.IntegerField(null=True, blank=True)
    interest_min_height = models.IntegerField(null=True, blank=True)
    interest_max_age = models.IntegerField(null=True, blank=True)
    interest_min_age = models.IntegerField(null=True, blank=True)
    #interest_education = models.CharField(max_length=10, null=True, blank=True)


class CompanyProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    company_started = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    bank_acc_no = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)


class WeddingPlanPackagesModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE,null=True,blank=True)

    packageImage = models.ImageField(null=True, blank=True)
    packageName = models.CharField(max_length=50)
    #code = models.CharField(max_length=10,null=True, blank=True)
    code = models.CharField(max_length=10, unique=True)
    price = models.IntegerField()
    description = models.TextField()

    # def __unicode__(self):
    #     return self.user

# class MeetRequestModel(models.Model):
#
#     sender  = models.ForeignKey(UserModel,on_delete=models.CASCADE)
#     reciever= models.ForeignKey(UserModel,on_delete=models.CASCADE)
#     is_accepted= models.BooleanField(default=False)
#     is_rejected= models.BooleanField(default=False)

class WishListModel(models.Model):

    user= models.ForeignKey(UserModel, on_delete=models.CASCADE,null=True,blank=True)
    wished_profile=models.ForeignKey(ProfileModel , on_delete=models.CASCADE,null=True,blank=True)

