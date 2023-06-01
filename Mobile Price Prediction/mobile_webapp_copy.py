import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pickle

train_data = pd.read_csv("train (1).csv")
test_data = pd.read_csv("test (2).csv")


# Add a title
st.title("SMARTPHONE PRICE CLASSIFICATION")
# Create a navigation bar
st.sidebar.title('Menu Bar')
selection = st.sidebar.radio("Go to", ('Data Visualisation', 'Prediction', 'Datasets'))

# Render content based on selection
if selection == 'Data Visualisation':
    st.header('Welcome to the Home Page')
    st.write('Here you can go through the visualised data for your understanding')

    # Create jointplot for clock speed and ram
    def create_jointplot(data):
        # Use Seaborn's jointplot
        sns.set_style('whitegrid')
        jointplot = sns.jointplot(x='clock_speed', y='ram', data=train_data,
                                  kind='scatter', hue='price_range', palette='coolwarm')

    # Add interactivity
        ax = jointplot.ax_joint
        ax.figure.set_size_inches(7, 7)
        ax.legend(loc='upper right', title='Price Range')

        return jointplot

    # Display the jointplot in Streamlit
    st.title('Clock Speed Vs Ram')
    jointplot = create_jointplot(train_data)
    st.pyplot(jointplot.fig)

    # Create Jointplot for battery power and ram
    def create_jointplot_2(data):
        # Use Seaborn's jointplot
        sns.set_style('whitegrid')
        jointplot = sns.jointplot(x='battery_power', y='ram', data=train_data,
                                  kind='scatter', hue='price_range', palette='coolwarm')

    # Add interactivity
        ax = jointplot.ax_joint
        ax.figure.set_size_inches(7, 7)
        ax.legend(loc='upper right', title='Price Range')

        return jointplot

# Display the jointplot in Streamlit
    st.title('Battery Power Vs Ram')
    jointplot = create_jointplot_2(train_data)
    st.pyplot(jointplot.fig)

    # Create Histogram of n_cores
    # Create an interactive histogram

    def create_histogram(data):
        fig = px.histogram(data, x='n_cores')
        fig.update_traces(marker=dict(color='yellow'))
        fig.update_layout(
            xaxis=dict(showgrid=True),
            yaxis=dict(showgrid=True),
            bargap=0.1
        )
        return fig

    # Display the interactive histogram in Streamlit
    st.title('Histogram of number of cores')
    fig = create_histogram(train_data)
    st.plotly_chart(fig)

    # Add content for the Home page
elif selection == 'Prediction':
    st.header('Welcome to Prediction Page')
    model = pickle.load(open('mobile.pkl', 'rb'))

    # Define the feature columns for the model
    feature_cols = ['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g', 'int_memory', 'm_dep', 'mobile_wt',
                    'n_cores', 'pc', 'px_height', 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g', 'touch_screen', 'wifi']

    # Define a function to make the prediction
    def predict_diabetes(batterypower, blue, clockspeed, dualsim, fc, fourg, intmemory, mdep, mobilewt, ncores, pc, pxheight, pxwidth, ram, sch, scw, talktime, threeg, touchscreen, wifi):
        features = [batterypower, blue, clockspeed, dualsim, fc, fourg, intmemory, mdep, mobilewt,
                    ncores, pc, pxheight, pxwidth, ram, sch, scw, talktime, threeg, touchscreen, wifi]
        if st.button("Predict"):
            prediction = model.predict([features])[0]
            if prediction == 0:
                return 'low cost'
            elif prediction == 1:
                return 'medium cost'
            elif prediction == 2:
                return "high cost"
            else:
                return 'very high'

    # Define the Streamlit app

    def app():
        # Add some explanation about the app
        st.write(
            'This app predicts what should be the price range of a smartphone based on its specifications')

        # Create sliders for the input features
        batterypower = st.number_input('Battery Power', 0, 3000, 0, 1)
        blue = st.slider('Bluetooth', 0, 1, 0)
        clockspeed = st.number_input('Clock Speed', 0.0, 5.0, 0.0, 0.1)
        dualsim = st.slider('Dual Sim', 0, 1, 0)
        fc = st.number_input('Front Camera Pixels', 0.0, 30.0, 0.0, 0.5)
        fourg = st.slider('Has 4G or Not', 0, 1, 0)
        intmemory = st.number_input('Internal Memory in GB', 0, 128, 0, 1)
        mdep = st.number_input('Mobile Dept in cm', 0.0, 1.0, 0.0, 0.1)
        mobilewt = st.number_input('Weight of Mobile', 0, 300, 0, 1)
        ncores = st.number_input('No of Cores of Processor', 0, 10, 0, 1)
        pc = st.number_input('Primary Camera Megapixels', 0, 500, 0, 1)
        pxheight = st.number_input('Pixel Resolution Height', 0, 3000, 0, 1)
        pxwidth = st.number_input('Pixel Resolution Width', 0, 3000, 0, 1)
        ram = st.number_input('Random Access Memory in MB', 0, 5000, 0, 100)
        sch = st.number_input('Screen Height of Mobile in cm', 0, 30, 0, 1)
        scw = st.number_input('Screen Width of Mobile in cm', 0, 30, 0, 1)
        talktime = st.number_input('Time that a single battery charge will last', 0, 20, 0, 1)
        threeg = st.slider('Has 3G or Not', 0, 1, 0)
        touchscreen = st.slider('Has TouchScreen or Not', 0, 1, 0)
        wifi = st.slider('Has Wifi or Not', 0, 1, 0)

        # Make the prediction and display the result
        result = predict_diabetes(batterypower, blue, clockspeed, dualsim, fc, fourg, intmemory, mdep,
                                  mobilewt, ncores, pc, pxheight, pxwidth, ram, sch, scw, talktime, threeg, touchscreen, wifi)
        st.write(f'The price range should be {result}')
    if __name__ == '__main__':
        app()

    

    # Add content for Page 1
elif selection == 'Datasets':
    st.header('Welcome to DataSet Page')
    st.write("Training Dataset")
    st.write(train_data)
    st.write("Testing Dataset")
    st.write(test_data)

    # Add content for Page 2
