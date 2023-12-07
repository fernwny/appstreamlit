import streamlit as st
import openai
import json
import pandas as pd

# Get OpenAI API key from the user
user_api_key = st.sidebar.text_input("OpenAI API key", type="password")

# Check if the API key is provided
if not user_api_key:
    st.warning("Please enter your OpenAI API key.")
else:
    # Display the entered API key securely
    st.text("Entered API Key: ************" + user_api_key[-4:])
    # Set the OpenAI API key
    openai.api_key = user_api_key
    prompt = """Act as an AI songwriter and generate lyrics for a song. 
    You will receive a title and a few keywords and you should generate the lyrics for the song. the song should be at least 25 words long.
    List the suggestions in a JSON array, one suggestion per line.
    Each suggestion should have 3 fields:
    - "keywords" - the keywords for the song
    - "title" -    the title of the song
    - "lyrics" -   the lyrics of the song
    Don't say anything at first. Wait for the user to say something
    """
    st.write("AUTO Songwriter You will type keywords and the AI will generate the lyrics for you.")
    # Get the user input
    user_input = st.text_input("Enter the keywords for the song lyrics", "You text here")
    # Check if the user input is provided
    if not user_input:
        st.warning("Please enter the keywords for the song lyrics.")
    else:
        try:
            # Set the parameters
            response = openai.completions.create(
                model='text-davinci-002',
                prompt=prompt + user_input,
                temperature=0.7,
                max_tokens=300,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=["\n", " Lyrics:", " Title:"]
            )
            # Check if the response is successful
            if response.choices and response.choices[0].text.strip():
                # Display the response
                st.markdown('**AI response:**')
                try:
                    sd = json.loads(response.choices[0].text)
                    suggestion_df = pd.DataFrame.from_dict(sd)
                    st.table(suggestion_df)
                except json.JSONDecodeError:
                    st.error("The response is not a valid JSON string.")
            else:
                st.error("No choices found in the OpenAI response.")
        except Exception as e:
            # Handle any exception here
            st.error(f"An error occurred: {e}")

        st.write("Lyrics have been successfully generated.")
