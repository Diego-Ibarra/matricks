'''
test2
'''



def clearall():
    '''Clears all variables from the workspace. Like Matlab's clear all'''
    from IPython import get_ipython
    get_ipython().magic('reset -sf') 
    return

    