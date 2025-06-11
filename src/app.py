"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

def get_http_code(body):
    if not body:
        return 400
    else:
        return 200

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_get_members():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    return jsonify(members),201


    return jsonify(response_body), 200
@app.route('/member', methods=['POST'])
@app.route('/members', methods=['POST'])
def handle_add_member():
    # this is how you can use the Family datastructure by calling its methods
    request_body = request.json
    response_body=jackson_family.add_member(request_body)
    return jsonify(response_body),get_http_code(response_body)

@app.route('/member/<int:member_id>', methods=['GET'])
@app.route('/members/<int:member_id>', methods=['GET'])
def handle_get_member(member_id):
    # this is how you can use the Family datastructure by calling its methods
    response_body = jackson_family.get_member(member_id)
    return jsonify(response_body),get_http_code(response_body)

@app.route('/member/<int:member_id>', methods=['DELETE'])
@app.route('/members/<int:member_id>', methods=['DELETE'])
def handle_delete_member(member_id):
    # this is how you can use the Family datastructure by calling its methods
    response_body = jackson_family.delete_member(member_id)
    return jsonify(response_body),get_http_code(response_body)
    

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
