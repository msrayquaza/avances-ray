/* NABVAR */

async function getUserInfo() {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/usuario_info/", {
            method: "GET",
            credentials: "include"  
        });

        if (!response.ok) {
            throw new Error("No autenticado");
        }

        return await response.json();
    } catch (error) {
        console.error("Usuario no autenticado.");
        return null;
    }
}


async function createNavbar() {
    const user = await getUserInfo();
    const userName = user ? user.nombre : "Invitado";


    let userProfilePic = "img/default-profile.jpg";

    if (user && user.imagen_perfil) {
        userProfilePic = user.imagen_perfil; 
    }

    console.log("Imagen de perfil URL:", userProfilePic); 

    const navbar = document.createElement("nav");
    navbar.id = "navbar";

    navbar.innerHTML = `
        <div class="navbar-container">
            <div class="left-section">
                <button id="menu-toggle" class="menu-toggle">☰</button>
                <div class="logo-container">
                    <img src="img/logo.png" alt="StockQuery Logo" class="logo-img">
                    <span class="logo">StockQuery</span>
                </div>
            </div>
            <div class="user-profile">
                <div class="profile-pic-container">
                    <img src="${userProfilePic}" alt="Usuario" class="profile-pic" onerror="this.src='img/default-profile.jpg'">
                </div>
                <span class="user-text">${userName}</span>
                <button id="logoutBtn" class="logout-btn">Logout</button>
            </div>
        </div>
    `;

    document.body.prepend(navbar);
 

    document.getElementById("logoutBtn").addEventListener("click", async () => {
        await fetch("http://127.0.0.1:8000/api/logout/", { method: "POST", credentials: "include" });
        window.location.href = "login.html";
    });

    document.getElementById("menu-toggle").addEventListener("click", () => {
        document.getElementById("sidebar").classList.toggle("collapsed");
        document.getElementById("app").classList.toggle("expanded");
    });
}

createNavbar();
