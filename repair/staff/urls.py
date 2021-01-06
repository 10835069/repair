from django.urls import path
from .views import *

urlpatterns = [
    # 行政人員帳號列表
    path('', StaffList.as_view(), name='staff_list'),
    # 新增行政人員帳號
    path('new/', StaffNew.as_view(), name='staff_new'),
    # 修改行政人員資料
    path('<int:pk>/update/', StaffUpdate.as_view(), name='staff_update'),
    # 修改行政人員密碼
    path('<int:pk>/passwd/', StaffPasswd.as_view(), name='staff_passwd'),
]