from django.shortcuts import render

def index(request):
    context = {'title': 'GeekShop - Админ панель'}
    return render(request, 'admins/index.html', context)

# CRUD
def admin_users_create(request):
    context = {'title': 'GeekShop - Созданиее пользователя'}
    return render(request, 'admins/admin-users-create.html', context)

def admin_users(request):
    context = {'title': 'GeekShop - Пользователи'}
    return render(request, 'admins/admin-users-read.html', context)

def admin_users_update(request):
    context = {'title': 'GeekShop - Обновление пользователя'}
    return render(request, 'admins/admin-users-update-delete.html', context)

def admin_users_delete(request):
    pass

