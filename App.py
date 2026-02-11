# Importamos Flask y la función render_template
# Flask se usa para crear la aplicación web
from flask import Flask, render_template

# Creamos la aplicación Flask
app = Flask(__name__)

# Ruta principal del sitio (Inicio)
# Esta función se ejecuta cuando el usuario entra a "/"
@app.route('/')
def index():
    # Renderiza la página principal y envía el breadcrumb
    return render_template(
        'index.html',
        breadcrumb=["Inicio"]
    )

# Ruta para la sección de Gestión Ambiental
@app.route('/gestion-ambiental')
def sistema():
    # Muestra la información sobre el Sistema de Gestión Ambiental
    return render_template(
        'sistema.html',
        breadcrumb=["Inicio", "Gestión Ambiental"]
    )

# Ruta para la sección Futuro del Planeta
@app.route('/futuro-planeta')
def futuro():
    # Página que invita a reflexionar sobre las futuras generaciones
    return render_template(
        'futuro.html',
        breadcrumb=["Inicio", "Futuro del Planeta"]
    )

# Ruta para la sección de las 3 R
@app.route('/acciones-verdes')
def tres_r():
    # Explica acciones sencillas para cuidar el medio ambiente
    return render_template(
        'tres_r.html',
        breadcrumb=["Inicio", "Las 3 R"]
    )

# Punto de inicio de la aplicación
# debug=True permite ver errores durante el desarrollo
if __name__ == '__main__':
    app.run(debug=True)
