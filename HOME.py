import streamlit as st
import PIL.Image
st.set_page_config(page_icon='🏏',page_title='PSL SCORE PREDICTOR',layout='wide',initial_sidebar_state='expanded')
img=PIL.Image.open('F:\project\PSL\OIP.jfif')
st.image(img)
st.markdown("<h1 style='text-align: center;'>WELCOME TO PSL SCORE PREDICTOR</h1>",unsafe_allow_html=True)
st.markdown('<p>Your go-to tool for forecasting the outcomes of Pakistan Super League (PSL) matches! Leveraging advanced machine learning techniques, this predictor has been meticulously trained on a comprehensive dataset spanning PSL matches from 2016 to 2023. Our sophisticated model analyzes historical match data to provide insightful predictions on match scores, giving fans and analysts a unique edge in anticipating game results. Whether you are a passionate cricket fan or a strategic analyst, our predictor offers data-driven insights to enhance your PSL experience. Explore the future of cricket analytics with us and stay ahead of the game!</p> ',unsafe_allow_html=True)
st.markdown("<h2>About Algorithm</h2>",unsafe_allow_html=True)
st.markdown("<p>The accuracy of our predictor is a testament to its robust design and the quality of the data it processes. By continuously refining our models and incorporating the latest match data, we strive to offer predictions that are not only insightful but also reliable. While no model can guarantee 100% accuracy due to the inherent unpredictability of sports, our predictor is designed to provide you with a high level of precision, enhancing your ability to forecast match score.</p>",unsafe_allow_html=True)
