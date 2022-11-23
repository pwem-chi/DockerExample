'''
    HttpResponse is used to pass information
        back to the view
'''

from django.http import HttpResponse

'''
defining a function that will recieve our request
    and excecute the logic we create within the function
'''
def greeting(response):

    '''
    This will return
    :param response:
    :return:
    '''
    return HttpResponse("Kiryu-Chan!")