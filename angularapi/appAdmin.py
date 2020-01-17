import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *

@csrf_exempt
def fn_view_users(req):
    try:
        data = json.loads(req.body)
        admin_obj = UserLogin.objects.get(id=data['userId'])
        if admin_obj.role == 'admin':
            users_obj = UserLogin.objects.filter(role='user')
            users = []
            for user in users_obj:
                user_obj = {
                    'username': user.username,
                    'active_flag': user.active_flag,
                    'id': user.id
                }
                users.append(user_obj)
            return JsonResponse({'status': True, 'users': users})
        return JsonResponse({'status': False, 'msg': 'Permission denied'})
    except Exception as identifier:
        return JsonResponse({'status': False, 'msg': str(identifier)})


@csrf_exempt
def fn_change_activeflag(req):
    try:
        data = json.loads(req.body)
        admin_obj = UserLogin.objects.get(id=data['adminId'])
        if admin_obj.role == 'admin':
            user_obj = UserLogin.objects.get(id=data['userId'])
            if data['activeFlag'] == 1:
                user_obj.active_flag = 0
            else:
                user_obj.active_flag = 1
            user_obj.save()
            return JsonResponse({'status': True, 'active_flag': user_obj.active_flag})
        return JsonResponse({'status': False, 'msg': 'Permission denied'}) 
    except Exception as identifier:
        return JsonResponse({'status': False, 'msg': str(identifier)})


@csrf_exempt
def fn_add_priority(req):
    try:
        data = json.loads(req.body)
        admin_obj = UserLogin.objects.get(id=data['userId'])
        if admin_obj.role == 'admin':
            priority_obj = ComplaintPriority(priority_name=data['name'], display_style=data['displayStyle'])
            priority_obj.save()
            return JsonResponse({'status': True})
        return JsonResponse({'status': False, 'msg': 'Permission denied'})
    except Exception as identifier:
        return JsonResponse({'status': False, 'msg': str(identifier)})


@csrf_exempt
def fn_delete_priority(req):
    try:
        data = json.loads(req.body)
        admin_obj = UserLogin.objects.get(id=data['userId'])
        if admin_obj.role == 'admin':
            ComplaintPriority.objects.get(id=data['priority_id']).delete()
            return JsonResponse({'status': True})
    except Exception as identifier:
        return JsonResponse({'status': False, 'msg': str(identifier)})
        