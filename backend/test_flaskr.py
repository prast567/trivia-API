import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia"
        #self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        self.database_path = "postgres://postgres:kumar@123@localhost:5432/trivia2"

        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.sample_question = {
            'question': 'What is the color of sky',
            'answer': 'blue',
            'category': 1,
            'difficulty': 1
        }
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_insert_question(self):
        response = self.client().post('/questions', json=self.sample_question,
                                 content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_insert_question_with_nodata(self):
        sample_question = {
            'question': '',
            'answer': '',
            'difficulty': None,
            'category': None,
        }

        # make request and process response
        response = self.client().post('/questions', json=sample_question)
        data = json.loads(response.data)

        # Assertions
        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)

    def test_search(self):

        searchTerm = {
            'searchTerm': 'color of sky',
        }

        response = self.client().post('/questions/search', json=searchTerm)
        data = json.loads(response.data)

        # Assertions
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_search_with_emptysearch_term(self):

        request_data = {
            'searchTerm': '',
        }

        # make request and process response
        response = self.client().post('/questions/search', json=request_data)
        data = json.loads(response.data)

        # Assertions
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource could not be found")

    def test_get_questions_by_category(self):

        response = self.client().get('/categories/1/questions')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_questions_by_category_fail(self):

        response = self.client().get('/categories/1000/questions')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)

    def test_delete_question(self):

        response = self.client().delete('/questions/1')
        data = json.loads(response.data)

        self.assertEqual(data['success'], False)

    def test_delete_question_fail(self):

        response = self.client().delete('/questions/1000')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)


    def test_retrieve_questions(self):
        response = self.client().get('/questions')
        self.assertEqual(response.status_code, 200)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()