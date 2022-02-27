from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Chest_Number_Diesel=0
    if request.method == 'POST':
        Age = int(request.form['Age'])
        Weight_Number=float(request.form['Weight_Number'])
        Body_type=int(request.form['Body_type'])
        Body_type2=np.log(Body_type)
        Torso=int(request.form['Torso'])
        Chest_Number_Petrol=request.form['Chest_Number_Petrol']
        if(Chest_Number_Petrol=='Petrol'):
                Chest_Number_Petrol=1
                Chest_Number_Diesel=0
        else:
            Chest_Number_Petrol=0
            Chest_Number_Diesel=1
        Age=2020-Age
        Waist_Number_Individual=request.form['Waist_Number_Individual']
        if(Waist_Number_Individual=='Individual'):
         Waist_Number_Individual=1
        else:
         Waist_Number_Individual=0	
        Hip_Number_Mannual=request.form['Hip_Number_Mannual']
        if(Hip_Number_Mannual=='Mannual'):
           Hip_Number_Mannual=1
        else:
           Hip_Number_Mannual=0
        prediction=model.predict([[Weight_Number,Body_type2,Torso,Age,Chest_Number_Diesel,Chest_Number_Petrol,Waist_Number_Individual,Hip_Number_Mannual]])
        output=round(prediction[0],1)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)

