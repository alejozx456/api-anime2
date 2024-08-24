from flask import Flask, jsonify, request
from flask_cors import CORS
from animeflv import AnimeFLV
with AnimeFLV() as api:
    # Do anything with api object
   ...

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search_anime():
    data = request.get_json()  # Obtiene el cuerpo de la solicitud en formato JSON
    if not data or 'query' not in data:
        return jsonify({'error': 'No query provided'}), 400
    
    query = data['query']  # Obtiene el valor de 'query' del JSON
    results = api.search(query)
    return jsonify(results)




@app.route('/title', methods=['POST'])
def title_anime():
    data = request.get_json()  # Obtiene el cuerpo de la solicitud en formato JSON
    if not data or 'query' not in data:
        return jsonify({'error': 'No query provided'}), 400
    
    query = data['query']  # Obtiene el valor de 'query' del JSON
    results = api.get_anime_info(query)
    return jsonify(results)


@app.route('/links', methods=['POST'])
def links_anime():
    data = request.get_json()  # Obtiene el cuerpo de la solicitud en formato JSON
    if not data or 'serie' not in data or 'episodio' not in data:
        return jsonify({'error': 'No query provided'}), 400
    
    serie = data['serie']
    episodio = data['episodio']  # Obtiene el valor de 'query' del JSON
    results = api.get_links(serie,episodio)
    # results=api.get_video_servers(serie,episodio)
    return jsonify(results)

@app.route('/servers', methods=['POST'])
def servers_anime():
    data = request.get_json()  # Obtiene el cuerpo de la solicitud en formato JSON
    if not data or 'serie' not in data or 'episodio' not in data:
        return jsonify({'error': 'No query provided'}), 400
    
    serie = data['serie']
    episodio = data['episodio']  # Obtiene el valor de 'query' del JSON
    # results = api.get_links(serie,episodio)
    results=api.get_video_servers(serie,episodio)
    return jsonify(results)



if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)




