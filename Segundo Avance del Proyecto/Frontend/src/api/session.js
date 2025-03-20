document.addEventListener("DOMContentLoaded", () => {
    verificarSesion();
});

async function verificarSesion() {
    console.log("🔍 Verificando sesión...");

    try {
        const response = await fetch("http://127.0.0.1:8000/api/usuario_info/", {
            method: "GET",
            credentials: "include"
        });

        if (!response.ok) {
            console.warn("⚠ No autenticado. Código:", response.status);
            throw new Error("No autenticado");
        }

        const data = await response.json();
        console.log("✅ Usuario autenticado:", data);

        localStorage.setItem("user", JSON.stringify(data));

    } catch (error) {

        if (!navigator.onLine) {
            console.warn("⚠ Sin conexión a internet, manteniendo sesión.");
            return;
        }

        console.warn("⚠ Usuario no autenticado, redirigiendo a login...");
        localStorage.removeItem("user");

        setTimeout(() => {
            window.location.href = "login.html";
        }, 500);
    }
}
