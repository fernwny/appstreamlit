

import streamlit as st
import openai
import json
import pandas as pd

# Get the API key from the sidebar called OpenAI API key
user_api_key = st.sidebar.text_input("OpenAI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)
prompt = """Act as a lyricist and write a song about a topic of your choice. The song should be at least 2 verses long.The song should be about the topic you choose. The song should have at least 3 words that have the same vowel sound.
list the topic, first verse to tenth verse but the sixth verse repeat the topic and the vocabulary of the song in a JSON array without index.
-second line should be the first verse of the song about the topic
-third line should be the second verse of the song about the topic 
-fourth line should be the third verse of the song about the topic
-fifth line should be the fourth verse of the song about the topic
-sixth line should include the topic in the verse
-seventh line should be the fifth verse of the song about the topic
-eighth line should be the sixth verse of the song about the topic
-ninth line should be the seventh verse of the song about the topic
-tenth line should be the vocabulary of the song and the meaning

"""

st.title("Lyricist")
st.markdown("This app uses the OpenAI API to generate lyrics based on a topic of your choice.")

# Get the topic from the user
topic = st.text_input("Topic", "ENTER TOPIC HERE")


if st.button('Submit'):
    messages_so_far = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': topic},
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_so_far
    )
    
    # Show the lyrics to the user
    st.markdown('**Lyrics:**')
    suggestion_dictionary = response.choices[0].message.content
    sd = json.loads(suggestion_dictionary)




    print (sd)
    suggestion_df = pd.DataFrame.from_dict(sd)
    print(suggestion_df)
    st.table(suggestion_df)



   

