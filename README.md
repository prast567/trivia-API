# trivia-API

# Full Stack API Final Project

## Full Stack Trivia
In this project we will be working with trivia app to make a quiz playing application. The application will contain:

1) Display questions - both all questions and by category. Questions will show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

## Installing dependencies
The starter dir contains a requirements.txt file which can be used to install all the dependecies.
command:- pip install -r requirements.txt

## Running the Server
To run
* For windows
    * set FLASK_APP=flaskr
    * set FLASK_ENV=development
    * flask run
* For linux
    * export FLASK_APP=flaskr
    * export FLASK_ENV=development
    * flask run
    
## Endpoints
* GET /categories
    * Returns all the categories
    * URI:- http://127.0.0.1:5000/categories
    * Response
        * {
        "categories": {
            "1": "history",
            "2": "science"
            },
        "success": true
            }
            
* GET /questions
    * Returns a list of questions(10 at a time)
    * URI:- http://127.0.0.1:5000/questions
    * Response
        * {
            "categories": {
                "1": "history",
                "2": "science"
            },
            "questions": [
                {
                    "answer": "fine1",
                    "category": "1",
                    "difficulty": 1,
                    "id": 3,
                    "question": "How are you2"
                },
                {
                    "answer": "fine4",
                    "category": "1",
                    "difficulty": 1,
                    "id": 4,
                    "question": "How are you4"
                },
                {
                    "answer": "fine5",
                    "category": "1",
                    "difficulty": 1,
                    "id": 5,
                    "question": "How are you5"
                },
                {
                    "answer": "fine6",
                    "category": "1",
                    "difficulty": 1,
                    "id": 6,
                    "question": "How are you6"
                },
                {
                    "answer": "fine7",
                    "category": "1",
                    "difficulty": 1,
                    "id": 7,
                    "question": "How are you7"
                },
                {
                    "answer": "fine8",
                    "category": "1",
                    "difficulty": 1,
                    "id": 8,
                    "question": "How are you8"
                },
                {
                    "answer": "fine9",
                    "category": "1",
                    "difficulty": 1,
                    "id": 9,
                    "question": "How are you9"
                },
                {
                    "answer": "fine10",
                    "category": "2",
                    "difficulty": 1,
                    "id": 10,
                    "question": "How are you10"
                },
                {
                    "answer": "fine11",
                    "category": "2",
                    "difficulty": 1,
                    "id": 11,
                    "question": "How are you11"
                },
                {
                    "answer": "fine12",
                    "category": "2",
                    "difficulty": 1,
                    "id": 12,
                    "question": "How are you12"
                }
            ],
            "total_questions": 10
        }
        
* DELETE /questions/<int:id>
    * Deletes question with given ID.
    * URI:- http://127.0.0.1:5000/questions/12
    * Response
        * {
                "id": 12,
                "message": "Question deleted successfully ",
                "success": true
            }
            
* POST /questions
    * Inserting a new question.
    * URI:- http://127.0.0.1:5000/questions
    * JSON file format
        * {
            "answer": "fine50",
            "category": "2",
            "difficulty": 1,    
            "id": 10,
            "question": "How are you50"
            }
    * Response
        * {
            "question": {
                "answer": "fine50",
                "category": "2",
                "difficulty": 1,
                "id": 17,
                "question": "How are you50"
                        },
            "success": true
         }
        
* POST /quizzes
    * Getting the questions based on category to play quiz
    * URI:- http://127.0.0.1:5000/quizzes
    * JSON file format
        * {
           
           "previous_questions":[1,2],
           "quiz_category":2
            }
    * Response
        * {
        "quizzes": [
            {
                "answer": "fine10",
                "category": "2",
                "difficulty": 1,
                "id": 10,
                "question": "How are you10"
            },
            {
                "answer": "fine11",
                "category": "2",
                "difficulty": 1,
                "id": 11,
                "question": "How are you11"
            },
            {
                "answer": "fine12",
                "category": "2",
                "difficulty": 1,
                "id": 12,
                "question": "How are you12"
            },
            {
                "answer": "fine13",
                "category": "2",
                "difficulty": 1,
                "id": 13,
                "question": "How are you13"
            },
            {
                "answer": "fine14",
                "category": "2",
                "difficulty": 1,
                "id": 14,
                "question": "How are you14"
            }
        ]
        }

* POST /search
    * Searching for questions based on key terms
    * URI:- http://127.0.0.1:5000/search
    * JSON file format
        * {
           "searchTerm":"you5"
        }
    * Response
        * {
            "categories": {
                "1": "history",
                "2": "science"
            },
            "questions": [
                {
                    "answer": "fine5",
                    "category": "1",
                    "difficulty": 1,
                    "id": 5,
                    "question": "How are you5"
                }
            ],
            "total_questions": 1
            }
    
* GET /categories/<int:category_id>/questions
    * Get questions based on categories
    * URI:- http://127.0.0.1:5000/categories/2/questions 
    * Response
                {
            "Number_of_questions": 4,
            "current_category": "2",
            "questions": [
                {
                    "answer": "fine10",
                    "category": "2",
                    "difficulty": 1,
                    "id": 10,
                    "question": "How are you10"
                },
                {
                    "answer": "fine11",
                    "category": "2",
                    "difficulty": 1,
                    "id": 11,
                    "question": "How are you11"
                },
                {
                    "answer": "fine13",
                    "category": "2",
                    "difficulty": 1,
                    "id": 13,
                    "question": "How are you13"
                },
                {
                    "answer": "fine14",
                    "category": "2",
                    "difficulty": 1,
                    "id": 14,
                    "question": "How are you14"
                }
            ]
        }
    
