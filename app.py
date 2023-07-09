from flask import Flask, render_template, request, session
from story_generator import StoryGenerator
# from flask import Flask, render_template, request, session, redirect, url_for, jsonify


app = Flask(__name__)
app.secret_key = 'your secret key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # extract the inputs
        age = request.form.get('age')
        gender = request.form.get('gender')
        # length = request.form.get('length')

        # save in session
        session['age'] = age
        session['gender'] = gender
        # session['length'] = length

        # generate the initial story and options
        story, options = StoryGenerator(age, gender).generate_story_and_options()
        # story, options = StoryGenerator(age, gender, length).generate_story_and_options()

        return render_template('story.html', story=story, options=options)

    else:
        return render_template('index.html')


@app.route('/story', methods=['GET', 'POST'])
def story():
    if request.method == 'POST':
        # get the chosen option from the form
        chosen_option = request.form.get('option')
        # print(chosen_option)        
        # You will also want to pass in the user's age and gender here, which you will 
        # need to get from the form as well or from the session.
        age = request.form.get('age')
        gender = request.form.get('gender')
        # length = request.form.get('length')

        if chosen_option is None:
            # this is the first request, no option was chosen yet
            chosen_option = " "

        # use the chosen option to influence the next story prompt
        story, options = StoryGenerator(age, gender).generate_story_and_options(chosen_option)
        # story, options = StoryGenerator(age, gender, length).generate_story_and_options(chosen_option)
        
        return render_template('story.html', story=story, options=options)
        # return jsonify({'story': story, 'options': options})


    else:
        # Handle initial page load...
        age = request.form.get('age')
        gender = request.form.get('gender')
        # length = request.form.get('length')
        sg = StoryGenerator(age, gender)
        # sg = StoryGenerator(age, gender, length)
        story, options = sg.generate_story_and_options("Once upon a time")
        return render_template('story.html', story=story, options=options)

if __name__ == "__main__":
    app.run(debug=True)
