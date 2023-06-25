
import quart
import quart_cors
from quart import request, send_file, jsonify, send_from_directory
from utils import create_presentation_new
import os

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

# Directory to store generated presentations
PRESENTATION_DIR = "./presentations"
TEMPLATE_DIR = "./templates"

@app.post("/presentation/link")
async def presentation_link_new():
    slide_data = (await request.get_json())['slide_data']
    presentation_file = create_presentation_new(slide_data, PRESENTATION_DIR)
    print(presentation_file)
    
    # Generate a unique download link for the file
    download_link = f"http://{request.host}/presentation/download/{os.path.basename(presentation_file)}"
    return jsonify({"download_link": download_link})

@app.get('/presentation/download/<presentation_id>')
async def presentation_download(presentation_id):
    # Serve the file from the presentations directory
    return await send_from_directory(PRESENTATION_DIR, presentation_id, as_attachment=True)

# create and endpoint to get the template
@app.get('/templates/<template_id>')
async def template_download(template_id):
    # Serve the file from the presentations directory
    return await send_from_directory(TEMPLATE_DIR, template_id, as_attachment=True)

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
