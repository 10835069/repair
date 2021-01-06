from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.
# 行政人員列表
class StaffList(PermissionRequiredMixin, ListView):
  permission_required = 'auth.view_user'
  model = User
  ordering = ['username']
  paginate_by = 15

# 新增行政人員帳號
class StaffNew(PermissionRequiredMixin, CreateView):
  permission_required = 'auth.add_user'
  model = User
  fields = ['username', 'first_name', 'password']

  def get_success_url(self):
    return reverse('staff_list')

  # 表單驗證
  def form_valid(self, form):
    user = form.save(commit=False)
    user.set_password(form.cleaned_data['password'])
    return super().form_valid(form)

# 修改行政人員帳號資料
class StaffUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'auth.change_user'
  model = User
  fields = ['username', 'first_name']

  def get_success_url(self):
    return reverse('staff_list')

# 修改行政人員密碼
class StaffPasswd(PermissionRequiredMixin, UpdateView):
  permission_required = 'auth.change_user'
  model = User
  fields = ['password']

  def get_success_url(self):
    return reverse('staff_list')

  # 設定初始值
  def get_initial(self):
    return {
      'password': '',
    }

  # 表單驗證
  def form_valid(self, form):
    user = form.save(commit=False)
    user.set_password(form.cleaned_data['password'])
    return super().form_valid(form)

