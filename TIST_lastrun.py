#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Fri  1 Aug 14:43:39 2025
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'TIST'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1920, 1080]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/Chenxiao/Documents/project_codes/TIST_stable_v1/TIST_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp_welcome') is None:
        # initialise key_resp_welcome
        key_resp_welcome = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_welcome',
        )
    if deviceManager.getDevice('key_resp_practice_instruct') is None:
        # initialise key_resp_practice_instruct
        key_resp_practice_instruct = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_practice_instruct',
        )
    if deviceManager.getDevice('key_resp_block_practice') is None:
        # initialise key_resp_block_practice
        key_resp_block_practice = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_block_practice',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_continue_check') is None:
        # initialise key_resp_continue_check
        key_resp_continue_check = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_continue_check',
        )
    if deviceManager.getDevice('key_resp_primary_welcome') is None:
        # initialise key_resp_primary_welcome
        key_resp_primary_welcome = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_primary_welcome',
        )
    if deviceManager.getDevice('key_resp_block') is None:
        # initialise key_resp_block
        key_resp_block = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_block',
        )
    if deviceManager.getDevice('key_resp_feedback_block') is None:
        # initialise key_resp_feedback_block
        key_resp_feedback_block = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_feedback_block',
        )
    if deviceManager.getDevice('key_resp_contiue_check_block') is None:
        # initialise key_resp_contiue_check_block
        key_resp_contiue_check_block = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_contiue_check_block',
        )
    if deviceManager.getDevice('key_resp_goodbye') is None:
        # initialise key_resp_goodbye
        key_resp_goodbye = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_goodbye',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "welcome" ---
    image_welcome = visual.ImageStim(
        win=win,
        name='image_welcome', 
        image='stimuli/welcome.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.1, 0.825),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_welcome = keyboard.Keyboard(deviceName='key_resp_welcome')
    
    # --- Initialize components for Routine "refresh" ---
    text_refresh = visual.TextStim(win=win, name='text_refresh',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "practice_instruct" ---
    image_practice_instruct = visual.ImageStim(
        win=win,
        name='image_practice_instruct', 
        image='stimuli/practice_instruct.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.1, 0.825),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_practice_instruct = keyboard.Keyboard(deviceName='key_resp_practice_instruct')
    
    # --- Initialize components for Routine "refresh" ---
    text_refresh = visual.TextStim(win=win, name='text_refresh',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "fixation" ---
    text_fixation = visual.TextStim(win=win, name='text_fixation',
        text='+',
        font='Noto Sans SC',
        pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "block_practice" ---
    image_block_practice = visual.ImageStim(
        win=win,
        name='image_block_practice', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.36, 0.41535),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_block_practice = keyboard.Keyboard(deviceName='key_resp_block_practice')
    
    # --- Initialize components for Routine "refresh" ---
    text_refresh = visual.TextStim(win=win, name='text_refresh',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "answer_block_practice" ---
    text_answer_block_practice = visual.TextStim(win=win, name='text_answer_block_practice',
        text='请按如下顺序输入答案（数字中间无间隔或任何字符）：\n\n快乐-平静-悲伤',
        font='Noto Sans SC',
        pos=(0, 0.3), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    textbox_answer_block_practice = visual.TextBox2(
         win, text=None, placeholder=None, font='Noto Sans SC',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textbox_answer_block_practice',
         depth=-1, autoLog=True,
    )
    button_text_block_practice = visual.TextStim(win=win, name='button_text_block_practice',
        text='点击这里继续',
        font='Noto Sans SC',
        pos=(0, -0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    mouse_block_practice = event.Mouse(win=win)
    x, y = [None, None]
    mouse_block_practice.mouseClock = core.Clock()
    # Run 'Begin Experiment' code from code
    feedback_text = ""
    
    # --- Initialize components for Routine "refresh" ---
    text_refresh = visual.TextStim(win=win, name='text_refresh',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "feedback_block_practice" ---
    text_feedback_block_practice = visual.TextStim(win=win, name='text_feedback_block_practice',
        text='',
        font='Noto Sans SC',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_feedback_note_practice = visual.TextStim(win=win, name='text_feedback_note_practice',
        text='请按空格键继续',
        font='Noto Sans SC',
        pos=(0, -0.25), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "refresh" ---
    text_refresh = visual.TextStim(win=win, name='text_refresh',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "continue_check" ---
    image_continue_check = visual.ImageStim(
        win=win,
        name='image_continue_check', 
        image='stimuli/continue_check.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.1, 0.825),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_continue_check = keyboard.Keyboard(deviceName='key_resp_continue_check')
    
    # --- Initialize components for Routine "refresh" ---
    text_refresh = visual.TextStim(win=win, name='text_refresh',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "primary_task_welcome" ---
    image_primary_welcome = visual.ImageStim(
        win=win,
        name='image_primary_welcome', 
        image='stimuli/welcome_primary.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.1, 0.825),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_primary_welcome = keyboard.Keyboard(deviceName='key_resp_primary_welcome')
    
    # --- Initialize components for Routine "refresh" ---
    text_refresh = visual.TextStim(win=win, name='text_refresh',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "fixation" ---
    text_fixation = visual.TextStim(win=win, name='text_fixation',
        text='+',
        font='Noto Sans SC',
        pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "block" ---
    image_block = visual.ImageStim(
        win=win,
        name='image_block', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.36, 0.41535),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_block = keyboard.Keyboard(deviceName='key_resp_block')
    
    # --- Initialize components for Routine "refresh" ---
    text_refresh = visual.TextStim(win=win, name='text_refresh',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "answer_block" ---
    text_answer_block = visual.TextStim(win=win, name='text_answer_block',
        text='请按如下顺序输入答案（数字中间无间隔或任何字符）：\n\n快乐-平静-悲伤',
        font='Noto Sans SC',
        pos=(0, 0.3), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    textbox_answer_block = visual.TextBox2(
         win, text=None, placeholder=None, font='Noto Sans SC',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textbox_answer_block',
         depth=-1, autoLog=True,
    )
    button_answer_block = visual.TextStim(win=win, name='button_answer_block',
        text='点击这里继续',
        font='Noto Sans SC',
        pos=(0, -0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    mouse_answer_block = event.Mouse(win=win)
    x, y = [None, None]
    mouse_answer_block.mouseClock = core.Clock()
    # Run 'Begin Experiment' code from code_answer_block
    feedback_text_primary = ""
    
    # --- Initialize components for Routine "refresh" ---
    text_refresh = visual.TextStim(win=win, name='text_refresh',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "feedback_block" ---
    text_feedback_block = visual.TextStim(win=win, name='text_feedback_block',
        text='',
        font='Noto Sans SC',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_feedback_block_note = visual.TextStim(win=win, name='text_feedback_block_note',
        text='请按空格键继续',
        font='Noto Sans SC',
        pos=(0, -0.25), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_feedback_block = keyboard.Keyboard(deviceName='key_resp_feedback_block')
    
    # --- Initialize components for Routine "refresh" ---
    text_refresh = visual.TextStim(win=win, name='text_refresh',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "continue_check_block" ---
    text_continue_check_block = visual.TextStim(win=win, name='text_continue_check_block',
        text=None,
        font='Noto Sans SC',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from code_progress_report
    block_counter = 0
    text_continue_prompt = visual.TextStim(win=win, name='text_continue_prompt',
        text='请按空格键继续。',
        font='Noto Sans SC',
        pos=(0, -0.25), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp_contiue_check_block = keyboard.Keyboard(deviceName='key_resp_contiue_check_block')
    
    # --- Initialize components for Routine "refresh" ---
    text_refresh = visual.TextStim(win=win, name='text_refresh',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "goodbye" ---
    text_goodbye = visual.TextStim(win=win, name='text_goodbye',
        text='测试结束。\n\n感谢您参与本测试，祝生活愉快！',
        font='Noto Sans SC',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_goodbye = keyboard.Keyboard(deviceName='key_resp_goodbye')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "welcome" ---
    # create an object to store info about Routine welcome
    welcome = data.Routine(
        name='welcome',
        components=[image_welcome, key_resp_welcome],
    )
    welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_welcome
    key_resp_welcome.keys = []
    key_resp_welcome.rt = []
    _key_resp_welcome_allKeys = []
    # store start times for welcome
    welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcome.tStart = globalClock.getTime(format='float')
    welcome.status = STARTED
    thisExp.addData('welcome.started', welcome.tStart)
    welcome.maxDuration = None
    # keep track of which components have finished
    welcomeComponents = welcome.components
    for thisComponent in welcome.components:
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
    
    # --- Run Routine "welcome" ---
    welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_welcome* updates
        
        # if image_welcome is starting this frame...
        if image_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_welcome.frameNStart = frameN  # exact frame index
            image_welcome.tStart = t  # local t and not account for scr refresh
            image_welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_welcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_welcome.started')
            # update status
            image_welcome.status = STARTED
            image_welcome.setAutoDraw(True)
        
        # if image_welcome is active this frame...
        if image_welcome.status == STARTED:
            # update params
            pass
        
        # *key_resp_welcome* updates
        waitOnFlip = False
        
        # if key_resp_welcome is starting this frame...
        if key_resp_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_welcome.frameNStart = frameN  # exact frame index
            key_resp_welcome.tStart = t  # local t and not account for scr refresh
            key_resp_welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_welcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_welcome.started')
            # update status
            key_resp_welcome.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_welcome.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_welcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_welcome.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_welcome.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_welcome_allKeys.extend(theseKeys)
            if len(_key_resp_welcome_allKeys):
                key_resp_welcome.keys = _key_resp_welcome_allKeys[-1].name  # just the last key pressed
                key_resp_welcome.rt = _key_resp_welcome_allKeys[-1].rt
                key_resp_welcome.duration = _key_resp_welcome_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcome
    welcome.tStop = globalClock.getTime(format='float')
    welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('welcome.stopped', welcome.tStop)
    # check responses
    if key_resp_welcome.keys in ['', [], None]:  # No response was made
        key_resp_welcome.keys = None
    thisExp.addData('key_resp_welcome.keys',key_resp_welcome.keys)
    if key_resp_welcome.keys != None:  # we had a response
        thisExp.addData('key_resp_welcome.rt', key_resp_welcome.rt)
        thisExp.addData('key_resp_welcome.duration', key_resp_welcome.duration)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "refresh" ---
    # create an object to store info about Routine refresh
    refresh = data.Routine(
        name='refresh',
        components=[text_refresh],
    )
    refresh.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for refresh
    refresh.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    refresh.tStart = globalClock.getTime(format='float')
    refresh.status = STARTED
    thisExp.addData('refresh.started', refresh.tStart)
    refresh.maxDuration = None
    # keep track of which components have finished
    refreshComponents = refresh.components
    for thisComponent in refresh.components:
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
    
    # --- Run Routine "refresh" ---
    refresh.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.2:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_refresh* updates
        
        # if text_refresh is starting this frame...
        if text_refresh.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_refresh.frameNStart = frameN  # exact frame index
            text_refresh.tStart = t  # local t and not account for scr refresh
            text_refresh.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_refresh, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_refresh.started')
            # update status
            text_refresh.status = STARTED
            text_refresh.setAutoDraw(True)
        
        # if text_refresh is active this frame...
        if text_refresh.status == STARTED:
            # update params
            pass
        
        # if text_refresh is stopping this frame...
        if text_refresh.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_refresh.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                text_refresh.tStop = t  # not accounting for scr refresh
                text_refresh.tStopRefresh = tThisFlipGlobal  # on global time
                text_refresh.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_refresh.stopped')
                # update status
                text_refresh.status = FINISHED
                text_refresh.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            refresh.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in refresh.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "refresh" ---
    for thisComponent in refresh.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for refresh
    refresh.tStop = globalClock.getTime(format='float')
    refresh.tStopRefresh = tThisFlipGlobal
    thisExp.addData('refresh.stopped', refresh.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if refresh.maxDurationReached:
        routineTimer.addTime(-refresh.maxDuration)
    elif refresh.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.200000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "practice_instruct" ---
    # create an object to store info about Routine practice_instruct
    practice_instruct = data.Routine(
        name='practice_instruct',
        components=[image_practice_instruct, key_resp_practice_instruct],
    )
    practice_instruct.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_practice_instruct
    key_resp_practice_instruct.keys = []
    key_resp_practice_instruct.rt = []
    _key_resp_practice_instruct_allKeys = []
    # store start times for practice_instruct
    practice_instruct.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    practice_instruct.tStart = globalClock.getTime(format='float')
    practice_instruct.status = STARTED
    thisExp.addData('practice_instruct.started', practice_instruct.tStart)
    practice_instruct.maxDuration = None
    # keep track of which components have finished
    practice_instructComponents = practice_instruct.components
    for thisComponent in practice_instruct.components:
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
    
    # --- Run Routine "practice_instruct" ---
    practice_instruct.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_practice_instruct* updates
        
        # if image_practice_instruct is starting this frame...
        if image_practice_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_practice_instruct.frameNStart = frameN  # exact frame index
            image_practice_instruct.tStart = t  # local t and not account for scr refresh
            image_practice_instruct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_practice_instruct, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_practice_instruct.started')
            # update status
            image_practice_instruct.status = STARTED
            image_practice_instruct.setAutoDraw(True)
        
        # if image_practice_instruct is active this frame...
        if image_practice_instruct.status == STARTED:
            # update params
            pass
        
        # *key_resp_practice_instruct* updates
        waitOnFlip = False
        
        # if key_resp_practice_instruct is starting this frame...
        if key_resp_practice_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_practice_instruct.frameNStart = frameN  # exact frame index
            key_resp_practice_instruct.tStart = t  # local t and not account for scr refresh
            key_resp_practice_instruct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_practice_instruct, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_practice_instruct.started')
            # update status
            key_resp_practice_instruct.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_practice_instruct.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_practice_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_practice_instruct.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_practice_instruct.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_practice_instruct_allKeys.extend(theseKeys)
            if len(_key_resp_practice_instruct_allKeys):
                key_resp_practice_instruct.keys = _key_resp_practice_instruct_allKeys[-1].name  # just the last key pressed
                key_resp_practice_instruct.rt = _key_resp_practice_instruct_allKeys[-1].rt
                key_resp_practice_instruct.duration = _key_resp_practice_instruct_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            practice_instruct.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_instruct.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_instruct" ---
    for thisComponent in practice_instruct.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for practice_instruct
    practice_instruct.tStop = globalClock.getTime(format='float')
    practice_instruct.tStopRefresh = tThisFlipGlobal
    thisExp.addData('practice_instruct.stopped', practice_instruct.tStop)
    # check responses
    if key_resp_practice_instruct.keys in ['', [], None]:  # No response was made
        key_resp_practice_instruct.keys = None
    thisExp.addData('key_resp_practice_instruct.keys',key_resp_practice_instruct.keys)
    if key_resp_practice_instruct.keys != None:  # we had a response
        thisExp.addData('key_resp_practice_instruct.rt', key_resp_practice_instruct.rt)
        thisExp.addData('key_resp_practice_instruct.duration', key_resp_practice_instruct.duration)
    thisExp.nextEntry()
    # the Routine "practice_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "refresh" ---
    # create an object to store info about Routine refresh
    refresh = data.Routine(
        name='refresh',
        components=[text_refresh],
    )
    refresh.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for refresh
    refresh.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    refresh.tStart = globalClock.getTime(format='float')
    refresh.status = STARTED
    thisExp.addData('refresh.started', refresh.tStart)
    refresh.maxDuration = None
    # keep track of which components have finished
    refreshComponents = refresh.components
    for thisComponent in refresh.components:
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
    
    # --- Run Routine "refresh" ---
    refresh.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.2:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_refresh* updates
        
        # if text_refresh is starting this frame...
        if text_refresh.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_refresh.frameNStart = frameN  # exact frame index
            text_refresh.tStart = t  # local t and not account for scr refresh
            text_refresh.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_refresh, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_refresh.started')
            # update status
            text_refresh.status = STARTED
            text_refresh.setAutoDraw(True)
        
        # if text_refresh is active this frame...
        if text_refresh.status == STARTED:
            # update params
            pass
        
        # if text_refresh is stopping this frame...
        if text_refresh.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_refresh.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                text_refresh.tStop = t  # not accounting for scr refresh
                text_refresh.tStopRefresh = tThisFlipGlobal  # on global time
                text_refresh.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_refresh.stopped')
                # update status
                text_refresh.status = FINISHED
                text_refresh.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            refresh.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in refresh.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "refresh" ---
    for thisComponent in refresh.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for refresh
    refresh.tStop = globalClock.getTime(format='float')
    refresh.tStopRefresh = tThisFlipGlobal
    thisExp.addData('refresh.stopped', refresh.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if refresh.maxDurationReached:
        routineTimer.addTime(-refresh.maxDuration)
    elif refresh.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.200000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    loop_practice = data.TrialHandler2(
        name='loop_practice',
        nReps=99.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('loop_block_practice.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(loop_practice)  # add the loop to the experiment
    thisLoop_practice = loop_practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_practice.rgb)
    if thisLoop_practice != None:
        for paramName in thisLoop_practice:
            globals()[paramName] = thisLoop_practice[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoop_practice in loop_practice:
        currentLoop = loop_practice
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_practice.rgb)
        if thisLoop_practice != None:
            for paramName in thisLoop_practice:
                globals()[paramName] = thisLoop_practice[paramName]
        
        # --- Prepare to start Routine "fixation" ---
        # create an object to store info about Routine fixation
        fixation = data.Routine(
            name='fixation',
            components=[text_fixation],
        )
        fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fixation
        fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fixation.tStart = globalClock.getTime(format='float')
        fixation.status = STARTED
        thisExp.addData('fixation.started', fixation.tStart)
        fixation.maxDuration = None
        # keep track of which components have finished
        fixationComponents = fixation.components
        for thisComponent in fixation.components:
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
        
        # --- Run Routine "fixation" ---
        # if trial has changed, end Routine now
        if isinstance(loop_practice, data.TrialHandler2) and thisLoop_practice.thisN != loop_practice.thisTrial.thisN:
            continueRoutine = False
        fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_fixation* updates
            
            # if text_fixation is starting this frame...
            if text_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_fixation.frameNStart = frameN  # exact frame index
                text_fixation.tStart = t  # local t and not account for scr refresh
                text_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_fixation.started')
                # update status
                text_fixation.status = STARTED
                text_fixation.setAutoDraw(True)
            
            # if text_fixation is active this frame...
            if text_fixation.status == STARTED:
                # update params
                pass
            
            # if text_fixation is stopping this frame...
            if text_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_fixation.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_fixation.tStop = t  # not accounting for scr refresh
                    text_fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    text_fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_fixation.stopped')
                    # update status
                    text_fixation.status = FINISHED
                    text_fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                fixation.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fixation
        fixation.tStop = globalClock.getTime(format='float')
        fixation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fixation.stopped', fixation.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fixation.maxDurationReached:
            routineTimer.addTime(-fixation.maxDuration)
        elif fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # set up handler to look after randomisation of conditions etc
        loop_block_practice = data.TrialHandler2(
            name='loop_block_practice',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(block_practice_file), 
            seed=None, 
        )
        thisExp.addLoop(loop_block_practice)  # add the loop to the experiment
        thisLoop_block_practice = loop_block_practice.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_block_practice.rgb)
        if thisLoop_block_practice != None:
            for paramName in thisLoop_block_practice:
                globals()[paramName] = thisLoop_block_practice[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisLoop_block_practice in loop_block_practice:
            currentLoop = loop_block_practice
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_block_practice.rgb)
            if thisLoop_block_practice != None:
                for paramName in thisLoop_block_practice:
                    globals()[paramName] = thisLoop_block_practice[paramName]
            
            # --- Prepare to start Routine "block_practice" ---
            # create an object to store info about Routine block_practice
            block_practice = data.Routine(
                name='block_practice',
                components=[image_block_practice, key_resp_block_practice],
            )
            block_practice.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_block_practice.setImage(stimulus)
            # create starting attributes for key_resp_block_practice
            key_resp_block_practice.keys = []
            key_resp_block_practice.rt = []
            _key_resp_block_practice_allKeys = []
            # store start times for block_practice
            block_practice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            block_practice.tStart = globalClock.getTime(format='float')
            block_practice.status = STARTED
            thisExp.addData('block_practice.started', block_practice.tStart)
            block_practice.maxDuration = None
            # keep track of which components have finished
            block_practiceComponents = block_practice.components
            for thisComponent in block_practice.components:
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
            
            # --- Run Routine "block_practice" ---
            # if trial has changed, end Routine now
            if isinstance(loop_block_practice, data.TrialHandler2) and thisLoop_block_practice.thisN != loop_block_practice.thisTrial.thisN:
                continueRoutine = False
            block_practice.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_block_practice* updates
                
                # if image_block_practice is starting this frame...
                if image_block_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_block_practice.frameNStart = frameN  # exact frame index
                    image_block_practice.tStart = t  # local t and not account for scr refresh
                    image_block_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_block_practice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_block_practice.started')
                    # update status
                    image_block_practice.status = STARTED
                    image_block_practice.setAutoDraw(True)
                
                # if image_block_practice is active this frame...
                if image_block_practice.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_block_practice* updates
                waitOnFlip = False
                
                # if key_resp_block_practice is starting this frame...
                if key_resp_block_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_block_practice.frameNStart = frameN  # exact frame index
                    key_resp_block_practice.tStart = t  # local t and not account for scr refresh
                    key_resp_block_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_block_practice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_block_practice.started')
                    # update status
                    key_resp_block_practice.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_block_practice.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_block_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_block_practice.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_block_practice.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_block_practice_allKeys.extend(theseKeys)
                    if len(_key_resp_block_practice_allKeys):
                        key_resp_block_practice.keys = _key_resp_block_practice_allKeys[-1].name  # just the last key pressed
                        key_resp_block_practice.rt = _key_resp_block_practice_allKeys[-1].rt
                        key_resp_block_practice.duration = _key_resp_block_practice_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    block_practice.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in block_practice.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "block_practice" ---
            for thisComponent in block_practice.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for block_practice
            block_practice.tStop = globalClock.getTime(format='float')
            block_practice.tStopRefresh = tThisFlipGlobal
            thisExp.addData('block_practice.stopped', block_practice.tStop)
            # check responses
            if key_resp_block_practice.keys in ['', [], None]:  # No response was made
                key_resp_block_practice.keys = None
            loop_block_practice.addData('key_resp_block_practice.keys',key_resp_block_practice.keys)
            if key_resp_block_practice.keys != None:  # we had a response
                loop_block_practice.addData('key_resp_block_practice.rt', key_resp_block_practice.rt)
                loop_block_practice.addData('key_resp_block_practice.duration', key_resp_block_practice.duration)
            # the Routine "block_practice" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "refresh" ---
            # create an object to store info about Routine refresh
            refresh = data.Routine(
                name='refresh',
                components=[text_refresh],
            )
            refresh.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for refresh
            refresh.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            refresh.tStart = globalClock.getTime(format='float')
            refresh.status = STARTED
            thisExp.addData('refresh.started', refresh.tStart)
            refresh.maxDuration = None
            # keep track of which components have finished
            refreshComponents = refresh.components
            for thisComponent in refresh.components:
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
            
            # --- Run Routine "refresh" ---
            # if trial has changed, end Routine now
            if isinstance(loop_block_practice, data.TrialHandler2) and thisLoop_block_practice.thisN != loop_block_practice.thisTrial.thisN:
                continueRoutine = False
            refresh.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.2:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_refresh* updates
                
                # if text_refresh is starting this frame...
                if text_refresh.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_refresh.frameNStart = frameN  # exact frame index
                    text_refresh.tStart = t  # local t and not account for scr refresh
                    text_refresh.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_refresh, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_refresh.started')
                    # update status
                    text_refresh.status = STARTED
                    text_refresh.setAutoDraw(True)
                
                # if text_refresh is active this frame...
                if text_refresh.status == STARTED:
                    # update params
                    pass
                
                # if text_refresh is stopping this frame...
                if text_refresh.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_refresh.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        text_refresh.tStop = t  # not accounting for scr refresh
                        text_refresh.tStopRefresh = tThisFlipGlobal  # on global time
                        text_refresh.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_refresh.stopped')
                        # update status
                        text_refresh.status = FINISHED
                        text_refresh.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    refresh.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in refresh.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "refresh" ---
            for thisComponent in refresh.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for refresh
            refresh.tStop = globalClock.getTime(format='float')
            refresh.tStopRefresh = tThisFlipGlobal
            thisExp.addData('refresh.stopped', refresh.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if refresh.maxDurationReached:
                routineTimer.addTime(-refresh.maxDuration)
            elif refresh.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.200000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'loop_block_practice'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "answer_block_practice" ---
        # create an object to store info about Routine answer_block_practice
        answer_block_practice = data.Routine(
            name='answer_block_practice',
            components=[text_answer_block_practice, textbox_answer_block_practice, button_text_block_practice, mouse_block_practice],
        )
        answer_block_practice.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        textbox_answer_block_practice.reset()
        # setup some python lists for storing info about the mouse_block_practice
        mouse_block_practice.x = []
        mouse_block_practice.y = []
        mouse_block_practice.leftButton = []
        mouse_block_practice.midButton = []
        mouse_block_practice.rightButton = []
        mouse_block_practice.time = []
        mouse_block_practice.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code
        win.mouseVisible = True
        # store start times for answer_block_practice
        answer_block_practice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        answer_block_practice.tStart = globalClock.getTime(format='float')
        answer_block_practice.status = STARTED
        thisExp.addData('answer_block_practice.started', answer_block_practice.tStart)
        answer_block_practice.maxDuration = None
        # keep track of which components have finished
        answer_block_practiceComponents = answer_block_practice.components
        for thisComponent in answer_block_practice.components:
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
        
        # --- Run Routine "answer_block_practice" ---
        # if trial has changed, end Routine now
        if isinstance(loop_practice, data.TrialHandler2) and thisLoop_practice.thisN != loop_practice.thisTrial.thisN:
            continueRoutine = False
        answer_block_practice.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_answer_block_practice* updates
            
            # if text_answer_block_practice is starting this frame...
            if text_answer_block_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_answer_block_practice.frameNStart = frameN  # exact frame index
                text_answer_block_practice.tStart = t  # local t and not account for scr refresh
                text_answer_block_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_answer_block_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_answer_block_practice.started')
                # update status
                text_answer_block_practice.status = STARTED
                text_answer_block_practice.setAutoDraw(True)
            
            # if text_answer_block_practice is active this frame...
            if text_answer_block_practice.status == STARTED:
                # update params
                pass
            
            # *textbox_answer_block_practice* updates
            
            # if textbox_answer_block_practice is starting this frame...
            if textbox_answer_block_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_answer_block_practice.frameNStart = frameN  # exact frame index
                textbox_answer_block_practice.tStart = t  # local t and not account for scr refresh
                textbox_answer_block_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_answer_block_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_answer_block_practice.started')
                # update status
                textbox_answer_block_practice.status = STARTED
                textbox_answer_block_practice.setAutoDraw(True)
            
            # if textbox_answer_block_practice is active this frame...
            if textbox_answer_block_practice.status == STARTED:
                # update params
                pass
            
            # *button_text_block_practice* updates
            
            # if button_text_block_practice is starting this frame...
            if button_text_block_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                button_text_block_practice.frameNStart = frameN  # exact frame index
                button_text_block_practice.tStart = t  # local t and not account for scr refresh
                button_text_block_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_text_block_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_text_block_practice.started')
                # update status
                button_text_block_practice.status = STARTED
                button_text_block_practice.setAutoDraw(True)
            
            # if button_text_block_practice is active this frame...
            if button_text_block_practice.status == STARTED:
                # update params
                pass
            # *mouse_block_practice* updates
            
            # if mouse_block_practice is starting this frame...
            if mouse_block_practice.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_block_practice.frameNStart = frameN  # exact frame index
                mouse_block_practice.tStart = t  # local t and not account for scr refresh
                mouse_block_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_block_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_block_practice.started', t)
                # update status
                mouse_block_practice.status = STARTED
                mouse_block_practice.mouseClock.reset()
                prevButtonState = mouse_block_practice.getPressed()  # if button is down already this ISN'T a new click
            if mouse_block_practice.status == STARTED:  # only update if started and not finished!
                buttons = mouse_block_practice.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(button_text_block_practice, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_block_practice):
                                gotValidClick = True
                                mouse_block_practice.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mouse_block_practice.clicked_name.append(None)
                        x, y = mouse_block_practice.getPos()
                        mouse_block_practice.x.append(x)
                        mouse_block_practice.y.append(y)
                        buttons = mouse_block_practice.getPressed()
                        mouse_block_practice.leftButton.append(buttons[0])
                        mouse_block_practice.midButton.append(buttons[1])
                        mouse_block_practice.rightButton.append(buttons[2])
                        mouse_block_practice.time.append(mouse_block_practice.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            # Run 'Each Frame' code from code
            allowed_chars = '0123456789'
            text = textbox_answer_block_practice.text
            filtered_text = ''
            for i in range(len(text)):
                if text[i] in allowed_chars:
                    filtered_text += text[i]
                if len(filtered_text) >= 3:
                    break  # stop after collecting 3 digits
            textbox_answer_block_practice.setText(filtered_text)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                answer_block_practice.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in answer_block_practice.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "answer_block_practice" ---
        for thisComponent in answer_block_practice.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for answer_block_practice
        answer_block_practice.tStop = globalClock.getTime(format='float')
        answer_block_practice.tStopRefresh = tThisFlipGlobal
        thisExp.addData('answer_block_practice.stopped', answer_block_practice.tStop)
        loop_practice.addData('textbox_answer_block_practice.text',textbox_answer_block_practice.text)
        # store data for loop_practice (TrialHandler)
        loop_practice.addData('mouse_block_practice.x', mouse_block_practice.x)
        loop_practice.addData('mouse_block_practice.y', mouse_block_practice.y)
        loop_practice.addData('mouse_block_practice.leftButton', mouse_block_practice.leftButton)
        loop_practice.addData('mouse_block_practice.midButton', mouse_block_practice.midButton)
        loop_practice.addData('mouse_block_practice.rightButton', mouse_block_practice.rightButton)
        loop_practice.addData('mouse_block_practice.time', mouse_block_practice.time)
        loop_practice.addData('mouse_block_practice.clicked_name', mouse_block_practice.clicked_name)
        # Run 'End Routine' code from code
        correct_answer_current = correct_answer
        correct_answer_current = str(correct_answer_current)
        participant_response = textbox_answer_block_practice.text.strip()
        num_correct = sum([1 for i in range(3) if participant_response[i] == correct_answer_current[i]])
        thisExp.addData('num_correct', num_correct)
        feedback_text = f"你答对了{num_correct}种表情的面孔数目。"
        win.mouseVisible = False
        # the Routine "answer_block_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "refresh" ---
        # create an object to store info about Routine refresh
        refresh = data.Routine(
            name='refresh',
            components=[text_refresh],
        )
        refresh.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for refresh
        refresh.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        refresh.tStart = globalClock.getTime(format='float')
        refresh.status = STARTED
        thisExp.addData('refresh.started', refresh.tStart)
        refresh.maxDuration = None
        # keep track of which components have finished
        refreshComponents = refresh.components
        for thisComponent in refresh.components:
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
        
        # --- Run Routine "refresh" ---
        # if trial has changed, end Routine now
        if isinstance(loop_practice, data.TrialHandler2) and thisLoop_practice.thisN != loop_practice.thisTrial.thisN:
            continueRoutine = False
        refresh.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_refresh* updates
            
            # if text_refresh is starting this frame...
            if text_refresh.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_refresh.frameNStart = frameN  # exact frame index
                text_refresh.tStart = t  # local t and not account for scr refresh
                text_refresh.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_refresh, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_refresh.started')
                # update status
                text_refresh.status = STARTED
                text_refresh.setAutoDraw(True)
            
            # if text_refresh is active this frame...
            if text_refresh.status == STARTED:
                # update params
                pass
            
            # if text_refresh is stopping this frame...
            if text_refresh.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_refresh.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_refresh.tStop = t  # not accounting for scr refresh
                    text_refresh.tStopRefresh = tThisFlipGlobal  # on global time
                    text_refresh.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_refresh.stopped')
                    # update status
                    text_refresh.status = FINISHED
                    text_refresh.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                refresh.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in refresh.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "refresh" ---
        for thisComponent in refresh.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for refresh
        refresh.tStop = globalClock.getTime(format='float')
        refresh.tStopRefresh = tThisFlipGlobal
        thisExp.addData('refresh.stopped', refresh.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if refresh.maxDurationReached:
            routineTimer.addTime(-refresh.maxDuration)
        elif refresh.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.200000)
        
        # --- Prepare to start Routine "feedback_block_practice" ---
        # create an object to store info about Routine feedback_block_practice
        feedback_block_practice = data.Routine(
            name='feedback_block_practice',
            components=[text_feedback_block_practice, text_feedback_note_practice, key_resp],
        )
        feedback_block_practice.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_feedback_block_practice.setText(feedback_text)
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # store start times for feedback_block_practice
        feedback_block_practice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_block_practice.tStart = globalClock.getTime(format='float')
        feedback_block_practice.status = STARTED
        thisExp.addData('feedback_block_practice.started', feedback_block_practice.tStart)
        feedback_block_practice.maxDuration = None
        # keep track of which components have finished
        feedback_block_practiceComponents = feedback_block_practice.components
        for thisComponent in feedback_block_practice.components:
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
        
        # --- Run Routine "feedback_block_practice" ---
        # if trial has changed, end Routine now
        if isinstance(loop_practice, data.TrialHandler2) and thisLoop_practice.thisN != loop_practice.thisTrial.thisN:
            continueRoutine = False
        feedback_block_practice.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_feedback_block_practice* updates
            
            # if text_feedback_block_practice is starting this frame...
            if text_feedback_block_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_feedback_block_practice.frameNStart = frameN  # exact frame index
                text_feedback_block_practice.tStart = t  # local t and not account for scr refresh
                text_feedback_block_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_feedback_block_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_feedback_block_practice.started')
                # update status
                text_feedback_block_practice.status = STARTED
                text_feedback_block_practice.setAutoDraw(True)
            
            # if text_feedback_block_practice is active this frame...
            if text_feedback_block_practice.status == STARTED:
                # update params
                pass
            
            # *text_feedback_note_practice* updates
            
            # if text_feedback_note_practice is starting this frame...
            if text_feedback_note_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_feedback_note_practice.frameNStart = frameN  # exact frame index
                text_feedback_note_practice.tStart = t  # local t and not account for scr refresh
                text_feedback_note_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_feedback_note_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_feedback_note_practice.started')
                # update status
                text_feedback_note_practice.status = STARTED
                text_feedback_note_practice.setAutoDraw(True)
            
            # if text_feedback_note_practice is active this frame...
            if text_feedback_note_practice.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback_block_practice.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_block_practice.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_block_practice" ---
        for thisComponent in feedback_block_practice.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_block_practice
        feedback_block_practice.tStop = globalClock.getTime(format='float')
        feedback_block_practice.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_block_practice.stopped', feedback_block_practice.tStop)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        loop_practice.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            loop_practice.addData('key_resp.rt', key_resp.rt)
            loop_practice.addData('key_resp.duration', key_resp.duration)
        # the Routine "feedback_block_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "refresh" ---
        # create an object to store info about Routine refresh
        refresh = data.Routine(
            name='refresh',
            components=[text_refresh],
        )
        refresh.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for refresh
        refresh.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        refresh.tStart = globalClock.getTime(format='float')
        refresh.status = STARTED
        thisExp.addData('refresh.started', refresh.tStart)
        refresh.maxDuration = None
        # keep track of which components have finished
        refreshComponents = refresh.components
        for thisComponent in refresh.components:
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
        
        # --- Run Routine "refresh" ---
        # if trial has changed, end Routine now
        if isinstance(loop_practice, data.TrialHandler2) and thisLoop_practice.thisN != loop_practice.thisTrial.thisN:
            continueRoutine = False
        refresh.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_refresh* updates
            
            # if text_refresh is starting this frame...
            if text_refresh.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_refresh.frameNStart = frameN  # exact frame index
                text_refresh.tStart = t  # local t and not account for scr refresh
                text_refresh.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_refresh, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_refresh.started')
                # update status
                text_refresh.status = STARTED
                text_refresh.setAutoDraw(True)
            
            # if text_refresh is active this frame...
            if text_refresh.status == STARTED:
                # update params
                pass
            
            # if text_refresh is stopping this frame...
            if text_refresh.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_refresh.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_refresh.tStop = t  # not accounting for scr refresh
                    text_refresh.tStopRefresh = tThisFlipGlobal  # on global time
                    text_refresh.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_refresh.stopped')
                    # update status
                    text_refresh.status = FINISHED
                    text_refresh.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                refresh.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in refresh.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "refresh" ---
        for thisComponent in refresh.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for refresh
        refresh.tStop = globalClock.getTime(format='float')
        refresh.tStopRefresh = tThisFlipGlobal
        thisExp.addData('refresh.stopped', refresh.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if refresh.maxDurationReached:
            routineTimer.addTime(-refresh.maxDuration)
        elif refresh.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.200000)
        
        # --- Prepare to start Routine "continue_check" ---
        # create an object to store info about Routine continue_check
        continue_check = data.Routine(
            name='continue_check',
            components=[image_continue_check, key_resp_continue_check],
        )
        continue_check.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_continue_check
        key_resp_continue_check.keys = []
        key_resp_continue_check.rt = []
        _key_resp_continue_check_allKeys = []
        # Run 'Begin Routine' code from code_continue_check
        loop_practice.finished = False
        # store start times for continue_check
        continue_check.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        continue_check.tStart = globalClock.getTime(format='float')
        continue_check.status = STARTED
        thisExp.addData('continue_check.started', continue_check.tStart)
        continue_check.maxDuration = None
        # keep track of which components have finished
        continue_checkComponents = continue_check.components
        for thisComponent in continue_check.components:
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
        
        # --- Run Routine "continue_check" ---
        # if trial has changed, end Routine now
        if isinstance(loop_practice, data.TrialHandler2) and thisLoop_practice.thisN != loop_practice.thisTrial.thisN:
            continueRoutine = False
        continue_check.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_continue_check* updates
            
            # if image_continue_check is starting this frame...
            if image_continue_check.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_continue_check.frameNStart = frameN  # exact frame index
                image_continue_check.tStart = t  # local t and not account for scr refresh
                image_continue_check.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_continue_check, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_continue_check.started')
                # update status
                image_continue_check.status = STARTED
                image_continue_check.setAutoDraw(True)
            
            # if image_continue_check is active this frame...
            if image_continue_check.status == STARTED:
                # update params
                pass
            
            # *key_resp_continue_check* updates
            waitOnFlip = False
            
            # if key_resp_continue_check is starting this frame...
            if key_resp_continue_check.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_continue_check.frameNStart = frameN  # exact frame index
                key_resp_continue_check.tStart = t  # local t and not account for scr refresh
                key_resp_continue_check.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_continue_check, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_continue_check.started')
                # update status
                key_resp_continue_check.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_continue_check.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_continue_check.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_continue_check.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_continue_check.getKeys(keyList=['space','Q','q'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_continue_check_allKeys.extend(theseKeys)
                if len(_key_resp_continue_check_allKeys):
                    key_resp_continue_check.keys = _key_resp_continue_check_allKeys[-1].name  # just the last key pressed
                    key_resp_continue_check.rt = _key_resp_continue_check_allKeys[-1].rt
                    key_resp_continue_check.duration = _key_resp_continue_check_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                continue_check.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in continue_check.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "continue_check" ---
        for thisComponent in continue_check.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for continue_check
        continue_check.tStop = globalClock.getTime(format='float')
        continue_check.tStopRefresh = tThisFlipGlobal
        thisExp.addData('continue_check.stopped', continue_check.tStop)
        # check responses
        if key_resp_continue_check.keys in ['', [], None]:  # No response was made
            key_resp_continue_check.keys = None
        loop_practice.addData('key_resp_continue_check.keys',key_resp_continue_check.keys)
        if key_resp_continue_check.keys != None:  # we had a response
            loop_practice.addData('key_resp_continue_check.rt', key_resp_continue_check.rt)
            loop_practice.addData('key_resp_continue_check.duration', key_resp_continue_check.duration)
        # Run 'End Routine' code from code_continue_check
        if 'Q' in key_resp_continue_check.keys:
            loop_practice.finished = False
        elif 'space' in key_resp_continue_check.keys:
            loop_practice.finished = True
        # the Routine "continue_check" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "refresh" ---
        # create an object to store info about Routine refresh
        refresh = data.Routine(
            name='refresh',
            components=[text_refresh],
        )
        refresh.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for refresh
        refresh.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        refresh.tStart = globalClock.getTime(format='float')
        refresh.status = STARTED
        thisExp.addData('refresh.started', refresh.tStart)
        refresh.maxDuration = None
        # keep track of which components have finished
        refreshComponents = refresh.components
        for thisComponent in refresh.components:
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
        
        # --- Run Routine "refresh" ---
        # if trial has changed, end Routine now
        if isinstance(loop_practice, data.TrialHandler2) and thisLoop_practice.thisN != loop_practice.thisTrial.thisN:
            continueRoutine = False
        refresh.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_refresh* updates
            
            # if text_refresh is starting this frame...
            if text_refresh.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_refresh.frameNStart = frameN  # exact frame index
                text_refresh.tStart = t  # local t and not account for scr refresh
                text_refresh.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_refresh, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_refresh.started')
                # update status
                text_refresh.status = STARTED
                text_refresh.setAutoDraw(True)
            
            # if text_refresh is active this frame...
            if text_refresh.status == STARTED:
                # update params
                pass
            
            # if text_refresh is stopping this frame...
            if text_refresh.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_refresh.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_refresh.tStop = t  # not accounting for scr refresh
                    text_refresh.tStopRefresh = tThisFlipGlobal  # on global time
                    text_refresh.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_refresh.stopped')
                    # update status
                    text_refresh.status = FINISHED
                    text_refresh.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                refresh.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in refresh.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "refresh" ---
        for thisComponent in refresh.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for refresh
        refresh.tStop = globalClock.getTime(format='float')
        refresh.tStopRefresh = tThisFlipGlobal
        thisExp.addData('refresh.stopped', refresh.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if refresh.maxDurationReached:
            routineTimer.addTime(-refresh.maxDuration)
        elif refresh.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.200000)
        thisExp.nextEntry()
        
    # completed 99.0 repeats of 'loop_practice'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "primary_task_welcome" ---
    # create an object to store info about Routine primary_task_welcome
    primary_task_welcome = data.Routine(
        name='primary_task_welcome',
        components=[image_primary_welcome, key_resp_primary_welcome],
    )
    primary_task_welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_primary_welcome
    key_resp_primary_welcome.keys = []
    key_resp_primary_welcome.rt = []
    _key_resp_primary_welcome_allKeys = []
    # store start times for primary_task_welcome
    primary_task_welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    primary_task_welcome.tStart = globalClock.getTime(format='float')
    primary_task_welcome.status = STARTED
    thisExp.addData('primary_task_welcome.started', primary_task_welcome.tStart)
    primary_task_welcome.maxDuration = None
    # keep track of which components have finished
    primary_task_welcomeComponents = primary_task_welcome.components
    for thisComponent in primary_task_welcome.components:
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
    
    # --- Run Routine "primary_task_welcome" ---
    primary_task_welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_primary_welcome* updates
        
        # if image_primary_welcome is starting this frame...
        if image_primary_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_primary_welcome.frameNStart = frameN  # exact frame index
            image_primary_welcome.tStart = t  # local t and not account for scr refresh
            image_primary_welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_primary_welcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_primary_welcome.started')
            # update status
            image_primary_welcome.status = STARTED
            image_primary_welcome.setAutoDraw(True)
        
        # if image_primary_welcome is active this frame...
        if image_primary_welcome.status == STARTED:
            # update params
            pass
        
        # *key_resp_primary_welcome* updates
        waitOnFlip = False
        
        # if key_resp_primary_welcome is starting this frame...
        if key_resp_primary_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_primary_welcome.frameNStart = frameN  # exact frame index
            key_resp_primary_welcome.tStart = t  # local t and not account for scr refresh
            key_resp_primary_welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_primary_welcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_primary_welcome.started')
            # update status
            key_resp_primary_welcome.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_primary_welcome.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_primary_welcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_primary_welcome.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_primary_welcome.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_primary_welcome_allKeys.extend(theseKeys)
            if len(_key_resp_primary_welcome_allKeys):
                key_resp_primary_welcome.keys = _key_resp_primary_welcome_allKeys[-1].name  # just the last key pressed
                key_resp_primary_welcome.rt = _key_resp_primary_welcome_allKeys[-1].rt
                key_resp_primary_welcome.duration = _key_resp_primary_welcome_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            primary_task_welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in primary_task_welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "primary_task_welcome" ---
    for thisComponent in primary_task_welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for primary_task_welcome
    primary_task_welcome.tStop = globalClock.getTime(format='float')
    primary_task_welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('primary_task_welcome.stopped', primary_task_welcome.tStop)
    # check responses
    if key_resp_primary_welcome.keys in ['', [], None]:  # No response was made
        key_resp_primary_welcome.keys = None
    thisExp.addData('key_resp_primary_welcome.keys',key_resp_primary_welcome.keys)
    if key_resp_primary_welcome.keys != None:  # we had a response
        thisExp.addData('key_resp_primary_welcome.rt', key_resp_primary_welcome.rt)
        thisExp.addData('key_resp_primary_welcome.duration', key_resp_primary_welcome.duration)
    thisExp.nextEntry()
    # the Routine "primary_task_welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "refresh" ---
    # create an object to store info about Routine refresh
    refresh = data.Routine(
        name='refresh',
        components=[text_refresh],
    )
    refresh.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for refresh
    refresh.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    refresh.tStart = globalClock.getTime(format='float')
    refresh.status = STARTED
    thisExp.addData('refresh.started', refresh.tStart)
    refresh.maxDuration = None
    # keep track of which components have finished
    refreshComponents = refresh.components
    for thisComponent in refresh.components:
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
    
    # --- Run Routine "refresh" ---
    refresh.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.2:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_refresh* updates
        
        # if text_refresh is starting this frame...
        if text_refresh.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_refresh.frameNStart = frameN  # exact frame index
            text_refresh.tStart = t  # local t and not account for scr refresh
            text_refresh.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_refresh, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_refresh.started')
            # update status
            text_refresh.status = STARTED
            text_refresh.setAutoDraw(True)
        
        # if text_refresh is active this frame...
        if text_refresh.status == STARTED:
            # update params
            pass
        
        # if text_refresh is stopping this frame...
        if text_refresh.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_refresh.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                text_refresh.tStop = t  # not accounting for scr refresh
                text_refresh.tStopRefresh = tThisFlipGlobal  # on global time
                text_refresh.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_refresh.stopped')
                # update status
                text_refresh.status = FINISHED
                text_refresh.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            refresh.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in refresh.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "refresh" ---
    for thisComponent in refresh.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for refresh
    refresh.tStop = globalClock.getTime(format='float')
    refresh.tStopRefresh = tThisFlipGlobal
    thisExp.addData('refresh.stopped', refresh.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if refresh.maxDurationReached:
        routineTimer.addTime(-refresh.maxDuration)
    elif refresh.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.200000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    loop_primary = data.TrialHandler2(
        name='loop_primary',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('loop_block.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(loop_primary)  # add the loop to the experiment
    thisLoop_primary = loop_primary.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_primary.rgb)
    if thisLoop_primary != None:
        for paramName in thisLoop_primary:
            globals()[paramName] = thisLoop_primary[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoop_primary in loop_primary:
        currentLoop = loop_primary
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_primary.rgb)
        if thisLoop_primary != None:
            for paramName in thisLoop_primary:
                globals()[paramName] = thisLoop_primary[paramName]
        
        # --- Prepare to start Routine "fixation" ---
        # create an object to store info about Routine fixation
        fixation = data.Routine(
            name='fixation',
            components=[text_fixation],
        )
        fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fixation
        fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fixation.tStart = globalClock.getTime(format='float')
        fixation.status = STARTED
        thisExp.addData('fixation.started', fixation.tStart)
        fixation.maxDuration = None
        # keep track of which components have finished
        fixationComponents = fixation.components
        for thisComponent in fixation.components:
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
        
        # --- Run Routine "fixation" ---
        # if trial has changed, end Routine now
        if isinstance(loop_primary, data.TrialHandler2) and thisLoop_primary.thisN != loop_primary.thisTrial.thisN:
            continueRoutine = False
        fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_fixation* updates
            
            # if text_fixation is starting this frame...
            if text_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_fixation.frameNStart = frameN  # exact frame index
                text_fixation.tStart = t  # local t and not account for scr refresh
                text_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_fixation.started')
                # update status
                text_fixation.status = STARTED
                text_fixation.setAutoDraw(True)
            
            # if text_fixation is active this frame...
            if text_fixation.status == STARTED:
                # update params
                pass
            
            # if text_fixation is stopping this frame...
            if text_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_fixation.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_fixation.tStop = t  # not accounting for scr refresh
                    text_fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    text_fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_fixation.stopped')
                    # update status
                    text_fixation.status = FINISHED
                    text_fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                fixation.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fixation
        fixation.tStop = globalClock.getTime(format='float')
        fixation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fixation.stopped', fixation.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fixation.maxDurationReached:
            routineTimer.addTime(-fixation.maxDuration)
        elif fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # set up handler to look after randomisation of conditions etc
        loop_block = data.TrialHandler2(
            name='loop_block',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(block_file), 
            seed=None, 
        )
        thisExp.addLoop(loop_block)  # add the loop to the experiment
        thisLoop_block = loop_block.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_block.rgb)
        if thisLoop_block != None:
            for paramName in thisLoop_block:
                globals()[paramName] = thisLoop_block[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisLoop_block in loop_block:
            currentLoop = loop_block
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_block.rgb)
            if thisLoop_block != None:
                for paramName in thisLoop_block:
                    globals()[paramName] = thisLoop_block[paramName]
            
            # --- Prepare to start Routine "block" ---
            # create an object to store info about Routine block
            block = data.Routine(
                name='block',
                components=[image_block, key_resp_block],
            )
            block.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_block.setImage(stimulus)
            # create starting attributes for key_resp_block
            key_resp_block.keys = []
            key_resp_block.rt = []
            _key_resp_block_allKeys = []
            # store start times for block
            block.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            block.tStart = globalClock.getTime(format='float')
            block.status = STARTED
            thisExp.addData('block.started', block.tStart)
            block.maxDuration = None
            # keep track of which components have finished
            blockComponents = block.components
            for thisComponent in block.components:
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
            
            # --- Run Routine "block" ---
            # if trial has changed, end Routine now
            if isinstance(loop_block, data.TrialHandler2) and thisLoop_block.thisN != loop_block.thisTrial.thisN:
                continueRoutine = False
            block.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_block* updates
                
                # if image_block is starting this frame...
                if image_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_block.frameNStart = frameN  # exact frame index
                    image_block.tStart = t  # local t and not account for scr refresh
                    image_block.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_block, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_block.started')
                    # update status
                    image_block.status = STARTED
                    image_block.setAutoDraw(True)
                
                # if image_block is active this frame...
                if image_block.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_block* updates
                waitOnFlip = False
                
                # if key_resp_block is starting this frame...
                if key_resp_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_block.frameNStart = frameN  # exact frame index
                    key_resp_block.tStart = t  # local t and not account for scr refresh
                    key_resp_block.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_block, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_block.started')
                    # update status
                    key_resp_block.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_block.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_block.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_block.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_block.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_block_allKeys.extend(theseKeys)
                    if len(_key_resp_block_allKeys):
                        key_resp_block.keys = _key_resp_block_allKeys[-1].name  # just the last key pressed
                        key_resp_block.rt = _key_resp_block_allKeys[-1].rt
                        key_resp_block.duration = _key_resp_block_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    block.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in block.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "block" ---
            for thisComponent in block.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for block
            block.tStop = globalClock.getTime(format='float')
            block.tStopRefresh = tThisFlipGlobal
            thisExp.addData('block.stopped', block.tStop)
            # check responses
            if key_resp_block.keys in ['', [], None]:  # No response was made
                key_resp_block.keys = None
            loop_block.addData('key_resp_block.keys',key_resp_block.keys)
            if key_resp_block.keys != None:  # we had a response
                loop_block.addData('key_resp_block.rt', key_resp_block.rt)
                loop_block.addData('key_resp_block.duration', key_resp_block.duration)
            # the Routine "block" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "refresh" ---
            # create an object to store info about Routine refresh
            refresh = data.Routine(
                name='refresh',
                components=[text_refresh],
            )
            refresh.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for refresh
            refresh.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            refresh.tStart = globalClock.getTime(format='float')
            refresh.status = STARTED
            thisExp.addData('refresh.started', refresh.tStart)
            refresh.maxDuration = None
            # keep track of which components have finished
            refreshComponents = refresh.components
            for thisComponent in refresh.components:
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
            
            # --- Run Routine "refresh" ---
            # if trial has changed, end Routine now
            if isinstance(loop_block, data.TrialHandler2) and thisLoop_block.thisN != loop_block.thisTrial.thisN:
                continueRoutine = False
            refresh.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.2:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_refresh* updates
                
                # if text_refresh is starting this frame...
                if text_refresh.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_refresh.frameNStart = frameN  # exact frame index
                    text_refresh.tStart = t  # local t and not account for scr refresh
                    text_refresh.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_refresh, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_refresh.started')
                    # update status
                    text_refresh.status = STARTED
                    text_refresh.setAutoDraw(True)
                
                # if text_refresh is active this frame...
                if text_refresh.status == STARTED:
                    # update params
                    pass
                
                # if text_refresh is stopping this frame...
                if text_refresh.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_refresh.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        text_refresh.tStop = t  # not accounting for scr refresh
                        text_refresh.tStopRefresh = tThisFlipGlobal  # on global time
                        text_refresh.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_refresh.stopped')
                        # update status
                        text_refresh.status = FINISHED
                        text_refresh.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    refresh.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in refresh.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "refresh" ---
            for thisComponent in refresh.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for refresh
            refresh.tStop = globalClock.getTime(format='float')
            refresh.tStopRefresh = tThisFlipGlobal
            thisExp.addData('refresh.stopped', refresh.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if refresh.maxDurationReached:
                routineTimer.addTime(-refresh.maxDuration)
            elif refresh.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.200000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'loop_block'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "answer_block" ---
        # create an object to store info about Routine answer_block
        answer_block = data.Routine(
            name='answer_block',
            components=[text_answer_block, textbox_answer_block, button_answer_block, mouse_answer_block],
        )
        answer_block.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        textbox_answer_block.reset()
        # setup some python lists for storing info about the mouse_answer_block
        mouse_answer_block.x = []
        mouse_answer_block.y = []
        mouse_answer_block.leftButton = []
        mouse_answer_block.midButton = []
        mouse_answer_block.rightButton = []
        mouse_answer_block.time = []
        mouse_answer_block.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code_answer_block
        win.mouseVisible = True
        # store start times for answer_block
        answer_block.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        answer_block.tStart = globalClock.getTime(format='float')
        answer_block.status = STARTED
        thisExp.addData('answer_block.started', answer_block.tStart)
        answer_block.maxDuration = None
        # keep track of which components have finished
        answer_blockComponents = answer_block.components
        for thisComponent in answer_block.components:
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
        
        # --- Run Routine "answer_block" ---
        # if trial has changed, end Routine now
        if isinstance(loop_primary, data.TrialHandler2) and thisLoop_primary.thisN != loop_primary.thisTrial.thisN:
            continueRoutine = False
        answer_block.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_answer_block* updates
            
            # if text_answer_block is starting this frame...
            if text_answer_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_answer_block.frameNStart = frameN  # exact frame index
                text_answer_block.tStart = t  # local t and not account for scr refresh
                text_answer_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_answer_block, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_answer_block.started')
                # update status
                text_answer_block.status = STARTED
                text_answer_block.setAutoDraw(True)
            
            # if text_answer_block is active this frame...
            if text_answer_block.status == STARTED:
                # update params
                pass
            
            # *textbox_answer_block* updates
            
            # if textbox_answer_block is starting this frame...
            if textbox_answer_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_answer_block.frameNStart = frameN  # exact frame index
                textbox_answer_block.tStart = t  # local t and not account for scr refresh
                textbox_answer_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_answer_block, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_answer_block.started')
                # update status
                textbox_answer_block.status = STARTED
                textbox_answer_block.setAutoDraw(True)
            
            # if textbox_answer_block is active this frame...
            if textbox_answer_block.status == STARTED:
                # update params
                pass
            
            # *button_answer_block* updates
            
            # if button_answer_block is starting this frame...
            if button_answer_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                button_answer_block.frameNStart = frameN  # exact frame index
                button_answer_block.tStart = t  # local t and not account for scr refresh
                button_answer_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_answer_block, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_answer_block.started')
                # update status
                button_answer_block.status = STARTED
                button_answer_block.setAutoDraw(True)
            
            # if button_answer_block is active this frame...
            if button_answer_block.status == STARTED:
                # update params
                pass
            # *mouse_answer_block* updates
            
            # if mouse_answer_block is starting this frame...
            if mouse_answer_block.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_answer_block.frameNStart = frameN  # exact frame index
                mouse_answer_block.tStart = t  # local t and not account for scr refresh
                mouse_answer_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_answer_block, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_answer_block.started', t)
                # update status
                mouse_answer_block.status = STARTED
                mouse_answer_block.mouseClock.reset()
                prevButtonState = mouse_answer_block.getPressed()  # if button is down already this ISN'T a new click
            if mouse_answer_block.status == STARTED:  # only update if started and not finished!
                buttons = mouse_answer_block.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(button_answer_block, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_answer_block):
                                gotValidClick = True
                                mouse_answer_block.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mouse_answer_block.clicked_name.append(None)
                        x, y = mouse_answer_block.getPos()
                        mouse_answer_block.x.append(x)
                        mouse_answer_block.y.append(y)
                        buttons = mouse_answer_block.getPressed()
                        mouse_answer_block.leftButton.append(buttons[0])
                        mouse_answer_block.midButton.append(buttons[1])
                        mouse_answer_block.rightButton.append(buttons[2])
                        mouse_answer_block.time.append(mouse_answer_block.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            # Run 'Each Frame' code from code_answer_block
            allowed_chars = '0123456789'
            text = textbox_answer_block.text
            filtered_text = ''
            for i in range(len(text)):
                if text[i] in allowed_chars:
                    filtered_text += text[i]
                if len(filtered_text) >= 3:
                    break  # stop after collecting 3 digits
            textbox_answer_block.setText(filtered_text)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                answer_block.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in answer_block.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "answer_block" ---
        for thisComponent in answer_block.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for answer_block
        answer_block.tStop = globalClock.getTime(format='float')
        answer_block.tStopRefresh = tThisFlipGlobal
        thisExp.addData('answer_block.stopped', answer_block.tStop)
        loop_primary.addData('textbox_answer_block.text',textbox_answer_block.text)
        # store data for loop_primary (TrialHandler)
        loop_primary.addData('mouse_answer_block.x', mouse_answer_block.x)
        loop_primary.addData('mouse_answer_block.y', mouse_answer_block.y)
        loop_primary.addData('mouse_answer_block.leftButton', mouse_answer_block.leftButton)
        loop_primary.addData('mouse_answer_block.midButton', mouse_answer_block.midButton)
        loop_primary.addData('mouse_answer_block.rightButton', mouse_answer_block.rightButton)
        loop_primary.addData('mouse_answer_block.time', mouse_answer_block.time)
        loop_primary.addData('mouse_answer_block.clicked_name', mouse_answer_block.clicked_name)
        # Run 'End Routine' code from code_answer_block
        correct_answer_primary_current = correct_answer
        correct_answer_primary_current = str(correct_answer_primary_current)
        participant_response = textbox_answer_block.text.strip()
        num_correct = sum([1 for i in range(3) if participant_response[i] == correct_answer_primary_current[i]])
        thisExp.addData('num_correct', num_correct)
        feedback_text_primary = f"你答对了{num_correct}种表情的面孔数目。"
        win.mouseVisible = False
        # the Routine "answer_block" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "refresh" ---
        # create an object to store info about Routine refresh
        refresh = data.Routine(
            name='refresh',
            components=[text_refresh],
        )
        refresh.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for refresh
        refresh.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        refresh.tStart = globalClock.getTime(format='float')
        refresh.status = STARTED
        thisExp.addData('refresh.started', refresh.tStart)
        refresh.maxDuration = None
        # keep track of which components have finished
        refreshComponents = refresh.components
        for thisComponent in refresh.components:
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
        
        # --- Run Routine "refresh" ---
        # if trial has changed, end Routine now
        if isinstance(loop_primary, data.TrialHandler2) and thisLoop_primary.thisN != loop_primary.thisTrial.thisN:
            continueRoutine = False
        refresh.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_refresh* updates
            
            # if text_refresh is starting this frame...
            if text_refresh.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_refresh.frameNStart = frameN  # exact frame index
                text_refresh.tStart = t  # local t and not account for scr refresh
                text_refresh.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_refresh, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_refresh.started')
                # update status
                text_refresh.status = STARTED
                text_refresh.setAutoDraw(True)
            
            # if text_refresh is active this frame...
            if text_refresh.status == STARTED:
                # update params
                pass
            
            # if text_refresh is stopping this frame...
            if text_refresh.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_refresh.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_refresh.tStop = t  # not accounting for scr refresh
                    text_refresh.tStopRefresh = tThisFlipGlobal  # on global time
                    text_refresh.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_refresh.stopped')
                    # update status
                    text_refresh.status = FINISHED
                    text_refresh.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                refresh.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in refresh.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "refresh" ---
        for thisComponent in refresh.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for refresh
        refresh.tStop = globalClock.getTime(format='float')
        refresh.tStopRefresh = tThisFlipGlobal
        thisExp.addData('refresh.stopped', refresh.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if refresh.maxDurationReached:
            routineTimer.addTime(-refresh.maxDuration)
        elif refresh.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.200000)
        
        # --- Prepare to start Routine "feedback_block" ---
        # create an object to store info about Routine feedback_block
        feedback_block = data.Routine(
            name='feedback_block',
            components=[text_feedback_block, text_feedback_block_note, key_resp_feedback_block],
        )
        feedback_block.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_feedback_block.setText(feedback_text_primary)
        # create starting attributes for key_resp_feedback_block
        key_resp_feedback_block.keys = []
        key_resp_feedback_block.rt = []
        _key_resp_feedback_block_allKeys = []
        # store start times for feedback_block
        feedback_block.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_block.tStart = globalClock.getTime(format='float')
        feedback_block.status = STARTED
        thisExp.addData('feedback_block.started', feedback_block.tStart)
        feedback_block.maxDuration = None
        # keep track of which components have finished
        feedback_blockComponents = feedback_block.components
        for thisComponent in feedback_block.components:
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
        
        # --- Run Routine "feedback_block" ---
        # if trial has changed, end Routine now
        if isinstance(loop_primary, data.TrialHandler2) and thisLoop_primary.thisN != loop_primary.thisTrial.thisN:
            continueRoutine = False
        feedback_block.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_feedback_block* updates
            
            # if text_feedback_block is starting this frame...
            if text_feedback_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_feedback_block.frameNStart = frameN  # exact frame index
                text_feedback_block.tStart = t  # local t and not account for scr refresh
                text_feedback_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_feedback_block, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_feedback_block.started')
                # update status
                text_feedback_block.status = STARTED
                text_feedback_block.setAutoDraw(True)
            
            # if text_feedback_block is active this frame...
            if text_feedback_block.status == STARTED:
                # update params
                pass
            
            # *text_feedback_block_note* updates
            
            # if text_feedback_block_note is starting this frame...
            if text_feedback_block_note.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_feedback_block_note.frameNStart = frameN  # exact frame index
                text_feedback_block_note.tStart = t  # local t and not account for scr refresh
                text_feedback_block_note.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_feedback_block_note, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_feedback_block_note.started')
                # update status
                text_feedback_block_note.status = STARTED
                text_feedback_block_note.setAutoDraw(True)
            
            # if text_feedback_block_note is active this frame...
            if text_feedback_block_note.status == STARTED:
                # update params
                pass
            
            # *key_resp_feedback_block* updates
            waitOnFlip = False
            
            # if key_resp_feedback_block is starting this frame...
            if key_resp_feedback_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_feedback_block.frameNStart = frameN  # exact frame index
                key_resp_feedback_block.tStart = t  # local t and not account for scr refresh
                key_resp_feedback_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_feedback_block, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_feedback_block.started')
                # update status
                key_resp_feedback_block.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_feedback_block.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_feedback_block.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_feedback_block.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_feedback_block.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_feedback_block_allKeys.extend(theseKeys)
                if len(_key_resp_feedback_block_allKeys):
                    key_resp_feedback_block.keys = _key_resp_feedback_block_allKeys[-1].name  # just the last key pressed
                    key_resp_feedback_block.rt = _key_resp_feedback_block_allKeys[-1].rt
                    key_resp_feedback_block.duration = _key_resp_feedback_block_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback_block.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_block.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_block" ---
        for thisComponent in feedback_block.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_block
        feedback_block.tStop = globalClock.getTime(format='float')
        feedback_block.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_block.stopped', feedback_block.tStop)
        # check responses
        if key_resp_feedback_block.keys in ['', [], None]:  # No response was made
            key_resp_feedback_block.keys = None
        loop_primary.addData('key_resp_feedback_block.keys',key_resp_feedback_block.keys)
        if key_resp_feedback_block.keys != None:  # we had a response
            loop_primary.addData('key_resp_feedback_block.rt', key_resp_feedback_block.rt)
            loop_primary.addData('key_resp_feedback_block.duration', key_resp_feedback_block.duration)
        # the Routine "feedback_block" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "refresh" ---
        # create an object to store info about Routine refresh
        refresh = data.Routine(
            name='refresh',
            components=[text_refresh],
        )
        refresh.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for refresh
        refresh.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        refresh.tStart = globalClock.getTime(format='float')
        refresh.status = STARTED
        thisExp.addData('refresh.started', refresh.tStart)
        refresh.maxDuration = None
        # keep track of which components have finished
        refreshComponents = refresh.components
        for thisComponent in refresh.components:
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
        
        # --- Run Routine "refresh" ---
        # if trial has changed, end Routine now
        if isinstance(loop_primary, data.TrialHandler2) and thisLoop_primary.thisN != loop_primary.thisTrial.thisN:
            continueRoutine = False
        refresh.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_refresh* updates
            
            # if text_refresh is starting this frame...
            if text_refresh.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_refresh.frameNStart = frameN  # exact frame index
                text_refresh.tStart = t  # local t and not account for scr refresh
                text_refresh.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_refresh, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_refresh.started')
                # update status
                text_refresh.status = STARTED
                text_refresh.setAutoDraw(True)
            
            # if text_refresh is active this frame...
            if text_refresh.status == STARTED:
                # update params
                pass
            
            # if text_refresh is stopping this frame...
            if text_refresh.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_refresh.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_refresh.tStop = t  # not accounting for scr refresh
                    text_refresh.tStopRefresh = tThisFlipGlobal  # on global time
                    text_refresh.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_refresh.stopped')
                    # update status
                    text_refresh.status = FINISHED
                    text_refresh.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                refresh.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in refresh.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "refresh" ---
        for thisComponent in refresh.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for refresh
        refresh.tStop = globalClock.getTime(format='float')
        refresh.tStopRefresh = tThisFlipGlobal
        thisExp.addData('refresh.stopped', refresh.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if refresh.maxDurationReached:
            routineTimer.addTime(-refresh.maxDuration)
        elif refresh.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.200000)
        
        # --- Prepare to start Routine "continue_check_block" ---
        # create an object to store info about Routine continue_check_block
        continue_check_block = data.Routine(
            name='continue_check_block',
            components=[text_continue_check_block, text_continue_prompt, key_resp_contiue_check_block],
        )
        continue_check_block.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_continue_check_block.setText('')
        # Run 'Begin Routine' code from code_progress_report
        block_counter += 1
        
        if block_counter == 6:
            text_continue_check_block.text = "您已经完成了四分之一。"
        elif block_counter == 13:
            text_continue_check_block.text = "您已经完成了一半。"
        elif block_counter == 19:
            text_continue_check_block.text = "您已经完成了四分之三。"
        else:
            text_continue_check_block.text = "如果您觉得累了，可以休息一会儿。"
        # create starting attributes for key_resp_contiue_check_block
        key_resp_contiue_check_block.keys = []
        key_resp_contiue_check_block.rt = []
        _key_resp_contiue_check_block_allKeys = []
        # store start times for continue_check_block
        continue_check_block.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        continue_check_block.tStart = globalClock.getTime(format='float')
        continue_check_block.status = STARTED
        thisExp.addData('continue_check_block.started', continue_check_block.tStart)
        continue_check_block.maxDuration = None
        # keep track of which components have finished
        continue_check_blockComponents = continue_check_block.components
        for thisComponent in continue_check_block.components:
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
        
        # --- Run Routine "continue_check_block" ---
        # if trial has changed, end Routine now
        if isinstance(loop_primary, data.TrialHandler2) and thisLoop_primary.thisN != loop_primary.thisTrial.thisN:
            continueRoutine = False
        continue_check_block.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_continue_check_block* updates
            
            # if text_continue_check_block is starting this frame...
            if text_continue_check_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_continue_check_block.frameNStart = frameN  # exact frame index
                text_continue_check_block.tStart = t  # local t and not account for scr refresh
                text_continue_check_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_continue_check_block, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_continue_check_block.started')
                # update status
                text_continue_check_block.status = STARTED
                text_continue_check_block.setAutoDraw(True)
            
            # if text_continue_check_block is active this frame...
            if text_continue_check_block.status == STARTED:
                # update params
                pass
            
            # *text_continue_prompt* updates
            
            # if text_continue_prompt is starting this frame...
            if text_continue_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_continue_prompt.frameNStart = frameN  # exact frame index
                text_continue_prompt.tStart = t  # local t and not account for scr refresh
                text_continue_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_continue_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_continue_prompt.started')
                # update status
                text_continue_prompt.status = STARTED
                text_continue_prompt.setAutoDraw(True)
            
            # if text_continue_prompt is active this frame...
            if text_continue_prompt.status == STARTED:
                # update params
                pass
            
            # *key_resp_contiue_check_block* updates
            waitOnFlip = False
            
            # if key_resp_contiue_check_block is starting this frame...
            if key_resp_contiue_check_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_contiue_check_block.frameNStart = frameN  # exact frame index
                key_resp_contiue_check_block.tStart = t  # local t and not account for scr refresh
                key_resp_contiue_check_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_contiue_check_block, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_contiue_check_block.started')
                # update status
                key_resp_contiue_check_block.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_contiue_check_block.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_contiue_check_block.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_contiue_check_block.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_contiue_check_block.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_contiue_check_block_allKeys.extend(theseKeys)
                if len(_key_resp_contiue_check_block_allKeys):
                    key_resp_contiue_check_block.keys = _key_resp_contiue_check_block_allKeys[-1].name  # just the last key pressed
                    key_resp_contiue_check_block.rt = _key_resp_contiue_check_block_allKeys[-1].rt
                    key_resp_contiue_check_block.duration = _key_resp_contiue_check_block_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                continue_check_block.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in continue_check_block.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "continue_check_block" ---
        for thisComponent in continue_check_block.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for continue_check_block
        continue_check_block.tStop = globalClock.getTime(format='float')
        continue_check_block.tStopRefresh = tThisFlipGlobal
        thisExp.addData('continue_check_block.stopped', continue_check_block.tStop)
        # check responses
        if key_resp_contiue_check_block.keys in ['', [], None]:  # No response was made
            key_resp_contiue_check_block.keys = None
        loop_primary.addData('key_resp_contiue_check_block.keys',key_resp_contiue_check_block.keys)
        if key_resp_contiue_check_block.keys != None:  # we had a response
            loop_primary.addData('key_resp_contiue_check_block.rt', key_resp_contiue_check_block.rt)
            loop_primary.addData('key_resp_contiue_check_block.duration', key_resp_contiue_check_block.duration)
        # the Routine "continue_check_block" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "refresh" ---
        # create an object to store info about Routine refresh
        refresh = data.Routine(
            name='refresh',
            components=[text_refresh],
        )
        refresh.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for refresh
        refresh.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        refresh.tStart = globalClock.getTime(format='float')
        refresh.status = STARTED
        thisExp.addData('refresh.started', refresh.tStart)
        refresh.maxDuration = None
        # keep track of which components have finished
        refreshComponents = refresh.components
        for thisComponent in refresh.components:
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
        
        # --- Run Routine "refresh" ---
        # if trial has changed, end Routine now
        if isinstance(loop_primary, data.TrialHandler2) and thisLoop_primary.thisN != loop_primary.thisTrial.thisN:
            continueRoutine = False
        refresh.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_refresh* updates
            
            # if text_refresh is starting this frame...
            if text_refresh.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_refresh.frameNStart = frameN  # exact frame index
                text_refresh.tStart = t  # local t and not account for scr refresh
                text_refresh.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_refresh, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_refresh.started')
                # update status
                text_refresh.status = STARTED
                text_refresh.setAutoDraw(True)
            
            # if text_refresh is active this frame...
            if text_refresh.status == STARTED:
                # update params
                pass
            
            # if text_refresh is stopping this frame...
            if text_refresh.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_refresh.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_refresh.tStop = t  # not accounting for scr refresh
                    text_refresh.tStopRefresh = tThisFlipGlobal  # on global time
                    text_refresh.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_refresh.stopped')
                    # update status
                    text_refresh.status = FINISHED
                    text_refresh.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                refresh.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in refresh.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "refresh" ---
        for thisComponent in refresh.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for refresh
        refresh.tStop = globalClock.getTime(format='float')
        refresh.tStopRefresh = tThisFlipGlobal
        thisExp.addData('refresh.stopped', refresh.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if refresh.maxDurationReached:
            routineTimer.addTime(-refresh.maxDuration)
        elif refresh.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.200000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'loop_primary'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "goodbye" ---
    # create an object to store info about Routine goodbye
    goodbye = data.Routine(
        name='goodbye',
        components=[text_goodbye, key_resp_goodbye],
    )
    goodbye.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_goodbye
    key_resp_goodbye.keys = []
    key_resp_goodbye.rt = []
    _key_resp_goodbye_allKeys = []
    # store start times for goodbye
    goodbye.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    goodbye.tStart = globalClock.getTime(format='float')
    goodbye.status = STARTED
    thisExp.addData('goodbye.started', goodbye.tStart)
    goodbye.maxDuration = None
    # keep track of which components have finished
    goodbyeComponents = goodbye.components
    for thisComponent in goodbye.components:
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
    
    # --- Run Routine "goodbye" ---
    goodbye.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_goodbye* updates
        
        # if text_goodbye is starting this frame...
        if text_goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_goodbye.frameNStart = frameN  # exact frame index
            text_goodbye.tStart = t  # local t and not account for scr refresh
            text_goodbye.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_goodbye, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_goodbye.started')
            # update status
            text_goodbye.status = STARTED
            text_goodbye.setAutoDraw(True)
        
        # if text_goodbye is active this frame...
        if text_goodbye.status == STARTED:
            # update params
            pass
        
        # if text_goodbye is stopping this frame...
        if text_goodbye.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_goodbye.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                text_goodbye.tStop = t  # not accounting for scr refresh
                text_goodbye.tStopRefresh = tThisFlipGlobal  # on global time
                text_goodbye.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_goodbye.stopped')
                # update status
                text_goodbye.status = FINISHED
                text_goodbye.setAutoDraw(False)
        
        # *key_resp_goodbye* updates
        waitOnFlip = False
        
        # if key_resp_goodbye is starting this frame...
        if key_resp_goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_goodbye.frameNStart = frameN  # exact frame index
            key_resp_goodbye.tStart = t  # local t and not account for scr refresh
            key_resp_goodbye.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_goodbye, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_goodbye.started')
            # update status
            key_resp_goodbye.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_goodbye.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_goodbye.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_goodbye.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_goodbye.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_goodbye_allKeys.extend(theseKeys)
            if len(_key_resp_goodbye_allKeys):
                key_resp_goodbye.keys = _key_resp_goodbye_allKeys[-1].name  # just the last key pressed
                key_resp_goodbye.rt = _key_resp_goodbye_allKeys[-1].rt
                key_resp_goodbye.duration = _key_resp_goodbye_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            goodbye.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in goodbye.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "goodbye" ---
    for thisComponent in goodbye.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for goodbye
    goodbye.tStop = globalClock.getTime(format='float')
    goodbye.tStopRefresh = tThisFlipGlobal
    thisExp.addData('goodbye.stopped', goodbye.tStop)
    # check responses
    if key_resp_goodbye.keys in ['', [], None]:  # No response was made
        key_resp_goodbye.keys = None
    thisExp.addData('key_resp_goodbye.keys',key_resp_goodbye.keys)
    if key_resp_goodbye.keys != None:  # we had a response
        thisExp.addData('key_resp_goodbye.rt', key_resp_goodbye.rt)
        thisExp.addData('key_resp_goodbye.duration', key_resp_goodbye.duration)
    thisExp.nextEntry()
    # the Routine "goodbye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
