"""This code is for an advanced FAQ chatbot for mohawk college, this Bot can be used as a helper bot for
software development students. This uses OpenAi's completion and chat API to generate responses to user's utterance.
This bot can be used in shell or on discord channel.

Sam Scott. EDIT: Sara Zendehboodi. EDIT: Hitarth Patel, Mohawk College, 2024"""

import discord
from openai import OpenAI

"""providing OpenAi API Key"""
client=OpenAI(api_key = "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")


class MyClient(discord.Client):
    """Class to represent the Client (bot user)"""

    def __init__(self):
        """This is the constructor. sets up discord and dialog management."""
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        ##dialog Management: Array is used to store all Conversations (Role Based).
        self.dialog = [
            {"role":"system", "content":"You are a Software Devloper Bot at Mohawk College. Your name is Sof†Bot, that answers questions of software developing students. Explain their questions in easy words as they are beginners. You are allowed to answer to greatings but if the user ask unrelated question to software development, apologize softly and tell them about your knowledge area and sometimes you may joke arround"},
        ]

    async def on_ready(self):
        """Called when the bot is fully logged in. prints success message for discord"""

        print('Logged on as', self.user)
        ##provinding discord link when server is ready
        print("Open the following link to access the discord server:")
        print("https://discord.com/oauth2/authorize?client_id=1302428443236892822&permissions=0&integration_type=0&scope=bot")


    async def on_message(self, message):
        """Called whenever the bot receives a message. The 'message' object
        contains all the pertinent information from discord."""

        # avoid responding to itself
        if message.author == self.user:
            return

        utterance = message.content     #getting the utterance from discord
        if "hey" in utterance.lower() or "softbot" in utterance.lower():
            response = self.get_response(utterance)     #proccessing and getting the response
            await message.channel.send(response)    #sending the response to user via discord


    def get_response(self, utterance):
        """this method performs 2 API calls and generates response in 2 stages.
            the first call will generate explanation of the utterance
            the second call will generate the answer to the utterance
            with this all the conversation is appended to the 'self.dialog' for dialog management"""

        self.dialog.append({"role":"user", "content":utterance})    #appending Utterance as content form user

        utterance = "What is the question asking, don't answer the question : '" + utterance + "'"      #getting prompt ready for 1st api call

        ##This is Completion Api, it takes the above prompt and generates explanation on what the user wants(utterance).
        utterance_explanation = client.completions.create(model="gpt-3.5-turbo-instruct", prompt= utterance, max_tokens=100, temperature=0.1)

        self.dialog.append({"role":"system", "content":utterance_explanation.choices[0].text})      #appending utterance_explanation as content form system

        ##This is Chat Api, it can take the dialog array so that it can proceess acording to the previous conversation and generate response for the utterance.
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages = self.dialog, temperature=0.8, max_tokens=150)

        self.dialog.append({"role": response.choices[0].message.role, "content":response.choices[0].message.content})   #appending response as content form assistant

        return response.choices[0].message.content      #returns response


    ## Main Function
    def main(self):
        """Implements a chat session in the shell."""

        print("Hello! I know stuff about Software Development. When you're done talking, just say 'goodbye'.")

        ##the code will accept utterance till the user say "goodbye"
        while True:
            utterance = input(">>> ")()
            if utterance == "goodbye": break        #exiting the loop to end the program

            response = self.get_response(utterance)     #getting the response
            print("Assistant: " + response)     #printing the response on shell

        print("Nice talking to you!")       #exit message


## Set up and log in on discord
discord_client = MyClient()
token = "MTMwMjQyODQ0MzIzNjg5MjgyMg.GMlNHY.quXRrocGnHZU2DAdRp5GVrPZKUdN3v9jVATd5I"      ##this is discord token

print("Select bot mode: 'use shell' or 'use discord'")
#discord_client.main()
bot_mode = input(">>> ")
if bot_mode == "use shell":
    discord_client.main()
elif bot_mode == "use discord":
    discord_client.run(token)
else:
    print("invalid bot mode!!!")