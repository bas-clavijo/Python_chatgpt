import openai
import config

openai.api_key = config.api_key

openai.ChatCompletion.create(model="gpt-3.5-turbo")


