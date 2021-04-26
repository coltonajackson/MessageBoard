from django.db import models
import re

class UserManager(models.Manager):
	def user_validator(self, postData):
		errors = {}
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

		if len(postData['username']) < 2:
			errors['username'] = "Username must be at least 2 characters"
		if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "Invalid email address"
		if len(postData['password']) < 8:
			errors['password'] = "Password must be at least 8 characters"
		return errors


class User(models.Model):
	username = models.CharField(max_length=45)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()