from flask import Flask, jsonify

app = Flask(__name__)

# topics available
topics = [
    {
        'topic': 'Python',
        'note': ['Python is an interpreted high-level programming language for general-purpose programming.']
    },
    {
        'topic': 'Java',
        'note': ['Java is a general-purpose computer-programming language.']
    }
]

# topics subscribed by the subscriber
sub_topics = []

# topics registered by the publisher
pub_topics = []

#Register/Unregister a subscriber to a topic - can be a string
#Register/Unregister a publisher to a topic
#Publish a note to a topic
#Receive a published note as a subscriber

#Show all topics
@app.route('/topics')
def get_topics():
    return jsonify({'topics': topics})

app.run(port=5000)
