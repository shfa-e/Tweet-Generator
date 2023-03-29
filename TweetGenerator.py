import openai
import streamlit as st

# Set up your OpenAI API key here
openai.api_key = "YOUR_API_KEY_GOES_HERE"

# Define the prompt that the model will use to generate tweets
prompt = "Generate a tweet about:"

# Define the types of content that the user can choose from
content_types = ["News", "Sports", "Entertainment", "Technology", "Politics"]

content = "Enter the content of the tweet you want to generate"

# Define the OpenAI model to use for generating the tweets
model_engine = "text-davinci-002"

# Define the maximum length of the generated tweet
max_length = 280

# Define the function that will generate the tweet
def generate_tweet(prompt, content_type, content, model_engine, max_length):
    prompt += content + " " + content_type + " "
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_length,
        n=1,
        stop=None,
        temperature=0.5,
    )
    tweet = response.choices[0].text.strip()
    return tweet

# Define the Streamlit app
def app():
    st.title("Tweet Generator")

    # Ask the user to choose a content type
    content_type = st.selectbox("Choose a content type:", content_types)
    content = st.text_input("Enter the content of the tweet you want to generate")
    if st.button("Generate"):
        # Generate the tweet
        tweet = generate_tweet(prompt, content_type, content, model_engine, max_length)

        # Display the tweet
        st.write("Here's your tweet:")
        st.write(tweet)

# Run the Streamlit app
if __name__ == "__main__":
    app()
