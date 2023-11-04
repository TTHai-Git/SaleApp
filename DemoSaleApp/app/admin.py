from app import app, db, admin

from app.models import Category, Product, Employee, Customer, Department, Tag
from flask_admin.contrib.sqla import ModelView


class ProductView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True
    column_list = ('id', 'name', 'price', 'description', 'status', 'create_date', 'category', 'tags')
    #column_exclude_list = ['url_img']
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
        'tag': "Khuyến Mãi"

    }
    form_excluded_columns = ['products']


class CategoryView(ModelView):
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True


admin.add_view(CategoryView(Category, db.session, name='Danh Mục'))
admin.add_view(ProductView(Product, db.session, name='Sản Phẩm'))
admin.add_view(ModelView(Employee, db.session, name='Nhân Viên'))
admin.add_view(ModelView(Customer, db.session, name='Khách Hàng'))
admin.add_view(ModelView(Department, db.session, name='Phòng Ban'))
admin.add_view(ModelView(Tag, db.session, name='Khuyến Mãi'))
