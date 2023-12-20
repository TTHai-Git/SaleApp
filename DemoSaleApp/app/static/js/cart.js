function addToCart(id, name, price) {
    fetch('/api/cart', {
        method: 'post',
        body: JSON.stringify({
            "id": id,
            "name": name,
            "price": price
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function(res) {
        return res.json();
    }).then(function(data) {
        console.info(data)
        let items = document.getElementsByClassName("cart-counter")
        for (let item of items)
            item.innerText = data.total_quantity
    });
}
function updateCart(id, obj){
//    obj là đại diện cho một element thông qua tham sô truyền vào là 'this' khi gọi hàm trong element đó qua một sự kiện
    obj.disabled = true;
//    literal function nhúng chuỗi và tham số (${tên tham số}) thành 1 biểu thức
    fetch(`/api/cart/${id}`,{
//      method: 'put' dùng cho cập nhật
        method: 'put',
        body: JSON.stringify({
            'quantity': obj.value
        }), headers:{
            'Content-Type':'application/json'
        }
    }).then(res => res.json()).then(data => {
        obj.disabled=false;
        let items = document.getElementsByClassName('cart-counter');
        for (let item of items)
            item.innerText = data.total_quantity
        let amount = document.getElementById('total-amount');
        amount.innerText = new Intl.NumberFormat().format(data.total_amount) + " " + "VNĐ"
    });
}
function deleteCart(id, obj){
    obj.disabled=true;
    if (confirm("Bạn có chắc muốn xóa không?") == true){
       fetch(`api/cart/${id}`,{
            method:'delete'
       }).then(function(res) {
            return res.json();
       }).then(function(data){
            obj.disabled=false;
            let items = document.getElementsByClassName('cart-counter');
            for (let item of items)
                item.innerText = data.total_quantity;
            let amount = document.getElementById('total-amount');
            amount.innerText = new Intl.NumberFormat().format(data.total_amount) + " " + "VNĐ"

            let d = document.getElementById(`product${id}`);
            d.style.display = "none";
       });
    }
}
