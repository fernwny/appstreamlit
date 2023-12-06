import streamlit as st
import openai
import json
import pandas as pd

# Get OpenAI API key from the user
user_api_key = st.sidebar.text_input("OpenAI API key", type="password")
export openai.api_key = user_api_key

prompt = """Act as an AI bookseller in English. You will receive a book title or author name or a short description of the book
and you should give a book title, a short description of the book and genre,
and a link to where it can be purchased and list the suggestions in a JSON array, one suggestion per line."""

st.title('Book seller')

st.markdown('Input the book title or author or description of the book that you want to buy. \nThe AI will give you suggestions on how the book is.')

# Get user input
user_input = st.text_area("Enter some text to correct:", "Your text here")
from openai import OpenAI

client = OpenAI()

completion = client.completions.create(model='curie')
print(completion.choices[0].text)
print(dict(completion).get('usage'))
print(completion.model_dump_json(indent=2))
# Streamlit form for submission
with st.form("my_form"):
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        messages_so_far = [
            {"role": "system", "content": prompt},
            {'role': 'user', 'content': user_input},
        ]

        try:
            # Use the OpenAI client consistently
            response = openai.Completion.create(
                engine="text-davinci-003",  # Use the appropriate engine name
                prompt=messages_so_far,
            )

            # Show the response from the AI in a box
            st.markdown('**AI response:**')
            suggestion_dictionary = response['choices'][0]['message']['content']

            sd = json.loads(suggestion_dictionary)
            suggestion_df = pd.DataFrame.from_dict(sd)
            st.table(suggestion_df)

        except Exception as e:
            st.error(f"An error occurred: {e}")



