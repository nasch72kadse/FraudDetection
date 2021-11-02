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
        parameter_list = {"time": query_params['time'], "x1": query_params['x1'], "x2": query_params['x2'],
                          "x3": query_params['x3'], "x4": query_params['x4'], "x5": query_params['x5'],
                          "x6": query_params['x6'], "x7": query_params['x7'], "x8": query_params['x8'],
                          "x9": query_params['x9'], "x10": query_params['x10'], "x11": query_params['x11'],
                          "x12": query_params['x12'], "x13": query_params['x13'], "x14": query_params['x14'],
                          "x15": query_params['x15'], "x16": query_params['x16'], "x17": query_params['x17'],
                          "x18": query_params['x18'], "x19": query_params['x19'], "x20": query_params['x20'],
                          "x21": query_params['x21'], "x22": query_params['x22'], "x23": query_params['x23'],
                          "x24": query_params['x24'], "x25": query_params['x25'], "x26": query_params['x26'],
                          "x27": query_params['x27'], "x28": query_params['x28'], "amount": query_params['amount']}
        if parameter_list:
            outcome = predictor.start_predictor(parameter_list)
            return str(outcome)
        else:
            return jsonify({'message': 'Invalid parameters'})
    except Exception as Ex:
        return jsonify({'message': 'Invalid parameters'})


app.run()
