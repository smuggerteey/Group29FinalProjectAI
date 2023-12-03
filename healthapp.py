import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Chronic Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           "Parkinson's Prediction",],
                          icons=['activity', 'heart', 'person'],
                          default_index=2) 

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # Page title
    st.title('Diabetes Prediction')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input('Number of Pregnancies', value='', help='Enter a numeric value')

    with col2:
        glucose = st.text_input('Glucose Level', value='', help='Enter a numeric value')

    with col3:
        blood_pressure = st.text_input('Blood Pressure value', value='', help='Enter a numeric value')

    with col1:
        skin_thickness = st.text_input('Skin Thickness value', value='', help='Enter a numeric value')

    with col2:
        insulin = st.text_input('Insulin Level', value='', help='Enter a numeric value')

    with col3:
        bmi = st.text_input('BMI value', value='', help='Enter a numeric value')

    with col1:
        diabetes_pedigree_function = st.text_input('Diabetes Pedigree Function value', value='', help='Enter a numeric value')

    with col2:
        age = st.text_input('Age of the Person', value='', help='Enter a numeric value')

    # Code for Prediction
    diab_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Diabetes Test Result', key='button1'):
        if (
            pregnancies != '' and glucose != '' and blood_pressure != '' and skin_thickness != ''
            and insulin != '' and bmi != '' and diabetes_pedigree_function != '' and age != ''
        ):
            # Perform data type conversion as needed
            try:
                pregnancies = float(pregnancies)
                glucose = float(glucose)
                blood_pressure = float(blood_pressure)
                skin_thickness = float(skin_thickness)
                insulin = float(insulin)
                bmi = float(bmi)
                diabetes_pedigree_function = float(diabetes_pedigree_function)
                age = float(age)
            except ValueError:
                diab_diagnosis = 'Please enter numeric values for all fields'
                st.error(diab_diagnosis)
                st.stop()

            diab_prediction = diabetes_model.predict([[
                pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi,
                diabetes_pedigree_function, age
            ]])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        else:
            diab_diagnosis = 'Please enter all the required information'

        st.success(diab_diagnosis)

    if st.button('Diabetes Education and Prevention Measures', key='button2'):
        education_text = """
        Diabetes is a chronic disease that affects how your body regulates blood sugar (glucose). 
        It is important to manage diabetes through a combination of healthy lifestyle choices and medical care.
        Here are some education and prevention measures to help you fight against diabetes:
    
        1. Eat a balanced diet: Include a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats in your diet. Limit sugary foods and drinks.
    
        2. Stay physically active: Engage in regular physical activity such as walking, jogging, swimming, or cycling. Aim for at least 150 minutes of moderate-intensity aerobic activity per week.
    
        3. Maintain a healthy weight: If you are overweight or obese, losing even a small amount of weight can help improve insulin sensitivity and blood sugar control.
    
        4. Monitor blood sugar levels: Regularly check your blood sugar levels as recommended by your healthcare provider. This can help you understand how certain foods and activities affect your blood sugar.
    
        5. Take prescribed medications: If you have been prescribed diabetes medication, make sure to take it as directed by your healthcare provider.
    
        6. Manage stress: Chronic stress can affect blood sugar levels. Find healthy ways to manage stress, such as practicing relaxation techniques, exercising, or engaging in hobbies.
    
        7. Get regular check-ups: Visit your healthcare provider regularly for diabetes screenings and to monitor your overall health.
    
        Remember, it is important to work with your healthcare provider to create an individualized diabetes management plan that suits your specific needs.
        """

        st.write(education_text)
    
# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # Page title
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age', value='', help='Enter a numeric value')

    with col2:
        sex = st.text_input('Sex', value='', help='Enter 0 for female, 1 for male')

    with col3:
        cp = st.text_input('Chest Pain types', value='', help='Enter a numeric value')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure', value='', help='Enter a numeric value')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', value='', help='Enter a numeric value')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', value='', help='Enter 0 for false, 1 for true')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', value='', help='Enter a numeric value')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', value='', help='Enter a numeric value')

    with col3:
        exang = st.text_input('Exercise Induced Angina', value='',help='Enter 0 for no, 1 for yes')

    with col1:
        oldpeak = st.text_input('ST Depression induced by exercise relative to rest', value='', help='Enter a numeric value')

    with col2:
        slope = st.text_input('The Slope of the peak exercise ST segment', value='', help='Enter a numeric value')

    with col3:
        ca = st.text_input('Number of major vessels colored by flourosopy', value='', help='Enter a numeric value')

    with col1:
        thal = st.text_input('Thalassemia', value='', help='Enter a numeric value')

    # Code for Prediction
    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Heart Disease Test Result', key='button3'):
        if (
            age != '' and sex != '' and cp != '' and trestbps != '' and chol != '' and fbs != ''
            and restecg != '' and thalach != '' and exang != '' and oldpeak != '' and slope != ''
            and ca != '' and thal != ''
        ):
            # Perform data type conversion as needed
            try:
                age = float(age)
                sex = int(sex)
                cp = float(cp)
                trestbps = float(trestbps)
                chol = float(chol)
                fbs = int(fbs)
                restecg = float(restecg)
                thalach = float(thalach)
                exang = int(exang)
                oldpeak = float(oldpeak)
                slope = float(slope)
                ca = float(ca)
                thal = float(thal)
            except ValueError:
                heart_diagnosis = 'Please enter valid values for all fields'
                st.error(heart_diagnosis)
                st.stop()

            heart_prediction = heart_disease_model.predict([[
                age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
            ]])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has heart disease'
            else:
                heart_diagnosis = 'The person does not have heart disease'
        else:
            heart_diagnosis = 'Please enter all the required information'

        st.success(heart_diagnosis)

    if st.button('Heart Disease Education and Prevention Measures', key='button4'):
    
        education_text = """
        Heart disease is a leading cause of death worldwide. Taking preventive measures and adopting a healthy lifestyle can help reduce the risk of developing heart disease. Here are some education and prevention measures to consider:

        1. Eat a heart-healthy diet: Include a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats in your diet. Limit saturated and trans fats, cholesterol, sodium, and added sugars.

        2. Maintain a healthy weight: Aim for a healthy weight range through a combination of balanced diet and regular physical activity. Losing excess weight can help reduce the strain on your heart.

        3. Stay physically active: Engage in regular aerobic exercise such as brisk walking, jogging, cycling, or swimming. Aim for at least 150 minutes of moderate-intensity exercise per week.

        4. Don't smoke: Smoking is a major risk factor for heart disease. If you smoke, seek help to quit. Avoid exposure to secondhand smoke as well.

        5. Limit alcohol consumption: Excessive alcohol consumption can contribute to heart disease. If you drink alcohol, do so in moderation according to recommended guidelines.

        6. Manage stress: Chronic stress can affect heart health. Find healthy ways to manage stress, such as exercise, relaxation techniques, hobbies, or talking to a supportive person.

        7. Get regular check-ups: Visit your healthcare provider for routine check-ups and screenings. Monitor your blood pressure, cholesterol levels, and other relevant health parameters.

        Remember, prevention is key when it comes to heart disease. Adopting a heart-healthy lifestyle and managing risk factors can significantly reduce the chances of developing heart disease.

        If you have any concerns or specific health conditions, consult with your healthcare provider for personalized advice and recommendations.
        """

        st.write(education_text)


# Parkinson's Disease Prediction Page
if selected == "Parkinson's Prediction":
    # Page title
    st.title("Parkinson's Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo (Hz)', value='', help='Enter a numeric value')

    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi (Hz)', value='', help='Enter a numeric value')

    with col3:
        MDVP_Flo = st.text_input('MDVP:Flo (Hz)', value='', help='Enter a numeric value')

    with col1:
        MDVP_Jitter_Percent = st.text_input('MDVP:Jitter(%)', value='', help='Enter a numeric value')

    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', value='', help='Enter a numeric value')

    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP', value='', help='Enter a numeric value')

    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ', value='', help='Enter a numeric value')

    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP', value='', help='Enter a numeric value')

    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer', value='', help='Enter a numeric value')

    with col1:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', value='', help='Enter a numeric value')

    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3', value='', help='Enter a numeric value')

    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5', value='', help='Enter a numeric value')

    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ', value='', help='Enter a numeric value')

    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA', value='', help='Enter a numeric value')

    with col3:
        NHR = st.text_input('NHR', value='', help='Enter a numeric value')

    with col1:
        HNR = st.text_input('HNR', value='', help='Enter a numeric value')

    # Code for Prediction
    parkinsons_diagnosis = ''

    # Creating a button for Prediction
    if st.button("Parkinson's Disease Test Result", key='button5'):
        if (
            MDVP_Fo != ''
            and MDVP_Fhi != ''
            and MDVP_Flo != ''
            and MDVP_Jitter_Percent != ''
            and MDVP_Jitter_Abs != ''
            and MDVP_RAP != ''
            and MDVP_PPQ != ''
            and Jitter_DDP != ''
            and MDVP_Shimmer != ''
            and MDVP_Shimmer_dB != ''
            and Shimmer_APQ3 != ''
            and Shimmer_APQ5 != ''
            and MDVP_APQ != ''
            and Shimmer_DDA != ''
            and NHR != ''
            and HNR != ''
        ):
            # Perform data type conversion as needed
            try:
                MDVP_Fo = float(MDVP_Fo)
                MDVP_Fhi = float(MDVP_Fhi)
                MDVP_Flo = float(MDVP_Flo)
                MDVP_Jitter_Percent = float(MDVP_Jitter_Percent)
                MDVP_Jitter_Abs = float(MDVP_Jitter_Abs)
                MDVP_RAP = float(MDVP_RAP)
                MDVP_PPQ = float(MDVP_PPQ)
                Jitter_DDP = float(Jitter_DDP)
                MDVP_Shimmer = float(MDVP_Shimmer)
                MDVP_Shimmer_dB = float(MDVP_Shimmer_dB)
                Shimmer_APQ3 = float(Shimmer_APQ3)
                Shimmer_APQ5 = float(Shimmer_APQ5)
                MDVP_APQ = float(MDVP_APQ)
                Shimmer_DDA = float(Shimmer_DDA)
                NHR = float(NHR)
                HNR = float(HNR)
            except ValueError:
                parkinsons_diagnosis = 'Please enter valid values for all fields'
                st.error(parkinsons_diagnosis)
                st.stop()

            parkinsons_prediction = parkinsons_model.predict([[
                MDVP_Fo,
                MDVP_Fhi,
                MDVP_Flo,
                MDVP_Jitter_Percent,
                MDVP_Jitter_Abs,
                MDVP_RAP,
                MDVP_PPQ,
                Jitter_DDP,
                MDVP_Shimmer,
                MDVP_Shimmer_dB,
                Shimmer_APQ3,
                Shimmer_APQ5,
                MDVP_APQ,
                Shimmer_DDA,
                NHR,
                HNR,
            ]])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
        else:
            parkinsons_diagnosis = 'Please enter all the required information'

        st.success(parkinsons_diagnosis)

    if st.button("Parkinson's Disease Education", key='button6'):
        education_text = """
        Parkinson's disease is a neurodegenerative disorder that affects movement control. It is characterized by symptoms such as tremors, stiffness, slow movement, and balance problems. Here are some key points about Parkinson's disease:

        1. Causes: Parkinson's disease is caused by a loss of dopamine-producing cells in the brain. The exact cause is unknown, but a combination of genetic and environmental factors is believed to play a role.

        2. Symptoms: Common symptoms of Parkinson's disease include tremors, rigidity, bradykinesia (slowness of movement), postural instability, and changes in speech and writing. Symptoms may vary from person to person and can worsen over time.

        3. Diagnosis: Parkinson's disease is diagnosed based on medical history, physical examination, and the presence of characteristic motor symptoms. Additional tests, such as brain imaging and response to medication, may be used to confirm the diagnosis.

        4. Treatment: While there is no cure for Parkinson's disease, treatment aims to manage symptoms and improve quality of life. Medications, such as levodopa, dopamine agonists, and MAO-B inhibitors, are commonly prescribed. Physical therapy, occupational therapy, and speech therapy can also be beneficial.

        5. Lifestyle and self-care: Adopting a healthy lifestyle can help manage Parkinson's disease. Regular exercise, a balanced diet, and getting enough rest and sleep are important. It is also essential to stay socially connected and seek support from loved ones and support groups.

        6. Research and advancements: Ongoing research is focused on better understanding Parkinson's disease and developing new treatments. Clinical trials and studies are conducted to test innovative therapies and interventions.

        It is important to consult with a healthcare professional for personalized advice and treatment options if you or someone you know is affected by Parkinson's disease. They can provide guidance and support tailored to individual needs.

        Remember, early detection and timely management can make a significant difference in managing Parkinson's disease and improving the overall quality of life.

        """

        st.write(education_text)

# python 3.8 (3.8.16) or it doesn't work
# pip install streamlit streamlit-chat langchain python-dotenv
import openai
import streamlit as st

st.title("ChatGPT-like ChatBot")

openai.api_key = "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"

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
