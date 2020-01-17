import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
# Create your views here.

@csrf_exempt
def fn_signup(req):
    if req.method == 'POST':
        data = json.loads(req.body)
        userexists = UserLogin.objects.filter(username=data['name']).exists()
        if not userexists:
            userlogin_obj = UserLogin(username=data['name'], password=data['password'])
            userlogin_obj.save()
            if userlogin_obj.id > 0:
                userdetails_obj = UserDetails(email=data['email'], mobile=data['mobile'], gender=data['gender'], dob=data['dob'], fk_login=userlogin_obj)
                userdetails_obj.save()
                if userdetails_obj.id > 0:
                    return JsonResponse({'status': True})
            return JsonResponse({'status': False, 'msg': 'failed to insert userdetails'})
        return JsonResponse({'status': False, 'msg': 'username already exists'})
    return JsonResponse({'status': False, 'msg': 'method not allowed'})


@csrf_exempt
def fn_check_username_exists(req):
    data = json.loads(req.body)
    userexists = UserLogin.objects.filter(username=data['name']).exists()
    return JsonResponse({'status': userexists})

@csrf_exempt
def fn_email_check(req):
    maildata = json.loads(req.body)
    email_exists = UserDetails.objects.filter(email=maildata['mail']).exists()
    return JsonResponse({'status': email_exists})

@csrf_exempt
def fn_login_usermail(request):
    logindata = json.loads(request.body)
    if UserLogin.objects.filter(username = logindata['username']).exists():
        user_obj = UserLogin.objects.get(username=logindata['username'])
        if user_obj.password == logindata['password']:
            if user_obj.active_flag == 1:
                return JsonResponse({'status': True, 'userId': user_obj.id, 'role': user_obj.role})
            return JsonResponse({'status': False, 'msg': 'Your account is disabled'})
        return JsonResponse({'status': False, 'msg': 'Invalid password'})      
    return JsonResponse({'status': False, 'msg': 'Invalid username' })

@csrf_exempt
def fn_save_register(req):
    regdata = json.loads(req.body)
    print(regdata)
    return JsonResponse({'status': False})


@csrf_exempt
def fn_get_user_details(req):
    data = json.loads(req.body)
    user_obj = UserDetails.objects.get(fk_login__id=data['userId'])
    user_detail = {
        'username': user_obj.fk_login.username,
        'email': user_obj.email,
        'mobile':user_obj.mobile,
        'sex':user_obj.gender,
        'dob': user_obj.dob
    }
    return JsonResponse({'status': True, 'details': user_detail})


@csrf_exempt
def fn_register_compaint(req):
    images = req.FILES
    user_obj = UserLogin.objects.get(id=req.POST['userId'])
    priority_obj = ComplaintPriority.objects.get(id=req.POST['priority'])
    complaint_obj = Complaintreg(complaint=req.POST['compaint'], fk_priority=priority_obj, fk_user=user_obj)
    complaint_obj.save()
    for key, value in images.items():
        comp_img_obj = ComplaintImages(image=value, fk_complaint=complaint_obj)
        comp_img_obj.save()
    return JsonResponse({'status': True})



@csrf_exempt
def fn_get_all_priority(req):
    try:
        priorities_obj = ComplaintPriority.objects.all()
        priorities = []
        for obj in priorities_obj:
            prio_obj = {
                'priority_name': obj.priority_name,
                'display_style': obj.display_style,
                'id': obj.id
            }
            priorities.append(prio_obj)
        return JsonResponse({'status': True, 'priorities': priorities})
    except Exception as identifier:
        return JsonResponse({'status': False, 'msg': str(identifier)})
