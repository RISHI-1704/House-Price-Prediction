<h1>House Price Prediction using KNN algorithm</h1>
This is a Flask-based web application that predicts house prices based on user input features using a machine learning model. The model is trained on an open-source housing dataset and makes predictions based on features like the total area, number of baths, balcony and location.

<h3>Dataset</h3>
<p>The dataset used for training the model is Housing Real Estate Data from Indian Cities</p>
<a href="https://www.kaggle.com/datasets/rakkesharv/real-estate-data-from-7-indian-cities">Link to the dataset</a>  

<h3>Model Implementation</h3>
<p>The model uses K-Nearest Neighbors (KNN) machine learning algorithm to predict house prices based on the input features. Here's a brief overview of the steps involved:</p>

<h4>1. Data Preprocessing:</h4>
<ul>
  <li>Handled missing values in the dataset.</li>
  <li>Scaled the data using StandardScaler to ensure all input features have the same scale.</li>
</ul>

<h4>2. Model Selection:</h4>
<ul>
  <li>Chose the KNN machine learning algorithm.</li>
  <li>The model considers that property prices might be influenced by the cities they are located in, which makes KNN suitable due to its ability to consider similarity between data points.</li>
</ul>

<h4>3. Training the model:</h4>
<ul>
  <li>The model was trained using the train-test split method (80% training, 20% testing).</li>
</ul>

<h4>4. Prediction:</h4>
<ul>
  <li>The Flask web application accepts user input (e.g., total area, number of baths, balcony, city), and the model predicts house prices based on the trained KNN algorithm.</li>
</ul>

<h3>Example Outputs</h3>
![input1](https://github.com/user-attachments/assets/38f2058d-d598-4267-870c-0d034f23c25a)
<h4>Input</h4>
<ul>
  <li>Total Area: 900 sq ft</li>
  <li>Number of Baths: 3</li>
  <li>Balcony: Yes</li>
  <li>City: Mumbai</li>
</ul>
<h4>Output</h4>
![image](https://github.com/user-attachments/assets/ab9bde05-9ea1-4e2c-9068-72e0d26a90a3)

<b>Based on your inputs the predicted price is ₹1.79 Crore</b>
