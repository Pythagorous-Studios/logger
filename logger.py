#doc: log lvl: 0=info,1=debug,2=warning,3=error
#doc: logmng inst=logmng, logcli inst=logcli

"""setup"""
mlr=[] #master log record
regclis=[] #registered clients,form: (src,srcoblbl)

intstack=[] #internal debug stack

class InvalidLogSource(BaseException):
    pass

def debug(debugmsg):
    intstack.append(debugmsg)

def register(src):
    """records new clients to setup log inbox"""
    #src should be a CONSISTENT unique identifier
    srcoblblname=str(src)+'_oblbl'
    globals()[srcoblblname]=[]
    regclis.append((src,srcoblblname))
    debug("registered: "+str(src))

def checksrc(src):
    for cliset in regclis:
        if cliset[0]==src:
            debug("src: "+str(src)+" found in list: "+str(regclis))
            return True
    debug("src: "+str(src)+" not found in list: "+str(regclis))
    return False

def inlog(src,lvl,msg):
    """takes new inbound logs"""
    if not checksrc(src):
        register(src)
        if not checksrc(src):
            debug("message: "+str(msg)+" from source: "+ str(src)+" is invalid")
            raise InvalidLogSource
    log=(src,lvl,msg)
    mlr.append(log)
    for cli in regclis:
        eval(cli[1]).append(log)

def outlog(src):
    if not checksrc(src):
        raise InvalidLogSource
    for cliset in regclis:
        if src==cliset[0]:
            templist=eval(cliset[1]).copy()
            eval(cliset[1]).clear()
            debug("sent message stack to source: "+str(src))
            return templist

def masterlog():
    return mlr