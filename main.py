import pickle
import streamlit as st
import pandas as pd
import numpy as np

@st.cache(suppress_st_warning=True)
def get_value(val, my_dict):    
    for key, value in my_dict.items():        
        if val == key:            
            return value

# Load model
model = pickle.load(open('model_predicting_player_placement.sav', 'rb'))
app_mode = st.sidebar.selectbox('Select Page', ['Home', 'Prediction'])  # two pages
if app_mode == 'Home':    
    # Title
    st.markdown("<h1 style='text-align: center;'>Predicting Player Placement</h1><br>", unsafe_allow_html=True)

    # Image
    st.image('SC.jpg')

    # Header for Dataset
    st.header("Dataset")

    # Read CSV
    df1 = pd.read_csv('SkillCraft.csv')

    # Display DataFrame
    st.dataframe(df1)

    # Chart for Age
    st.write("Grafik Age")
    chart_age = pd.DataFrame(df1, columns=["Age"])
    st.line_chart(chart_age)

    # Chart for Hours per Week
    st.write("Grafik Hours per Week")
    chart_hours = pd.DataFrame(df1, columns=["HoursPerWeek"])
    st.line_chart(chart_hours)

    # Chart for League Index
    st.write("Grafik Total Map Explores")
    chart_league = pd.DataFrame(df1, columns=["LeagueIndex"])
    st.line_chart(chart_league)

elif app_mode == 'Prediction':    
    st.image('SC.jpg')    

    # Input features
    Age = st.number_input('Age', 0, 10000000)
    HoursPerWeek = st.number_input('Hours PerWeek', 0, 10000000)
    LeagueIndex = st.number_input('League Index', 0, 10000000)

    # Prediction button
    if st.button('Prediksi'):
        player_placement = model.predict([[Age, HoursPerWeek, LeagueIndex]])
        
        # Format and display the prediction
        player_placement_str = np.array(player_placement)
        player_placement_float = float(player_placement_str[0])
        player_placement_formatted = "{:,.2f}".format(player_placement_float)
        
        st.markdown(f'Analisa Penempatan Pemain: {player_placement_formatted}')
