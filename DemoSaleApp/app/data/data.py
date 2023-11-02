import json
from app import db,app
from app.models import Department, Employee, Customer


def read_data_phongban():
    with open('data_phongban.json', encoding='utf-8') as f:
        return json.load(f)

def read_data_nhanvien():
    with open('data_nhanvien.json', encoding='utf-8') as f:
        return json.load(f)

def read_data_khachhang():
    with open('data_khachang.json', encoding='utf-8') as f:
        return json.load(f)


def add_data_phongban(data, mapb, tenpb):
    pb = {
        "mapb": mapb,
        "tenpb": tenpb,
    }
    #ghi dữ liệu tạm thời
    data['listphongban'].append(pb)

    #Ghi dữ liệu vào file.json
    with open('data_phongban.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def add_data_nhanvien(data, manv, tennv, sodienthoai, diachi, ma_pb):
    nv = {
        "manv": manv,
        "tennv": tennv,
        "sodienthoai": sodienthoai,
        "diachi": diachi,
        "ma_pb": ma_pb
    }
    #ghi dữ liệu tạm thời
    data['listnhanvien'].append(nv)

    #Ghi dữ liệu vào file.json
    with open('data_nhanvien.json.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def add_data_khachhang(data, makh, tenkh, sodienthoai, diachi, email):
    nv = {
        "makh": makh,
        "tenkh": tenkh,
        "sodienthoai": sodienthoai,
        "diachi": diachi,
        "email": email
    }
    #ghi dữ liệu tạm thời
    data['listkhachhang'].append(nv)

    #Ghi dữ liệu vào file.json
    with open('data_khachang.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def add_datapb_database():
    #Đọc dữ liệu
    datapb = read_data_phongban()
    for item in datapb['listphongban']:
        department = Department(mapb=item["mapb"], tenpb=item["tenpb"])
        db.session.add(department)
        db.session.commit()

def add_datanv_database():
    #Đọc dữ liệu
    datanv = read_data_nhanvien()
    for item in datanv['listnhanvien']:
        employee = Employee(manv=item["manv"], tennv=item["tennv"],
                            sodienthoai=item["sodienthoai"], diachi=item["diachi"], ma_pb=item["ma_pb"])
        db.session.add(employee)
        db.session.commit()

def add_datakh_database():
    #Đọc dữ liệu
    datakh = read_data_khachhang()
    for item in datakh['listkhachhang']:
        customer = Customer(makh=item["makh"], tenkh=item["tenkh"],
                            sodienthoai=item["sodienthoai"], diachi=item["diachi"], email=item["email"])
        db.session.add(customer)
        db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        pass
