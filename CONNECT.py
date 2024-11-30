from flask import Flask, request, redirect, url_for, render_template, jsonify
import nbformat
import os
import pickle
import json
import numpy as np
app = Flask(__name__)
file_pointer = open('./multi_target_model.pkl','rb')
model = pickle.load(file_pointer)
file_pointer.close()



@app.route('/')
def index():
    return render_template('LEUKEMIA_DETECTION.html')

@app.route('/submit-parameters', methods=['POST'])
def submit_parameters():
    data = request.form.to_dict()
    print(len(data.keys()))
    inp = [float(data[key]) for key in data.keys()]
    prediction = basic_parameter_model(inp)
    return render_template('result.html', prediction=prediction)

@app.route('/upload-image', methods=['POST'])
def upload_image():
    file = request.files['cellImage']
    if file:

        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)

        prediction = ({'image_path': filepath})

        return render_template('result.html', prediction=prediction)
    else:
        return jsonify({"message": "No file uploaded"}), 400

def basic_parameter_model(parameters):
    parameters = np.array(parameters).reshape(1,-1) 
    diagnosis_pred, stage_pred = model.predict(parameters)[0]
    diagnosis_label = "Malignant" if diagnosis_pred == 1 else "Benign"
    return f"Predicted Diagnosis {diagnosis_label} and predicted Cancer Stage{stage_pred}"

def image_model(file_path:str):
    pass

if __name__ == '__main__':
    app.run(debug=True)
