import re

from django import template

register = template.Library()


@register.filter()
def censor(text):
    non_cens = ['редиска', 'овечкин', 'новость', 'стрем']
    for word in non_cens:
        text = re.sub(word, word[0] + '*' * (len(word) - 1), text)
        title_word = word.title()
        text = re.sub(title_word, title_word[0] + '*' * (len(word) - 1), text)
    return text
