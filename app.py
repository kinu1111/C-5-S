import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="পঞ্চম শ্রেণীর বৃত্তি প্রস্তুতি", layout="centered")

# শিরোনাম
st.title("🎓 পঞ্চম শ্রেণীর বৃত্তি পরীক্ষার প্রস্তুতি")
st.write("বাংলা, ইংরেজি, গণিত ও সাধারণ বিজ্ঞান বিষয়ক প্রশ্ন অনুশীলন করুন।")

# ডেটা লোড করা
@st.cache_data
def load_questions():
    df = pd.read_csv("data/questions.csv")
    return df

questions = load_questions()

# প্রশ্নের সংখ্যা সিলেক্টর
num_qs = st.slider("আপনি কয়টি প্রশ্ন অনুশীলন করতে চান?", 5, 20, 10)

# র‍্যান্ডম প্রশ্ন বাছাই
sample_qs = questions.sample(num_qs)

score = 0
answers = {}

# প্রশ্ন দেখানো
for i, row in enumerate(sample_qs.itertuples(), 1):
    st.subheader(f"প্রশ্ন {i}: {row.question}")
    options = [row.option_a, row.option_b, row.option_c, row.option_d]
    user_ans = st.radio("একটি উত্তর বেছে নিন:", options, key=f"q{i}")
    answers[i] = (user_ans, row.answer)

# সাবমিট বাটন
if st.button("✅ উত্তর জমা দিন"):
    score = sum([1 for k, v in answers.items() if v[0] == v[1]])
    st.success(f"আপনার স্কোর: {score} / {num_qs}")
    st.write("ভুল উত্তর গুলো দেখে নিন:")
    for i, (ua, ca) in answers.items():
        if ua != ca:
            st.error(f"❌ প্রশ্ন {i} → আপনার উত্তর: {ua}, সঠিক উত্তর: {ca}")
