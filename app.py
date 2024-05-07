import streamlit as st
import json
import requests

st.title('Predict Median House Pricing')


with open('input_options.json') as f:
    side_bar_options = json.load(f)
    options = {}
    for key, value in side_bar_options.items():
        if key in ['ocean_proximity']:
            options[key] = st.sidebar.selectbox(key, value)
        else:
            min_val, max_val = value
            current_value = (min_val + max_val)/2
            options[key] = st.sidebar.slider(key, min_val, max_val, value=current_value)


st.write(options)

if st.button('Predict'): 
    # payload = json.dumps({'inputs': options})
    # response = requests.post(
    #     url=f"http://159.203.68.179:5001/invocations",
    #     data=payload,
    #     headers={"Content-Type": "application/json"},
    # )

    payload = json.dumps(options)
    response = requests.post(
        url=f"http://159.203.132.225:8889/",
        data=payload,
        headers={"Content-Type": "application/json"},
    )

    response = response.json()
    prediction = response.get('prediction')
    model_name =response.get('model_name')
    model_last_updated =response.get('model_last_updated')
    st.write(f'The predicted median house value is: ${prediction:,}')
    st.write(f'Model {model_name} was last updated {model_last_updated}.')
