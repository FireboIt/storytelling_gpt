import openai
# from dotenv import load_dotenv
import os
# import sys
# print(sys.executable)


class StoryGenerator:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender
        # load_dotenv()
        openai.api_key = os.getenv('OPENAI_KEY')

    def generate_story_and_options(self, chosen_option):

        if chosen_option == " ":
            global story
            story = "Once upon a time there was a "
        else:
            story = story + " " + chosen_option

        prompt = f"Fill the next sentence to make a story - only fill one sentence - the prompt for the story starts after a colon : {story}"
        print(prompt)
        response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          temperature=1.0,
          max_tokens=2000,
          n=3
        )

        # print(response)

        options = [None]*3

        tmp = response.choices[0].text.strip().partition('.')[0]
        if len(tmp)<3:
            tmp = response.choices[0].text.strip().partition('.')[1]
        options[0] = tmp+'. '

        tmp = response.choices[1].text.strip().partition('.')[0]
        if len(tmp)<3:
            tmp = response.choices[1].text.strip().partition('.')[1]
        options[1] = response.choices[1].text.strip().partition('.')[0]+'.'

        tmp = response.choices[2].text.strip().partition('.')[0]
        if len(tmp)<3:
            tmp = response.choices[2].text.strip().partition('.')[1]
        options[2] = response.choices[2].text.strip().partition('.')[0]+'.'

        return story, options
