import streamlit as st
import random

st.set_page_config(page_title="Vocab Trainer", page_icon="📚")

st.title("📚 Entraînement Vocabulaire")

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
    "bridge this gap": "réduire l'écart",
    "to remain": "demeurer",
    "takeover bid": "offre de rachat",
    "merger": "fusion"
}

# -------- MODE --------
mode = st.radio(
    "Choisir le mode :",
    ["Anglais → Français", "Français → Anglais"]
)

# -------- INITIALISATION --------
if "current_word" not in st.session_state:
    st.session_state.current_word = random.choice(list(vocab.keys()))

if "input_key" not in st.session_state:
    st.session_state.input_key = 0

if "hint_level" not in st.session_state:
    st.session_state.hint_level = 0

# -------- NOUVELLE QUESTION --------
def new_question():
    st.session_state.current_word = random.choice(list(vocab.keys()))
    st.session_state.input_key += 1
    st.session_state.hint_level = 0

# -------- LOGIQUE QUESTION --------
if mode == "Anglais → Français":
    question = st.session_state.current_word
    correct_answer = vocab[st.session_state.current_word]
else:
    reverse_vocab = {v: k for k, v in vocab.items()}
    question = vocab[st.session_state.current_word]
    correct_answer = reverse_vocab[question]

st.markdown(f"### Traduire : **{question}**")

user_input = st.text_input(
    "Ta réponse :",
    key=f"user_input_{st.session_state.input_key}"
)

# -------- BOUTONS --------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Vérifier"):
        if user_input.strip().lower() == correct_answer.lower():
            st.success("✅ Correct")
        else:
            st.error(f"❌ Faux → {correct_answer}")

with col2:
    if st.button("Indice"):
        st.session_state.hint_level += 1

with col3:
    if st.button("Mot suivant"):
        new_question()
        st.rerun()

# -------- AFFICHAGE INDICE --------
if st.session_state.hint_level > 0:
    length = len(correct_answer)

    if st.session_state.hint_level == 1:
        hint = correct_answer[0] + "_" * (length - 1)
    elif st.session_state.hint_level == 2:
        half = length // 2
        hint = correct_answer[:half] + "_" * (length - half)
    else:
        hint = correct_answer

    st.info(f"💡 Indice : {hint}")
