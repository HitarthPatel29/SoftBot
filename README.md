# SoftBot V2

## Description of the Bot:
The **SoftBot V2** is an advanced version of an FAQ chatbot. This bot can be used as a helper bot for software development students to ask software development questions. This bot is designed to be a bot for **students**, hence, it is able to answer questions in a much simpler way for beginners to understand better.

- The Bot answers to any text with ‘Hey_’, ‘Softbot’ or ‘Hey Softbot’.

### Invitation Link:
[Click here to invite the bot](https://discord.com/oauth2/authorize?client_id=1302428443236892822&permissions=0&integration_type=0&scope=bot)

---

## API Calls:

### 1) Completion API Call:
With this API, I am getting the explanation of the utterance. This is helpful for:
- Expanding the question
- Getting the tone
- Correcting typing mistakes
- Providing an overall explanation of the user’s utterance.

The output will be used to generate more accurate responses.

#### **Settings:**
```
model: "gpt-3.5-turbo-instruct"
max tokens: 50
temperature: 0.1
```
## 2) Second API Call: Chat API

With this one, I am getting the response to the **Utterance**. This will use all the past conversations for **dialog management**. 

The Chat API supports **role-based prompts**,
- The current **Utterance** is passed as content from **‘User’**.
- Its **explanation** (from the first API call) is passed as content from **‘System’**
- All the past conversations are also saved and passed on every API call to ensure **Dialog Management**

### **Settings:**
```yaml
model: "gpt-3.5-turbo"
max tokens: 150
temperature: 0.8
```
## Prompt Engineering
- For the first Api call, I am giving order to explain the utterance but at the same time restraining it to not give the answer to question.
- For the second one, I am prompting context based. I am telling it to be a Software Developing Bot at mohawk college. And then constraining it to give simpler response for students and to not give response to any irrelevant questions except for greetings rather refuse them to answer any irrelevant questions politely. 


## Performance
- It close to perfect for now, cause it is already capable of apologizing for irrelevant question in a very polite way and sometimes it even reply with funny comment like in the picture:
<div align="center">
  <img alt="image" src="https://github.com/user-attachments/assets/8a57b34c-88aa-4bad-9f70-d0ab8da65d4d" />
  <img alt="image" src="https://github.com/user-attachments/assets/60475fab-b96c-40ae-aa1b-c703424fea63" />
</div>  

- It gives sarcastic answers but still always focuses on Software development.
- To improve this further, I would like to work on providing some visual explanation like a simple diagram or table something.
  
<div align="center">
 <img alt="image" src="https://github.com/user-attachments/assets/5c66b3a7-7185-4101-b763-527781efb262" />
</div>  

- The Bot is already capable of generating a special text box for code snippets but when the user asks it just decline that it cannot. 

