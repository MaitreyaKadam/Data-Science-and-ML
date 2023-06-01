import streamlit as st
import pandas as pd
from collections.abc import Mapping
import pickle

# Load the diabetes model
model = pickle.load(open('mobile.pkl', 'rb'))

# Load the diabetes data
mobile_data = pd.read_csv('train (1).csv')

# Define the feature columns for the model
feature_cols = ['battery_power','blue','clock_speed','dual_sim','fc','four_g','int_memory','m_dep','mobile_wt','n_cores','pc','px_height','px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi']

# Define a function to make the prediction


def predict_diabetes(batterypower,blue,clockspeed,dualsim,fc,fourg,intmemory,mdep,mobilewt,ncores,pc,pxheight,pxwidth,ram,sch,scw,talktime,threeg,touchscreen,wifi):
    features = [batterypower,blue,clockspeed,dualsim,fc,fourg,intmemory,mdep,mobilewt,ncores,pc,pxheight,pxwidth,ram,sch,scw,talktime,threeg,touchscreen,wifi]
    if st.button("Predict"):
        prediction = model.predict([features])[0]
        if prediction == 0:
            return '0'
        elif prediction == 1:
            return '1'
        elif prediction == 2:
            return "2"
        else:
            return '3'

# Define the Streamlit app
def app():
    # Set the app title
    st.title('SmartPhone Price Classification')

    # Add some explanation about the app
    st.write('This app predicts what should be the price range of a smartphone based on its specifications')

    # Create sliders for the input features
    batterypower = st.slider('Battery Power', 0, 3000, 10,1)
    blue = st.slider('Bluetooth', 0, 1, 0)
    clockspeed = st.slider('Clock Speed', 0.0, 5.0, 0.0, 0.1)
    dualsim = st.slider('Dual Sim', 0, 1, 0)
    fc = st.slider('Front Camera Pixels', 0.0, 30.0, 0.0, 0.5)
    fourg = st.slider('Has 4G or Not', 0, 1, 0)
    intmemory = st.slider('Internal Memory in GB', 0, 128, 0, 1)
    mdep = st.slider('Mobile Dept in cm', 0.0, 1.0, 0.0, 0.1)
    mobilewt = st.slider('Weight of Mobile', 0, 300, 0, 1)
    ncores = st.slider('No of Cores of Processor', 0, 10, 0, 1)
    pc = st.slider('Primary Camera Megapixels', 0, 500, 0, 1)
    pxheight = st.slider('Pixel Resolution Height', 0, 3000, 0, 1)
    pxwidth =  st.slider('Pixel Resolution Width',0, 3000, 0, 1)
    ram = st.slider('Random Access Memory in MB', 0, 5000, 0, 100)  
    sch = st.slider('Screen Height of Mobile in cm', 0, 30, 0, 1)
    scw = st.slider('Screen Width of Mobile in cm', 0, 30, 0, 1)
    talktime = st.slider('Time that a single battery charge will last', 0, 20, 0, 1) 
    threeg = st.slider('Has 3G or Not', 0, 1, 0)
    touchscreen = st.slider('Has TouchScreen or Not', 0, 1, 0)
    wifi = st.slider('Has Wifi or Not', 0, 1, 0)

    # Make the prediction and display the result
    result = predict_diabetes(batterypower,blue,clockspeed,dualsim,fc,fourg,intmemory,mdep,mobilewt,ncores,pc,pxheight,pxwidth,ram,sch,scw,talktime,threeg,touchscreen,wifi)
    st.write(f'The price range is {result}')


if __name__ == '__main__':
    app()
