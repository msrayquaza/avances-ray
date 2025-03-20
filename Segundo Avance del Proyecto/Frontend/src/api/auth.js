/* AQUI SE MANEJA EL LOGIN Y CREA LA SESION */


document.getElementById("loginForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const correo = document.getElementById("email").value;
    const contraseña = document.getElementById("password").value;

    try {
        const response = await fetch("http://127.0.0.1:8000/api/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            credentials: "include", // Asegura que el navegador reciba la cookie de sesión
            body: JSON.stringify({ correo, contraseña }),
        });

        if (!response.ok) {
            throw new Error("Error en el inicio de sesión");
        }

        const data = await response.json();

        if (data.usuario) {
            localStorage.setItem("user", JSON.stringify(data.usuario));
            console.log("✅ Usuario guardado en localStorage:", data.usuario);
            
            // Esperar brevemente antes de redirigir para asegurar que la cookie se guarde
            setTimeout(() => {
                window.location.href = "dashboard.html";
            }, 500);

        } else {
            console.warn("⚠ No se recibió un usuario en la respuesta del backend.");
        }

    } catch (error) {
        console.error("Error:", error);
        alert("Error: " + error.message);
    }
});
