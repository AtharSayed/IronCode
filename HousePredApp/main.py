import streamlit as st 
import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import plotly.express as px

# Generate synthetic house data
def generate_house_data(n_samples=100):
    np.random.seed(50)
    size = np.random.normal(1400, 50, n_samples)
    price = size * 50 + np.random.normal(0, 50, n_samples)
    return pd.DataFrame({"size": size, "price": price})

# Train a linear regression model
def train_model():
    df = generate_house_data(n_samples=100)
    X = df[['size']]
    Y = df[['price']]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, Y_train)
    return model

# Streamlit app
def main():
    st.title("🏡 Simple Linear Regression House Price Prediction App")
    st.write("Enter your house size to estimate its price:")

    # Train the model
    model = train_model()

    # User input
    size = st.number_input('House size (in sq ft)', min_value=500, max_value=2000, value=1500)

    if st.button("Predict Price"):
        predicted_price = model.predict([[size]])[0][0]
        st.success(f"Estimated Price: ${predicted_price:,.2f}")

        # Show scatter plot with prediction
        df = generate_house_data()
        fig = px.scatter(df, x='size', y='price', title='Size vs House Price')
        fig.add_scatter(
            x=[size],
            y=[predicted_price],
            mode='markers',
            marker=dict(size=15, color='red'),
            name='Prediction'
        )
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
