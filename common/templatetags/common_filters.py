from django import template

register = template.Library()

@register.filter
def swap(value):
    if value in ['5','6','7','8']:
        newvalue = 'Anagram Hunt'
    if value == 'x':
        newvalue = 'Multiplication'
    if value == '/':
        newvalue = 'Division'
    if value == '+':
        newvalue = 'Addition'
    if value == '-':
        newvalue = 'Subtraction'
    return newvalue
