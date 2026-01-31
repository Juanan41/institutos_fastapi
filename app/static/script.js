const API = "http://127.0.0.1:8000/api/v1";

async function cargarInstitutos() {
  const res = await fetch(`${API}/institutos`);
  const data = await res.json();

  const ul = document.getElementById("listaInstitutos");
  ul.innerHTML = "";

  data.forEach(inst => {
    const li = document.createElement("li");
    li.className = "list-group-item";
    li.innerHTML = `<b>${inst.nombre}</b> - ${inst.codigo_instituto}`;
    ul.appendChild(li);
  });
}

async function cargarEstudiantes() {
  const res = await fetch(`${API}/estudiantes`);
  const data = await res.json();

  const ul = document.getElementById("listaEstudiantes");
  ul.innerHTML = "";

  data.forEach(est => {
    const li = document.createElement("li");
    li.className = "list-group-item";
    li.innerHTML = `<b>${est.nombre} ${est.apellidos}</b> - DNI: ${est.dni}`;
    ul.appendChild(li);
  });
}
