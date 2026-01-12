/*jslint browser: true*/
/*jslint plusplus: true*/
/*global FormData: false */
/*global $, jQuery, alert, console*/
/*..............................................................................................
... PARA VALIDAR LOS DATOS .....................................................
.............................................................................................*/
var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method) {
    "use strict";
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/*-------------------------------------------------------------------------
--------- PASO 1 --- AGREGAR PRIMER PRODUCTO A PEDIDO TRANSITORIO ---------
-------------------------------------------------------------------------*/
function AgregarI(cada_producto_id, valor) {
    "use strict";
    $.ajax({
        beforeSend : function (xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		url : "/tienda/agregar_i/",
		type : "GET",
		data : { cada_producto_id:cada_producto_id, valor:valor},
		success : function (json) {
            $('#'+json[0].idproducto +' .vervalor').val(json[0].cantida);
            localStorage.setItem(json[0].idproducto.toString(), json[0].cantida.toString());
            for(i = 0; i < localStorage.length; i++){
                let clave = localStorage.key(i);
                let valcp;
                valcp = ".cp_" + clave.toString()
                $( valcp ).attr("disabled", true);
              }
            console.log("ok++++++++++PASO 1++++++++++++++")
		},
		error : function (xhr, errmsg, err) {
			console.log('Error en carga de respuesta');
		}
    });
}
$('.agregar_i').click(function (event) {
    "use strict";
    event.preventDefault();
    let cada_producto_id = $(this).parent().find('.verid').val();
    let valor = $(this).parent().find('.vervalor').val();
    let i;
    // SI LA CLAVE NO INICIA CON prestige_ la elimino
    for(i = 0; i < localStorage.length; i++){
        let clave_eliminar = localStorage.key(i);;
        if(!clave_eliminar.startsWith("prestige_")){
            localStorage.removeItem(clave_eliminar);
        }
    }
    // SE FIJA SI EL VALOR YA EXISTE (POR SI EL BOTÓN NO ESTUVIERA ANUALDO LUEGO DE LA SELECCIÓN)
    // SE ENVÍA EL VALOR Y CLAVE DEL BOTÓN SELECCIONADO
    for(i = 0; i < localStorage.length; i++){
        let clave = localStorage.key(i);
        let el_valor = localStorage[clave];
        if(clave == cada_producto_id){
            valor = el_valor;
        }else{
            console.log("no hay coincidencia");
        }   
    }
   AgregarI(cada_producto_id, valor);
});

/*-------------------------------------------------------------------------
--------- PASO 2 -----  IR AL CARRITO -------------------------------------
-------------------------------------------------------------------------*/
$('.boton_carrito').click(function() {
    for(i = 0; i < localStorage.length; i++){
        let clave_eliminar = localStorage.key(i);
        if(!clave_eliminar.startsWith("prestige_")){
            localStorage.removeItem(clave_eliminar);
        }
    }
    $.ajax({
        url: "/tienda/crear_localstorage/",
        data:{producto : JSON.stringify(localStorage)},
        type: 'get',
        dataType: 'json',
        contentType: 'application/json',
        success: function (data) {
            var urla = window.location.origin + "/carrito";    
            window.location.href = urla;
        },
    });
  });

/*-------------------------------------------------------------------------
--------- PASO 3 RESTA CANTIDAD DE PRODUCTO EN LA TIENDA ------------------ 
-------------------------------------------------------------------------*/
function Quitar(cada_producto_id, valor) {
    "use strict";
    $.ajax({
        beforeSend : function (xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		url : "/tienda/quitar/",
		type : "GET",
		data : { cada_producto_id:cada_producto_id, valor:valor},
		success : function (json) {
            $('#'+json[0].idproducto +' .vervalor').val(json[0].cantida);
            let cant = json[0].cantida
            if (cant == 0){
                console.log("vacío");
                localStorage.removeItem(json[0].idproducto.toString(), json[0].cantida.toString());
                $.ajax({
                    url: "/tienda/crear_localstorage/",
                    data:{producto : JSON.stringify(localStorage)},
                    type: 'get',
                    dataType: 'json',
                    contentType: 'application/json',
                    success: function (data) {
                        var urla = window.location.origin + "/carrito";    
                        window.location.href = urla;
                    },
                });
                location.reload();
            }else{
                localStorage.setItem(json[0].idproducto.toString(), json[0].cantida.toString());
                location.reload();
            }
            location.reload();
		},
		error : function (xhr, errmsg, err) {
			console.log('Error en carga de respuesta');
		}
    });
}
$('.quitar').click(function (event) {
    "use strict";
    let cada_producto_id = $(this).parent().get(0).id;
    let valor = $(this).parent().find('.vervalor').val();
    let i;
    for(i = 0; i < localStorage.length; i++){
        let clave_eliminar = localStorage.key(i);
        if(!clave_eliminar.startsWith("prestige_")){
            localStorage.removeItem(clave_eliminar);
        }
    }
    for(i = 0; i < localStorage.length; i++){
        let clave = localStorage.key(i);
        let el_valor = localStorage[clave];
        if(clave == cada_producto_id){
            valor = el_valor;
        }else{
            console.log("no hay coincidencia");
        }   
    }
    Quitar(cada_producto_id, valor);
});

/*-------------------------------------------------------------------------
--------- PASO 3 INCREMENTA CANTIDAD DE PRODUCTO EN LA TIENDA -------------
-------------------------------------------------------------------------*/
function Agregar(cada_producto_id, valor) {
    "use strict";
    $.ajax({
        beforeSend : function (xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		url : "/tienda/agregar/",
		type : "GET",
		data : { cada_producto_id:cada_producto_id, valor:valor},
		success : function (json) {
            localStorage.setItem(json[0].idproducto.toString(), json[0].cantida.toString());
            location.reload();
		},
		error : function (xhr, errmsg, err) {
			console.log('Error en carga de respuesta');
		}
    });
}
$('.agregar').click(function (event) {
    "use strict";
    event.preventDefault(); 
    let cada_producto_id = $(this).parent().get(0).id;
    let valor = $(this).parent().find('.vervalor').val();
    let i;
    for(i = 0; i < localStorage.length; i++){
        let clave_eliminar = localStorage.key(i);
        if(!clave_eliminar.startsWith("prestige_")){
            localStorage.removeItem(clave_eliminar);
        }
    }
    for(i = 0; i < localStorage.length; i++){
        let clave = localStorage.key(i);
        let el_valor = localStorage[clave];
        if(clave == cada_producto_id){
            valor = el_valor;
        }else{
            console.log("no hay coincidenciaaaa");
        }   
    }
   Agregar(cada_producto_id, valor);
});

/*-------------------------------------------------------------------------
--------- PASO 4 BORRAR PRODUCTO DEL CARRITO ------------------------------
-------------------------------------------------------------------------*/
$('.eliminar_producto').click(function (event) {
    "use strict";
    let cada_producto_id = $(this).attr('id');
    cada_producto_id = cada_producto_id.replace(/^el/, "prestige_"); 
    let i;

    for(i = 0; i < localStorage.length; i++){
        let clave_eliminar = localStorage.key(i);
        if(!clave_eliminar.startsWith("prestige_")){
            localStorage.removeItem(clave_eliminar);
        }
    }
    localStorage.removeItem(cada_producto_id);
    $.ajax({
        url: "/tienda/crear_localstorage/",
        data:{producto : JSON.stringify(localStorage)},
        type: 'get',
        dataType: 'json',
        contentType: 'application/json',
        success: function (data) {
        var urla = window.location.origin + "/carrito";    
        window.location.href = urla;
        },
    });
});

 