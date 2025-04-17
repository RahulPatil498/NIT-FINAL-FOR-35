from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/normalize', methods=['POST'])
def normalize():
    try:
        data = request.get_json()
        a = [float(x.strip()) for x in data['a'].split(',') if x.strip()]
        t = float(data['t'])
        coe = [float(x.strip()) for x in data['tn'].split(',') if x.strip()]  # renamed tn to coe (for clarity)

        if len(a) != 100 or len(coe) != 100:
            return jsonify({'error': 'Both "a" and "coe" must contain exactly 100 float values.'})

        tn = 35 - t
        fin = [round(a[i] - (coe[i] * tn), 4) for i in range(100)]

        return jsonify({'cv': ", ".join(str(v) for v in fin)})

    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
