import json
from app import db, app
from app.models import Department, Employee, Customer, Product, Category


def read_data_phongban():
    with open('data_phongban.json', encoding='utf-8') as f:
        return json.load(f)


def read_data_nhanvien():
    with open('data_nhanvien.json', encoding='utf-8') as f:
        return json.load(f)


def read_data_khachhang():
    with open('data_khachang.json', encoding='utf-8') as f:
        return json.load(f)

def read_data_product():
    with open('data_product.json', encoding='utf-8') as f:
        return json.load(f)

def read_data_category():
    with open('data_category.json', encoding='utf-8') as f:
        return json.load(f)


def add_data_phongban(data, mapb, tenpb):
    pb = {
        "maphongban": mapb,
        "tenphongban": tenpb,
    }
    # ghi dữ liệu tạm thời
    data['listphongban'].append(pb)

    # Ghi dữ liệu vào file.json
    with open('data_phongban.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def add_data_nhanvien(data, manv, tennv, sodienthoai, diachi, ma_pb):
    nv = {
        "manhanvien": manv,
        "tennhanvien": tennv,
        "sodienthoai": sodienthoai,
        "diachi": diachi,
        "ma_phongban": ma_pb
    }
    # ghi dữ liệu tạm thời
    data['listnhanvien'].append(nv)

    # Ghi dữ liệu vào file.json
    with open('data_nhanvien.json.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def add_data_khachhang(data, makh, tenkh, sodienthoai, diachi, email):
    nv = {
        "makhachhang": makh,
        "tenkhachhang": tenkh,
        "sodienthoai": sodienthoai,
        "diachi": diachi,
        "email": email
    }
    # ghi dữ liệu tạm thời
    data['listkhachhang'].append(nv)

    # Ghi dữ liệu vào file.json
    with open('data_khachang.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def add_data_product(data, name, price, description, status, url_img, category_id):
    pd = {
        "name": name,
        "price": price,
        "description": description,
        "status": status,
        "url_img": url_img,
        "category_id": category_id
    }
    # ghi dữ liệu tạm thời
    data['listproduct'].append(pd)

    # Ghi dữ liệu vào file.json
    with open('data_product.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def add_data_category(data, name):
    category = {
        "name": name
    }
    # ghi dữ liệu tạm thời
    data['listcategory'].append(category)

    # Ghi dữ liệu vào file.json
    with open('data_category.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)



def add_datapb_database():
    # Đọc dữ liệu
    datapb = read_data_phongban()
    for item in datapb['listphongban']:
        department = Department(maphongban=item["maphongban"], tenphongban=item["tenphongban"])
        db.session.add(department)
        db.session.commit()


def add_datanv_database():
    # Đọc dữ liệu
    datanv = read_data_nhanvien()
    for item in datanv['listnhanvien']:
        employee = Employee(manhanvien=item["manhanvien"], tennhanvien=item["tennhanvien"],
                            sodienthoai=item["sodienthoai"], diachi=item["diachi"], ma_phongban=item["ma_phongban"])
        db.session.add(employee)
        db.session.commit()


def add_datakh_database():
    # Đọc dữ liệu
    datakh = read_data_khachhang()
    for item in datakh['listkhachhang']:
        customer = Customer(makhachhang=item["makhachhang"], tenkhachhang=item["tenkhachhang"],
                            sodienthoai=item["sodienthoai"], diachi=item["diachi"], email=item["email"])
        db.session.add(customer)
        db.session.commit()

def add_dataprodouct_database():
    # Đọc dữ liệu
    dataproduct = read_data_product()
    for item in dataproduct['listproduct']:
        product = Product(name=item["name"], price=item["price"],
                          description=item["description"], status=item["status"], url_img=item["url_img"],
                          category_id=item["category_id"])
        db.session.add(product)
        db.session.commit()

def add_datacategory_database():
    # Đọc dữ liệu
    datacategory = read_data_category()
    for item in datacategory['listcategory']:
        category = Category(name=item["name"])
        db.session.add(category)
        db.session.commit()



if __name__ == '__main__':
    with app.app_context():
        pass
        add_datacategory_database()
        add_dataprodouct_database()
        add_datapb_database()
        add_datanv_database()
        add_datakh_database()

