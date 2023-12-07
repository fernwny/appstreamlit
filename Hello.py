import streamlit as st
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
    prompt = """Act as an AI songwriter and generate lyrics for a song. You will type the key words then the AI will generate the lyrics for you like this: Keywords: love, hate, life, death, war, peace, etc.
    The AI will generate the next 5 lines of the song, and you will choose the best one.
    Each line will be generated based on the previous line, and each line should have 10 words. The lyrics should have 3-5 verses and 3 choruses, and the song should have a title. """
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
            if response.choices:
                generated_text = response.choices[0].text
                st.write("Lyrics:")
                st.success(generated_text)
            
                # Display the generated title
                st.write("Title:")
                st.success(generate_text)
            else:
                st.error("No choices found in the OpenAI response.")
        except Exception as e:
            # Handle any exception here
            st.error(f"An error occurred: {e}")
        
        st.write("Lyrics have been successfully generated.")
        

