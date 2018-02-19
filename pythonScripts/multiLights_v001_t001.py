import maya.cmds as cmds
global win
global sel
global intensityField

def deleteWindow(*args):
    global win
    cmds.deleteUI(win)
    
def createUI():
    global win
    global intensityField
    win="multiLightWin"
    if cmds.window(win,exists=True):
        deleteWindow()
        
    myWindow=cmds.window(win,title="multi light",width=100,height=150, sizeable=False,mxb=False,mnb=False)
    cmds.columnLayout(adjustableColumn=True)
    intensityField=cmds.floatField(minValue=0)
    cmds.button(label="set",align="center",command=setIntensity)
    cmds.checkBox(label="invisible",onCommand=("invisible(1)"),offCommand=("invisible(0)"))  
    cmds.button(label="close",align="center", command=deleteWindow)  
    cmds.showWindow(myWindow)
    
def setIntensity(*args):
    global intensityField
    vrLights=[]
    myIntensity=cmds.floatField(intensityField,query=True,value=True)
    
    selection=cmds.ls(selection=True)
    for obj in selection:
        
        cmds.setAttr(obj+".intensityMult",myIntensity)
    



def selection():
    global sel
    sel=[]
    mySelection=cmds.ls(selection=True)
    
    if(len(mySelection)<1):
        cmds.error("please,select at least one vray light")
    for obj in mySelection:
        shapeNode=cmds.listRelatives(obj,shapes=True)
        nodeType=cmds.nodeType(shapeNode)
        if(nodeType=="VRayLightIESShape" or nodeType=="VRayLightSphereShape" or nodeType=="VRayLightDomeShape" or nodeType=="VRayLightRectShape"):
            sel.append(str(obj))
      
def invisible(state):
    global sel
    
    for VrLight in sel:
        cmds.setAttr(VrLight+".invisible",state)        
        
selection()

createUI()
