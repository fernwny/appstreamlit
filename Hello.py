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

    # Prompt for song lyrics
    prompt = f"""
    You are an AI songwriter. Generate lyrics for a song based on the user's input.

    System: Act as an AI songwriter and generate lyrics for a song.
    User: {user_input}
    """

    # Get the user input
    user_input = st.text_input("Enter the keywords for the song lyrics", "You text here")

    # Check if the user input is provided
    if not user_input:
        st.warning("Please enter the keywords for the song lyrics.")
    else:
        try:
            # Set the parameters
            response = openai.completions.create(
                engine="text-davinci-003",
                prompt=prompt,
                temperature=0.7,
                max_tokens=300,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=["\n", " Lyrics:", " Title:"]
            )

            # Check if the response is successful
            if response and response.choices and response.choices[0].text.strip():
                # Display the response
                st.markdown('**AI response:**')
                st.text(response.choices[0].text.strip())
            else:
                st.error("No valid choices found in the OpenAI response.")
        except Exception as e:
            # Handle any exception here
            st.error(f"An error occurred: {e}")

        st.write("Lyrics have been successfully generated.")
