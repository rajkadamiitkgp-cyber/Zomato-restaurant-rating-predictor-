import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))
le = pickle.load(open('le_location.pkl', 'rb'))

st.title('🍽️ Zomato Restaurant Success Predictor')
st.subheader('Predict your restaurant rating before you launch!')

# Input fields
online_order = st.selectbox('Online Order Available?', ['Yes', 'No'])
book_table = st.selectbox('Table Booking Available?', ['Yes', 'No'])
votes = st.number_input('Expected Votes', min_value=0, value=100)
cost = st.number_input('Approximate Cost for 2 People (INR)', min_value=0, value=500)
cuisine_count = st.slider('Number of Cuisines Offered', 1, 10, 3)

# Predict button
if st.button('Predict Rating'):
    online_order = 1 if online_order == 'Yes' else 0
    book_table = 1 if book_table == 'Yes' else 0
    
    input_data = np.array([[online_order, book_table, 0, 0, cost, votes, cuisine_count]])
    prediction = model.predict(input_data)[0]
    
    st.success(f'⭐ Predicted Rating: {prediction:.2f} / 5.0')
    
    if prediction >= 4.0:
        st.balloons()
        st.write('Excellent! Your restaurant is likely to be a hit!')
    elif prediction >= 3.5:
        st.write(' Good! Your restaurant has decent prospects!')
    else:
        st.write('Average! Consider improving your offerings!')