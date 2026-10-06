from PySide6.QtWidgets import *

import os#for connection to groq
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
client=Groq(api_key=api_key)


app=QApplication([]) #initialize gui application ; handles mouse and keyboard
window=QMainWindow() #main window bna skte ho
window.setWindowTitle("AI Chat Assistant") #title of window

window.resize(600, 400)


chat_box=QTextEdit() #chat messages dikhane ke liye text box banana
central_widget=QWidget()

#container ko main window ka central widget banana
window.setCentralWidget(central_widget)

#widgets ko upar se neeche arrange karne ke liye layout banana
main_layout=QVBoxLayout()
central_widget.setLayout(main_layout)

main_layout.addWidget(chat_box)#chat box ko main layout me add krna

input_box=QLineEdit()#user message type karne ke liye input box

send_button=QPushButton("Send")#message send karne ke liye button


def send_message(): # when send click then this function runs
    message=input_box.text()

    # connection to groq
    response=client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role":"user","content":message}]
    )

    ai_reply=response.choices[0].message.content

    chat_box.append("You: " + message)#questions and answer
    chat_box.append("AI: " + ai_reply)

    input_box.clear()


send_button.clicked.connect(send_message)

bottom_layout=QHBoxLayout()#input box aur send button ko ek row me rakhne ke liye

bottom_layout.addWidget(input_box)#input box ko bottom layout me add krna

bottom_layout.addWidget(send_button)#send button ko button layout me add krna

main_layout.addLayout(bottom_layout)#bottom row ko main layout me add krna


#input box me hint dikhana
input_box.setPlaceholderText("Type your message.........")
chat_box.setReadOnly(True)

window.show()
app.exec()

