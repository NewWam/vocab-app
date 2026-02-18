import streamlit as st
import random

st.set_page_config(page_title="Vocab Trainer", page_icon="📚")

st.title("📚 Entraînement Vocabulaire Anglais")

# =========================
# AJOUTE TON VOCABULAIRE ICI
# =========================

vocab = {
    "apple": "pomme",
    "house": "maison",
    "car": "voiture",
    "book": "livre",
    "dog": "chien",
    "water": "eau",
    "happy": "heureux"
}

# =========================

# Initialisation session
if "score" not in st.session_state:
    st.session_state.score = 0

if "total" not in st.session_state:
    st.session_state.total = 0

if "mode" not in st.session_state:
    st.session_state.mode = random.choice(["EN→FR", "FR→EN"])

if "current_word" not in st.session_state:
    st.session_state.current_word = random.choice(list(vocab.keys()))

if "answered" not in st.session_state:
    st.session_state.answered = False


def new_question():
    st.session_state.mode = random.choice(["EN→FR", "FR→EN"])
    st.session_state.current_word = random.choice(list(vocab.keys()))
    st.session_state.answered = False
    st.session_state.user_input = ""


# Déterminer question
if st.session_state.mode == "EN→FR":
    question = st.session_state.current_word
    correct_answer = vocab[st.session_state.current_word]
else:
    question = vocab[st.session_state.current_word]
    correct_answer = st.session_state.current_word


st.subheader(f"Mode : {st.session_state.mode}")
st.markdown(f"### Traduire : **{question}**")

user_input = st.text_input("Ta réponse :", key="user_input")

col1, col2 = st.columns(2)

with col1:
    if st.button("Vérifier"):
        if not st.session_state.answered:
            st.session_state.total += 1
            if user_input.strip().lower() == correct_answer.lower():
                st.success("✅ Correct !")
                st.session_state.score += 1
            else:
                st.error(f"❌ Faux. Réponse correcte : {correct_answer}")
            st.session_state.answered = True

with col2:
    if st.button("Mot suivant"):
        new_question()
        st.rerun()

st.markdown("---")
st.write(f"🎯 Score : {st.session_state.score} / {st.session_state.total}")
