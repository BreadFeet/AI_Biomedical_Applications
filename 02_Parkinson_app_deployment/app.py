# Gradio demonstration
import gradio as gr
import pickle
import pandas as pd
import requests
import cloudpickle as cp

# ## This requires to include the trained model in the container for deployment.
# ## This increases the size of the container and delays the container creation, so will not be used for deployment.
# # Load the trained and pickled model from the previous notebook
# rf = pickle.load(open('../rf_model_parkinson', 'rb'))

# Load the trained and pickled model from Github
url = "https://github.com/BreadFeet/AI_Biomedical_Applications/raw/refs/heads/master/rf_model_parkinson"
response = requests.get(url)
response.raise_for_status()
rf = cp.loads(response.content)

# Get the feature names
feature_names = rf.feature_names_in_

# Main function
def detect_parkinson(var):
    """
    var: parkinson feature values in string format, separated by new lines. \
    The order of the features should be the same as the feature names in the dataset.
    """
    # Split the var string line by line
    vars = var.strip().split('\n')
    df_temp = pd.DataFrame([vars], columns=feature_names)

    # Make prediction of the input data
    prediction = rf.predict(df_temp)
    if prediction == 1:  
        return "Predicted label: 1 --> Parkinson detected"
    else:
        return "Predicted label: 0  --> No Parkinson detected"
    
inputs = gr.Textbox(placeholder='\n'.join(feature_names), lines=22, label='Parkinson feature values')
outputs = gr.Textbox()

demo = gr.Interface(detect_parkinson, inputs, outputs)
demo.launch()
