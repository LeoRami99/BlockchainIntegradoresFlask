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
    const ulr_ipfs = "http://localhost:8080/ipfs/" + hash_decrypt;
    window.open(ulr_ipfs);
}
// Esta función imp
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
    // Una vez que se imprime la observación se deshabilita el botón de observación
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
    // Una vez que se imprime la calificación se deshabilita el botón de calificación
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
            "lengthMenu": "Mostrar _MENU_ registros por página",
            "search": "Buscar",
            "zeroRecords":"Ningún Registro Encontrado",
            "info":"Página _PAGE_ de _PAGES_",
            "infoEmpty": "Ningún registro disponible",
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
    $('#tabla_profe_2').DataTable({
        "aLengthMenu":[[3,5,10,25,-1],[3,5,10,24], "todo"],
        "iDisplayLength":3,
        "language":{
            "lengthMenu": "Mostrar _MENU_ registros por página",
            "search": "Buscar",
            "zeroRecords":"Ningún Registro Encontrado",
            "info":"Página _PAGE_ de _PAGES_",
            "infoEmpty": "Ningún registro disponible",
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
            "lengthMenu": "Mostrar _MENU_ registros por página",
            "search": "Buscar",
            "zeroRecords":"Ningún Registro Encontrado",
            "info":"Página _PAGE_ de _PAGES_",
            "infoEmpty": "Ningún registro disponible",
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
            "lengthMenu": "Mostrar _MENU_ registros por página",
            "search": "Buscar",
            "zeroRecords":"Ningún Registro Encontrado",
            "info":"Página _PAGE_ de _PAGES_",
            "infoEmpty": "Ningún registro disponible",
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
            "lengthMenu": "Mostrar _MENU_ registros por página",
            "search": "Buscar",
            "zeroRecords":"Ningún Registro Encontrado",
            "info":"Página _PAGE_ de _PAGES_",
            "infoEmpty": "Ningún registro disponible",
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