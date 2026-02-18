import streamlit as st
import random

st.set_page_config(page_title="Vocab Trainer", page_icon="📚")

st.title("📚 Entraînement Vocabulaire Anglais")

vocab = {
    "apple": "pomme",
    "house": "maison",
    "car": "voiture",
    "book": "livre",
    "dog": "chien",
    "water": "eau",
    "happy": "heureux"
}

# Initialisation
if "score" not in st.session_state:
    st.session_state.score = 0

if "total" not in st.session_state:
    st.session_state.total = 0

if "mode" not in st.session_state:
    st.session_state.mode = random.choice(["EN→FR", "FR→EN"])

if "current_word" not in st.session_state:
    st.session_state.current_word = random.choice(list(vocab.keys()))

def new_question():
    st.session_state.mode = random.choice(["EN→FR", "FR→EN"])
    st.session_state.current_word = random.choice(list(vocab.keys()))

# Déterminer la question
if st.session_state.mode == "EN→FR":
    question = st.session_state.current_word
    correct_answer = vocab[st.session_state.current_word]
else:
    question = vocab[st.session_state.current_word]
    correct_answer = st.session_state.current_word

st.subheader(f"Mode : {st.session_state.mode}")
st.markdown(f"### Traduire : **{question}**")

user_input = st.text_input("Ta réponse :")

col1, col2 = st.columns(2)

with col1:
    if st.button("Vérifier"):
        st.session_state.total += 1
        if user_input.strip().lower() == correct_answer.lower():
            st.success("✅ Correct !")
            st.session_state.score += 1
        else:
            st.error(f"❌ Faux. Réponse correcte : {correct_answer}")

with col2:
    if st.button("Mot suivant"):
        new_question()
        st.rerun()

st.markdown("---")
st.write(f"🎯 Score : {st.session_state.score} / {st.session_state.total}")
