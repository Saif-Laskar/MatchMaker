from django.urls import path

from user_app.views import *

urlpatterns = [
    path('', home_view, name="home"),
    path('login/', login_view, name="login"),
    path('signup/', signup_view, name="signup"),
    path('logout/', logout_view, name='logout'),
    path('weddingSignup/', weddingPlannerSignup_view, name="weddingSignup"),

    path('profile/<str:pk>', profile_view, name='profile'),
    path('weddingPlannersProfile/<str:pk>', wedding_planners_profile_view, name='weddingPlannersProfile'),
    path('update-profile/', edit_profile_view, name='edit-profile'),
    path('edit-WeddingPlannerProfile/', editWeddingProfile_view, name='edit-WeddingPlannerProfile'),

    path('update-interests/', update_interests_view, name='update-interests'),

    path('createWeddingPlanPackage/', create_wedding_plan_package_view, name='createWeddingPlanPackage'),
    path('<str:pk>',add_to_wishList_view,name='addToWishList'),

    path('myWishList/', my_fav_view, name='wish'),

]
