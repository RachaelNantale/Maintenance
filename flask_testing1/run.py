from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/users/requests' ,methods= ['POST'])
def create_test():
    return jsonify({'status_code':'lakeli', 'username':'seada'})

@app.route('/users/requests/requestID', methods= ['GET'])
def fetch_request_id():
    return jsonify({'name':'lakeli', 'username':'seada'})
@app.route('/user/requests/requestID' ,methods= ['PUT'])
def modify_request():
    return jsonify({'name':'lakeli', 'username':'seada'})
                

@app.route('/user/requests',methods= ['GET'])
def fetch_all_requests():
    return jsonify({'name':'lakeli', 'username':'seada'})
                
                