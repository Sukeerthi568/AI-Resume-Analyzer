# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer that compares a candidate's resume with a job description and provides an ATS (Applicant Tracking System) score, matching skills, missing skills, and personalized improvement suggestions using Google's Gemini AI.

---

## 🚀 Features

- 📄 Upload Resume (PDF)
- 💼 Paste Job Description
- 🤖 AI-powered Resume Analysis using Google Gemini
- 📊 ATS Score Generation
- ✅ Matching Skills Detection
- ❌ Missing Skills Identification
- 💡 Personalized Resume Improvement Suggestions
- 📝 Overall Resume Feedback
- ⚡ Fast and Easy-to-use Streamlit Interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- PyPDF2
- python-dotenv
- Git & GitHub

---

## 📂 Project Structure

```
AI-Resume-Analyzer/
│
├── app.py
├── analyzer.py
├── utils.py
├── requirements.txt
├── .gitignore
└── .env
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sukeerthi568/AI-Resume-Analyzer.git
```

### 2. Navigate to the Project

```bash
cd AI-Resume-Analyzer
```

### 3. Create a Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` File

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### 6. Run the Application

```bash
python -m streamlit run app.py
```

---

## 📊 Sample Output

- ATS Score: **80/100**
- Matching Skills
- Missing Skills
- Resume Improvement Suggestions
- Overall AI Feedback

---

## 💡 How It Works

1. Upload a PDF Resume.
2. Paste the Job Description.
3. The application extracts text from the resume.
4. Gemini AI compares the resume with the job description.
5. The application displays:
   - ATS Score
   - Matching Skills
   - Missing Skills
   - Suggestions
   - Overall Feedback

---

## 🔮 Future Improvements

- Resume Keyword Highlighting
- Download Report as PDF
- Resume Ranking
- Multiple Resume Comparison
- Dark Mode
- Drag & Drop Resume Upload
- Dashboard with Analytics
- Support for DOCX Resumes

---

## 📸 Screenshots

### Home Page

_Add a screenshot here._

### AI Analysis

_Add a screenshot here._

---

## 👩‍💻 Author

**Sukeerthi Pathakamudi**

GitHub: https://github.com/Sukeerthi568

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub!
