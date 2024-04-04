# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.tree import DecisionTreeRegressor
import streamlit as st
import warnings
warnings.simplefilter("ignore")
from PIL import Image
import base64
import io
from streamlit_option_menu import option_menu


# Set page title and icon
icon = Image.open("icn.png")
st.set_page_config(
    page_title="Finance: Loan Default Prediction | By Nahid Banu",
    page_icon=icon,
    layout="wide"
)


box_style = """
    <style>
        .box {
            border: 1px solid #3F1209;
            padding: 1px;
            border-radius: 1px;
            background-color: #F7E4DE;
        }
    </style>
"""

# Apply the CSS style and the text within a box
st.markdown(box_style, unsafe_allow_html=True)
st.markdown("<div class='box'><h1 style='text-align: center; color:Black; font-size:35px;'>LOAN DEFAULT PREDICTION</h1></div>", unsafe_allow_html=True)


def setting_bg(background_image_url):
    st.markdown(f""" 
    <style>
        .stApp {{
            background: url('{background_image_url}') no-repeat center center fixed;
            background-size: cover;
            transition: background 0.5s ease;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #f3f3f3;
            font-family: 'Roboto', sans-serif;
        }}
        .stButton>button {{
            color: #4e4376;
            background-color: #f3f3f3;
            transition: all 0.3s ease-in-out;
        }}
        .stButton>button:hover {{
            color: #f3f3f3;
            background-color: #2b5876;
        }}
        .stTextInput>div>div>input {{
            color: #4e4376;
            background-color: #f3f3f3;
        }}
    </style>
    """, unsafe_allow_html=True)

# # Background image
background_image_url = "https://t4.ftcdn.net/jpg/05/51/71/61/360_F_551716108_yZSbx76w5A8ZX8Hjn9FhCKfaFp2hd2X9.jpg"
setting_bg(background_image_url)

with st.sidebar:
    st.header("Loan Default Prediction")
        
    selected = option_menu(None,["Home","Predictions"], 
                        icons=["house","trophy"],
                        default_index=0,
                        orientation="vertical",
                        styles={"nav-link": {"font-size": "35px", "text-align": "centre", "margin": "0px", "--hover-color": "#6495ED"},
                                "icon": {"font-size": "35px"},
                                "container" : {"max-width": "6000px"},
                                "nav-link-selected": {"background-color": "#B4964E"}})
    
if selected=="Home":
    st.markdown('<p style="font-size: 44px; color: black;">Monitoring existing loans and identifying customers at risk of default helps banks manage and mitigate credit risk.</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 33px; color: blue;"This data is crucial for banks to make informed decisions about lending, manage risk, and tailor financial products to meet the needs of their customers while ensuring the stability and profitability of the institution  </p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 33px; color: blue;"> Age: Age can be a significant factor in determining financial behavior and risk assessment. Younger individuals might have less stable income streams or credit history compared to older individuals.  </p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 33px; color: blue;"> Gender: Used in demographic analysis, gender may play a role in assessing risk profiles and tailoring financial products. </p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 33px; color: blue;"> Income: It is a crucial factor in determining loan eligibility and the amount of credit a customer can access. Higher income generally indicates a greater ability to repay loans. </p>', unsafe_allow_html=True) 
    st.markdown('<p style="font-size: 33px; color: blue;"> Employment_Status: It is essential for assessing stability and ability to repay loans. Unemployed individuals might pose a higher risk for default.. </p>', unsafe_allow_html=True) 
    st.markdown('<p style="font-size: 33px; color: blue;"> Location: Location can influence cost of living, job market conditions & overall economic stability, which in turn impact financial behaviors.. </p>', unsafe_allow_html=True) 
    st.markdown('<p style="font-size: 33px; color: blue;"> Credit_Score:It is a person creditworthiness. Higher credit scores indicate lower credit risk. </p>', unsafe_allow_html=True) 
    st.markdown('<p style="font-size: 33px; color: blue;"> Debt_to_Income_Ratio: It is total monthly debt payments to their gross monthly income. It helps assess ones ability to manage additional debt. Lower ratios suggest better financial health and lower risk. </p>', unsafe_allow_html=True) 
    st.markdown('<p style="font-size: 33px; color: blue;"> Existing_Loan_Balance:The balance remaining on any existing loans. It gives insight into the customers current debt obligations and repayment behavior. </p>', unsafe_allow_html=True) 
    st.markdown('<p style="font-size: 33px; color: blue;"> Loan_Status: Indicates whether the customers loan is in default or non-default status. </p>', unsafe_allow_html=True) 
    st.markdown('<p style="font-size: 33px; color: green;"> Default means the customer has failed to meet the loan repayment terms </p>', unsafe_allow_html=True) 
    st.markdown('<p style="font-size: 33px; color: green;"> Non-default indicates regular and timely payments. </p>', unsafe_allow_html=True) 
    st.markdown('<p style="font-size: 33px; color: blue;"> Loan_Amount: The amount of money borrowed by the customer as part of the loan.</p>', unsafe_allow_html=True) 
    st.markdown('<p style="font-size: 33px; color: blue;"> Interest_Rate: The rate at which interest is charged on the loan amount, it depends on creditworthiness, loan term, and prevailing market rates.</p>', unsafe_allow_html=True) 
    st.markdown('<p style="font-size: 33px; color: blue;"> Loan_Duration_Months: It influences the total amount of interest paid and the monthly repayment amount. </p>', unsafe_allow_html=True) 
    

if selected =="Predictions":
    st.subheader("Customer Details")

# Define unique values for select boxes
    Gender = ['Male', 'Female']
    EmploymentStatus = ['Employed', 'Unemployed']
    Location = ['Suburban', 'Urban', 'Rural']

    tab1, tab2, tab3, tab4, tab5= st.columns(5)
    with tab1:
        Gender = st.selectbox("Gender", options=Gender)
        EmploymentStatus = st.selectbox("Employee Status", options=EmploymentStatus)
        
    with tab2:
        Location = st.selectbox("Location", options=Location)
        Age = st.number_input("Age", min_value=18, max_value=64, value=18)       

    with tab3:
        Credit_Score =st.number_input("Credit Score", min_value=250, max_value=850, value=250)
        Income = st.number_input("Income", min_value=24156, max_value=97722, value=24156)
        
    with tab4:
        Debt_to_Income_Ratio = st.number_input("Debt to Income Ratio", min_value=0.0001, max_value=0.9999, value=0.0001)
        Existing_Loan_Balance = st.number_input("Existing Loan Balance", min_value=0, max_value=50000, value=0)
    with tab5:
        Loan_Amount = st.number_input("Loan Amount", min_value=5000, max_value=50000, value=5000)
        Interest_Rate = st.number_input("Interest Rate", min_value=3, max_value=20, value=3)
        Loan_Duration_Months = st.number_input("Loan Duration (Months)", min_value=12, max_value=71, value=12)

    if st.button("Predict Loan Default status"):
        input_data = pd.DataFrame({
        'Age': [Age],
        'Income': [Income],
        'Credit_Score': [Credit_Score],
        'Debt_to_Income_Ratio':[Debt_to_Income_Ratio],
        'Existing_Loan_Balance': [Existing_Loan_Balance],
        'Loan_Amount': [Loan_Amount],
        'Interest_Rate': [Interest_Rate],
        'Loan_Duration_Months': [Loan_Duration_Months],
        'Gender': [Gender],
        'EmploymentStatus': [EmploymentStatus],
        'Location': [Location]})  

        import pickle

        with open(r'model_gb.pkl', 'rb') as file:
                model_gb = pickle.load(file)
        with open(r'scaler_gb.pkl', 'rb') as file:
                scaler_gb = pickle.load(file)
        with open(r'ohe.pkl', 'rb') as file:
                ohe = pickle.load(file)
        with open(r'ohe2.pkl', 'rb') as file:
                ohe2 = pickle.load(file)
        with open(r'ohe3.pkl', 'rb') as file:
                ohe3 = pickle.load(file)   


        from sklearn.preprocessing import LabelEncoder
        label_encoder = LabelEncoder()
        label_encoder.fit(["Non-Default", "Default"])   
        def decode_labels(encoded_data, label_encoder):
                decoded_data = label_encoder.inverse_transform(encoded_data)
                return decoded_data   

        #(X[['year','floor_area_sqm','lease_commence_date','years_holding','current_remaining_lease']].values, X1, X2, X3, X4)
        new_sample = np.array([[Age,float(Income),Credit_Score,float(Debt_to_Income_Ratio),float(Existing_Loan_Balance),float(Loan_Amount),float(Interest_Rate),Loan_Duration_Months, Gender, EmploymentStatus, Location]])
        new_sample_gender = ohe.transform(new_sample[:, [8]]).toarray()
        new_sample_employeeStatus = ohe2.transform(new_sample[:, [9]]).toarray()
        new_sample_Location = ohe3.transform(new_sample[:, [10]]).toarray()
        new_sample = np.concatenate((new_sample[:, [0, 1, 2, 3, 4, 5, 6, 7]], new_sample_gender, new_sample_employeeStatus, new_sample_Location), axis=1)
        # Scaling numerical features
        new_sample1 = scaler_gb.transform(new_sample)
        new_pred = model_gb.predict(new_sample1)[0].reshape(1)
        # Decode the predicted labels
        decoded_pred = decode_labels(new_pred, label_encoder)
        decoded_pred_str = decoded_pred[0] 
        st.write('## <span style="color:black;">Loan_Default_prediction is:</span>', decoded_pred_str, unsafe_allow_html=True)


        if decoded_pred == 'Default':
            st.write("## <span style='color:#00008B;'>Customer has failed to meet the loan repayment terms</span>", unsafe_allow_html=True)

        else:
            st.write("## <span style='color:#00008B;'>Customer has done regular and timely payments</span>", unsafe_allow_html=True)


st.write('<h6 style="color:#730640 ;">App Created by Nahid Banu K</h6>', unsafe_allow_html=True)