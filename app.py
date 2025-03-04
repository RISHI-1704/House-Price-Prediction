from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained KNN model and scaler
knn = pickle.load(open("knn_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

cities = ['City_Bangalore', 'City_Chennai', 'City_Hyderabad', 'City_Kolkata', 'City_Mumbai', 'City_New Delhi', 'City_Pune', 'City_Thane']

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get the values from the form
        total_area = float(request.form['area'])
        baths = int(request.form['baths'])
        balcony = 1 if request.form['balcony'] == "Yes" else 0
        city = request.form['city']
        city = city.capitalize()  # Capitalizes the first letter of the city name
        
        city_encoded = [0] * len(cities)  # Initialize all city features to 0
        
        city_index = cities.index(f"City_{city}")
        city_encoded[city_index] = 1  # Set the selected city to 1
        
        features = np.array([total_area, baths, balcony] + city_encoded).reshape(1, -1)

        # Scale the features before prediction using the loaded scaler
        scaled_features = scaler.transform(features)

        # Predicting the values using KNN algorithm
        prediction = knn.predict(scaled_features)

        # Converting the price to display the user
        predicted_price = prediction[0]
        if predicted_price >= 100:
            predicted_price_crore = predicted_price / 100
            output = f"Based on your inputs the predicted price is ₹{predicted_price_crore:.2f} Crore"
        else:
            output = f"Based on your inputs the predicted price is ₹{predicted_price:.2f} Lakh"

        # Return the result to the template
        return render_template('index.html', output=output)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
