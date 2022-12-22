import streamlit as st
import numpy as np

def Input(est_diameter_min, est_diameter_max, relative_velocity,miss_d,magnitude):
    x = est_diameter_min
    y = est_diameter_max
    z = relative_velocity
    zz = miss_d
    zzz = magnitude
    x = np.asarray(x)
    y = np.asarray(y)
    z = np.asarray(z)
    zz = np.asarray(zz)
    zzz = np.asarray(zzz)
    input_data = [[x,y,z,zz,zzz]]
    prediction = RF.predict(input_data)
    # Decision Maker part
    if (prediction == 0) :
        print("Asteriod is not hazardous")
    elif(prediction == 1) :
        print("Asteriod is Hazardous")

def main():

    # Giving Title
    st.title("NASA NEO Hazardous Asteriod Prediction Web App")

    # getting the input data from the user
    # Estimated Diameter Minimum,Estimated Diameter Maximum, Relative Velocity, Missed Distance, Absolute magnitude

    est_diameter_min = st.text_input("Value of Estimated Diameter Minimum for Asteriod")
    est_diameter_max = st.text_input("Value of Estimated Diamter Maximum for Asteriod ")
    relative_velocity = st.text_input("Value of Relative Velocity for Asteriod ")
    missed_distance = st.text_input("Value of missed distance for Asteriod ")
    magnitude = st.text_input("Value of absolute magnitude for Asteriod")

    # code for prediction
    Prediction = ''

    # code for Prediction

    # creating a button for Prediction
    if st.button('Hazardous Asteriod Test Result'):
        diagnosis = Input(est_diameter_min,est_diameter_max, relative_velocity,missed_distance,magnitude)

    st.success(diagnosis)



if __name__ == '__main__':
    main()

