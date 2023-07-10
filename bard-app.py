import streamlit as st
from bardapi import Bard
from htmlTemplates import css, bot_template, user_template


if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


def handle_userinput(user_question):
    token = "Ygi1SjuTG12VYmLL5he9ui93b1-gSe0Cdbl1IS41l2yRbEWlShgGujF5y4LKDZK8h77ryw."
    bard = Bard(token=token, timeout=60)
    response1 = bard.get_answer(user_question)['content']
    if 'Response Error:' not in response1:
        response1 = 'Something went wrong, Please try again!'
    st.session_state.chat_history.append(user_question)
    st.session_state.chat_history.append(response1)

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message), unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Chat with bard",
                       page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Website Summarization")
    user_question = st.text_input("Put a website for summarization:")
    if user_question:
        handle_userinput(user_question)


if __name__ == '__main__':
    main()
