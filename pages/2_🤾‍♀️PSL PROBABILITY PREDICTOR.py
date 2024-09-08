import streamlit as st
import pandas as pd 
import pickle 
import time
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

st.set_page_config(layout='wide', initial_sidebar_state='expanded')
algo=pickle.load(open("F:\project\PSL\model_p_de",'rb'))

st.markdown("<h3 style='text-align: center;'>PSL Match Winning Probability Predictor</h3>",unsafe_allow_html=True)
st.markdown("---")
st.sidebar.title('Provide Values Below')
bat_t=st.sidebar.selectbox("Select Batting Team:",batting)
new=bowling.copy()
new.remove(bat_t)
bow_t=st.sidebar.selectbox("Select Bowling Team:",new)
#Toss=st.sidebar.radio("Toss Winner:",[bat_t,bow_t])

ven=st.sidebar.radio("Match is Played at:",venu)
trgt=st.number_input("Target Score:",value=0)
#tr_ov=st.slider('Target Over:',min_value=20,max_value=10,step=1)

col1,col2=st.columns(2)
cur_sc=col1.number_input("Current Score:",value=0)
r_5o=col2.number_input('Current Run Rate:',value=0.0)


ov_left=st.slider("Over :",min_value=5,max_value=19,step=1)
re_run=st.number_input("Required Run:",value=0)


col5,col6=st.columns(2)
req_rr=col5.number_input('Required Run Rate:',value=0.0)
wick=col6.number_input("Wickets Fell:",value=0)

if st.button("Predict Probability"):
    if cur_sc==0 or trgt==0  or req_rr==0:
        st.warning("Please Enter Values")
    elif wick>10 or wick<0 or cur_sc<0 or trgt<50 or req_rr<0:
        st.warning("Given Values are not Valid Values")
    else:
        bar=st.progress(0,text="Predicting Probability........")
        
        for i in range(100):
            bar.progress(i+1,text='Predicting Probability.......')
            time.sleep(0.01)
            bar.empty()
        col=['venue', 'Team', 'Opposition', 'Over Number', 'current_run', 'Wickets','run_5_overs', 'required_run', 'required_run_rate', 'Target Runs']
        inns=[ven,bat_t,bow_t,ov_left,cur_sc,wick,r_5o,re_run,req_rr,trgt]
        inpu=pd.DataFrame([inns],columns=col)
        resul=algo.predict_proba(inpu)
        st.markdown("---")
        u,d=st.columns(2)
        u.markdown('Winning Probability of **{}**  : {}%'.format(bat_t,round((resul[0][1])*100,0)))
        d.markdown('Winning Probability of **{}**  : {}%'.format(bow_t,round((resul[0][0])*100,0)))
        st.markdown("---")