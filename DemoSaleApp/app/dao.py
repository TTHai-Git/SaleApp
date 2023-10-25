def loaditemnavbar():
    navitems = [{
        "id": 1,
        "title": "Điện Thoại"

    }, {
        "id": 2,
        "title": "Laptop"

    }, {
        "id": 3,
        "title": "Tablet"

    }, {
        "id": 4,
        "title": "Đồ Gia Dụng"

    }, {
        "id": 5,
        "title": "PC"

    }]
    return navitems

def loadphoneitem(kw=None):
    phones = [{
        "ma_dt": 1,
        "ten_dt": "Iphone 14 ProMax",
        "gia": 35000000,
        "tinhtrang": "Còn Hàng",
        "url_image": "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-purple-1.jpg"

    }, {
        "ma_dt": 2,
        "ten_dt": "Samsung S20 Ultra",
        "gia": 19050000,
        "tinhtrang": "Còn Hàng",
        "url_image": "https://cdn.tgdd.vn/Products/Images/42/217937/samsung-galaxy-s20-ultra-xam-1-org.jpg"

    }, {
        "ma_dt": 3,
        "ten_dt": "Iphone 14 ProMax",
        "gia": 35000000,
        "tinhtrang": "Còn Hàng",
        "url_image": "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-purple-1.jpg"

    }, {
        "ma_dt": 4,
        "ten_dt": "Iphone 14 ProMax",
        "gia": 35000000,
        "tinhtrang": "Còn Hàng",
        "url_image": "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-purple-1.jpg"

    }, {
        "ma_dt": 5,
        "ten_dt": "Iphone 14 ProMax",
        "gia": 35000000,
        "tinhtrang": "Còn Hàng",
        "url_image": "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-purple-1.jpg"

    }, {
        "ma_dt": 6,
        "ten_dt": "Iphone 14 ProMax",
        "gia": 35000000,
        "tinhtrang": "Còn Hàng",
        "url_image": "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-purple-1.jpg"

    }]
    if kw:
        phones = [p for p in phones if p["ten_dt"].lower().find(kw.lower()) >= 0]
    else:
        return phones
    return phones
