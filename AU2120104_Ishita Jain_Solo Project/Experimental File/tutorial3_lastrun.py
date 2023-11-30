#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on November 29, 2023, at 20:14
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'tutorial3'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\Ahmedabad University - BA (Hons.)\\Third Year\\Monsoon Semester\\PSY310 Lab in Psychology\\Final Project = 30 mks\\Experimental File\\tutorial3_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "trial_5" ---
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
target = visual.TextStim(win=win, name='target',
    text='C',
    font='Open Sans',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
distractors = visual.TextStim(win=win, name='distractors',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
distractors_2 = visual.TextStim(win=win, name='distractors_2',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
distractors_3 = visual.TextStim(win=win, name='distractors_3',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
distractors_4 = visual.TextStim(win=win, name='distractors_4',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
distractors_5 = visual.TextStim(win=win, name='distractors_5',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
distractors_6 = visual.TextStim(win=win, name='distractors_6',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "trial_10" ---
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
target_2 = visual.TextStim(win=win, name='target_2',
    text='C',
    font='Open Sans',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
distractors_7 = visual.TextStim(win=win, name='distractors_7',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
distractors_8 = visual.TextStim(win=win, name='distractors_8',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
distractors_9 = visual.TextStim(win=win, name='distractors_9',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
distractors_10 = visual.TextStim(win=win, name='distractors_10',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
distractors_11 = visual.TextStim(win=win, name='distractors_11',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
distractors_12 = visual.TextStim(win=win, name='distractors_12',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
distractors_13 = visual.TextStim(win=win, name='distractors_13',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
distractors_14 = visual.TextStim(win=win, name='distractors_14',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
distractors_16 = visual.TextStim(win=win, name='distractors_16',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
distractors_15 = visual.TextStim(win=win, name='distractors_15',
    text='O',
    font='Open Sans',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=25.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('colorcondition.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial_5" ---
    continueRoutine = True
    # update component parameters for each repeat
    target.setColor(color, colorSpace='rgb')
    target.setPos((random()-0.5, random()-0.5))
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    mouse.mouseClock.reset()
    distractors.setColor('red', colorSpace='rgb')
    distractors.setPos((random()-0.5, random()-0.5))
    distractors_2.setColor('red', colorSpace='rgb')
    distractors_2.setPos((random()-0.5, random()-0.5))
    distractors_3.setColor('red', colorSpace='rgb')
    distractors_3.setPos((random()-0.5, random()-0.5))
    distractors_4.setColor('yellow', colorSpace='rgb')
    distractors_4.setPos((random()-0.5, random()-0.5))
    distractors_5.setColor('yellow', colorSpace='rgb')
    distractors_5.setPos((random()-0.5, random()-0.5))
    distractors_6.setColor('yellow', colorSpace='rgb')
    distractors_6.setPos((random()-0.5, random()-0.5))
    # keep track of which components have finished
    trial_5Components = [fixation, target, mouse, distractors, distractors_2, distractors_3, distractors_4, distractors_5, distractors_6]
    for thisComponent in trial_5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_5" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        
        # if fixation is starting this frame...
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation.started')
            # update status
            fixation.status = STARTED
            fixation.setAutoDraw(True)
        
        # if fixation is active this frame...
        if fixation.status == STARTED:
            # update params
            pass
        
        # if fixation is stopping this frame...
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.stopped')
                # update status
                fixation.status = FINISHED
                fixation.setAutoDraw(False)
        
        # *target* updates
        
        # if target is starting this frame...
        if target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target.started')
            # update status
            target.status = STARTED
            target.setAutoDraw(True)
        
        # if target is active this frame...
        if target.status == STARTED:
            # update params
            pass
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(target, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # *distractors* updates
        
        # if distractors is starting this frame...
        if distractors.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors.frameNStart = frameN  # exact frame index
            distractors.tStart = t  # local t and not account for scr refresh
            distractors.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors.started')
            # update status
            distractors.status = STARTED
            distractors.setAutoDraw(True)
        
        # if distractors is active this frame...
        if distractors.status == STARTED:
            # update params
            pass
        
        # *distractors_2* updates
        
        # if distractors_2 is starting this frame...
        if distractors_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors_2.frameNStart = frameN  # exact frame index
            distractors_2.tStart = t  # local t and not account for scr refresh
            distractors_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors_2.started')
            # update status
            distractors_2.status = STARTED
            distractors_2.setAutoDraw(True)
        
        # if distractors_2 is active this frame...
        if distractors_2.status == STARTED:
            # update params
            pass
        
        # *distractors_3* updates
        
        # if distractors_3 is starting this frame...
        if distractors_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors_3.frameNStart = frameN  # exact frame index
            distractors_3.tStart = t  # local t and not account for scr refresh
            distractors_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors_3.started')
            # update status
            distractors_3.status = STARTED
            distractors_3.setAutoDraw(True)
        
        # if distractors_3 is active this frame...
        if distractors_3.status == STARTED:
            # update params
            pass
        
        # *distractors_4* updates
        
        # if distractors_4 is starting this frame...
        if distractors_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors_4.frameNStart = frameN  # exact frame index
            distractors_4.tStart = t  # local t and not account for scr refresh
            distractors_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors_4.started')
            # update status
            distractors_4.status = STARTED
            distractors_4.setAutoDraw(True)
        
        # if distractors_4 is active this frame...
        if distractors_4.status == STARTED:
            # update params
            pass
        
        # *distractors_5* updates
        
        # if distractors_5 is starting this frame...
        if distractors_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors_5.frameNStart = frameN  # exact frame index
            distractors_5.tStart = t  # local t and not account for scr refresh
            distractors_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors_5.started')
            # update status
            distractors_5.status = STARTED
            distractors_5.setAutoDraw(True)
        
        # if distractors_5 is active this frame...
        if distractors_5.status == STARTED:
            # update params
            pass
        
        # *distractors_6* updates
        
        # if distractors_6 is starting this frame...
        if distractors_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors_6.frameNStart = frameN  # exact frame index
            distractors_6.tStart = t  # local t and not account for scr refresh
            distractors_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors_6.started')
            # update status
            distractors_6.status = STARTED
            distractors_6.setAutoDraw(True)
        
        # if distractors_6 is active this frame...
        if distractors_6.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_5" ---
    for thisComponent in trial_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('mouse.x', mouse.x)
    trials.addData('mouse.y', mouse.y)
    trials.addData('mouse.leftButton', mouse.leftButton)
    trials.addData('mouse.midButton', mouse.midButton)
    trials.addData('mouse.rightButton', mouse.rightButton)
    trials.addData('mouse.time', mouse.time)
    trials.addData('mouse.clicked_name', mouse.clicked_name)
    # the Routine "trial_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_10" ---
    continueRoutine = True
    # update component parameters for each repeat
    target_2.setColor(color, colorSpace='rgb')
    target_2.setPos((random()-0.5, random()-0.5))
    # setup some python lists for storing info about the mouse_2
    mouse_2.x = []
    mouse_2.y = []
    mouse_2.leftButton = []
    mouse_2.midButton = []
    mouse_2.rightButton = []
    mouse_2.time = []
    mouse_2.clicked_name = []
    gotValidClick = False  # until a click is received
    mouse_2.mouseClock.reset()
    distractors_7.setColor('yellow', colorSpace='rgb')
    distractors_7.setPos((random()-0.5, random()-0.5))
    distractors_8.setColor('yellow', colorSpace='rgb')
    distractors_8.setPos((random()-0.5, random()-0.5))
    distractors_9.setColor('yellow', colorSpace='rgb')
    distractors_9.setPos((random()-0.5, random()-0.5))
    distractors_10.setColor('yellow', colorSpace='rgb')
    distractors_10.setPos((random()-0.5, random()-0.5))
    distractors_11.setColor('yellow', colorSpace='rgb')
    distractors_11.setPos((random()-0.5, random()-0.5))
    distractors_12.setColor('red', colorSpace='rgb')
    distractors_12.setPos((random()-0.5, random()-0.5))
    distractors_13.setColor('red', colorSpace='rgb')
    distractors_13.setPos((random()-0.5, random()-0.5))
    distractors_14.setColor('red', colorSpace='rgb')
    distractors_14.setPos((random()-0.5, random()-0.5))
    distractors_16.setColor('red', colorSpace='rgb')
    distractors_16.setPos((random()-0.5, random()-0.5))
    distractors_15.setColor('red', colorSpace='rgb')
    distractors_15.setPos((random()-0.5, random()-0.5))
    # keep track of which components have finished
    trial_10Components = [fixation_2, target_2, mouse_2, distractors_7, distractors_8, distractors_9, distractors_10, distractors_11, distractors_12, distractors_13, distractors_14, distractors_16, distractors_15]
    for thisComponent in trial_10Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_10" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_2* updates
        
        # if fixation_2 is starting this frame...
        if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_2.frameNStart = frameN  # exact frame index
            fixation_2.tStart = t  # local t and not account for scr refresh
            fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_2.started')
            # update status
            fixation_2.status = STARTED
            fixation_2.setAutoDraw(True)
        
        # if fixation_2 is active this frame...
        if fixation_2.status == STARTED:
            # update params
            pass
        
        # if fixation_2 is stopping this frame...
        if fixation_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation_2.tStop = t  # not accounting for scr refresh
                fixation_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_2.stopped')
                # update status
                fixation_2.status = FINISHED
                fixation_2.setAutoDraw(False)
        
        # *target_2* updates
        
        # if target_2 is starting this frame...
        if target_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target_2.frameNStart = frameN  # exact frame index
            target_2.tStart = t  # local t and not account for scr refresh
            target_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_2.started')
            # update status
            target_2.status = STARTED
            target_2.setAutoDraw(True)
        
        # if target_2 is active this frame...
        if target_2.status == STARTED:
            # update params
            pass
        # *mouse_2* updates
        
        # if mouse_2 is starting this frame...
        if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_2.started', t)
            # update status
            mouse_2.status = STARTED
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(target, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_2):
                            gotValidClick = True
                            mouse_2.clicked_name.append(obj.name)
                    x, y = mouse_2.getPos()
                    mouse_2.x.append(x)
                    mouse_2.y.append(y)
                    buttons = mouse_2.getPressed()
                    mouse_2.leftButton.append(buttons[0])
                    mouse_2.midButton.append(buttons[1])
                    mouse_2.rightButton.append(buttons[2])
                    mouse_2.time.append(mouse_2.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # *distractors_7* updates
        
        # if distractors_7 is starting this frame...
        if distractors_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors_7.frameNStart = frameN  # exact frame index
            distractors_7.tStart = t  # local t and not account for scr refresh
            distractors_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors_7.started')
            # update status
            distractors_7.status = STARTED
            distractors_7.setAutoDraw(True)
        
        # if distractors_7 is active this frame...
        if distractors_7.status == STARTED:
            # update params
            pass
        
        # *distractors_8* updates
        
        # if distractors_8 is starting this frame...
        if distractors_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors_8.frameNStart = frameN  # exact frame index
            distractors_8.tStart = t  # local t and not account for scr refresh
            distractors_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors_8.started')
            # update status
            distractors_8.status = STARTED
            distractors_8.setAutoDraw(True)
        
        # if distractors_8 is active this frame...
        if distractors_8.status == STARTED:
            # update params
            pass
        
        # *distractors_9* updates
        
        # if distractors_9 is starting this frame...
        if distractors_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors_9.frameNStart = frameN  # exact frame index
            distractors_9.tStart = t  # local t and not account for scr refresh
            distractors_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors_9.started')
            # update status
            distractors_9.status = STARTED
            distractors_9.setAutoDraw(True)
        
        # if distractors_9 is active this frame...
        if distractors_9.status == STARTED:
            # update params
            pass
        
        # *distractors_10* updates
        
        # if distractors_10 is starting this frame...
        if distractors_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors_10.frameNStart = frameN  # exact frame index
            distractors_10.tStart = t  # local t and not account for scr refresh
            distractors_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors_10.started')
            # update status
            distractors_10.status = STARTED
            distractors_10.setAutoDraw(True)
        
        # if distractors_10 is active this frame...
        if distractors_10.status == STARTED:
            # update params
            pass
        
        # *distractors_11* updates
        
        # if distractors_11 is starting this frame...
        if distractors_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors_11.frameNStart = frameN  # exact frame index
            distractors_11.tStart = t  # local t and not account for scr refresh
            distractors_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors_11.started')
            # update status
            distractors_11.status = STARTED
            distractors_11.setAutoDraw(True)
        
        # if distractors_11 is active this frame...
        if distractors_11.status == STARTED:
            # update params
            pass
        
        # *distractors_12* updates
        
        # if distractors_12 is starting this frame...
        if distractors_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors_12.frameNStart = frameN  # exact frame index
            distractors_12.tStart = t  # local t and not account for scr refresh
            distractors_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors_12.started')
            # update status
            distractors_12.status = STARTED
            distractors_12.setAutoDraw(True)
        
        # if distractors_12 is active this frame...
        if distractors_12.status == STARTED:
            # update params
            pass
        
        # *distractors_13* updates
        
        # if distractors_13 is starting this frame...
        if distractors_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors_13.frameNStart = frameN  # exact frame index
            distractors_13.tStart = t  # local t and not account for scr refresh
            distractors_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors_13.started')
            # update status
            distractors_13.status = STARTED
            distractors_13.setAutoDraw(True)
        
        # if distractors_13 is active this frame...
        if distractors_13.status == STARTED:
            # update params
            pass
        
        # *distractors_14* updates
        
        # if distractors_14 is starting this frame...
        if distractors_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors_14.frameNStart = frameN  # exact frame index
            distractors_14.tStart = t  # local t and not account for scr refresh
            distractors_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors_14.started')
            # update status
            distractors_14.status = STARTED
            distractors_14.setAutoDraw(True)
        
        # if distractors_14 is active this frame...
        if distractors_14.status == STARTED:
            # update params
            pass
        
        # *distractors_16* updates
        
        # if distractors_16 is starting this frame...
        if distractors_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors_16.frameNStart = frameN  # exact frame index
            distractors_16.tStart = t  # local t and not account for scr refresh
            distractors_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors_16.started')
            # update status
            distractors_16.status = STARTED
            distractors_16.setAutoDraw(True)
        
        # if distractors_16 is active this frame...
        if distractors_16.status == STARTED:
            # update params
            pass
        
        # *distractors_15* updates
        
        # if distractors_15 is starting this frame...
        if distractors_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractors_15.frameNStart = frameN  # exact frame index
            distractors_15.tStart = t  # local t and not account for scr refresh
            distractors_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractors_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'distractors_15.started')
            # update status
            distractors_15.status = STARTED
            distractors_15.setAutoDraw(True)
        
        # if distractors_15 is active this frame...
        if distractors_15.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_10" ---
    for thisComponent in trial_10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('mouse_2.x', mouse_2.x)
    trials.addData('mouse_2.y', mouse_2.y)
    trials.addData('mouse_2.leftButton', mouse_2.leftButton)
    trials.addData('mouse_2.midButton', mouse_2.midButton)
    trials.addData('mouse_2.rightButton', mouse_2.rightButton)
    trials.addData('mouse_2.time', mouse_2.time)
    trials.addData('mouse_2.clicked_name', mouse_2.clicked_name)
    # the Routine "trial_10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 25.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
