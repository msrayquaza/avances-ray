console.log("📌 main.js cargado en:", window.location.pathname);

if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/service-worker.js")
        .then(reg => console.log("✅ SW registrado en:", reg.scope))
        .catch(error => console.error("❌ Error al registrar SW:", error));
} else {
    console.warn("⚠ Service Workers no son soportados en este navegador.");
}

document.addEventListener("DOMContentLoaded", () => {
    console.log("📌 DOM completamente cargado en:", window.location.pathname);
});
