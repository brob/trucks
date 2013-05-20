from django.template import Library, Node
from django import template
from truck.models import *
from django.contrib.auth.models import User

register = Library()


def get_checkins(parser, token):
	bits = token.contents.split()
	
	#userId = User.objects.get(id = bits[2])
	return LatestCheckinsNode(bits[1], bits[2], bits[4])

class LatestCheckinsNode(Node):
	def __init__(self, num, user, var):
		self.num = num
		self.user = template.Variable(user)
		self.var = var


	def render(self, context):
		user = self.user.resolve(context)
		context[self.var] = checkin.objects.all()
		context["test"] = user
		return ''


get_checkins = register.tag(get_checkins)