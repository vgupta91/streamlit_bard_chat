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
.chat-message {
    padding: 0.5rem; 
    border-radius: 0.5rem; 
    display: inline-block;
    max-width: 450px;
}
.chat-message.user {
    background-color: #7b818e;
    float: right;
    margin-top: 20px;
    box-shadow: 0 1px 2px 0 rgba(60, 64, 67, 0.302), 0 1px 3px 1px rgba(60, 64, 67, 0.149);
}
.chat-message.bot {
    background-color: #969fb4;
    float: left;
    margin-top: 20px;
    box-shadow: 0 1px 2px 0 rgba(60, 64, 67, 0.302), 0 1px 3px 1px rgba(60, 64, 67, 0.149);
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
.stTextInput {
      position: fixed;
      bottom: 3rem;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user"> 
    <div class="message">{{MSG}}</div>
</div>
'''
