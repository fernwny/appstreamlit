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
    # Set the OpenAI API key
    openai.api_key = user_api_key

    prompt = """Act as an AI songswriter and generate lyrics for a song. You will type the key words then the AI will generate the lyrics for you.
    """
    st.write(prompt)
    # Get the user input
    user_input = st.text_input("Enter the keywords for the song lyrics", "I love you")
    # Check if the user input is provided
    if not user_input:
        st.warning("Please enter the keywords for the song lyrics.")
    else:
        # Set the parameters
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt + user_input,
            temperature=0.7,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["\n", " Lyrics:", " Title:"]
        )
        # Display the generated lyrics
        st.subheader("Generated Lyrics")
        st.write(response["choices"][0]["text"])
        # Display the generated lyrics in a file
        st.subheader("Generated Lyrics in a File")
        # Get the file name from the user
        file_name = st.text_input("Enter the file name", "lyrics.txt")
        # Check if the file name is provided
        if not file_name:
            st.warning("Please enter the file name.")
        else:
            # Save the generated lyrics in a file
            with open(file_name, "w") as f:
                f.write(response["choices"][0]["text"])
            # Display the file content
            with open(file_name, "r") as f:
                st.write(f.read())
            
