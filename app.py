import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translation Tool", layout="centered")

st.title("Language Translation Tool")
st.markdown("Translate text between 100+ languages using Google Translate.")

LANGUAGES = GoogleTranslator().get_supported_languages(as_dict=True)
language_names = sorted(LANGUAGES.keys())

input_text = st.text_area("Enter text to translate:", height=150)

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Source Language", ["auto"] + language_names)
with col2:
    target_lang = st.selectbox("Target Language", language_names, index=language_names.index("urdu"))

if st.button("Translate"):
    if not input_text.strip():
        st.warning("Please enter some text.")
    else:
        try:
            result = GoogleTranslator(source=source_lang, target=target_lang).translate(input_text)
            st.subheader("Translated Text")
            st.success(result)
        except Exception as e:
            st.error(f"Translation failed. Error: {e}")