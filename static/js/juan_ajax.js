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
--------- PRESTIGE-------------------- ------------------------------------
console.log("hola");
$( "*" ).css({
      "background-color": "red",
      "font-weight": "bolder"
    });
-------------------------------------------------------------------------*/
 

/*-------------------------------------------------------------------------
--------- QUITAR A PEDIDO TRANSITORIO ------------------------------------
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
            console.log(typeof(cant))
            if (cant == 0){
                console.log("vacío");
                localStorage.removeItem(json[0].idproducto.toString(), json[0].cantida.toString());

                console.log(JSON.stringify(localStorage));
                console.log("JSON.stringify(localStorage)");
                $.ajax({
                    url: "/tienda/crear_localstorage/",
                    data:{producto : JSON.stringify(localStorage)},
                    type: 'get',
                    dataType: 'json',
                    contentType: 'application/json',
                    success: function (data) {
                        var urla = window.location.origin + "/carrito";    
                        //var urla = "http://127.0.0.1:8000/"+ "panel/carrito";
                        window.location.href = urla;
                    },
                    //data: JSON.stringify(person)
                });
                location.reload();
            }else{
                console.log("no vacío");
                localStorage.setItem(json[0].idproducto.toString(), json[0].cantida.toString());
                location.reload();
            }
            location.reload();
            console.log("ok -----------")
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
    console.log(cada_producto_id);
    console.log(valor);

    console.log("JSON.stringify(localStorage)");
    console.log(JSON.stringify(localStorage));
    let i;

    for(i = 0; i < localStorage.length; i++){
        let clave_eliminar = localStorage.key(i);
        if(!clave_eliminar.startsWith("prestige_")){
            console.log("retorna NO verdadero !!!!!!!!!!!!!");
            localStorage.removeItem(clave_eliminar);
            console.log("retorna NO verdadero !!!!!!!!!!!!!");
        }

        /*
        if(isNaN(clave_eliminar)){
            localStorage.removeItem(i);
        }

        if(clave_eliminar == "django.admin.navSidebarIsOpen"){
            localStorage.removeItem("django.admin.navSidebarIsOpen");
        } */
        /*
        if(clave_eliminar == "django.admin.navSidebarIsOpen"){
            localStorage.removeItem("django.admin.navSidebarIsOpen");
        } */
    }


    for(i = 0; i < localStorage.length; i++){
        let clave = localStorage.key(i);
        let el_valor = localStorage[clave];
        if(clave == cada_producto_id){
            console.log("-----111------")
            console.log(clave);
            console.log(valor);
            valor = el_valor;
            console.log("-----111------")
        }else{
            console.log("no hay coincidencia");
        }   
    }
    Quitar(cada_producto_id, valor);
});

/*-------------------------------------------------------------------------
--------- AGREGAR A PEDIDO TRANSITORIO ------------------------------------
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
            console.log(json[0].idproducto.toString())
            console.log(json[0].cantida.toString())
            localStorage.setItem(json[0].idproducto.toString(), json[0].cantida.toString());
            location.reload();
            console.log("ok++++++++++++++++++++++++")
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
    console.log(cada_producto_id);
    console.log(valor);

    console.log("JSON.stringify(localStorage)");
    console.log(JSON.stringify(localStorage));
    let i;

    for(i = 0; i < localStorage.length; i++){
        let clave_eliminar = localStorage.key(i);
        console.log(typeof clave_eliminar);
        if(!clave_eliminar.startsWith("prestige_")){
            console.log("retorna NO verdadero !!!!!!!!!!!!!");
            localStorage.removeItem(clave_eliminar);
            console.log("retorna NO verdadero !!!!!!!!!!!!!");
        }

        /*
        if(isNaN(clave_eliminar)){
            localStorage.removeItem(i);
        }

        if(clave_eliminar == "django.admin.navSidebarIsOpen"){
            localStorage.removeItem("django.admin.navSidebarIsOpen");
        } */
        /*
        if(clave_eliminar == "django.admin.navSidebarIsOpen"){
            localStorage.removeItem("django.admin.navSidebarIsOpen");
        } */
    }


    for(i = 0; i < localStorage.length; i++){
        let clave = localStorage.key(i);
        let el_valor = localStorage[clave];
        if(clave == cada_producto_id){
            console.log("-----1112------")
            console.log(clave);
            console.log(valor);
            valor = el_valor;
            console.log("-----1112------")
        }else{
            console.log("no hay coincidenciaaaa");
        }   
    }

   Agregar(cada_producto_id, valor);
});

/*-------------------------------------------------------------------------
--------- AGREGAR VALOR INTRODUCIDO EN EL CAMPO .VERVALOR ----------------- 
-------------------------------------------------------------------------*/
function AgregarValor(cada_producto_id, valor) {
    "use strict";
    $.ajax({
        beforeSend : function (xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		url : "/tienda/agregar_valor/",
		type : "GET",
		data : { cada_producto_id:cada_producto_id, valor:valor},
		success : function (json) {
            console.log(json[0].idproducto.toString())
            console.log(json[0].cantida.toString())
            localStorage.setItem(json[0].idproducto.toString(), json[0].cantida.toString());
            location.reload();
            console.log("ok++++++++++++++++++++++++")
		},
		error : function (xhr, errmsg, err) {
			console.log('Error en carga de respuesta');
		}
    });
}

$('.vervalor').focusout(function (event) {
    "use strict";
    event.preventDefault();
    
    let cada_producto_id = $(this).parent().get(0).id;
    let valor = $(this).parent().find('.vervalor').val();
    console.log(cada_producto_id);
    console.log(valor);
 
    console.log("JSON.stringify(localStorage)");
    console.log(JSON.stringify(localStorage));
    let i;

    for(i = 0; i < localStorage.length; i++){
        let clave_eliminar = localStorage.key(i);
        if(!clave_eliminar.startsWith("prestige_")){
            console.log("retorna NO verdadero !!!!!!!!!!!!!");
            localStorage.removeItem(clave_eliminar);
            console.log("retorna NO verdadero !!!!!!!!!!!!!");
        }

        /*
        if(isNaN(clave_eliminar)){
            localStorage.removeItem(i);
        }

        if(clave_eliminar == "django.admin.navSidebarIsOpen"){
            localStorage.removeItem("django.admin.navSidebarIsOpen");
        } */
        /*
        if(clave_eliminar == "django.admin.navSidebarIsOpen"){
            localStorage.removeItem("django.admin.navSidebarIsOpen");
        } */
    }


    for(i = 0; i < localStorage.length; i++){
        let clave = localStorage.key(i);
        //let el_valor = localStorage[clave];
        if(clave == cada_producto_id){
            console.log("-----111------")
            console.log(clave);
            console.log(valor);
            valor = valor;
            console.log("-----111------")
        }else{
            console.log("no hay coincidencia");
        }   
    }
    console.log(cada_producto_id);
    console.log(valor);
   AgregarValor(cada_producto_id, valor);
});
/*-------------------------------------------------------------------------
--------- AGREGAR PRIMER PRODUCTO A PEDIDO TRANSITORIO -------------------- 
-------------------------------------------------------------------------*/
function AgregarI(cada_producto_id, valor) {
    "use strict";
    console.log("------aaaa-----")
    console.log(cada_producto_id);
    console.log(valor);
    console.log("------bbbb-----")
    
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
            console.log(json[0].idproducto.toString())
            console.log(json[0].cantida.toString())
            localStorage.setItem(json[0].idproducto.toString(), json[0].cantida.toString());

            for(i = 0; i < localStorage.length; i++){
                let clave = localStorage.key(i);
                let valcp;
                valcp = ".cp_" + clave.toString()
                $( valcp ).attr("disabled", true);
              }

            console.log("ok++++++++++++++++++++++++")
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
    console.log("JSON.stringify(localStorage)");
    console.log(JSON.stringify(localStorage));
    let i;

    for(i = 0; i < localStorage.length; i++){
        let clave_eliminar = localStorage.key(i);
        console.log("bbbbbbbb");
        console.log(typeof clave_eliminar);
        console.log(clave_eliminar);
        if(!clave_eliminar.startsWith("prestige_")){
            console.log("retorna NO verdadero !!!!!!!!!!!!!");
            localStorage.removeItem(clave_eliminar);
            console.log("retorna NO verdadero !!!!!!!!!!!!!");
        }

        /*
        if(isNaN(clave_eliminar)){
            localStorage.removeItem(i);
        }

        if(clave_eliminar == "django.admin.navSidebarIsOpen"){
            localStorage.removeItem("django.admin.navSidebarIsOpen");
        } */
    }
    for(i = 0; i < localStorage.length; i++){
        let clave = localStorage.key(i);
        let el_valor = localStorage[clave];
        if(clave == cada_producto_id){
            console.log("-----111------")
            console.log(clave);
            console.log(valor);
            valor = el_valor;
            console.log("-----111------")
        }else{
            console.log("no hay coincidencia");
        }   
    }
    console.log("----------s------------------")
    console.log(cada_producto_id)
    console.log(valor)
    console.log("----------s------------------")
   AgregarI(cada_producto_id, valor);
});

function ImprimirProductos(valor) {
    "use strict";
    print(valor);
}

/* 
function Crear(valor) {
    "use strict";
    console.log("valor");
    console.log(valor);
    console.log(typeof(valor));
    console.log("valor");
    var person = {
        "id": "ddddddddddd",
        "cantidad": "ddddddssss",
    }
    $.ajax({
        url: "/crear_localstorage/",
        data:{producto : JSON.stringify(valor)},
        type: 'get',
        dataType: 'json',
        contentType: 'application/json',
        success: function (data) {
            //$('#target').html(data.msg);
        },
        //data: JSON.stringify(person)
    }); 
}
*/
/*-------------------------------------------------------------------------
--------- IR AL CARRITO --------------------------------------------------- 
-------------------------------------------------------------------------*/
$('.boton_carrito').click(function() {
    /*
    $("*").css({
    "background-color": "blue",
    "font-weight": "bolder"
    
    });
    */
    console.log("JSON.stringify(localStorage)");
    console.log(JSON.stringify(localStorage));
    console.log("JSON.stringify(localStorage)");
    for(i = 0; i < localStorage.length; i++){
        let clave_eliminar = localStorage.key(i);
        if(!clave_eliminar.startsWith("prestige_")){
            console.log("retorna NO verdadero !!!!!!!!!!!!!");
            localStorage.removeItem(clave_eliminar);
            console.log("retorna NO verdadero !!!!!!!!!!!!!");
        }

        /*
        if(isNaN(clave_eliminar)){
            localStorage.removeItem(i);
        }

        if(clave_eliminar == "django.admin.navSidebarIsOpen"){
            localStorage.removeItem("django.admin.navSidebarIsOpen");
        } */
        /*
        if(clave_eliminar == "django.admin.navSidebarIsOpen"){
            localStorage.removeItem("django.admin.navSidebarIsOpen");
        } */
    }

    $.ajax({
        url: "/tienda/crear_localstorage/",
        data:{producto : JSON.stringify(localStorage)},
        type: 'get',
        dataType: 'json',
        contentType: 'application/json',
        success: function (data) {
            var urla = window.location.origin + "/carrito";    
            //var urla = "http://127.0.0.1:8000/"+ "panel/carrito";

            window.location.href = urla;
        },
        //data: JSON.stringify(person)
    });

  });

/*-------------------------------------------------------------------------
--------- FINALIZAR COMPRA  ----------------------------------------------- 
------------------------------------------------------------------------- 
   
/*-------------------------------------------------------------------------
--------- AGRUPAR PRODUCTOS ----------------------------------------------- 
-------------------------------------------------------------------------*/
  function agruparfunc(mi_lista){
      "use strict";
      let valParam = JSON.stringify(mi_lista);
      $.ajax({
          beforeSend : function (xhr, settings) {
              if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                  xhr.setRequestHeader("X-CSRFToken", csrftoken);
              }
          },
          url : "/tienda/agrupar_productos_admin/",
          type : "GET",
          data: { mi_lista: valParam} ,
          contentType: 'application/json; charset=utf-8',
          success : function (json) {
            var urla = window.location.origin + "/admin/productos/producto";
            window.location.href = urla;
              console.log("ok++++++++++++++++++++++++")
          },
          error : function (xhr, errmsg, err) {
              console.log('Error en carga de respuesta');
          }
      });
  }

/* *************************************************************
* Borrar producto del carrito
************************************************************** */


$('.eliminar_producto').click(function (event) {
    "use strict";
    let cada_producto_id = $(this).attr('id');
    console.log("!!!2222!!!!");
    console.log(cada_producto_id);
    cada_producto_id = cada_producto_id.replace(/^el/, "prestige_"); 
    console.log(cada_producto_id);
    console.log("JSON.stringify(localStorage)");
    console.log(JSON.stringify(localStorage));

    let i;

    for(i = 0; i < localStorage.length; i++){
        let clave_eliminar = localStorage.key(i);
        if(!clave_eliminar.startsWith("prestige_")){
            console.log("retorna NO verdadero !!!!!!!!!!!!!");
            localStorage.removeItem(clave_eliminar);
            console.log("retorna NO verdadero !!!!!!!!!!!!!");
        }

        /*
        if(isNaN(clave_eliminar)){
            localStorage.removeItem(i);
        }

        if(clave_eliminar == "django.admin.navSidebarIsOpen"){
            localStorage.removeItem("django.admin.navSidebarIsOpen");
        } */
        /*
        if(clave_eliminar == "django.admin.navSidebarIsOpen"){
            localStorage.removeItem("django.admin.navSidebarIsOpen");
        } */
    }


 
    localStorage.removeItem(cada_producto_id);
                console.log(JSON.stringify(localStorage));
                console.log("JSON.stringify(localStorage)");
                $.ajax({
                    url: "/tienda/crear_localstorage/",
                    data:{producto : JSON.stringify(localStorage)},
                    type: 'get',
                    dataType: 'json',
                    contentType: 'application/json',
                    success: function (data) {
                        
                    var urla = window.location.origin + "/carrito";    
                    //var urla = "http://127.0.0.1:8000/"+ "panel/carrito";
                        window.location.href = urla;
                    },
                    //data: JSON.stringify(person)
                });
 
});


/* *****************************************************************
* ACTUALIZAR CLAVE MAYORISTA
******************************************************************/
function CambiarClave(clave) {
    "use strict";
    $.ajax({
        beforeSend : function (xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		url : "/panel/actualizar_clave/",
		type : "GET",
		data : {clave:clave},
		success : function (json) {
            $('#resulado_actualizar_clave').html("<p>La clave fue actualizada correctamente a: <span style='font-size:20px; color:yellow;'>" + json[0].clave + "</span></p>");
            location.reload();
            console.log("ok -----------")
		},
		error : function (xhr, errmsg, err) {
			console.log('Error en carga de respuesta');
		}
    });
}
$('#actualizar_c').focusout(function (event) {
    "use strict";
    let clave = $(this).val();
    console.log(clave);

    CambiarClave(clave);
});
$('#actualizar_c2').focusout(function (event) {
    "use strict";
    let clave = $(this).val();
    console.log(clave);

    CambiarClave(clave);
});
/* *****************************************************************
* Checkout
******************************************************************/