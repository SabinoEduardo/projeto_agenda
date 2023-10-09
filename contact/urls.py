from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search_contact'), # Buscar objetos pelo first_name ou last_name

    # contact (CRUD)
    path('contact/<int:contact_id>/', views.get_contact, name='get_contact'), # buscar por um conatcto
    path('contact/create/', views.create, name='create_contact'), # Criar um contacto
    path('contact/<int:contact_id>/update', views.update, name='update_contact'), # Atualizar um contacto
    path('contact/<int:contact_id>/delete', views.delete, name='delete_contact'),

    # user
    path('user/create_user', views.create_user, name='create_user'),

    path('user/login', views.login_user, name='login'),
    path('user/logout', views.logout_user, name='logout'),

]
