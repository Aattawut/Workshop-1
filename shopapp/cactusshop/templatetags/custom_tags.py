from django import template

register = template.Library()

def getDictValue(dictionary,key):
    return dictionary.get(key)
    
register.filter('get_dict_value', getDictValue)