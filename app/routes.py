from flask import Flask, request
from flask_restplus import Api, Resource, fields
from app import flask_app
from app import user_service
from app import post_service
import logging
from app import utils

app = Api(app = flask_app, 
    version = "1.0", 
	title = "Simple Blog", 
	description = "Manage Blog entities")

user_space = app.namespace('users', description='Blog Users')
post_space = app.namespace('posts', description='User Posts')

user_model = app.model('User Model',
    {
		'id': fields.Integer(required = True, description="id", help="id"),
		'username': fields.String(required = True, description="Name of the person", help="Name cannot be blank."),
		'email': fields.String(required = True,	description="email of the person", help="email of the person"),
		'password_hash': fields.String(required = False, description="password hash", help="password hash"),
		'created_on': fields.DateTime(required = False, description="created on", help="created on"),
		'updated_on': fields.DateTime(required = False, description="updated on", help="updated on")
	})

post_model = app.model('Post Model',
    {
		'id': fields.Integer(required = True, description="id", help="id"),
		'body': fields.String(required = True, description="Body of the post", help="Body of the post"),
		'timestamp': fields.DateTime(required = True,	description="timestamp", help="timestamp"),
		'user_id': fields.String(required = False, description="user id", help="user id"),
		'created_on': fields.DateTime(required = False, description="created on", help="created on"),
		'updated_on': fields.DateTime(required = False, description="updated on", help="updated on")
	})	

@user_space.route("/")
class AllUsersClass(Resource):

	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
	def get(self):
		"""
		returns all users
		"""
		try:
			return user_service.get_all()
		except AssertionError as e:
			user_space.abort(400, e.args[0], status = "Could not get all users", statusCode = "400")
		except Exception as e:
			user_space.abort(500, e.args[0], status = "Could not get all users", statusCode = "500")

@user_space.route("/<int:id>")
class UserClass(Resource):

	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'id': 'Specify the Id associated with the person' })
	def get(self, id):
		"""
		returns user by id
		"""
		try:
			flask_app.logger.debug('We are getting the user: %d', id)
			return user_service.get(id)
		except AssertionError as e:
			user_space.abort(400, e.args[0], status = "Could not get user", statusCode = "400")
		except Exception as e:
			user_space.abort(500, e.args[0], status = "Could not get user", statusCode = "500")

	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'id': 'Specify the Id associated with the person' })
	@app.expect(user_model)		
	def post(self, id):
		"""
		inserts a user
		"""
		try:
			user_service.add(request.json)
			return user_service.get(id)
		except AssertionError as e:
			user_space.abort(400, e.args[0], status = "Could not insert user", statusCode = "400")
		except Exception as e:
			user_space.abort(500, e.args[0], status = "Could not insert user", statusCode = "500")


	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'id': 'Specify the Id associated with the entity' })
	def delete(self, id):
		"""
		deletes a user by id
		"""
		try:
			user_service.delete(id)
		except AssertionError as e:
			user_space.abort(400, e.args[0], status = "Could not delete user", statusCode = "400")
		except Exception as e:
			user_space.abort(500, e.args[0], status = "Could not delete user", statusCode = "500")

@post_space.route("/")
class AllPostClass(Resource):

	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
	def get(self):
		"""
		returns all posts
		"""		
		try:
			return post_service.get_all()
		except AssertionError as e:
			post_space.abort(400, e.args[0], status = "Could not get all posts", statusCode = "400")
		except Exception as e:
			post_space.abort(500, e.args[0], status = "Could not get all posts", statusCode = "500")

@post_space.route("/<int:id>")
class PostClass(Resource):

	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'id': 'Specify the Id associated with the person' })
	def get(self, id):
		"""
		returns a post by id
		"""		
		try:
			return post_service.get(id)
		except AssertionError as e:
			post_space.abort(400, e.args[0], status = "Could not get post", statusCode = "400")
		except Exception as e:
			post_space.abort(500, e.args[0], status = "Could not get post", statusCode = "500")

	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'id': 'Specify the Id associated with the person' })
	@app.expect(post_model)		
	def post(self, id):
		"""
		inserts a post
		"""		
		try:
			post_service.add(request.json)
			return post_service.get(id)
		except AssertionError as e:
			post_space.abort(400, e.args[0], status = "Could not insert post", statusCode = "400")
		except Exception as e:
			post_space.abort(500, e.args[0], status = "Could not insert post", statusCode = "500")


	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'id': 'Specify the Id associated with the entity' })
	def delete(self, id):
		"""
		deletes a post by id
		"""		
		try:
			post_service.delete(id)
		except AssertionError as e:
			post_space.abort(400, e.args[0], status = "Could not delete post", statusCode = "400")
		except Exception as e:
			post_space.abort(500, e.args[0], status = "Could not delete post", statusCode = "500")
