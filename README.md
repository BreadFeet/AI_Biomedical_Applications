# Parkinson Detection with Classification

An AI-powered biomedical application for detecting Parkinson's disease using machine learning classification. This project includes both a model training pipeline and a deployment-ready web application.

## Project Overview

This project implements a machine learning solution to detect Parkinson's disease based on biomedical features using a Random Forest classifier. The trained model is packaged as a web application using Gradio and containerized with Docker for easy deployment.


## Quick Start

### Option 1: Run the Web Application Locally

1. **Install dependencies:**
   ```bash
   cd 02_Parkinson_app_deployment
   pip install -r requirements.txt
   ```

2. **Launch the app:**
   ```bash
   python app.py
   ```

3. **Access the interface:**
   - Open your browser and navigate to the URL shown in the terminal (typically `http://127.0.0.1:7860`)
   - Enter 22 biomedical feature values (one per line) in the input field
   - Click submit to get the prediction

### Option 2: Deploy with Docker

1. **Build the Docker image:**
   ```bash
   cd 02_Parkinson_app_deployment
   docker build -t parkinson-detector .
   ```

2. **Run the container:**
   ```bash
   docker run -p 7860:7860 parkinson-detector
   ```

3. **Access at:** `http://localhost:7860`


## Code to Deploy on IBM Cloud Code Engine
To deploy in serverless environment of IBM Cloude Code Engine from Github repositories using IBM Cloud Container Registry, 
1) Create the build configuration:
```
ibmcloud ce build create --name build-git-dockerfile1 \
    --build-type git --size large \
    --source https://github.com/BreadFeet/AI_Biomedical_Applications \
    --context-dir 02_Parkinson_app_deployment \
    --image us.icr.io/${SN_ICR_NAMESPACE}/myapp1 \
    --registry-secret ${SN_ICR_SECRET}
```
`${SN_ICR_NAMESPACE}` should be replaced by the private IBM Cloud Container Registry namespace; `${SN_ICR_SECRET}` by IBM Cloud Registry Secret.

2) Submit a buildrun to the Container Registry:
```
ibmcloud ce buildrun submit --name buildrun-git-dockerfile1 \
    --build build-git-dockerfile1
```

3) Create the app in the IBM Cloud:
```
ibmcloud ce application create --name demo1 \
    --image us.icr.io/${SN_ICR_NAMESPACE}/myapp1  \
    --registry-secret ${SN_ICR_SECRET} --ephemeral-storage 2G \
    --port 7860 --minscale 1
```
When it's done, the app is successfuly deployed.

4) Get the URL and access the app:
```
ibmcloud ce app get --name demo1 --output url
```

## Model Input Features

The model expects 22 biomedical features as input. These are typically voice/speech-related measurements from the University of California Irvine (UCI) Parkinson's dataset, which may include:
- Jitter, Shimmer, Fundamental Frequency measurements
- Mel-Frequency Cepstral Coefficients (MFCC)
- And other acoustic/voice analysis features

## License

See the [LICENSE](LICENSE) file for license information.


