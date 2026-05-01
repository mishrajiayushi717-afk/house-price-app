import pickle
import streamlit as st
import numpy as np
model = pickle.load(open('model.pkl', 'rb'))
#st.error("Model file not found. Please check the file path.")
st.title('House Price Prediction')
sqft = st.number_input("SqFt Area", min_value=0.0)
bed = st.number_input("Bedrooms", min_value=0.0)
bath = st.number_input("Bathrooms", min_value=0.0)
nb = st.number_input("Neighborhood", options = [0,1,],help="0 for Area A,1 for Area B")

if st.button("predict Price"):
  data = np.array([[sqft,bed,bath,nb]])
  prediction = model.predict(data)
  st.success('Predicted Price: {}'.format(prediction))
