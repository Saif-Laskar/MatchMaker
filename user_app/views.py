from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from .forms import *
from .utils import *


def home_view(request):
    if request.user.is_authenticated and not request.user.is_company :
        user = request.user

        user_interests = InterestModel.objects.get(user=user)
        profiles = ProfileModel.objects.all()

        interested_profiles = get_interested_profiles(user_interests, profiles)

        context = {
            'interested_profiles': interested_profiles
        }
        return render(request, "index.html", context)

    return render(request, "index.html")


def login_view(request):
    form = LoginForm()
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user and user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})

    context = {
        'form': form,
    }

    return render(request, "login.html", context)


def signup_view(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST['email']
            password = request.POST['password1']
            user = authenticate(request, email=email, password=password)
            ProfileModel.objects.create(user=user)
            InterestModel.objects.create(user=user)
            login(request, user)

            return redirect('home')

        else:
            form = SignupForm()
            context = {
                'form': form,
            }
            return render(request, "Signup.html", context)
    # name='Name'
    context = {
        'form': form,
        # 'name': name,
    }
    return render(request, "signup.html", context)


def weddingPlannerSignup_view(request):
    form = WeddingPlannerSignupForm()

    if request.method == 'POST':
        form = WeddingPlannerSignupForm(request.POST)
        if form.is_valid():
            # form.is_company=True
            # print(form.is_company)
            form.save()
            email = request.POST['email']
            password = request.POST['password1']
            user = authenticate(request, email=email, password=password)
            user.is_company = True
            user.save()
            CompanyProfileModel.objects.create(user=user)
            # user.set_isCompany()
            print(user.name)
            login(request, user)
            return redirect('home')

        else:
            form = WeddingPlannerSignupForm()
            context = {
                'form': form,
                # 'name': name,
            }
            return render(request, "wedding_signup.html", context)
    # name='Name'
    context = {
        'form': form,
        # 'name': name,
    }
    return render(request, "wedding_signup.html", context)


def profile_view(request, pk):
    user = UserModel.object.get(id=pk)
    list = WishListModel.objects.all()



    is_self = False
    if user == request.user:
        is_self = True
    profile = ProfileModel.objects.get(user=user)

    interest = InterestModel.objects.get(user=user)

    not_wished = not_in_wish_list(request.user, list, profile)
    print(not_wished)
    context = {
        'not_wished':not_wished,
        'is_self': is_self,
        'user': user,
        'profile': profile,
        'interest': interest
    }
    # return render(request,"profile.html",context)
    return render(request, "profile.html", context)


def edit_profile_view(request):
    profile = ProfileModel.objects.get(user=request.user)
    form = EditProfileForm(instance=profile)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            profile = form.save()

            if profile.date_of_birth:
                dob = profile.date_of_birth
                age = calculate_age(dob)
                profile.age = age
            profile.save()
            return redirect('profile', profile.user.id)
        else:
            return redirect('edit-profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, "edit-profile.html", context)


def logout_view(request):
    logout(request)
    return redirect('login')


def wedding_planners_profile_view(request, pk):
    user = UserModel.object.get(id=pk)

    is_self = False

    if user == request.user:
        is_self = True
    profile = CompanyProfileModel.objects.get(user=user)
    allplans = WeddingPlanPackagesModel.objects.all()

    packages = get_my_wedding_plans(user, allplans)

    context = {
        'is_self': is_self,
        'user': user,
        'profile': profile,
        'packages': packages,
    }
    return render(request, 'weddingPlannersProfile.html', context)



def editWeddingProfile_view(request):
    profile = CompanyProfileModel.objects.get(user=request.user)
    form = EditCompanyProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditCompanyProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            # ProfileModel.objects.update()
            print(profile.user.name)
            print(profile.user.id)
            return redirect('weddingPlannersProfile', profile.user.id)
        else:
            return redirect('edit-WeddingPlannerProfile')

    context = {
        'form': form,
        'profile': profile,

    }

    return render(request, "edit-WeddingPlannerProfile.html", context)




def  create_wedding_plan_package_view(request):

    form = CreatePackageForm()
    user = request.user
    print(user.id)
    if request.method == 'POST':
        print("in method")
        form=CreatePackageForm(request.POST,request.FILES)

        if form.is_valid():

            plan=form.save(commit=False)
            plan.user=request.user
            plan.save()
            # packageName = request.POST['packageName']
            # code = request.POST['code']
            # price = request.POST['price']
            # description = request.POST['description']
            # WeddingPlanPackagesModel.objects.create(user=user,packageImage=request.POST['packageImage'],packageName=packageName,code=code,price=price,description=description)


            return redirect('weddingPlannersProfile',user.id)
            #return redirect('home')
        else:
            context={
                'form':form,
                'user': user,
            }
            return render(request,'createWeddingPlanPackage.html',context)

    context = {
            'form': form,
            'user': user,
        }
    return render(request, 'createWeddingPlanPackage.html', context)





def update_interests_view(request):
    user = request.user
    interest = InterestModel.objects.get(user=user)
    form = InterestForm(instance=interest)

    if request.method == 'POST':
        form = InterestForm(request.POST, instance=interest)

        if form.is_valid():
            form.save()
            return redirect('profile', user.id)
        else:
            return redirect('update-interests')

    context = {
        'form': form,
        'user': user,
    }

    return render(request, "update-interests.html", context)

def add_to_wishList_view(request,pk):
    form =  WishListModel()
    user = request.user
    form.user=user
    pUser =UserModel.object.get(id=pk)
    print(pUser.id)
    profile= ProfileModel.objects.get(user=pUser)
    form.wished_profile= profile
    form.save()
    user_interests = InterestModel.objects.get(user=user)
    profiles = ProfileModel.objects.all()
    interested_profiles = get_interested_profiles(user_interests, profiles)
    context = {
        'interested_profiles': interested_profiles
    }
    return render(request, "index.html",context)

def my_fav_view(request):
    user=request.user

    wishModel = WishListModel.objects.all()
    Wishedprofiles = my_wish_list(user,wishModel)
    context = {
        'Wishedprofiles': Wishedprofiles
    }

    return render(request,"myWishList.html",context)
