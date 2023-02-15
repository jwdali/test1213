import streamlit as st
from transformers import pipeline

st.title('Sentiment Analysis Demo')
st.write('It is using Hugging Face Transformer')

st.write('*Class: Institute of Data, Signapore*')

form = st.form(key='test_form')
user_input = form.text_area('Please provide your text below:')
submit = form.form_submit_button('Submit')

if submit:
    classifier = pipeline("sentiment-analysis")
    result = classifier(user_input)[0] #it returns list, so take first element
    label = result['label']
    score = result['score']

    if label == 'POSITIVE':
        st.success(f'{label} sentiment (score: {score})')
    else:
        st.error(f'{label} sentiment (score: {score})')
    #else:
    #    st.success(f'{label} sentiment (score: {score})')