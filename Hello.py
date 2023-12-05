# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


import openai
import json
import pandas as pd
user_api_key = st.sidebar.text_input("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", type="password")
client = openai.OpenAI(api_key=user_api_key)

prompt = """Act as an AI writing tutor in English. 
You will receive a first sentence and you should give suggestions on how to improve it. 
List the suggestions in a JSON array, one suggestion per line. Each suggestion should have 3 fields: - "before" - the text before the suggestion - "after" - the text after the suggestion - "category" - the category of the suggestion one of "grammar", "style", "word choice", "other" - "comment" - a comment about the suggestion Don't say anything at first. 
Wait for the user to say something."""  

st.title('Writing tutor')
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

if __name__ == "__main__":
    run()
