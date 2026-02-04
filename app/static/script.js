// ================================
// ESTUDIANTES
// ================================

function verEstudiante(id){
    alert("Ver estudiante " + id);
}

function editarEstudiante(id){
    if(confirm("¿Editar estudiante " + id + "?")){
        window.location.href = "/estudiantes/editar/" + id;
    }
}

function borrarEstudiante(id){
    if(confirm("¿Seguro que deseas borrar el estudiante " + id + "?")){
        window.location.href = "/estudiantes/borrar/" + id;
    }
}

// ================================
// INSTITUTOS
// ================================

function verInstituto(id){
    alert("Ver instituto " + id);
}

function editarInstituto(id){
    if(confirm("¿Editar instituto " + id + "?")){
        window.location.href = "/institutos/editar/" + id;
    }
}

function borrarInstituto(id){
    if(confirm("¿Seguro que deseas borrar el instituto " + id + "?")){
        window.location.href = "/institutos/borrar/" + id;
    }
}
