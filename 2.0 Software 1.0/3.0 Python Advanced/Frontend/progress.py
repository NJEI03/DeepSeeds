import streamlit as st
import time as time

progress = st.progress(0)

for i in range(100):
    time.sleep(0.02)  #simulate computation
    progress.progress(i + 1 )

st.success("✔ Generation Complete!")

#Tabs Seperatnto multiple pages without navigation
tab1, tab2 = st.tabs(['prompt','Output'])

with tab1:
    prompt = st.text_input('Enter your prompt')
    if st.button('Submit'): 
        # st.write(f'You entered: {prompt}')
        st.success('Prompt submitted successfully!')
with tab2:
    st.write('This is the output tab')
    if st.button('Show Output'):
        st.write('Here is the output for your prompt')   
cside = st.sidebar.selectbox(
     "Models" ,
     ['GPT-3.5', 'GPT-4', 'Claude 2', 'Gemini Pro'] 
)


