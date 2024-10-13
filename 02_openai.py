from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''
[20:30, 12/6/2024] Subhajit: jo sunke coding ho sake?
[20:30, 12/6/2024] Rohan Das: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:30, 12/6/2024] Rohan Das: ye
[20:30, 12/6/2024] Rohan Das: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:31, 12/6/2024] Subhajit: This is hindi
[20:31, 12/6/2024] Subhajit: send me some english songs
[20:31, 12/6/2024] Subhajit: but wait
[20:31, 12/6/2024] Subhajit: this song is amazing
[20:31, 12/6/2024] Subhajit: so I will stick to it
[20:31, 12/6/2024] Subhajit: send me some english song also
[20:31, 12/6/2024] Rohan Das: hold on
[20:31, 12/6/2024] Subhajit: I know what you are about to send
[20:32, 12/6/2024] Subhajit: 😂😂
[20:32, 12/6/2024] Rohan Das: https://www.youtube.com/watch?v=ar-3chBG4NU
ye hindi English mix hai but best hai
[20:33, 12/6/2024] Subhajit: okok
[20:33, 12/6/2024] Rohan Das: Haan
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Subhajit who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Subhajit"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)