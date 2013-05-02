// Setup your quiz text and questions here

// NOTE: pay attention to commas, IE struggles with those bad boys


// Set via json option or quizJSON variable (see slickQuiz-config.js)

var quizJSON = {
    "info": {
        "name":    "Know Your Invasive Species!",
        "main":    "<p>Combating invasive species is one of the biggest challenges facing the Galapagos Islands. Whether they were brought by humans or arrived to the islands accidentally by air or sea, invasive species threaten the already vulnerable natural ecosystem in the Galapagos. Although 95% of the islands' native species remain intact, a growing number invasive species threatens their environment.</p></br><p>Knowledge is the first step in protecting native species from invasive species. Can you spot the invasive species?</p>",
        "results": "<h5>Invasive Species in the Galapagos Today</h5><p>The good news is that eradication and restoration programs have eliminated many problems with invasive species -- but not all. As human activity in the Galapagos increases, so does the threat of invasive species. Keeping an eye on the Galapagos ecosystem will ensure that the islands remain a biological paradise.</p>",
        "level1":  "Endemic Species",
        "level2":  "Native Species",
        "level3":  "Practically a Native",
        "level4":  "Introduced Species",
        "level5":  "Invasive Species" // no comma here
    },
    "questions": [
        { // Question 1
            "q": "Which animal is invasive: a goat or an iguana?",
            "a": [
                {"option": "Goat",      "correct": true},
                {"option": "Iguana",     "correct": false} // no comma here
            ],
            "correct": "<p><span>Right, it's invasive!</span>Goats eliminate vegetation on the Galapagos, causing erosion and displacing native fauna.</p>",
            "incorrect": "<p><span>Nope - it's native!</span>Marine iguanas are the only oceangoing lizard in the world, and they can only be found in the Galapagos.</p>" // no comma here
        },
        { // Question 2
            "q": "Which is invasive: sea lions or guava?",
            "a": [
                {"option": "Sea Lion",    "correct": false},
                {"option": "Guava",   "correct": true} // no comma here
            ],
            "correct": "<p><span>Nice job!</span>Guava is an invasive plant that threatens native vegetation in the Galapagos.</p>",
            "incorrect": "<p><span>Not quite...</span>These playful creatures are all native.</p>" // no comma here
        },
        { // Question 3
            "q": "Which animal is invasive: a tortoise or a rat?",
            "a": [
                {"option": "Tortoise",        "correct": false},
                {"option": "Rat",   "correct": true} // no comma here
            ],
            "correct": "<p><span>It's invasive!</span>Rats were most likely brought to the Galapagos on pirate ships in the late 17th century. They carry a lot of diseases and threaten species of mice that are native to the Galapagos.</p>",
            "incorrect": "<p><span>Sorry, it's native!</span>Galapagos tortoises are one of two groups of giant tortoises left in the world. After being exploited by humans and introduced to invasive species, many are endangered or extinct.</p>" // no comma here
        },
        { // Question 4
            "q": "Which is invasive: penguins or blackberries?",
            "a": [
                {"option": "Penguins",    "correct": false},
                {"option": "Blackberries",     "correct": true} // no comma here
            ],
            "correct": "<p><span>Right!</span>Blackberries are an invasive species. They make farming difficult and compete with other native plant species.</p>",
            "incorrect": "<p><span>Wrong, it's native!</span>Galapagos penguins are the only species of penguin that live above the equator. They are currently listed as endangered.</p>" // no comma here
        },
        { // Question 5
            "q": "Which animal is invasive: a cat or a donkey?",
            "a": [
                {"option": "Cat",   "correct": true},
                {"option": "Donkey",  "correct": false} // no comma here
            ],
            "correct": "<p><span>Both are correct!</span>Feral cats became a huge problem on the island of Baltra, where they preyed on native marine iguanas. Donkeys were introduced by humans but soon reverted back to their wild state, causing visible damage to the ecosystem.</p>",
            "incorrect": "<p><span>Both are correct!</span>Feral cats became a huge problem on the island of Baltra, where they preyed on native marine iguanas. Donkeys were introduced by humans but soon reverted back to their wild state, causing visible damage to the ecosystem.</p>" // no comma here
        } // no comma here

    ]
};