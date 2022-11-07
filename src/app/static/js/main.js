function miembrosGrupo(){
    var numeromiembros = document.getElementById("numero_miembros").value;
    // Si en select es uno aparece el input de nombre
    if (numeromiembros == 1){
        document.getElementById("miembros_grupo_1").style.display = "block";
        document.getElementById("miembros_grupo_2").style.display = "none";
        document.getElementById("miembros_grupo_3").style.display = "none";

        document.getElementById("miembros_grupo_2").disabled = true;
        document.getElementById("miembros_grupo_3").disabled = true;
    }
    // Si en select es dos aparecen los dos inputs de nombre
    else if (numeromiembros == 2){
        document.getElementById("miembros_grupo_1").style.display = "block";
        document.getElementById("miembros_grupo_2").style.display = "block";
        document.getElementById("miembros_grupo_3").style.display = "none";
        document.getElementById("miembros_grupo_2").disabled = false;
        document.getElementById("miembros_grupo_3").disabled = true;
    }
    // Si en select es tres aparecen los tres inputs de nombre
    else if (numeromiembros == 3){
        document.getElementById("miembros_grupo_3").style.display = "block";
        document.getElementById("miembros_grupo_1").style.display = "block";
        document.getElementById("miembros_grupo_2").style.display = "block";
        document.getElementById("miembros_grupo_3").disabled = false;
    } 
}
window.addEventListener('load', function() {
    if (typeof web3 !== 'undefined') {
        console.log("Web3 fallando"+ web3.currentProvider.constructor.name);
        window.web3 = new Web3(Web3.currentProvider);
    }else{
        console.log("Web3 exitoso");
        //url=this.prompt("Ingrese la direccion del servidor");
        window.web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
        // window.web3 = new Web3(new Web3.providers.HttpProvider("localhost:8545"));
    }
})

function decryptInput(hash_doc){
    return web3.utils.hexToUtf8(hash_doc);
}

function establcerSrc(hash_decrypt) {
    // establecer src con el hash_doc
    const ulr_ipfs="http://localhost:8080/ipfs/"+hash_decrypt;
    window.open(ulr_ipfs);
}
// Esta función imp
function imprimir_resultado_observacion(id, hash_doc){
    var parrafo=document.getElementById("observacion-"+id);
    // crear un nodo hijo de tipo parrafo
    var nodo=document.createElement("p");
    // crear un nodo hijo de tipo texto
    var texto=document.createTextNode(decryptInput(hash_doc));
    // agregar el nodo hijo de tipo texto al nodo hijo de tipo parrafo
    nodo.appendChild(texto);
    // agregar el nodo hijo de tipo parrafo al nodo padre
    parrafo.appendChild(nodo);
    // Una vez que se imprime la observación se deshabilita el botón de observación
    document.getElementById("boton-"+id).disabled = true;
}
function imprimir_resultado_calificacion(id, hash_doc){
    var parrafo=document.getElementById("calificacion-"+id);
    // crear un nodo hijo de tipo parrafo
    var nodo=document.createElement("p");
    // crear un nodo hijo de tipo texto
    var texto=document.createTextNode(decryptInput(hash_doc));
    // agregar el nodo hijo de tipo texto al nodo hijo de tipo parrafo
    nodo.appendChild(texto);
    // agregar el nodo hijo de tipo parrafo al nodo padre
    parrafo.appendChild(nodo);
}