import re

from django import template

register = template.Library()


class CensorException(Exception):
    pass


@register.filter()
def censor(text):
    non_cens = ['редиска', 'овечкин', 'новость', 'это', 'что', 'год']
    try:
        if not isinstance(text, str):
            raise CensorException('Error')
        for word in non_cens:
            text = re.sub(word, word[0] + '*' * (len(word) - 1), text)
            title_word = word.title()
            text = re.sub(title_word, title_word[0] + '*' * (len(word) - 1), text)
        return text
    except CensorException as e:
        print(e)
