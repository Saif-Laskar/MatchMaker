from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from .models import *


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=300, help_text=('Required. Enter an existing email address.'))
    name = forms.CharField(max_length=200)
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        help_text='Password Must be at least 8 character including numeric values',

    )

    class Meta:
        model = UserModel
        fields = ("name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'name'
        self.fields['name'].label = ''
        self.fields[
            'name'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['email'].label = ''
        self.fields[
            'email'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class WeddingPlannerSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=300, help_text=('Required. Enter an existing email address.'))
    name = forms.CharField(max_length=200)
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        help_text='Password Must be at least 8 character including numeric values',

    )
    is_company = True

    class Meta:
        model = UserModel
        fields = ("name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(WeddingPlannerSignupForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'name'
        self.fields['name'].label = ''
        self.fields[
            'name'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['email'].label = ''
        self.fields[
            'email'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=300, help_text=('Required. Enter an existing email address.'))
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        help_text='Password Must be at least 8 character including numeric values',

    )

    class Meta:
        model = UserModel
        fields = ("email", "password")


class EditProfileForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Prefer Not to Say', 'Prefer Not to Say')
    ]

    BLOOD_GROUP_CHOICES = [
        ('', 'Select Blood Group'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    RELIGION = [
        ('', 'Select Religion'),
        ('Islam', 'Islam'),
        ('Hindu', 'Hindu'),
        ('Cristian', 'Cristian'),
        ('Buddhist', 'Buddhist'),
        ('Jainism', 'Jainism'),
        ('Tribe', 'Tribe'),
        ('Atheist', 'Atheist'),
        ('Prefer Not to Say', 'Prefer Not to Say')
    ]

    RELATIONSHIP = [
        ('', 'Select Relationship Status'),
        ('Unmarried', 'Unmarried'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
        ('Married', 'Married')
    ]

    DISTRICTS = [
        ('', 'Select a District'),
        ('Bagerhat', 'Bagerhat'),

        ('Bandarban', 'Bandarban'),

        ('Barguna', 'Barguna'),

        ('Barishal', 'Barishal'),

        ('Bhola', 'Bhola'),

        ('Bogura', 'Bogura'),

        ('Brahmanbaria', 'Brahmanbaria'),

        ('Chandpur', 'Chandpur'),

        ('Chapainawabganj', 'Chapainawabganj'),

        ('Chattogram', 'Chattogram'),

        ('Chuadanga', 'Chuadanga'),

        ('Cox’s Bazar', 'Cox’s Bazar'),

        ('Cumilla', 'Cumilla'),

        ('Dhaka', 'Dhaka'),

        ('Dinajpur', 'Dinajpur'),

        ('Faridpur', 'Faridpur'),

        ('Feni', 'Feni'),

        ('Gaibandha', 'Gaibandha'),

        ('Gazipur', 'Gazipur'),

        ('Gopalganj', 'Gopalganj'),

        ('Habiganj', 'Habiganj'),

        ('Jamalpur', 'Jamalpur'),

        ('Jashore', 'Jashore'),

        ('Jhalokati', 'Jhalokati'),

        ('Jhenaidah', 'Jhenaidah'),

        ('Joypurhat', 'Joypurhat'),

        ('Khagrachhari', 'Khagrachhari'),

        ('Khulna', 'Khulna'),

        ('Kishoreganj', 'Kishoreganj'),

        ('Kushtia', 'Kushtia'),

        ('Kurigram', 'Kurigram'),

        ('Lakshmipur', 'Lakshmipur'),

        ('Lalmonirhat', 'Lalmonirhat'),

        ('Madaripur', 'Madaripur'),

        ('Magura', 'Magura'),

        ('Manikganj', 'Manikganj'),

        ('Meherpur', 'Meherpur'),

        ('Moulvibazar', 'Moulvibazar'),

        ('Munshiganj', 'Munshiganj'),

        ('Mymensingh', 'Mymensingh'),

        ('Naogaon', 'Naogaon'),

        ('Narayanganj', 'Narayanganj'),

        ('Narail', 'Narail'),

        ('Narsingdi', 'Narsingdi'),

        ('Natore', 'Natore'),

        ('Netrokona', 'Netrokona'),

        ('Nilphamari', 'Nilphamari'),

        ('Noakhali', 'Noakhali'),

        ('Pabna', 'Pabna'),

        ('Panchagarh', 'Panchagarh'),

        ('Patuakhali', 'Patuakhali'),

        ('Pirojpur', 'Pirojpur'),

        ('Rajbari', 'Rajbari'),

        ('Rajshahi', 'Rajshahi'),

        ('Rangamati', 'Rangamati'),

        ('Rangpur', 'Rangpur'),

        ('Satkhira', 'Satkhira'),

        ('Shariatpur', 'Shariatpur'),

        ('Sherpur', 'Sherpur'),

        ('Sirajganj', 'Sirajganj'),

        ('Sunamganj', 'Sunamganj'),

        ('Sylhet', 'Sylhet'),

        ('Tangail', 'Tangail'),

        ('Thakurgaon', 'Thakurgaon')
    ]

    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES))
    blood_group = forms.CharField(widget=forms.Select(choices=BLOOD_GROUP_CHOICES))
    religion = forms.CharField(widget=forms.Select(choices=RELIGION))
    relation_status = forms.CharField(widget=forms.Select(choices=RELATIONSHIP))
    district = forms.CharField(widget=forms.Select(choices=DISTRICTS))

    class Meta:
        model = ProfileModel
        fields = '__all__'
        exclude = ('user',)


class InterestForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('', 'Select Blood Group'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    RELIGION = [
        ('Islam', 'Islam'),
        ('Hindu', 'Hindu'),
        ('Cristian', 'Cristian'),
        ('Buddhist', 'Buddhist'),
        ('Jainism', 'Jainism'),
        ('Tribe', 'Tribe'),
        ('Atheist', 'Atheist'),
        ('Any', 'Any')
    ]

    DISTRICTS = [
        ('', 'Select a District'),
        ('Bagerhat', 'Bagerhat'),

        ('Bandarban', 'Bandarban'),

        ('Barguna', 'Barguna'),

        ('Barishal', 'Barishal'),

        ('Bhola', 'Bhola'),

        ('Bogura', 'Bogura'),

        ('Brahmanbaria', 'Brahmanbaria'),

        ('Chandpur', 'Chandpur'),

        ('Chapainawabganj', 'Chapainawabganj'),

        ('Chattogram', 'Chattogram'),

        ('Chuadanga', 'Chuadanga'),

        ('Cox’s Bazar', 'Cox’s Bazar'),

        ('Cumilla', 'Cumilla'),

        ('Dhaka', 'Dhaka'),

        ('Dinajpur', 'Dinajpur'),

        ('Faridpur', 'Faridpur'),

        ('Feni', 'Feni'),

        ('Gaibandha', 'Gaibandha'),

        ('Gazipur', 'Gazipur'),

        ('Gopalganj', 'Gopalganj'),

        ('Habiganj', 'Habiganj'),

        ('Jamalpur', 'Jamalpur'),

        ('Jashore', 'Jashore'),

        ('Jhalokati', 'Jhalokati'),

        ('Jhenaidah', 'Jhenaidah'),

        ('Joypurhat', 'Joypurhat'),

        ('Khagrachhari', 'Khagrachhari'),

        ('Khulna', 'Khulna'),

        ('Kishoreganj', 'Kishoreganj'),

        ('Kushtia', 'Kushtia'),

        ('Kurigram', 'Kurigram'),

        ('Lakshmipur', 'Lakshmipur'),

        ('Lalmonirhat', 'Lalmonirhat'),

        ('Madaripur', 'Madaripur'),

        ('Magura', 'Magura'),

        ('Manikganj', 'Manikganj'),

        ('Meherpur', 'Meherpur'),

        ('Moulvibazar', 'Moulvibazar'),

        ('Munshiganj', 'Munshiganj'),

        ('Mymensingh', 'Mymensingh'),

        ('Naogaon', 'Naogaon'),

        ('Narayanganj', 'Narayanganj'),

        ('Narail', 'Narail'),

        ('Narsingdi', 'Narsingdi'),

        ('Natore', 'Natore'),

        ('Netrokona', 'Netrokona'),

        ('Nilphamari', 'Nilphamari'),

        ('Noakhali', 'Noakhali'),

        ('Pabna', 'Pabna'),

        ('Panchagarh', 'Panchagarh'),

        ('Patuakhali', 'Patuakhali'),

        ('Pirojpur', 'Pirojpur'),

        ('Rajbari', 'Rajbari'),

        ('Rajshahi', 'Rajshahi'),

        ('Rangamati', 'Rangamati'),

        ('Rangpur', 'Rangpur'),

        ('Satkhira', 'Satkhira'),

        ('Shariatpur', 'Shariatpur'),

        ('Sherpur', 'Sherpur'),

        ('Sirajganj', 'Sirajganj'),

        ('Sunamganj', 'Sunamganj'),

        ('Sylhet', 'Sylhet'),

        ('Tangail', 'Tangail'),

        ('Thakurgaon', 'Thakurgaon')
    ]

    QUALIFICATION = [
        ('NONE', 'NONE'),
        ('SSC', 'SSC'),
        ('HSC', 'HSC'),
        ('BACHELOR', 'BACHELOR'),
        ('MASTERS', 'MASTERS'),
        ('PhD', 'PhD')
    ]

    interest_religion=forms.CharField(widget=forms.Select(choices=RELIGION))
    interest_district=forms.CharField(widget=forms.Select(choices=DISTRICTS))
    interest_gender=forms.CharField(widget=forms.Select(choices=GENDER_CHOICES))
    class Meta:
        model = InterestModel
        fields = '__all__'
        exclude = ['user']


class EditCompanyProfileForm(forms.ModelForm):
    company_started = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CompanyProfileModel
        fields = '__all__'
        exclude = ['user']


class CreatePackageForm(forms.ModelForm):
    class Meta:
        model = WeddingPlanPackagesModel
        fields = '__all__'
        exclude = ['user']

class WishListForm(forms.ModelForm):
    class Meta:
        model = WishListModel
        fields = '__all__'
