from flask import Flask, jsonify, request
from module.similitudes import calcular_similitud_archivo

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():  
    return "<p>Hello, World!</p>"

@app.route('/upload', methods=['POST'])
def upload_file():
    # Verificar si el archivo está en la solicitud
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    filetyp = file.filename.split('.')

    # Verificar si el archivo tiene nombre y está presente
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400

    if file:
        # Aquí puedes hacer lo que necesites con el archivo
        # Ejemplo: Guardar el archivo en el servidor o procesarlo directamente
        # file.save(os.path.join("/path/to/save", file.filename))
        if filetyp[-1] == 'pdf':
            filetyp = 'PDF'
        elif filetyp[-1] == 'doc' or filetyp[-1] == 'docx':
            filetyp = 'DOCX'
        else:
            return jsonify({"error":"No se aceptan archivos distintos a .pdf o .docx"})
        results = calcular_similitud_archivo(filetyp, file)


        # Procesamiento del archivo
        file_content = file.read()  # Leer contenido del archivo
        # Haz lo que necesites con file_content

        # Retornar alguna información
        return results

if __name__ == "__main__":
    app.run(debug=True)
