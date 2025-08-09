import streamlit as st
import time as time
# from profile import markdown
# st.form( key='my_form')
# with st.form(key='my_for'):
#     name = st.text_input('Enter your name')
#     age = st.number_input('Enter your age')
#     submit_button = st.form_submit_button(label='Submit')
# if submit_button:
#     st.write(f'Hello {name}, you are {age} years old')


# st.title("My First StreamLit App")
# st.header("Welcome to my app!")
# st.write("This is a simple StreamLit application.")
# pressed = st.button("See my profile")
# print(markdown)

# st.image("https://i.ibb.co/SDR0kxVK/Black-and-Gold-Elegant-Portrait-Linked-In-Profile-Picture.png", caption="Profile Picture" , use_column_width=False)
   

# st.image('./darkjj.jpg', caption='Dark JJ', use_column_width=False)

# uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])
# if uploaded_file:
#     st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)


st.write('BOT: Hello, I am JJBot')
with st.form(key = 'form_name'):
    user_name= st.text_input('Enter your name')
    user_prompt = st.text_area('Ask JJBot Anything' )
    user_file = st.file_uploader ('Choose a file' , type = [ 'pdf' 'png' 'JPG' ] )
    submit_button = st.form_submit_button (label = 'Submit')

while user_name != '' and user_prompt != '' :
    if submit_button:
         st.balloons()
         st.success(body='Submitted Successfully',icon='😎')
         st.write (f' Me : {user_prompt} ' )
         st.write(f'BOT: Hello {user_name}. I will answer in a minute' )
         
    break
else:
    st.warning('Fill all inputs')
   
progress = st.progress(0)

for i in range(100):
    time.sleep(0.02)  #simulate computation
    progress.progress(i + 1 )

st.success("✔ Generation Complete!")


st.sidebar.title('Setting')
import streamlit as st

cside = st.sidebar.selectbox(
     "Models" ,
    options=[
        "GPT-3.5",
        "GPT-4",
        "Claude 2",
        "Gemini",
        "Llama 2",
        "Mistral",
    ],
)

temperature = st.sidebar.slider('Temperature' , 0.0 , 1.0 , 0.7 )


