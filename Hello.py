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
    prompt = """Act as an AI songswriter and generate lyrics for a song. You will type the key words then the AI will generate the lyrics for you.
    """
    st.write(prompt)
    # Get the user input
    user_input = st.text_input("Enter the keywords for the song lyrics", "I love you")
    # Check if the user input is provided
    if not user_input:
        st.warning("Please enter the keywords for the song lyrics.")
    else:
        try:
            # Set the parameters
            response = openai.completions.create(
                model ="text-davinci-002",
                prompt=prompt + user_input,
                temperature=0.7,
                max_tokens=100,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=["\n", " Lyrics:", " Title:"]
            )

            # Check for API errors
           if "choices" in response and response["choices"]:
                # Display the generated lyrics
                st.subheader("Generated Lyrics")
                # Display the generated lyrics
                st.write(response["choices"][0]["message"]["content"])
            else:
                st.error(f"API Error: {response.get('error', {}).get('message', 'Unknown error')}")

                # Display the generated lyrics in a file
            st.subheader("Generated Lyrics in a File")
                # Get the file name from the user
            file_name = st.text_input("Enter the file name", "lyrics.txt")
                # Check if the file name is provided
                # Check if the file name is provided
                if file_name:
                    # Save the generated lyrics in a file
                    with open(file_name, "w") as f:
                        f.write(response["choices"][0]["text"])
                    # Display the file content
                    with open(file_name, "r") as f:
                        st.write(f.read())
            else:
                st.error(f"API Error: {response.get('error', {}).get('message', 'Unknown error')}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
