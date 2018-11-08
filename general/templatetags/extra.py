from django import template

from general.models import *

register = template.Library()

@register.filter
def percent(val):
    return val if val else '-';

@register.filter
def liked(uid):
    return 'done' if uid and FavPlayer.objects.filter(player__uid=uid).exists() else ''

@register.filter
def ou_ml(game, team):
    if not game.ml:
        return ''

    if team in game.ml:
        return '( {} )'.format(game.ml.split(' ')[-1])
    else:
        return '( {} )'.format(int(game.ou))

@register.filter
def salery_per_projection(player):
	return '{:.1f}'.format(player.salary / player.proj_points) if player.proj_points else '-'
