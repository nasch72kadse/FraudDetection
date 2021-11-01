from flask import Flask, request, jsonify
import FraudAPI.fraud_predictor.predictor as predictor
import FraudAPI.fraud_predictor.utils as utils

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'This is a testing API!'})


@app.route('/api/fraud', methods=['GET'])
def get_fraud():
    query_params = request.args
    try:
        parameter_list = {}
        parameter_list["time"] = query_params['time']
        parameter_list["x1"] = query_params['x1']
        parameter_list["x2"] = query_params['x2']
        parameter_list["x3"] = query_params['x3']
        parameter_list["x4"] = query_params['x4']
        parameter_list["x5"] = query_params['x5']
        parameter_list["x6"] = query_params['x6']
        parameter_list["x7"] = query_params['x7']
        parameter_list["x8"] = query_params['x8']
        parameter_list["x9"] = query_params['x9']
        parameter_list["x10"] = query_params['x10']
        parameter_list["x11"] = query_params['x11']
        parameter_list["x12"] = query_params['x12']
        parameter_list["x13"] = query_params['x13']
        parameter_list["x14"] = query_params['x14']
        parameter_list["x15"] = query_params['x15']
        parameter_list["x16"] = query_params['x16']
        parameter_list["x17"] = query_params['x17']
        parameter_list["x18"] = query_params['x18']
        parameter_list["x19"] = query_params['x19']
        parameter_list["x20"] = query_params['x20']
        parameter_list["x21"] = query_params['x21']
        parameter_list["x22"] = query_params['x22']
        parameter_list["x23"] = query_params['x23']
        parameter_list["x24"] = query_params['x24']
        parameter_list["x25"] = query_params['x25']
        parameter_list["x26"] = query_params['x26']
        parameter_list["x27"] = query_params['x27']
        parameter_list["x28"] = query_params['x28']
        parameter_list["amount"] = query_params['amount']
        if parameter_list:
            outcome = predictor.start_predictor(parameter_list)
            return jsonify({outcome})
        else:
            return jsonify({'message': 'Invalid parameters'})
    except:
        return jsonify({'message': 'Invalid parameters'})


app.run()
