# ptgstu-logger
A custom,dependency free,logging solution developed for use in Pythagorous Studio Software and wherever the standard library is unavailable.


Here's a demo of a standard client side implementation of logger
```
import logger

displog=True #set displaying inbound logs to true

logger.register(__name__) #add our script as a registered in/out box
print(logger.regclis) #print out all registered clients

def log(msg,lvl=0):
    """wraper for the logger library"""
    logger.inlog(msg=msg,lvl=lvl,src=__name__) #send our message for processing
    if displog==True:
        print(logger.outlog(__name__)) #if displaying of logs is enabled print out the new messages
    else:
        pass

log("hello")
print(logger.intstack) #view the internal debugging stack log
log("ello")
```
Will give the following output
```
[('__main__', '__main___oblbl')] #all registered clients
[('__main__', 0, 'hello')] #Our first message
['registered: __main__', "src: __main__ found in list: [('__main__', '__main___oblbl')]", "src: __main__ found in list: [('__main__', '__main___oblbl')]", 'sent message stack to source: __main__'] #The internal debug stack log
[('__main__', 0, 'ello')] #our Second message
```
