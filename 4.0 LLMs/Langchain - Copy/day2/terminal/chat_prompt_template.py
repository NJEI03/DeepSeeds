from langchain_core.prompts import ChatPromptTemplate
from config import load_google_chat_model

chat_model = load_google_chat_model()

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an {expert} in {domain}, please break down any questions the user is going to ask you in a clear and coincise manner with real world analogies"),
    ("user", "Please {expert} help me with my questions"),
    ("ai", "Sure {name}, I can do just that"),
    ("user", "{user_input}")
])

prompt = chat_prompt.format_messages(
    expert="GEN AI Engineer",
    domain="Artificial Intelligence",
    name="Mben",
    user_input="Please explain news on sports"
)

for part in chat_model.stream(prompt):
    print(part.content, end="", flush=True)