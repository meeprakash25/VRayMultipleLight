import maya.cmds as cmds
global win
global intensityField
global skp
global sskp
global noDecayBox
global doubleSidedBox

def deleteWindow(*args):
    global win
    cmds.deleteUI(win)
    
def createUI():
    global win
    global intensityField
    global skp
    global sskp
    global noDecayBox
    global doubleSidedBox
    
    win="multiLightWin"
    if cmds.window(win,exists=True):
        deleteWindow()
        
    myWindow=cmds.window(win,title="VRay Multiple Light",resizeToFitChildren=True, sizeable=False,maximizeButton=False,minimizeButton=True)
    cmds.columnLayout(adjustableColumn=True,rowSpacing=2,columnAttach=("both",8))
    
    cmds.separator( height=15, style='in')
    
    cmds.checkBox(label="Enabled",onCommand=("enabled(True)"),offCommand=("enabled(False)"), value=True)
    
    cmds.separator( height=15, style='in')
    
    #cmds.rowLayout(numberOfColumns=2)
    
    cmds.columnLayout(adjustableColumn=True,rowSpacing=2,columnAttach=("both",8))
    cmds.text(label="Intensity",align="center",font="smallBoldLabelFont")
    #cmds.separator( height=5)
    intensityField=cmds.floatSliderGrp(field=True, minValue=0.00, maxValue=100.00, fieldMinValue=0.00, fieldMaxValue=1000000000.00,dragCommand=setIntensity,changeCommand=setIntensity, value=30.00)
    cmds.setParent("..")
    
    cmds.separator( height=15, style='in')
    
    
    noDecayBox=cmds.checkBox(label="No Decay",onCommand=("noDecay(True)"),offCommand=("noDecay(False)"))
    doubleSidedBox=cmds.checkBox(label="Double Sided",onCommand=("doubleSided(True)"),offCommand=("doubleSided(False)"))
    cmds.checkBox(label="invisible",onCommand=("invisible(True)"),offCommand=("invisible(False)"))
    skp=cmds.checkBox(label="Skylight Portal",onCommand=("skylightPortal(True)"),offCommand=("skylightPortal(False)"))
    sskp=cmds.checkBox(label="Simple Skylight Portal",onCommand=("simpleSkylightPortal(True)"),offCommand=("simpleSkylightPortal(False)"),enable=False) 
    cmds.checkBox(label="Store With Irradiance Map",onCommand=("storeWithIrradianceMap(True)"),offCommand=("storeWithIrradianceMap(False)")) 
    
    cmds.separator( height=12, style='in')
    
    cmds.checkBox(label="Affect Diffuse",onCommand=("affectDiffuse(True)"),offCommand=("affectDiffuse(False)"), value=True)
    cmds.checkBox(label="Affect Specular",onCommand=("affectSpecular(True)"),offCommand=("affectSpecular(False)"), value=True)
    cmds.checkBox(label="Affect Reflections",onCommand=("affectReflections(True)"),offCommand=("affectReflections(False)"), value=True)
     
    cmds.separator( height=15, style='in')
    
    cmds.columnLayout(adj=True,cat=("both",70))    
    cmds.button(label="close",align="center", command=deleteWindow)
    cmds.setParent("..")
    
     
    cmds.separator( height=15, style='in')
    cmds.showWindow(myWindow)


def VRayLightList(selection):
    sel=[]
    if(len(selection)<1):
        cmds.error("please,select at least one vray light")
    for obj in selection:
        shapeNode=cmds.listRelatives(obj,shapes=True)
        
        nodeType=cmds.nodeType(shapeNode)
        if(nodeType=="VRayLightIESShape" or nodeType=="VRayLightSphereShape" or nodeType=="VRayLightDomeShape" or nodeType=="VRayLightRectShape"):   
            sel.append(str(obj))
    return sel

def ignore(light):
    cmds.warning("option ignored for {}".format(light))
    

def setIntensity(*args):
    global intensityField
       
    mySelection=cmds.ls(selection=True)
   
    vRayLight=VRayLightList(mySelection)   
    
    myIntensity=cmds.floatSliderGrp(intensityField,query=True,value=True)
    
    for light in vRayLight:        
        cmds.setAttr(light+".intensityMult",myIntensity)
        
def noDecay(state):
    mySelection=cmds.ls(selection=True) 
    
    vRayLight=[]
    if(len(mySelection)<1):
        cmds.error("please,select at least one vray light")
    for obj in mySelection:
        shapeNode=cmds.listRelatives(obj,shapes=True)
        
        nodeType=cmds.nodeType(shapeNode)
        if(nodeType=="VRayLightSphereShape" or nodeType=="VRayLightRectShape"):   
            vRayLight.append(str(obj))
            
        elif(nodeType=="VRayLightIESShape" or nodeType=="VRayLightDomeShape"):
            ignore(obj)          
    
    for light in vRayLight:
        cmds.setAttr(light+".noDecay",state)
        
def doubleSided(state):
    mySelection=cmds.ls(selection=True) 
    
    vRayLight=[]
    if(len(mySelection)<1):
        cmds.error("please,select at least one vray light")
    for obj in mySelection:
        shapeNode=cmds.listRelatives(obj,shapes=True)
        
        nodeType=cmds.nodeType(shapeNode)
        if(nodeType=="VRayLightRectShape"):   
            vRayLight.append(str(obj))
            
        elif(nodeType=="VRayLightIESShape" or nodeType=="VRayLightSphereShape" or nodeType=="VRayLightDomeShape"):
            ignore(obj)            
    
    for light in vRayLight:
        cmds.setAttr(light+".doubleSided",state)
      
def invisible(state):
    mySelection=cmds.ls(selection=True) 
    
    vRayLight=[]
    if(len(mySelection)<1):
        cmds.error("please,select at least one vray light")
    for obj in mySelection:
        shapeNode=cmds.listRelatives(obj,shapes=True)
        
        nodeType=cmds.nodeType(shapeNode)
        if(nodeType=="VRayLightSphereShape" or nodeType=="VRayLightDomeShape" or nodeType=="VRayLightRectShape"):   
            vRayLight.append(str(obj))
            
        elif(nodeType=="VRayLightIESShape"):
            ignore(obj)            
    
    for light in vRayLight:
        cmds.setAttr(light+".invisible",state)  

def skylightPortal(state):
    global skp
    global sskp
    global noDecayBox
    global doubleSidedBox
    mySelection=cmds.ls(selection=True) 
    
    vRayLight=[]
    if(len(mySelection)<1):
        cmds.error("please,select at least one vray light")
    for obj in mySelection:
        shapeNode=cmds.listRelatives(obj,shapes=True)
        
        nodeType=cmds.nodeType(shapeNode)
        if(nodeType=="VRayLightRectShape"):   
            vRayLight.append(str(obj))
            
        elif(nodeType=="VRayLightDomeShape" or nodeType=="VRayLightSphereShape" or nodeType=="VRayLightIESShape"):
            ignore(obj)            
    
    for light in vRayLight:
        cmds.setAttr(light+".skylightPortal",state)
        
    skpValue= cmds.checkBox(skp,query=True,value=True)
    
    if(skpValue==True):
        cmds.checkBox(sskp,edit=True,enable=True)
        cmds.checkBox(noDecayBox,edit=True,enable=False)
        cmds.checkBox(doubleSidedBox,edit=True,enable=False)
    else:
        cmds.checkBox(sskp,edit=True,enable=False)
        cmds.checkBox(noDecayBox,edit=True,enable=True)
        cmds.checkBox(doubleSidedBox,edit=True,enable=True)
           
def simpleSkylightPortal(state):
    mySelection=cmds.ls(selection=True) 
    
    vRayLight=[]
    if(len(mySelection)<1):
        cmds.error("please,select at least one vray light")
    for obj in mySelection:
        shapeNode=cmds.listRelatives(obj,shapes=True)
        
        nodeType=cmds.nodeType(shapeNode)
        if(nodeType=="VRayLightRectShape"):   
            vRayLight.append(str(obj))
            
        elif(nodeType=="VRayLightDomeShape" or nodeType=="VRayLightSphereShape" or nodeType=="VRayLightIESShape"):
            ignore(obj)            
    
    for light in vRayLight:
        cmds.setAttr(light+".simpleSkylightPortal",state)

def enabled(state):
    mySelection=cmds.ls(selection=True)    
    vRayLight=VRayLightList(mySelection)
    for light in vRayLight:
        cmds.setAttr(light+".enabled",state)  

def affectReflections(state):
    mySelection=cmds.ls(selection=True)
    
    vRayLight=[]
    if(len(mySelection)<1):
        cmds.error("please,select at least one vray light")
    for obj in mySelection:
        shapeNode=cmds.listRelatives(obj,shapes=True)
        
        nodeType=cmds.nodeType(shapeNode)
        if(nodeType=="VRayLightSphereShape" or nodeType=="VRayLightDomeShape" or nodeType=="VRayLightRectShape"):   
            vRayLight.append(str(obj))
            
        elif(nodeType=="VRayLightIESShape"):
            ignore(obj)        
    
    for light in vRayLight:
        cmds.setAttr(light+".affectReflections",state)
        
def storeWithIrradianceMap(state):
    mySelection=cmds.ls(selection=True)    
    vRayLight=VRayLightList(mySelection)
    for light in vRayLight:
        cmds.setAttr(light+".storeWithIrradianceMap",state)  
        
def affectDiffuse(state):
    mySelection=cmds.ls(selection=True)    
    vRayLight=VRayLightList(mySelection)
    for light in vRayLight:
        cmds.setAttr(light+".affectDiffuse",state) 
        
def affectSpecular(state):
    mySelection=cmds.ls(selection=True)    
    vRayLight=VRayLightList(mySelection)
    for light in vRayLight:
        cmds.setAttr(light+".affectSpecular",state) 
createUI()