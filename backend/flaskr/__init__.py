import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
#from starter.backend.models import  setup_db, Question, Category
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  """

  Creates and sets up a Flask application
  @param test_config: None
  @return: app
  """
  app = Flask(__name__)
  setup_db(app)

  CORS(app, resources={r"/api/*": {"origins": "*"}})

  @app.after_request
  def after_request(response):
    """

    @param response: HTTP headed
    @return: Add proper permissions to the HTTP header
    """
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  @app.route('/')
  def index():
    """
    Index page handler
    @return: Welcome Note
    """
    return 'Welcome to Trivia API'

  @app.route('/categories', methods=['GET'])
  def retrive_categories():
    """
    Fetching all the categories
    @return: Json object containing all categories
    """
    categories = Category.query.order_by(Category.id).all()
    categories_dict = {}
    for category in categories:
      categories_dict[category.id] = category.type

    return jsonify({
      'success': True,
      'categories': categories_dict
    })


  @app.route('/questions')
  def retrieve_questions():
    """
    Retrieve all the questions.
    @return: Json object containg all the questions
    """
    questions = Question.query.order_by(Question.id).all()
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    formatted_questions = [question.format() for question in questions]

    categories = Category.query.order_by(Category.id).all()
    categories_dict = {}
    for category in categories:
      categories_dict[category.id] = category.type

    if len(formatted_questions) == 0:
      abort(404)

    return jsonify({
      'questions': formatted_questions[start:end],
      'total_questions': len(formatted_questions[start:end]),
      'categories': categories_dict
    })

  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    """
    delete question based on id
    @param question_id: id of the question to be deleted
    @return: json object with proper message
    """
    try:
      question = Question.query.get(question_id)

      if not question:
        return abort(404)
      question.delete()

      return jsonify({
        "success": True,
        'message': "Question deleted successfully ",
        "id": question_id
      })
    except:
      abort(500)

  @app.route('/questions', methods=['POST'])
  def insert_question():
    """
    insert a new question
    @return: json object containg the inserted question
    """
    try:
      question = request.json.get('question')
      answer = request.json.get('answer')
      category = request.json.get('category')
      difficulty = request.json.get('difficulty')
      if not question or not answer or not category or not difficulty:
        return abort(422)
      question = Question(question, answer, category, difficulty)
      question.insert()
      return jsonify({
        'success':True,
        'question': question.format()
      })
    except:
      abort(500)

  @app.route('/search', methods=['POST'])
  def search():
    """
    Search for question based keyword
    @return: json object
    """
    search = request.json.get('searchTerm', None)
    try:
      if search:
        questions = Question.query.filter(Question.question.ilike(f'%{search}%')).all()
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        formatted_questions = [question.format() for question in questions]
        categories = Category.query.order_by(Category.id).all()

        categories_dict = {}
        for category in categories:
          categories_dict[category.id] = category.type

        if len(formatted_questions) == 0:
          abort(404)

        return jsonify({
          'questions': formatted_questions[start:end],
          'total_questions': len(formatted_questions[start:end]),
          'categories': categories_dict
        })

      else:
        abort(422)
    except:
      abort(500)

  @app.route('/categories/<int:category_id>/questions')
  def get_questions_by_category(category_id):
    """
    Get question by category
    @param category_id: id for the category
    @return: Json object containing questions
    """
    try:
      questions = Question.query.filter_by(category=str(category_id))
      if not questions:
        return abort(422)

      question_list = []
      for question in questions.all():
        question_list.append(question.format())
      return jsonify({
        "questions": question_list,
        "Number_of_questions": len(question_list),
        "current_category": question.category
      })

    except:
      abort(500)


  @app.route('/quizzes', methods=['POST'])
  def play_quiz():
    """
    getting quiz questions
    @return: json object containing asked quizzes
    """
    body = request.get_json()
    previous_questions = body.get('previous_questions', [])
    quiz_category = body.get('quiz_category', None)

    try:
      if quiz_category:
        if quiz_category['id'] == 0:
          quiz = Question.query.all()
        else:
          quiz = Question.query.filter_by(category=quiz_category['id']).all()
      if not quiz:
        return abort(422)
      selected = []
      for question in quiz:
        if question.id not in previous_questions:
          selected.append(question.format())
      if len(selected) != 0:
        result = random.choice(selected)
        return jsonify({
          'question': result
        })
      else:
        return jsonify({
          'question': False
        })

    except:
      abort(500)

  @app.errorhandler(500)
  def internal_server_error(e):
    """
    handling error
    @param e: error message
    @return: json object containing user freindly message
    """
    return jsonify({
        "success": False,
        "error": 500,
        "message": "internal server error"
    }), 500

  @app.errorhandler(404)
  def not_found(e):
    """
    handling error
    @param e: error message
    @return: json object containing user freindly message
    """
    return jsonify({
      "success": False,
      "error": 404,
      "message": "resource could not be found"
    }), 404


  @app.errorhandler(422)
  def unprocessable(e):
    """
    handling error
    @param e: error message
    @return: json object containing user freindly message
    """
    return jsonify({
      "success": False,
      "error": 422,
      "message": "Could not be processed"
    }), 422


  return app




