import streamlit as st
import json
import pandas as pd
import openai
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
    prompt = """Act as an AI songswriter and generate lyrics for a song. You will type the key words then the AI will generate the lyrics for you like this:    Keywords: love, hate, life, death, war, peace, etc.
    The AI will generate the next 5 lines of the song, and you will choose the best one.
    Each line will be generated based on the previous line
    and each line shoud have 10 words. the lyrics should have 3-5 verses and 3 choruses and the song should have a title. """
    st.write("AUTO Songwriter You will type keywords and the AI will generate the lyrics for you.")
    # Get the user input
    user_input = st.text_input("Enter the keywords for the song lyrics", "You text here")
    # Check if the user input is provided
    if not user_input:
        st.warning("Please enter the keywords for the song lyrics.")
    else:
        try:
            # Set the parameters
            client = OpenAI()

            completion = client.completions.create(model='curie')
            print(completion.choices[0].text)
            print(dict(completion).get('usage'))
            print(completion.model_dump_json(indent=2))
            if "choices" in response and response["choices"]:
                # Extract lyrics and title from the response
                generated_text = response.choices[0].text
                title = response.choices[1].text

                # Display the generated lyrics
                st.write("Lyrics:")
                st.success(generated_text)
    
                # Display the generated title
                st.write("Title:")
                st.success(title)

            else:
                    st.error("No choices found in the OpenAI response.")

        except Exception as e:
            # Handle any exception here
            # Handle any exception he
            st.error(f"An error occurred: {e}")

    st.write("Lyrics have been successfully generated.")
