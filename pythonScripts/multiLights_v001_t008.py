import maya.cmds as cmds
global win
global colorField
global temperatureField
global intensityField
global subdivsField
global skp
global sskp
global noDecayBox
global doubleSidedBox
global radiusField
global sphereSegmentsField
global rayDistanceField

def deleteWindow(*args):
    global win
    cmds.deleteUI(win)
    
def createUI():
    global win
    global colorField
    global temperatureField
    global intensityField
    global subdivsField
    global skp
    global sskp
    global noDecayBox
    global doubleSidedBox
    global radiusField
    global sphereSegmentsField
    global rayDistanceField
    
    win="multiLightWin"
    if cmds.window(win,exists=True):
        deleteWindow()
       
    myWindow=cmds.window(win,title="VRay Multiple Light v1.0",resizeToFitChildren=True,sizeable=True,maximizeButton=True,minimizeButton=True)    
    
    cmds.columnLayout(adjustableColumn=True,rowSpacing=2,columnAttach=("both",8))
     
    cmds.separator( height=15, style='in')
    
    cmds.frameLayout( label='Common Attributes',  bgc=(0.341,0.341,0.341), collapsable=True)
    
    cmds.columnLayout(adjustableColumn=True,rowSpacing=2,columnAttach=("both",8))
    
    cmds.checkBox(label="Enabled",onCommand=("enabled(True)"),offCommand=("enabled(False)"), value=True)
    
    cmds.separator( height=15, style='in')
    
    cmds.radioButtonGrp(label="Color Mode",numberOfRadioButtons=2, width=266, labelArray2=["color","temperature"], changeCommand1="setColorMode(False)",changeCommand2="setColorMode(True)",select=1,adjustableColumn=True,columnAlign=(1,"left"))
    
    cmds.separator( height=15, style='in')
    
    colorField=cmds.colorSliderGrp(label="Color",width=266,hsv=(360,0,0.700),changeCommand=setColor,dragCommand=setColor,adjustableColumn=True,columnAlign=(1,"left"))
    
    temperatureField=cmds.floatSliderGrp(label="Temperature",field=True,width=266, minValue=1000, maxValue=10000, fieldMinValue=1000, fieldMaxValue=30000,dragCommand=setTemperature,changeCommand=setTemperature,value=6500, precision=3, enable=False,adjustableColumn=True,columnAlign=(1,"left"))
        
    intensityField=cmds.floatSliderGrp(label="Intensity",field=True,width=266, minValue=0, maxValue=100, fieldMinValue=0, fieldMaxValue=1000000000,dragCommand=setIntensity,changeCommand=setIntensity,value=30, precision=3,adjustableColumn=True,columnAlign=(1,"left"))
    
    subdivsField=cmds.intSliderGrp(label="Subdivs",field=True,width=266, minValue=1, maxValue=32, fieldMinValue=1, fieldMaxValue=1000000000,dragCommand=setSubdivs,changeCommand=setSubdivs,value=8,adjustableColumn=True,columnAlign=(1,"left"))

    cmds.separator( height=15, style='in')
    
    noDecayBox=cmds.checkBox(label="No Decay",onCommand=("noDecay(True)"),offCommand=("noDecay(False)"))
    #doubleSidedBox=cmds.checkBox(label="Double Sided",onCommand=("doubleSided(True)"),offCommand=("doubleSided(False)"))
    cmds.checkBox(label="Invisible",onCommand=("invisible(True)"),offCommand=("invisible(False)"))
    #skp=cmds.checkBox(label="Skylight Portal",onCommand=("skylightPortal(True)"),offCommand=("skylightPortal(False)"))
    #sskp=cmds.checkBox(label="Simple Skylight Portal",onCommand=("simpleSkylightPortal(True)"),offCommand=("simpleSkylightPortal(False)"),enable=False) 
    cmds.checkBox(label="Store With Irradiance Map",onCommand=("storeWithIrradianceMap(True)"),offCommand=("storeWithIrradianceMap(False)")) 
    
    cmds.separator( height=12, style='in')
    
    cmds.checkBox(label="Affect Diffuse",onCommand=("affectDiffuse(True)"),offCommand=("affectDiffuse(False)"), value=True)
    cmds.checkBox(label="Affect Specular",onCommand=("affectSpecular(True)"),offCommand=("affectSpecular(False)"), value=True)
    cmds.checkBox(label="Affect Reflections",onCommand=("affectReflections(True)"),offCommand=("affectReflections(False)"), value=True)
    cmds.checkBox(label="Shadows",onCommand=("shadows(True)"),offCommand=("shadows(False)"), value=True)
    cmds.separator( height=15, style='in')
    
    cmds.setParent("..")
    cmds.setParent("..")
    cmds.setParent("..")
     
    cmds.frameLayout(label='Individual Attributes',backgroundColor=(0.341,0.341,0.341), collapsable=True,collapse=True)
    cmds.scrollLayout(height=200,childResizable=True)    
    cmds.columnLayout(adjustableColumn=True,rowSpacing=2,columnAttach=("both",8))
    
    cmds.frameLayout( label='VRayLightSphere',backgroundColor=(0.341,0.341,0.341), collapsable=True)
    cmds.columnLayout(adjustableColumn=True,rowSpacing=2,columnAttach=("both",8))
    
    radiusField=cmds.floatSliderGrp(label="Radius",field=True,width=266, minValue=0, maxValue=10, fieldMinValue=0, fieldMaxValue=1000000000,value=1, precision=3,dragCommand=setRadius,changeCommand=setRadius,adjustableColumn=True,columnAlign=(1,"left"))
    sphereSegmentsField=cmds.intSliderGrp(label="Sphere Segments",field=True,width=266, minValue=3, maxValue=64, fieldMinValue=1, fieldMaxValue=1000000000,value=20,dragCommand=setSphereSegments,changeCommand=setSphereSegments,adjustableColumn=True,columnAlign=(1,"left"))
        
    cmds.separator( height=15, style='in')
    
    cmds.setParent("..")
    cmds.setParent("..")
    
    cmds.frameLayout( label='VRayLightDome',backgroundColor=(0.341,0.341,0.341), collapsable=True)
    cmds.columnLayout(adjustableColumn=True,rowSpacing=2,columnAttach=("both",8))
    
    cmds.checkBox(label="Dome Spherical",onCommand=("domeSpherical(True)"),offCommand=("domeSpherical(False)"))
    cmds.checkBox(label="Use Ray Distance",onCommand=("useRayDistance(True)"),offCommand=("useRayDistance(False)"))
    rayDistanceField=cmds.floatSliderGrp(label="Ray Distance",field=True,width=266,enable=False, minValue=0, maxValue=100000, fieldMinValue=0, fieldMaxValue=1000000000,value=100000,dragCommand=setRayDistance,changeCommand=setRayDistance,precision=3,adjustableColumn=True,columnAlign=(1,"left"))
    
    cmds.separator( height=15, style='in')
    
    cmds.setParent("..")
    cmds.setParent("..")
    
    cmds.frameLayout( label='VRayLightRect',backgroundColor=(0.341,0.341,0.341), collapsable=True)
    cmds.columnLayout(adjustableColumn=True,rowSpacing=2,columnAttach=("both",8))
    
    doubleSidedBox=cmds.checkBox(label="Double Sided",onCommand=("doubleSided(True)"),offCommand=("doubleSided(False)"))
    skp=cmds.checkBox(label="Skylight Portal",onCommand=("skylightPortal(True)"),offCommand=("skylightPortal(False)"))
    sskp=cmds.checkBox(label="Simple Skylight Portal",onCommand=("simpleSkylightPortal(True)"),offCommand=("simpleSkylightPortal(False)"),enable=False)
    
    cmds.separator( height=15, style='in')
    
    cmds.setParent("..")
    cmds.setParent("..")
    
    cmds.frameLayout( label='VRayLightIES',backgroundColor=(0.341,0.341,0.341), collapsable=True)
    cmds.columnLayout(adjustableColumn=True,rowSpacing=2,columnAttach=("both",8))
    
    cmds.checkBox(label="Area Speculars",onCommand=("areaSpeculars(True)"),offCommand=("areaSpeculars(False)"), value=True)
    #skp=cmds.checkBox(label="Skylight Portal",onCommand=("skylightPortal(True)"),offCommand=("skylightPortal(False)"))
    #sskp=cmds.checkBox(label="Simple Skylight Portal",onCommand=("simpleSkylightPortal(True)"),offCommand=("simpleSkylightPortal(False)"),enable=False)
    
    #cmds.separator( height=15, style='in')
    
    cmds.setParent("..")
    cmds.setParent("..")
    
    cmds.setParent("..")
    cmds.setParent("..")
    
    cmds.setParent("..")
    
    cmds.separator( height=15, style='in')
    
    cmds.columnLayout(adjustableColumn=True,columnAttach=("both",80))    
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
    
def setColorMode(state):
    global temperatureField
    global colorField
    
    #value=cmds.radioButtonGrp(rButton,query=True,enable1=True)
    #print value
       
    mySelection=cmds.ls(selection=True)
   
    vRayLight=VRayLightList(mySelection)   
    
    for light in vRayLight:        
        cmds.setAttr(light+".colorMode",state)
        
    
    if state==False:
        cmds.floatSliderGrp(temperatureField,edit=True,enable=False)
        cmds.colorSliderGrp(colorField,edit=True,enable=True)
    elif state==True:
        cmds.colorSliderGrp(colorField,edit=True,enable=False)
        cmds.floatSliderGrp(temperatureField,edit=True,enable=True)    
        
    

def setColor(*args):
    global colorField
       
    mySelection=cmds.ls(selection=True)
   
    vRayLight=VRayLightList(mySelection)   
    
    myColor=cmds.colorSliderGrp(colorField,query=True,rgbValue=True)
    
    for light in vRayLight:        
        cmds.setAttr(light+".lightColor",myColor[0],myColor[1],myColor[2])
    
def setTemperature(*args):
    global temperatureField
       
    mySelection=cmds.ls(selection=True)
   
    vRayLight=VRayLightList(mySelection)   
    
    myTemperature=cmds.floatSliderGrp(temperatureField,query=True,value=True)
    
    for light in vRayLight:        
        cmds.setAttr(light+".temperature",myTemperature)   
        
     

def setIntensity(*args):
    global intensityField
       
    mySelection=cmds.ls(selection=True)
   
    vRayLight=VRayLightList(mySelection)   
    
    myIntensity=cmds.floatSliderGrp(intensityField,query=True,value=True)
    
    for light in vRayLight:        
        cmds.setAttr(light+".intensityMult",myIntensity)
        
def setSubdivs(*args):
    global subdivsField
       
    mySelection=cmds.ls(selection=True)
   
    vRayLight=VRayLightList(mySelection)   
    
    mySubdivs=cmds.intSliderGrp(subdivsField,query=True,value=True)
    
    for light in vRayLight:        
        cmds.setAttr(light+".subdivs",mySubdivs)

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
        if nodeType=="VRayLightSphereShape" or nodeType=="VRayLightDomeShape" or nodeType=="VRayLightRectShape":   
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
        
def shadows(state):
    mySelection=cmds.ls(selection=True)
    vRayLight=VRayLightList(mySelection)
            
    for light in vRayLight:
        cmds.setAttr(light+".shadows",state)

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
        
#VRAYLIGHTSPHERE 
def setRadius(*args):
    global radiusField
    
    mySelection=cmds.ls(selection=True) 
    
    vRayLight=[]
    if(len(mySelection)<1):
        cmds.error("please,select at least one vray light")
    for obj in mySelection:
        shapeNode=cmds.listRelatives(obj,shapes=True)
        
        nodeType=cmds.nodeType(shapeNode)
        if(nodeType=="VRayLightSphereShape"):   
            vRayLight.append(str(obj))
            
        elif(nodeType=="VRayLightIESShape" or nodeType=="VRayLightDomeShape" or nodeType=="VRayLightRectShape"):
            ignore(obj)          
    
    myRadius=cmds.floatSliderGrp(radiusField,query=True,value=True)
    for light in vRayLight:
        cmds.setAttr(light+".radius",myRadius)
        
def setSphereSegments(*args):
    global sphereSegmentsField
    
    mySelection=cmds.ls(selection=True) 
    
    vRayLight=[]
    if(len(mySelection)<1):
        cmds.error("please,select at least one vray light")
    for obj in mySelection:
        shapeNode=cmds.listRelatives(obj,shapes=True)
        
        nodeType=cmds.nodeType(shapeNode)
        if(nodeType=="VRayLightSphereShape"):   
            vRayLight.append(str(obj))
            
        elif(nodeType=="VRayLightIESShape" or nodeType=="VRayLightDomeShape" or nodeType=="VRayLightRectShape"):
            ignore(obj)          
    
    mySphereSegments=cmds.intSliderGrp(sphereSegmentsField,query=True,value=True)
    for light in vRayLight:
        cmds.setAttr(light+".sphereSegments",mySphereSegments)
        

#VRAYLIGHTDOME
def domeSpherical(state):
    mySelection=cmds.ls(selection=True) 
    
    vRayLight=[]
    if(len(mySelection)<1):
        cmds.error("please,select at least one vray light")
    for obj in mySelection:
        shapeNode=cmds.listRelatives(obj,shapes=True)
        
        nodeType=cmds.nodeType(shapeNode)
        if(nodeType=="VRayLightDomeShape"):   
            vRayLight.append(str(obj))
            
        elif(nodeType=="VRayLightRectShape" or nodeType=="VRayLightSphereShape" or nodeType=="VRayLightIESShape"):
            ignore(obj)            
    
    for light in vRayLight:
        cmds.setAttr(light+".domeSpherical",state)
        
def useRayDistance(state):
    global rayDistanceField
    
    mySelection=cmds.ls(selection=True) 
    
    vRayLight=[]
    if(len(mySelection)<1):
        cmds.error("please,select at least one vray light")
    for obj in mySelection:
        shapeNode=cmds.listRelatives(obj,shapes=True)
        
        nodeType=cmds.nodeType(shapeNode)
        if(nodeType=="VRayLightDomeShape"):   
            vRayLight.append(str(obj))
            
        elif(nodeType=="VRayLightRectShape" or nodeType=="VRayLightSphereShape" or nodeType=="VRayLightIESShape"):
            ignore(obj)            
    
    for light in vRayLight:
        cmds.setAttr(light+".rayDistanceOn",state)
        
    if state==False:
        cmds.floatSliderGrp(rayDistanceField,edit=True,enable=False)
        
    else:
        cmds.floatSliderGrp(rayDistanceField,edit=True,enable=True)
        
def setRayDistance(state):
    global rayDistanceField
    
    mySelection=cmds.ls(selection=True) 
    
    vRayLight=[]
    if(len(mySelection)<1):
        cmds.error("please,select at least one vray light")
    for obj in mySelection:
        shapeNode=cmds.listRelatives(obj,shapes=True)
        
        nodeType=cmds.nodeType(shapeNode)
        if(nodeType=="VRayLightDomeShape"):   
            vRayLight.append(str(obj))
            
        elif(nodeType=="VRayLightRectShape" or nodeType=="VRayLightSphereShape" or nodeType=="VRayLightIESShape"):
            ignore(obj)            
    myRayDistance=cmds.floatSliderGrp(rayDistanceField,query=True,value=True)
    
    for light in vRayLight:
        cmds.setAttr(light+".rayDistance",myRayDistance)
        
#VRAYLIGHTRECT
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
        
#VRAYLIGHTIES
def areaSpeculars(state):
    mySelection=cmds.ls(selection=True) 
    
    vRayLight=[]
    if(len(mySelection)<1):
        cmds.error("please,select at least one vray light")
    for obj in mySelection:
        shapeNode=cmds.listRelatives(obj,shapes=True)
        
        nodeType=cmds.nodeType(shapeNode)
        if(nodeType=="VRayLightIESShape"):   
            vRayLight.append(str(obj))
            
        elif(nodeType=="VRayLightDomeShape" or nodeType=="VRayLightSphereShape" or nodeType=="VRayLightRectShape"):
            ignore(obj)            
    
    for light in vRayLight:
        cmds.setAttr(light+".areaSpeculars",state)

        
createUI()