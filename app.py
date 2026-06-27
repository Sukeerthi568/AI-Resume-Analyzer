import streamlit as st
from utils import extract_text_from_pdf
from analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste the Job Description"
)

if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.error("Please upload a PDF resume.")

    elif job_description.strip() == "":
        st.error("Please enter a job description.")

    else:

        with st.spinner("Analyzing Resume..."):

            resume_text = extract_text_from_pdf(uploaded_file)

            result = analyze_resume(
                resume_text,
                job_description
            )

            st.success("Analysis Completed!")

            st.markdown(result)