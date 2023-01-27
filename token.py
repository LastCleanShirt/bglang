"""
TODO: List of tokens
"""
DCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"
DNUM   = "0123456789"
DOP    = ".$;=*#@&%"
DSOP   = "\"\'"
DNEW   = "\n"
DWSP   = " \t"

CHAR = "character"
NUM  = "number/digit"
OP   = "operators"
NEW  = "new line"
WSP  = "whitespace"
STR  = "string"

"""
Keywords man
"""
KW_NEW = "<keyword new>"
KW_SET = "<keyword set>"


"""
GUIs Properties
"""
PR_winsize = "winsize"
PR_title = "title"

"""
Operators
"""
OP_VDEC = "$Var Declaration"

# To append Tokens
def Token(t, prop): 
	if prop: return {"type": t, "prop": prop}
	return {"type": t, "prop": prop}