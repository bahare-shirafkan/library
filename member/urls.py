from django.urls import path
from member import views


urlpatterns = [
    path('api/member', views.store, name="member-store"),
    path('api/members', views.getAll, name="members"),
    path('api/member/<int:id>', views.detail, name="member-detail"),
    path('api/member/update/<int:id>', views.update, name="member-update"),
    path('api/member/delete/<int:id>', views.delete, name="member-delete")

]
