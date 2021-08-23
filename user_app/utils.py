from datetime import date


def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age


def get_interested_profiles(user_interests, profiles):
    interested = []
    interested = [profile for profile in profiles
                  if profile.gender == user_interests.interest_gender
                  and profile.religion == user_interests.interest_religion]
    return interested

def get_my_wedding_plans(user,packages):
    myPacks=[]

    myPacks=[package for package in packages
             if package.user.id==user.id]

    return myPacks

def not_in_wish_list(user,models,profile):

    for model in models:
        if model.user==user and model.wished_profile==profile:
            return False
    return True

def my_wish_list(user,wishModel):
    my_list=[]

    my_list=[wish.wished_profile for wish in wishModel
             if wish.user==user]
    return my_list
