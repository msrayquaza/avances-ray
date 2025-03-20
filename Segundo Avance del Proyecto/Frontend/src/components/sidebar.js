/* MENU */

function createSidebar() {
    const sidebar = document.createElement("aside");
    sidebar.id = "sidebar";

    sidebar.innerHTML = `
        <h2 class="menu-title">Menú</h2>
        <ul class="sidebar-menu">
            <li class="menu-item"><a href="dashboard.html"><i class="fas fa-home icon"></i> <span>Home</span></a></li>
            <li class="menu-item"><a href="usuarios.html"><i class="fas fa-users icon"></i> <span>Usuarios</span></a></li>
            <li class="menu-item"><a href="#"><i class="fas fa-box icon"></i> <span>Materia P.</span></a></li>
            <li class="menu-item"><a href="#"><i class="fas fa-search icon"></i> <span>Trazabilidad</span></a></li>
            <li class="menu-item"><a href="#"><i class="fas fa-trash icon"></i> <span>Mermas</span></a></li>
            <li class="menu-item"><a href="#"><i class="fas fa-warehouse icon"></i> <span>G. Inventario</span></a></li>
            <li class="menu-item"><a href="#"><i class="fas fa-bell icon"></i> <span>H. Alertas</span></a></li>
        </ul>
    `;

    document.body.prepend(sidebar);
}

createSidebar();
