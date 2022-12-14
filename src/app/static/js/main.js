function miembrosGrupo() {
    var numeromiembros = document.getElementById("numero_miembros").value;
    // Si en select es uno aparece el input de nombre
    if (numeromiembros == 1) {
        document.getElementById("miembros_grupo_1").style.display = "block";
        document.getElementById("miembros_grupo_2").style.display = "none";
        document.getElementById("miembros_grupo_3").style.display = "none";

        document.getElementById("miembros_grupo_2").disabled = true;
        document.getElementById("miembros_grupo_3").disabled = true;
    }
    // Si en select es dos aparecen los dos inputs de nombre
    else if (numeromiembros == 2) {
        document.getElementById("miembros_grupo_1").style.display = "block";
        document.getElementById("miembros_grupo_2").style.display = "block";
        document.getElementById("miembros_grupo_3").style.display = "none";
        document.getElementById("miembros_grupo_2").disabled = false;
        document.getElementById("miembros_grupo_3").disabled = true;
    }
    // Si en select es tres aparecen los tres inputs de nombre
    else if (numeromiembros == 3) {
        document.getElementById("miembros_grupo_3").style.display = "block";
        document.getElementById("miembros_grupo_1").style.display = "block";
        document.getElementById("miembros_grupo_2").style.display = "block";
        document.getElementById("miembros_grupo_3").disabled = false;
    }
}
function numero_jurados_ciclo() {
    numero_integrantes = document.getElementById("num_jurados").value;
    if (numero_integrantes == 1) {
        document.getElementById("jurado_uno").style.display = "block";
        document.getElementById("jurado_dos").style.display = "none";
        document.getElementById("jurado_tres").style.display = "none";
        document.getElementById("jurado_cuatro").style.display = "none";
        document.getElementById("jurado_cinco").style.display = "none";
        
        document.getElementById("jurado_dos").disabled = true;
        document.getElementById("jurado_tres").disabled = true;
        document.getElementById("jurado_cuatro").disabled = true;
        document.getElementById("jurado_cinco").disabled = true;
    }else if (numero_integrantes == 2) {
        document.getElementById("jurado_uno").style.display = "block";
        document.getElementById("jurado_dos").style.display = "block";
        document.getElementById("jurado_tres").style.display = "none";
        document.getElementById("jurado_cuatro").style.display = "none";
        document.getElementById("jurado_cinco").style.display = "none";

        document.getElementById("jurado_dos").disabled = false;
        document.getElementById("jurado_tres").disabled = true;
        document.getElementById("jurado_cuatro").disabled = true;
        document.getElementById("jurado_cinco").disabled = true;
    }else if (numero_integrantes == 3) {
        document.getElementById("jurado_uno").style.display = "block";
        document.getElementById("jurado_dos").style.display = "block";
        document.getElementById("jurado_tres").style.display = "block";
        document.getElementById("jurado_cuatro").style.display = "none";
        document.getElementById("jurado_cinco").style.display = "none";

        document.getElementById("jurado_dos").disabled = false;
        document.getElementById("jurado_tres").disabled = false;
        document.getElementById("jurado_cuatro").disabled = true;
        document.getElementById("jurado_cinco").disabled = true;
    }else if (numero_integrantes == 4) {
        document.getElementById("jurado_uno").style.display = "block";
        document.getElementById("jurado_dos").style.display = "block";
        document.getElementById("jurado_tres").style.display = "block";
        document.getElementById("jurado_cuatro").style.display = "block";
        document.getElementById("jurado_cinco").style.display = "none";

        document.getElementById("jurado_dos").disabled = false;
        document.getElementById("jurado_tres").disabled = false;
        document.getElementById("jurado_cuatro").disabled = false;
        document.getElementById("jurado_cinco").disabled = true;
    }else if (numero_integrantes == 5) {
        document.getElementById("jurado_uno").style.display = "block";
        document.getElementById("jurado_dos").style.display = "block";
        document.getElementById("jurado_tres").style.display = "block";
        document.getElementById("jurado_cuatro").style.display = "block";
        document.getElementById("jurado_cinco").style.display = "block";

        document.getElementById("jurado_dos").disabled = false;
        document.getElementById("jurado_tres").disabled = false;
        document.getElementById("jurado_cuatro").disabled = false;
        document.getElementById("jurado_cinco").disabled = false;
    }
}
window.addEventListener('load', function () {
    if (typeof web3 !== 'undefined') {
        console.log("Web3 fallando" + web3.currentProvider.constructor.name);
        window.web3 = new Web3(Web3.currentProvider);
    } else {
        console.log("Web3 exitoso");
        //url=this.prompt("Ingrese la direccion del servidor");
        window.web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
        // window.web3 = new Web3(new Web3.providers.HttpProvider("localhost:8545"));
    }
})

function decryptInput(hash_doc) {
    return web3.utils.hexToUtf8(hash_doc);
}

function establcerSrc(hash_decrypt) {
    // establecer src con el hash_doc
    const ulr_ipfs = "http://192.168.0.19:8080/ipfs/" + hash_decrypt;
    window.open(ulr_ipfs, '_blank','location=0,height=570,width=520,scrollbars=yes,status=yes');
}
// Esta funci??n imp
function imprimir_resultado_observacion(id, hash_doc) {
    var parrafo = document.getElementById("observacion-" + id);
    // crear un nodo hijo de tipo parrafo
    var nodo = document.createElement("p");
    // crear un nodo hijo de tipo texto
    var texto = document.createTextNode(decryptInput(hash_doc));
    // agregar el nodo hijo de tipo texto al nodo hijo de tipo parrafo
    nodo.appendChild(texto);
    // agregar el nodo hijo de tipo parrafo al nodo padre
    parrafo.appendChild(nodo);
    // Una vez que se imprime la observaci??n se deshabilita el bot??n de observaci??n
    document.getElementById("boton-" + id).disabled = true;
}
function imprimir_resultado_calificacion(id, hash_doc) {
    var parrafo = document.getElementById("calificacion-"+id);
    // crear un nodo hijo de tipo parrafo
    var nodo = document.createElement("p");
    // crear un nodo hijo de tipo texto
    var texto = document.createTextNode(decryptInput(hash_doc));
    // agregar el nodo hijo de tipo texto al nodo hijo de tipo parrafo
    nodo.appendChild(texto);
    // agregar el nodo hijo de tipo parrafo al nodo padre
    parrafo.appendChild(nodo);
    // Una vez que se imprime la calificaci??n se deshabilita el bot??n de calificaci??n
    document.getElementById("boton-" + id).disabled = true;
}
/*
Tablas para los modales de profesor

*/
$(document).ready( function () {
    $('#tabla_profe_1').DataTable({
        "aLengthMenu":[[3,5,10,25,-1],[3,5,10,24], "todo"],
        "iDisplayLength":3,
        "language":{
            "lengthMenu": "Mostrar _MENU_ registros por p??gina",
            "search": "Buscar",
            "zeroRecords":"Ning??n Registro Encontrado",
            "info":"P??gina _PAGE_ de _PAGES_",
            "infoEmpty": "Ning??n registro disponible",
            "infoFiltered":"(Filtrado de _MAX_ registro(s) totales)",
            "paginate":{
                "first":"Primero",
                "last":"Ultimo",
                "next":"Siguiente",
                "previous": "Anterior"
            }
        },


    });
} );


    

$(document).ready( function () {
    $('#tabla_profe_2').DataTable({
        "aLengthMenu":[[3,5,10,25,-1],[3,5,10,24], "todo"],
        "iDisplayLength":3,
        "language":{
            "lengthMenu": "Mostrar _MENU_ registros por p??gina",
            "search": "Buscar",
            "zeroRecords":"Ning??n Registro Encontrado",
            "info":"P??gina _PAGE_ de _PAGES_",
            "infoEmpty": "Ning??n registro disponible",
            "infoFiltered":"(Filtrado de _MAX_ registro(s) totales)",
            "paginate":{
                "first":"Primero",
                "last":"Ultimo",
                "next":"Siguiente",
                "previous": "Anterior"
            }
        }
    });
} );
$(document).ready( function () {
    $('#tabla_profe_3').DataTable({
        "aLengthMenu":[[3,5,10,25,-1],[3,5,10,24], "todo"],
        "iDisplayLength":5,
        "language":{
            "lengthMenu": "Mostrar _MENU_ registros por p??gina",
            "search": "Buscar",
            "zeroRecords":"Ning??n Registro Encontrado",
            "info":"P??gina _PAGE_ de _PAGES_",
            "infoEmpty": "Ning??n registro disponible",
            "infoFiltered":"(Filtrado de _MAX_ registro(s) totales)",
            "paginate":{
                "first":"Primero",
                "last":"Ultimo",
                "next":"Siguiente",
                "previous": "Anterior"
            }
        }
    });
} );

/*
Tablas para los modales de administrador

*/

$(document).ready( function () {
    $('#tabla_admin').DataTable({
        "aLengthMenu":[[3,5,10,25,-1],[3,5,10,24], "todo"],
        "iDisplayLength":3,
        "language":{
            "lengthMenu": "Mostrar _MENU_ registros por p??gina",
            "search": "Buscar",
            "zeroRecords":"Ning??n Registro Encontrado",
            "info":"P??gina _PAGE_ de _PAGES_",
            "infoEmpty": "Ning??n registro disponible",
            "infoFiltered":"(Filtrado de _MAX_ registro(s) totales)",
            "paginate":{
                "first":"Primero",
                "last":"Ultimo",
                "next":"Siguiente",
                "previous": "Anterior"
            }
        }
    });
} );
// Tabla proyectos
$(document).ready( function () {
    $('#tabla_proyecto').DataTable({
        "aLengthMenu":[[3,5,10,25,-1],[3,5,10,24], "todo"],
        "iDisplayLength":3,
        "language":{
            "lengthMenu": "Mostrar _MENU_ registros por p??gina",
            "search": "Buscar",
            "zeroRecords":"Ning??n Registro Encontrado",
            "info":"P??gina _PAGE_ de _PAGES_",
            "infoEmpty": "Ning??n registro disponible",
            "infoFiltered":"(Filtrado de _MAX_ registro(s) totales)",
            "paginate":{
                "first":"Primero",
                "last":"Ultimo",
                "next":"Siguiente",
                "previous": "Anterior"
            }
        }
    });
} );


/* Tablas para jurados */
$(document).ready( function () {
    $('#tabla_ciclo_1').DataTable({
        "aLengthMenu":[[3,5,10,25,-1],[3,5,10,24], "todo"],
        "iDisplayLength":3,
        "language":{
            "lengthMenu": "Mostrar _MENU_ registros por p??gina",
            "search": "Buscar",
            "zeroRecords":"Ning??n Registro Encontrado",
            "info":"P??gina _PAGE_ de _PAGES_",
            "infoEmpty": "Ning??n registro disponible",
            "infoFiltered":"(Filtrado de _MAX_ registro(s) totales)",
            "paginate":{
                "first":"Primero",
                "last":"Ultimo",
                "next":"Siguiente",
                "previous": "Anterior"
            }
        }
    });
} );
$(document).ready( function () {
    $('#tabla_ciclo_2').DataTable({
        "aLengthMenu":[[3,5,10,25,-1],[3,5,10,24], "todo"],
        "iDisplayLength":3,
        "language":{
            "lengthMenu": "Mostrar _MENU_ registros por p??gina",
            "search": "Buscar",
            "zeroRecords":"Ning??n Registro Encontrado",
            "info":"P??gina _PAGE_ de _PAGES_",
            "infoEmpty": "Ning??n registro disponible",
            "infoFiltered":"(Filtrado de _MAX_ registro(s) totales)",
            "paginate":{
                "first":"Primero",
                "last":"Ultimo",
                "next":"Siguiente",
                "previous": "Anterior"
            }
        }
    });
} );
$(document).ready( function () {
    $('#tabla_ciclo_3').DataTable({
        "aLengthMenu":[[3,5,10,25,-1],[3,5,10,24], "todo"],
        "iDisplayLength":3,
        "language":{
            "lengthMenu": "Mostrar _MENU_ registros por p??gina",
            "search": "Buscar",
            "zeroRecords":"Ning??n Registro Encontrado",
            "info":"P??gina _PAGE_ de _PAGES_",
            "infoEmpty": "Ning??n registro disponible",
            "infoFiltered":"(Filtrado de _MAX_ registro(s) totales)",
            "paginate":{
                "first":"Primero",
                "last":"Ultimo",
                "next":"Siguiente",
                "previous": "Anterior"
            }
        }
    });
} );
$(document).ready( function () {
    $('#tabla_ciclo_evaluado_1').DataTable({
        "aLengthMenu":[[3,5,10,25,-1],[3,5,10,24], "todo"],
        "iDisplayLength":3,
        "language":{
            "lengthMenu": "Mostrar _MENU_ registros por p??gina",
            "search": "Buscar",
            "zeroRecords":"Ning??n Registro Encontrado",
            "info":"P??gina _PAGE_ de _PAGES_",
            "infoEmpty": "Ning??n registro disponible",
            "infoFiltered":"(Filtrado de _MAX_ registro(s) totales)",
            "paginate":{
                "first":"Primero",
                "last":"Ultimo",
                "next":"Siguiente",
                "previous": "Anterior"
            }
        }
    });
} );
$(document).ready( function () {
    $('#tabla_ciclo_evaluado_2').DataTable({
        "aLengthMenu":[[3,5,10,25,-1],[3,5,10,24], "todo"],
        "iDisplayLength":3,
        "language":{
            "lengthMenu": "Mostrar _MENU_ registros por p??gina",
            "search": "Buscar",
            "zeroRecords":"Ning??n Registro Encontrado",
            "info":"P??gina _PAGE_ de _PAGES_",
            "infoEmpty": "Ning??n registro disponible",
            "infoFiltered":"(Filtrado de _MAX_ registro(s) totales)",
            "paginate":{
                "first":"Primero",
                "last":"Ultimo",
                "next":"Siguiente",
                "previous": "Anterior"
            }
        }
    });
} );
$(document).ready( function () {
    $('#tabla_ciclo_evaluado_3').DataTable({
        "aLengthMenu":[[3,5,10,25,-1],[3,5,10,24], "todo"],
        "iDisplayLength":3,
        "language":{
            "lengthMenu": "Mostrar _MENU_ registros por p??gina",
            "search": "Buscar",
            "zeroRecords":"Ning??n Registro Encontrado",
            "info":"P??gina _PAGE_ de _PAGES_",
            "infoEmpty": "Ning??n registro disponible",
            "infoFiltered":"(Filtrado de _MAX_ registro(s) totales)",
            "paginate":{
                "first":"Primero",
                "last":"Ultimo",
                "next":"Siguiente",
                "previous": "Anterior"
            }
        }
    });
} );

// Funciones para las notas
function nota_1(nota1){
    return web3.utils.hexToUtf8(nota1)
}
function nota_2(nota1, nota2){
    var notas1=parseFloat(web3.utils.hexToUtf8(nota1))
    var notas2=parseFloat(web3.utils.hexToUtf8(nota2))
    var promedio=(notas1+notas2)/2
    // aplicar un decimal format para que solo muestre 2 decimales
    promedio=promedio.toFixed(2)
    return promedio
}
function nota_3(nota1, nota2, nota3){
    var notas1=parseFloat(web3.utils.hexToUtf8(nota1))
    var notas2=parseFloat(web3.utils.hexToUtf8(nota2))
    var notas3=parseFloat(web3.utils.hexToUtf8(nota3))
    var promedio=(notas1+notas2+notas3)/3
    promedio=promedio.toFixed(2)
    return promedio
}
function nota_4(nota1, nota2, nota3, nota4){
    var notas1=parseFloat(web3.utils.hexToUtf8(nota1))
    var notas2=parseFloat(web3.utils.hexToUtf8(nota2))
    var notas3=parseFloat(web3.utils.hexToUtf8(nota3))
    var notas4=parseFloat(web3.utils.hexToUtf8(nota4))
    var promedio=(notas1+notas2+notas3+notas4)/4
    promedio=promedio.toFixed(2)
    return promedio
    

}
function nota_5(nota1, nota2, nota3, nota4, nota5){
    var notas1=parseFloat(web3.utils.hexToUtf8(nota1))
    var notas2=parseFloat(web3.utils.hexToUtf8(nota2))
    var notas3=parseFloat(web3.utils.hexToUtf8(nota3))
    var notas4=parseFloat(web3.utils.hexToUtf8(nota4))
    var notas5=parseFloat(web3.utils.hexToUtf8(nota5))
    var promedio=(notas1+notas2+notas3+notas4+notas5)/5
    promedio=promedio.toFixed(2)
    return promedio
}

function imprimir_promedio_calificacion(id, nota) {
    var parrafo = document.getElementById("calificacion-"+id);
    // crear un nodo hijo de tipo parrafo
    
    var nodo = document.createElement("p");
    // crear un nodo hijo de tipo texto
    var texto = document.createTextNode(nota);
    // agregar el nodo hijo de tipo texto al nodo hijo de tipo parrafo
    nodo.appendChild(texto);
    // agregar el nodo hijo de tipo parrafo al nodo padre
    parrafo.appendChild(nodo);
    // Una vez que se imprime la calificaci??n se deshabilita el bot??n de calificaci??n
    document.getElementById("boton-" + id).disabled = true;
}

function obser_1(nota1){
    return web3.utils.hexToUtf8(nota1)
}
function obser_2(nota1, nota2){
    var notas1=web3.utils.hexToUtf8(nota1)
    var notas2=web3.utils.hexToUtf8(nota2)
    var observacion=notas1+"\n"+notas2
    return observacion
}
function obser_3(nota1, nota2, nota3){
    var notas1=web3.utils.hexToUtf8(nota1)
    var notas2=web3.utils.hexToUtf8(nota2)
    var notas3=web3.utils.hexToUtf8(nota3)
    var observacion=notas1+"\n"+notas2+"\n"+notas3
    return observacion
}
function obser_4(nota1, nota2, nota3, nota4){
    var notas1=web3.utils.hexToUtf8(nota1)
    var notas2=web3.utils.hexToUtf8(nota2)
    var notas3=web3.utils.hexToUtf8(nota3)
    var notas4=web3.utils.hexToUtf8(nota4)
    var observacion=notas1+"\n"+notas2+"\n"+notas3+"\n"+notas4
    return observacion
    

}
function obser_5(nota1, nota2, nota3, nota4, nota5){
    var notas1=web3.utils.hexToUtf8(nota1)
    var notas2=web3.utils.hexToUtf8(nota2)
    var notas3=web3.utils.hexToUtf8(nota3)
    var notas4=web3.utils.hexToUtf8(nota4)
    var notas5=web3.utils.hexToUtf8(nota5)
    var observacion=notas1+"\n"+notas2+"\n"+notas3+"\n"+notas4+"\n"+notas5
    return observacion
}

function imprimir_observaciones(id, obser) {
    var parrafo = document.getElementById("observacion-" + id);
    // crear un nodo hijo de tipo parrafo
    var nodo = document.createElement("p");
    // crear un nodo hijo de tipo texto
    var texto = document.createTextNode(obser);
    // agregar el nodo hijo de tipo texto al nodo hijo de tipo parrafo
    nodo.appendChild(texto);
    // agregar el nodo hijo de tipo parrafo al nodo padre
    parrafo.appendChild(nodo);
    // Una vez que se imprime la observaci??n se deshabilita el bot??n de observaci??n
    document.getElementById("boton-" + id).disabled = true;
}


