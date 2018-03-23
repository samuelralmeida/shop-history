$(document).ready(function() {
    submitProduct();
    getProducts()
});

function submitProduct() {
    $(".form-product").submit(function (event) {
        // get elemnts of save product form
        event.preventDefault();
        var nameProduct = $(".name_product");
        var unityProduct = $(".unity_product");
        var btnSaveProduct = $(".btn-save-product");

        // disable fields to block resend
        btnSaveProduct.prop("disabled", true);
        nameProduct.prop("disabled", true);
        unityProduct.prop("disabled", true);

        var data = {
            'name': nameProduct.val(),
            'unity': unityProduct.val()
        };

        $.ajax({
            url: Flask.url_for("create_product"),
            type: 'POST',
            data: JSON.stringify(data),
            contentType: "application/json; charset=utf-8",
            success: function (response) {
                console.log('sucesso');
                console.log(response)
            },
            error: function (response) {
                console.log('error');
                console.log(response)
            },
            complete: function () {
                nameProduct.val('');
                unityProduct.val('');
                btnSaveProduct.prop("disabled", false);
                nameProduct.prop("disabled", false);
                unityProduct.prop("disabled", false);
            }

        })
    });
}

function getProducts() {
    console.log('teste');
    var data = {
        'email': 'samuel@gmail.com'
    };
    $.ajax({
       url: Flask.url_for("get_products"),
       type: 'GET',
       data: data,
       success: function (response) {
           $.each(response, function (index, value) {
               listItemProduct(value);
           });
           console.log('sucesso');
       },
       error: function (response) {
           console.log('error');
           console.log(response)
       },
       complete: function () {
           console.log('complete')
       }
   })
}

function listItemProduct(value) {
    var listProducts = $('.list-products');
    var li = $('<li/>');
    li.addClass("list-group-item");
    li.text(value.name);
    li.appendTo(listProducts)
}