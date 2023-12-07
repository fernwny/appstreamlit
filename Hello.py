

import streamlit as st
import openai
import json
import pandas as pd

# Get the API key from the sidebar called OpenAI API key
user_api_key = st.sidebar.text_input("OpenAI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)
prompt = """Act as an AI songwriter in English. You will receive text input from a user and you should respond with a song. The user will then rate your song and give you feedback.
 You should use this feedback to improve your song. You will be scored on how well you can improve your song. The better you are at improving your song, the higher your score will be.
 list the songs you have written so far in a JSON array. Each song should be a JSON object with the following fields:
    - song: the song you wrote
    - rating: the rating the user gave your song
    - feedback: the feedback the user gave your song
    - score: the score you received for this song
    - suggestions: the suggestions the user gave you for this song



"""
st.title('Writing song')
st.markdown('Input the writing that you want to improve. \n\
            The AI will give you suggestions on how to improve it.')

user_input = st.text_area("Enter some text to correct:", "Your text here")


# submit button after text input
if st.button('Submit'):
    messages_so_far = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': user_input},
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
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

