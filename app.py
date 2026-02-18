import streamlit as st
import random

st.set_page_config(page_title="Vocab Trainer", page_icon="📚")

st.title("📚 Entraînement Vocabulaire Anglais")

vocab = {
  "sat through": "assister à jusqu'au bout",
    "droned on": "s'éterniser",
    "peculiar": "particulier",
    "frenzy": "frénésie",
    "to pledge": "promettre",
    "corporate life": "vie en entreprise",
    "yet something": "pourtant quelque chose",
    "onboarding": "intégration",
    "to factor": "prendre en compte",
    "factored in": "pris en compte",
    "baffling": "déconcertant",
    "chasm": "fossé",
    "bite-sized": "format court",
    "to tailor": "adapter",
    "stubbornly": "obstinément",
    "one-size-fits-all": "solution universelle",
    "to check out": "se déconnecter mentalement",
    "wholesale": "à grande échelle",
    "substantial": "important",
    "plummeted": "s'est effondré",
    "completion rates": "taux d'achèvement",
    "crack the code": "trouver la solution",
    "blended learning": "formation hybride",
    "accountability": "responsabilité",
    "nine-tenths": "9/10",
    "unmistakable": "indéniable",
    "bridge the gap": "réduire l'écart",
    "to remain": "demeurer",
    "takeover bid": "offre de rachat",
    "merger": "fusion"
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
