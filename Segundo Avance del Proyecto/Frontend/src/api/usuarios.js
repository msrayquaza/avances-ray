/* LOGICA DE LA VISTA USUARIOS */


document.addEventListener("DOMContentLoaded", () => {
    cargarUsuarios();
});

async function cargarUsuarios() {
    try {
        const response = await fetch("http://localhost:8000/api/usuarios/", {
            method: "GET",
            credentials: "include", 
        });

        if (!response.ok) {
            throw new Error("Error al obtener usuarios");
        }

        const usuarios = await response.json();
        renderizarUsuarios(usuarios);
    } catch (error) {
        console.error("Error al obtener usuarios:", error);
    }
}

function renderizarUsuarios(usuarios) {
    const tbody = document.querySelector("#users-table tbody");
    tbody.innerHTML = ""; 

    usuarios.forEach(usuario => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${usuario.id_usuario}</td>
            <td>${usuario.nombre}</td>
            <td>${usuario.correo}</td>
            <td>${usuario.rol}</td>
            <td>${usuario.activo ? 'Activo' : 'Inactivo'}</td>
            <td><img src="${usuario.imagen_perfil || 'default.png'}" width="40" height="40"></td>
        `;
        tbody.appendChild(row);
    });
}

document.getElementById("users-table").addEventListener("reload", cargarUsuarios);
