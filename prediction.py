import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# from sklearn.preprocessing import LabelEncoder
import joblib
sns.set_style(style='dark')

# Or use "with" notation:
with st.sidebar:
    st.image("https://static.vecteezy.com/system/resources/previews/029/899/758/non_2x/hrm-human-resource-management-icon-label-badge-stock-illustration-vector.jpg")
    menu = st.sidebar.radio("Dashboard Human Resource Menu", [
    "Data Overview",
    "Visualization Data",
    "Prediction Employee",
    "Result & Recommendation"
])
    
if menu == "Data Overview":
    st.title("Dataset Exploration Employee")
    st.write("This is the Data Employee JayaMaju Overview page.")
    
    @st.cache_data
    def load_data():
        df = pd.read_csv('/mount/src/bpds/employee_data.csv')
        return df

    df = load_data()

    st.dataframe(df)

    if st.checkbox("Show Summary Statistics"):
        st.subheader("Summary Statistics")
        st.write(df.describe())

    if st.checkbox("Show Missing Values"):
        st.subheader("Missing Values")
        st.write(df.isnull().sum())

    if st.checkbox("Show Correlation Heatmap"):
        st.subheader("Correlation Heatmap")
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, fmt=".2f", cmap='coolwarm')
        st.pyplot(plt)  

if menu == "Visualization Data":
    st.title("Visualization Data Employee")
    
    @st.cache_data
    def load_data():
        df = pd.read_csv('/mount/src/bpds/employee_data_cleaned.csv')
        return df

    df = load_data()

    # Pisahkan numeric & categorical
    num_cols = df.select_dtypes(exclude="object").columns.tolist()
    cat_cols = df.select_dtypes(include="object").columns.tolist()

    # # Encode kategorikal → jadi numeric klo mau numeric comparison
    # le_dict = {}
    # for col in cat_cols:
    #     le = LabelEncoder()
    #     df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
    #     le_dict[col] = le  # kalau nanti mau inverse_transform

    # Hapus kolom label 'Attrition' dari list fitur
    if "Attrition" in num_cols:
        num_cols.remove("Attrition")
    if "Attrition" in cat_cols:
        cat_cols.remove("Attrition")

    selected_num_feature = st.selectbox("Select a Internal Factor", num_cols)

    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Attrition', y=selected_num_feature, data=df)
    plt.title(f'{selected_num_feature} Distribution by Attrition')
    st.pyplot(plt)

    st.subheader("Attrition Factor Count by Categorical Feature")
    selected_cat_feature = st.selectbox("Select a Categorical Feature", cat_cols)

    plt.figure(figsize=(8, 5))
    sns.countplot(hue="Attrition", y=selected_cat_feature, data=df)
    plt.title(f'{selected_cat_feature} Distribution by Attrition')
    st.pyplot(plt)


# --- Menu Predict ---
if menu == "Prediction Employee":
    st.title("Predict Attrition Employee")
    st.write("This is the Predict Attrition Employee page.")

    # Load data
    @st.cache_data
    def load_data():
        df = pd.read_csv('/mount/src/bpds/employee_data_cleaned.csv')
        return df
    
    @st.cache_resource
    def load_model():
        model = joblib.load("/mount/src/bpds/model.joblib")
        return model
    
    df = load_data()
    model = load_model()

    education_mapping = {
    1: "Below College",
    2: "College",
    3: "Bachelor",
    4: "Master",
    5: "Doctor"
    }

    # Input features
    st.subheader("Input Employee Features")
    input_data = {}
    for col in df.columns:
        if col == "Education":
            # Pilihan angka 1–5, ditampilkan sebagai label
            selected_value = st.selectbox(
                f"Select {col}",
                options=list(education_mapping.keys()),                      # hanya angka
                format_func=lambda x: education_mapping[x]     # tampil teks
            )
            input_data[col] = selected_value
        if col not in ["Attrition", "Education"]:  # Exclude target variable
            if df[col].dtype == 'object':
                input_data[col] = st.selectbox(f"Select {col}", df[col].unique())
            else:
                input_data[col] = st.number_input(f"Enter {col}", value=float(df[col].min()))

    if st.button("Predict Resign"):
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)
        prediction_proba = model.predict_proba(input_df)

        st.subheader("Prediction Result")
        attrition_result = "⚠️ Employee At Risk" if prediction[0] == 1 else "✅ Employee Likely to Stay"
        st.write(f"Predicted Resign: {attrition_result}")
        st.write(f"Resign Probability: {prediction_proba[0][1]:.2f}")

if menu == "Result & Recommendation":
    st.title("Result & Recommendation")
    st.write("This is the Result & Recommendation page.")

    st.subheader("Key Findings from Data Analysis")
    st.markdown("""
    - Employees with longer commute times tend to have higher attrition rates.
    - Lower job satisfaction and work-life balance scores are strongly correlated with employee resignations.
    - Certain departments and job roles exhibit higher turnover rates, indicating potential management or workload issues.
    - Employees with fewer years at the company are more likely to leave, suggesting onboarding and early engagement challenges.
    """)

    st.subheader("Recommendations to Reduce Employee Attrition")
    st.markdown("""
    1. **Enhance Work-Life Balance**: Implement flexible working hours and remote work options to help employees manage their personal and professional lives better.
    2. **Improve Job Satisfaction**: Conduct regular surveys to understand employee needs and address concerns related to job roles, responsibilities, and workplace environment.
    3. **Focus on Career Development**: Provide clear career paths, training programs, and opportunities for advancement to keep employees motivated and engaged.
    4. **Strengthen Onboarding Processes**: Develop comprehensive onboarding programs to help new hires integrate smoothly into the company culture and understand their roles better.
    5. **Address Department-Specific Issues**: Analyze high-turnover departments to identify specific problems and implement targeted interventions, such as management training or workload adjustments.
    """)

    st.subheader("Conclusion")
    st.markdown("""
    By leveraging data-driven insights, JayaMaju can implement strategic initiatives to enhance employee satisfaction and retention. Continuous monitoring of key metrics and adapting strategies based on employee feedback will be crucial in maintaining a motivated and committed workforce.
    """)