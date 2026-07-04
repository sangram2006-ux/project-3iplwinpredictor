import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals',
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru',
]

st.set_page_config(page_title='IPL Win Predictor', layout='wide')
st.title('IPL Win Predictor')
st.write('Predict the winner of a chasing IPL innings using the saved model.')

model_path = Path('C:\\Users\\SANGRAM DAS\\OneDrive\\Desktop\\ipl_match_prediction_project\\pipe.pkl')
if not model_path.exists():
    st.error('Model file pipe.pkl not found in the project folder.')
    st.stop()

try:
    pipe = pickle.load(model_path.open('rb'))
except Exception as exc:
    st.error(f'Could not load the model: {exc}')
    st.stop()

with st.form('prediction_form'):
    st.subheader('Match and inning details')

    col1, col2, col3 = st.columns(3)
    with col1:
        batting_team = st.selectbox('Batting team', teams)
        city = st.selectbox('City', cities)
        runs_left = st.number_input('Runs left', min_value=0, value=50, step=1)
    with col2:
        bowling_team = st.selectbox('Bowling team', teams, index=1)
        total_runs_scored = st.number_input('Current batting score', min_value=0, value=100, step=1)
        balls_left = st.number_input('Balls left', min_value=0, value=30, step=1)
    with col3:
        wickets_left = st.number_input('Wickets left', min_value=0, max_value=10, value=7, step=1)
        crr = st.number_input('Current run rate', min_value=0.0, value=6.0, step=0.1, format='%f')
        rrr = st.number_input('Required run rate', min_value=0.0, value=8.0, step=0.1, format='%f')

    submit = st.form_submit_button('Predict winner')

if submit:
    if batting_team == bowling_team:
        st.warning('Batting team and bowling team must be different.')
    else:
        input_data = pd.DataFrame([
            {
                'batting_team': batting_team,
                'bowling_team': bowling_team,
                'city': city,
                'runs_left': runs_left,
                'balls_left': balls_left,
                'wickets_left': wickets_left,
                'total_runs_x': total_runs_scored,
                'crr': crr,
                'rrr': rrr,
            }
        ])

        try:
            probability = pipe.predict_proba(input_data)[0]
            winner_label = batting_team if probability[1] >= probability[0] else bowling_team
            batting_prob = probability[1] * 100
            bowling_prob = probability[0] * 100

            st.success(f'Predicted winner: {winner_label}')
            st.write(f'Batting team win probability: {batting_prob:.1f}%')
            st.write(f'Bowling team win probability: {bowling_prob:.1f}%')
        except Exception as exc:
            st.error(f'Prediction failed: {exc}')
