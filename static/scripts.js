$(document).ready(function() {
    submitProduct();
    getProducts();
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
                console.log(response)
            },
            error: function (response) {
                console.log(response)
            },
            complete: function () {
                nameProduct.val('');
                unityProduct.val('');
                btnSaveProduct.prop("disabled", false);
                nameProduct.prop("disabled", false);
                unityProduct.prop("disabled", false);
                getProducts();
            }

        })
    });
}

function getProducts() {
    var data = {
        'email': 'samuel@gmail.com'
    };
    $.ajax({
       url: Flask.url_for("get_products"),
       type: 'GET',
       data: data,
       success: function (response) {
           $.each(response, function (index, value) {
               listItemProduct(index, value);
           });
       },
       error: function (response) {
           console.log(response)
       },
       complete: function () {
           console.log('complete')
       }
   })
}

function listItemProduct(index, value) {
    var listProducts = $('.list-products');
    var li = '<li class="list-group-item list-product" data-index="' + index + '">';
    li += '<div class="item-product">';
    li += '<span>' + value.name + '</span>';
    li += '<span class="float-right">';
    li += '<button type="button" class="btn btn-warning" id="edit-item" onclick=askEdit('+index+');>Edit</button>';
    li += '<button type="button" class="btn btn-danger" id="delete-item" onclick=askDelete('+index+');>Delete</button>';
    li += '</span></div>';
    li += '<div class="edit-product" data-key="' + value.key + '" hidden>';
    li += '<span>Certeza que quer deletar o item?</span><span>SIM | NÃO</span></div>';
    li += '<div class="delete-product" data-key="' + value.key + '" hidden>';
    li += '<span>DELETAR ITEM</span></div></li>';

    $(li).appendTo(listProducts)
}

function askDelete(index) {
    var li = $("li[data-index='?']".replace('?', index));
    li.find(".delete-product").removeAttr('hidden');
}

function askEdit(index) {
    var li = $("li[data-index='?']".replace('?', index));
    li.find(".edit-product").removeAttr('hidden');
}