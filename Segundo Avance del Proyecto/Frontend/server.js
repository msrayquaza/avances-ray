const express = require("express");
const path = require("path");

const app = express();
const PORT = 5500;

// Servir archivos estáticos desde 'public'
app.use(express.static(path.join(__dirname, "public")));

// Servir estilos y scripts correctamente
app.use("/styles", express.static(path.join(__dirname, "styles")));
app.use("/src", express.static(path.join(__dirname, "src")));

app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
