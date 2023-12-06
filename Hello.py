
import streamlit as st
import openai
import json
import pandas as pd
import time


try:
    # Your OpenAI API request
    response = openai.Completion.create(
        # Your request parameters
    )
except openai.error.APIConnectionError as e:
    print(f"API Connection Error: {e}")
except openai.error.APIRemovedInV1 as e:
    print(f"API Removed in V1 Error: {e}")
    # Handle the error or log it appropriately
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    # Handle other types of errors here
else:
    # Handle success here
    print("Success!")
    print(response)
user_api_key = st.sidebar.text_input("OpenAI API key", type="password")
client = openai.OpenAI(api_key=user_api_key)

prompt = """Act as an AI bookseller in English. You will receive a book title or author name or a short description of the book
and you should give a book title, a short description of the book and genre ,
 and a link to where it can be purchased and list the suggestions in a JSON array, one suggestion per line."""

st.title('Book seller')


st.markdown('Input the book title or author or description of book that you want to buy. \n\The AI will give you suggestions on how The book is.')


user_input = st.text_area("Enter some text to correct:", "Your text here")



# submit button after text input

if st.button('Submit'):
    messages_so_far = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': user_input},
    ]
    response = client.chat.completions.create(
        model="davinci",
        messages=messages_so_far
    )
    # Show the response from the AI in a box
    st.markdown('**AI response:**')
    suggestion_dictionary = response.choices[0].message.content


    sd = json.loads(suggestion_dictionary)

    print (sd)
    suggestion_df = pd.DataFrame.from_dict(sd)
    print(suggestion_df)
    st.table(suggestion_df)
