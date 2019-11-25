"""multipleserviceproviders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('delete_session',delete_session),
    path('',index),
    path('index', index),

    path('services',services),
    path('about',about),
    path('contact',contact),
    path('error',error),
    path('gallery',gallery),
    path('typography',typography),
    path('addadmin',addadmin),
    path('insertadmin',insertadmin),
    path('viewadmin',viewadmin),
    path('removeadmin',removeadmin),
    path('fetchadminforupdate',fetchadmindetailsforupdate),
    path('updateadmin',updateadmins),
    path('adminlogin',adminlogin),
    path('adminlogin2',adminlogin2),
    path('admindashboard',admindashboard),
    path('forgetpassword',forgetpassword),
    path('searchuser',searchuser),
    path('changepassword',changepassword),
    path('addcategory',addcategory),
    path('addcategoryaction',addcategoryaction),
    path('viewcateogry',viewcateogry),
    path('deletecategory',deletecategory),
    path('otp',otp),
    path('sendotp',sendotp),
    path('verifyotp',verifyotp),
    path('usersignup2',usersignup2),
    path('insertuserdata',insertuserdata),
    path('userlogin',userlogin),
    path('userindex',userindex),
    path('merchantsignup',serviceprovidersignup),
    path('serviceprovidersignin',serviceprovidersignin),
    path('forgetmerchantpassword', forgetmerchantpassword),
    path('serviceproviderlogin',serviceproviderlogin),
    path('merchantdashboaard',merchantdashboaard),
    path('merchantservices',merchantservices),
    path('addmerchantservices',addmerchantservices),
    path('insertserviceprovider',insertserviceprovider),
    path('viewmerchants',viewmerchants),
    path('merchantstatusdone',merchantstatusdone),
    path('approvedmerchants',approvedmerchants),
    path('merchantstatuspending',merchantstatuspending),
    path('searchservice1',searchservice1),
    path('searchservice2',searchservice2),
    path('demomodel',demomodel),
    path('getmerchantdetails',getmerchantdetails),
    path('getmerchantavailbality',getmerchantavailbality),
    path('gotopaymentpage',gotopaymentpage),
    path('inserttodb',inserttodb),
    path('viewappointments',viewappointments),
    path('statusdone', statusdone),
    path('viewuserorders',viewuserorders),
    path('vieworders',vieworders),
    path('viewserviceforrating',viewserviceforrating),
    path('ratingdemo',ratingdemo),
    path('AddRating',AddRating),
    path('getAverageRating',getAverageRating),
    path('getallcategory',getallcategory),
    path('fetchcategory',fetchcategory),
    path('userenquiry',userenquiry),
    path('carpenter',carpenter),
    path('gotocarpenter',gotocarpenter),
    path('electrician',electrician),
    path('gotoelectrician',gotoelectrician),
    path('plumber',plumber),
    path('gotoplumber',gotoplumber),
    path('welder',welder),
    path('painter',painter),
    path('fitter',fitter),
    path('usersignup',usersignup),
    path('logout',logout)


    # path('signup2',signup2),
]
