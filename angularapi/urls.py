from django.urls import path
from .import views
from .import appAdmin

urlpatterns = [
    path('signup/', views.fn_signup),
    path('checkUsernameExists/', views.fn_check_username_exists),
    path('emailexist/',views.fn_email_check),
    path('loginemail/',views.fn_login_usermail),
    path('complaintregister/',views.fn_save_register),
    path('getUserDetail/', views.fn_get_user_details),
    path('registerComplaint/', views.fn_register_compaint),
    path('getAllPriorities', views.fn_get_all_priority)
]

urlpatterns += [
    path('getAllUsers/', appAdmin.fn_view_users),
    path('changeActiveFlag/', appAdmin.fn_change_activeflag),
    path('addPriority/', appAdmin.fn_add_priority),
    path('deletePriority/', appAdmin.fn_delete_priority)
]
