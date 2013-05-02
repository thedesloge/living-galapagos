// Setup your quiz text and questions here

// NOTE: pay attention to commas, IE struggles with those bad boys

var quizJSON = {
    "info": {
        "name":    "Darwin's Galapagos",
        "main":    "<p>Want to become a scientific explorer like Charles Darwin? Take this quiz and you'll be on your way!</p>",
        "results": "<h5>Learn More</h5><p>Go to the Living Galapagos home page to hear stories about the Galapagos islands in the wake of Charles Darwin's important discoveries.</p>",
        "level1":  "Super Researcher",
        "level2":  "Intelligent Assitant",
        "level3":  "Adventurous Explorer",
        "level4":  "Enthusiastic Student",
        "level5":  "Tortoise at a Computer" // no comma here
    },
    "questions": [
        { // Question 1
            "q": "What islands did Darwin visit?",
            "a": [
                {"option": "Baltra, Floreana and Santa Cruz",      "correct": false},
                {"option": "Bartolome, Pinta, Santa Cruz and Espanola",      "correct": false},
                {"option": "San Cristobal, Isabela, Floreana and Santiago",    "correct": true}// no comma here
            ],
            "correct": "<p><span>Correct!</span>You charted the same route as Darwin did.</p>",
            "incorrect": "<p><span>Almost!</span>Darwin visited the islands of San Cristobal, Isabela, Floreana and Santiago.</p>" // no comma here
        },
        { // Question 2
            "q": "What type of bird did Darwin first notice had different species on each island?",
            "a": [
                {"option": "Finch",    "correct": false},
                {"option": "Mockingbird",    "correct": true},
                {"option": "Thrush",     "correct": false}// no comma here
            ],
            "correct": "<p><span>Good job!</span> The islands contained three different species of mockingbird, even though they had similar environments.</p>",
            "incorrect": "<p><span>Not quite.</span> The islands contained three different species of mockingbird.</p>" // no comma here
        },
        { // Question 3
            "q": "Who helped Darwin correctly identify the finches he had collected on the islands?",
            "a": [
                {"option": "John Gould",    "correct": true},
                {"option": "John Gold",    "correct": false},
                {"option": "Joseph Hooker",     "correct": false}// no comma here
            ],
            "correct": "<p><span>Right!</span> John Gould realized that some of the birds Darwin had collected were 12 new species of ground finch.</p>",
            "incorrect": "<p><span>Not quite.</span> It was John Gould who identified the 12 new species of ground finch that Darwin had collected.</p>" // no comma here
        },{ // Question 4
            "q": "True or False: are there any native species in the Galapagos islands?",
            "a": [
                {"option": "True",    "correct": false},
                {"option": "False",     "correct": true}// no comma here
            ],
            "correct": "<p><span>Great job!</span>Plants and animals arrived to the Galapagos by air or sea.</p>",
            "incorrect": "<p><span>Nope!</span> There are no native species in the Galapagos, all plants and animals arrived by air or sea.</p>" // no comma here
        },
        { // Question 5
            "q": "When was <i>On the Origin of the Species</i> published?",
            "a": [
                {"option": "1860",        "correct": false},
                {"option": "1859",           "correct": true},
                {"option": "1858",  "correct": false}// no comma here
            ],
            "correct": "<p><span>Correct!</span></p>",
            "incorrect": "<p><span>Incorrect.</span> The book was published in 1859.</p>" // no comma here
        }
    ]
};