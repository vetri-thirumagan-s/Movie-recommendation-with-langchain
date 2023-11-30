from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()

llm=GooglePalm(temperature=0.4)

def recommend(prompt):
    movie_input=prompt.strip()thunivu

    prompt_template = PromptTemplate.from_template(
        "give me a ten movie recommendation similar to {movie_name} based on its story summary, genre, ratings and it would be on same language and sort them by the rating and just give the movie name and year only"
    )
    input=prompt_template.format(movie_name=movie_input)
    output=llm(input)
    return output