from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='Jarvis:latest', messages=[
  {
    'role': 'user',
    'content': 'como estas',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)
