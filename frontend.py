import os
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from sklearn.preprocessing import LabelEncoder
from joblib import load

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}
app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def Results_Decoding(Value)-> np.int8:
    if Value == 0:
        return '<30'
    
    elif Value == 1:
        return '>30'
    
    elif Value == 2:
        return 'None'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
@app.route("/", methods=['GET', 'POST'])
def main_page(name=None):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            df=pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            clf = load(os.path.join(app.config['UPLOAD_FOLDER'], 'filename.joblib'))
            print(df)


            prediction = clf.predict(df)

            y_pred_df = pd.DataFrame(prediction, columns = ['Prediction'])

            df['Prediction'] = y_pred_df.Prediction

            df['Prediction'] = df['Prediction'].apply(Results_Decoding)

            df.to_csv(os.path.join(app.config['UPLOAD_FOLDER'], 'Prediction.csv'), index = False)

            print("Prediction:", prediction)

            return redirect(url_for('download_file', name='Prediction.csv'))
        

    return render_template('index1.html', name=name)

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

if __name__ == '__main__':
    app.run(debug=True)