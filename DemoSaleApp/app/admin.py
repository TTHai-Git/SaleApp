from flask import redirect
from flask_admin import BaseView, expose
from flask_login import current_user, logout_user

from app import app, db, admin

from app.models import Category, Product, Employee, Customer, Department, Tag, Order_Details, UserRole
from flask_admin.contrib.sqla import ModelView


class AdminAuthenticated(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN

class ProductView(AdminAuthenticated):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True
    column_list = ('id', 'name', 'price', 'description', 'status', 'create_date', 'category', 'tags')
    # column_exclude_list = ['url_img']

    column_filters = ['name', 'price']
    column_searchable_list = ['name']

    column_labels = {
        'id': "Mã Sản Phẩm",
        'name': "Tên Sản Phẩm",
        'price': "Đơn Giá",
        'description': "Mô Tả",
        'status': "Tình Trạng",
        'create_date': "Ngày Nhập Hàng",
        'category': "Danh Mục",
        'tags': "Khuyến Mãi"

    }
    form_excluded_columns = ['products']

    # def is_accessible(self):
    #     return current_user.is_authenticated

class CategoryView(AdminAuthenticated):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True

    # def is_accessible(self):
    #     return current_user.is_authenticated


class OrderDetailsView(AdminAuthenticated):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True

    column_list = ('id', 'makhachhangmua', 'customer', 'masanphammua', 'product', 'soluongmua', 'thanhtien',
                   'ngaylaphoadon', 'ghichu')
    column_labels = {
        'id': "STT",
        'makhachhangmua': "Mã Khách Hàng Mua",
        'customer': "Tên Khách Hàng",
        'masanphammua': "Mã Sản Phẩm Mua",
        'product': "Tên Sản Phẩm Mua",
        'soluongmua': "Số Lượng Mua",
        'thanhtien': "Thành Tiền",
        'ngaylaphoadon': "Ngày Tạo Hóa Đơn",
        'ghichu': "Ghi Chú"
    }

    # def is_accessible(self):
    #     return current_user.is_authenticated


class CustomerView(AdminAuthenticated):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True

    column_filters = ['tenkhachhang', 'makhachhang', 'sodienthoai']
    column_searchable_list = ['makhachhang']

    # def is_accessible(self):
    #     return current_user.is_authenticated

class EmployeeView(AdminAuthenticated):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True

    column_searchable_list = ['tennhanvien']
    column_filters = ['tennhanvien', 'manhanvien', 'sodienthoai']

    # def is_accessible(self):
    #     return current_user.is_authenticated

class DepartmentView(AdminAuthenticated):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True

    column_list = ('maphongban', 'tenphongban')
    column_searchable_list = ['tenphongban']
    column_filters = ['tenphongban', 'maphongban']

    # def is_accessible(self):
    #     return current_user.is_authenticated

class TagsView(AdminAuthenticated):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True

    column_labels = {
        'id': "Mã Khuyến Mãi",
        'name': "Tên Mã Khuyến Mãi",
        'description': "Mô Tả Khuyến Mãi"
    }

    column_searchable_list = ['name']
    column_filters = ['name', 'id']

    # def is_accessible(self):
    #     return current_user.is_authenticated


class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()

        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated

admin.add_view(CategoryView(Category, db.session, name='Danh Mục'))
admin.add_view(ProductView(Product, db.session, name='Sản Phẩm'))
admin.add_view(EmployeeView(Employee, db.session, name='Nhân Viên'))
admin.add_view(CustomerView(Customer, db.session, name='Khách Hàng'))
admin.add_view(DepartmentView(Department, db.session, name='Phòng Ban'))
admin.add_view(TagsView(Tag, db.session, name='Khuyến Mãi'))
admin.add_view(OrderDetailsView(Order_Details, db.session, name='Chi Tiết Đặt Hàng'))
admin.add_view(StatsView(name='BÁO CÁO THỐNG KÊ'))
admin.add_view(LogoutView(name='ĐĂNG XUẤT'))
