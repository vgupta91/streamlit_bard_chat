import streamlit as st
from bardapi import Bard
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
# from htmlTemplates import css, bot_template, user_template
from streamlit_extras.add_vertical_space import add_vertical_space
# from hugchat import hugchat
css = '''
<style>
section.main .block-container{
    top: 50px;
    overflow: auto;
    padding-bottom: 1rem;
    padding-top: 1rem;
    display: flex;
    flex-direction: column-reverse;
    height:calc(100% - 170px);
}
.stTextInput {
      position: fixed;
      bottom: 3rem;
}
hr{
    display: none;
}
iframe .avatar{
    display: none !important;
}
</style>
'''
st.set_page_config(page_title="HugChat - An LLM-powered Streamlit app")
st.write(css, unsafe_allow_html=True)

# Sidebar contents
with st.sidebar:
    st.title('🤗💬 HugChat App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [HugChat](https://github.com/Soulter/hugging-chat-api)
    - [OpenAssistant/oasst-sft-6-llama-30b-xor](https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor) LLM model

    💡 Note: No API key required!
    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ by [Data Professor](https://youtube.com/dataprofessor)')

# Generate empty lists for generated and past.
## generated stores AI generated responses
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
## past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = []

# Layout of input/response containers
input_container = st.container()
colored_header(label='', description='', color_name='blue-70')
response_container = st.container()


def submit():
    print(st.session_state)
    # st.write(st.session_state.input)


# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", value="", key="input")
    return input_text


## Applying the user input box
with input_container:
    user_input = get_text()


# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    token = "Xwi1SlRZKnBb5sMAuBmNWcPfJfFfFjL9E3dpOFekhUuGmG-vMAi-oEW_dCKo22LcvyUYyg."
    bard = Bard(token=token, timeout=60)
    response = bard.get_answer(prompt)['content']
    # summarize the offerings for Station Labs, Inc. www.station.express in 2 lines
    print(response)
    # chatbot = hugchat.ChatBot()
    # response = chatbot.chat(prompt)
    return response


## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    print(user_input)
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        user_input = ''
        st.session_state.generated.append(response)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
