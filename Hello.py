

import streamlit as st
import openai
import json
import pandas as pd

# Get the API key from the sidebar called OpenAI API key
user_api_key = st.sidebar.text_input("OpenAI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)
prompt = """Act as a lyricist and write a song about a topic of your choice. The song should be at least 2 verses long.The song should be about the topic you choose. The song should have at least 3 words that have the same vowel sound.
list the first verse to ninth and the vocabulary of the song in a JSON array without index.
-first line should be the first verse
-second line should be the second verse
-third line should be the third verse
-fourth line should be the fourth verse
-fifth line should be the chorus
-sixth line should be the sixth verse
-seventh line should be the seventh verse
-eighth line should be the eighth verse
-ninth line should be the ninth verse
-tenth line should be the vocabulary in the verses with meaning

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

    if isinstance(sd, list):
        for i, verse in enumerate(sd[:-1], 1):  # Exclude the last item (vocab)
            st.write(f"Verse {i} {verse}")
    else:
        st.error("The response is not a list.")

   
    
 



    print (sd)
    suggestion_df = pd.DataFrame.from_dict(sd)
    print(suggestion_df)
  

    # Show the vocabulary to the user
    st.markdown('**Vocabulary:**')
    vocab = sd[9]
    if isinstance(vocab, dict):
        for i, (word, meaning) in enumerate(vocab.items(), 1):
            st.write(f"{i}. {word} - {meaning}")
    else:
        vocab_str = str(vocab).strip('[]').replace(',', '\n')
        vocab_list = vocab_str.split('\n')
        for i, item in enumerate(vocab_list, 1):
            st.write(f"{i}. {item.strip()}")


   
