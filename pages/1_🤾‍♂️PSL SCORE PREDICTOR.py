import streamlit as st
import pandas as pd
import pickle
import time

#@st.cache
st.set_page_config(layout='centered',initial_sidebar_state='expanded')

st.markdown("<h2 style='text-align: center;'>PSL MATCH SCORE PREDICTOR</h2>",unsafe_allow_html=True)
st.markdown("---")
model=pickle.load(open("F:\project\PSL\model",'rb'))

batting=['Multan Sultans',
 'Peshawar Zalmi',
 'Quetta Gladiators',
 'Lahore Qalandars',
 'Karachi Kings',
 'Islamabad United']
bowling=['Lahore Qalandars',
 'Quetta Gladiators',
 'Islamabad United',
 'Karachi Kings',
 'Peshawar Zalmi',
 'Multan Sultans']
venu=['Gaddafi Stadium, Lahore',
 'Rawalpindi Cricket Stadium',
 'Sharjah Cricket Stadium',
 'Dubai International Cricket Stadium',
 'National Stadium, Karachi',
 'Sheikh Zayed Stadium, Abu Dhabi',
 'Multan Cricket Stadium']

st.sidebar.title("Insert Values Below")

bat_team=st.sidebar.selectbox("Select Batting Team",batting)
new=bowling.copy()
new.remove(bat_team)
bowl_team=st.sidebar.selectbox("Select Bowling Team",new)
stadium=st.sidebar.radio("Select Venue",venu)

cur_run=st.number_input("Enter Current Score")
run_rate=st.number_input("Enter Run Rate")

a,b=st.columns(2)
over=a.slider("Over",min_value=5,max_value=19 ,step=1)
player_left=b.slider("Players Left",min_value=10,max_value=1,step=1)

run_five=st.number_input("Enter Runs Made in Five overs")

st.markdown("---")

if st.button("Predict Score"):
    bar=st.progress(0)
    if cur_run<10 or run_five<=10 or run_rate<=0:
        st.warning("Provide Valid Values!")
    else:
        for i in range(100):
            bar.progress(i+1,text='Predictiong...')
            time.sleep(0.01)
            bar.empty()
        colum=['venue', 'batting_team', 'bowling_team', 'Over', 'current_run','run_rate', 'wickets_left', 'run_5_overs']
        pred=pd.DataFrame([[stadium,bat_team,bowl_team,over,cur_run,run_rate,player_left,run_five]],columns=colum)
        result=model.predict(pred)
        st.markdown("#### Predicted Run Score    :   " + str(int(result[0])))
      