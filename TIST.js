/************* 
 * Tist *
 *************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'TIST';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(refreshRoutineBegin());
flowScheduler.add(refreshRoutineEachFrame());
flowScheduler.add(refreshRoutineEnd());
flowScheduler.add(practice_instructRoutineBegin());
flowScheduler.add(practice_instructRoutineEachFrame());
flowScheduler.add(practice_instructRoutineEnd());
flowScheduler.add(refreshRoutineBegin());
flowScheduler.add(refreshRoutineEachFrame());
flowScheduler.add(refreshRoutineEnd());
const loop_practiceLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loop_practiceLoopBegin(loop_practiceLoopScheduler));
flowScheduler.add(loop_practiceLoopScheduler);
flowScheduler.add(loop_practiceLoopEnd);












flowScheduler.add(primary_task_welcomeRoutineBegin());
flowScheduler.add(primary_task_welcomeRoutineEachFrame());
flowScheduler.add(primary_task_welcomeRoutineEnd());
flowScheduler.add(refreshRoutineBegin());
flowScheduler.add(refreshRoutineEachFrame());
flowScheduler.add(refreshRoutineEnd());
const loop_primaryLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loop_primaryLoopBegin(loop_primaryLoopScheduler));
flowScheduler.add(loop_primaryLoopScheduler);
flowScheduler.add(loop_primaryLoopEnd);












flowScheduler.add(goodbyeRoutineBegin());
flowScheduler.add(goodbyeRoutineEachFrame());
flowScheduler.add(goodbyeRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'loop_block_practice.xlsx', 'path': 'loop_block_practice.xlsx'},
    {'name': 'block_practice_1.xlsx', 'path': 'block_practice_1.xlsx'},
    {'name': 'faces/HAM1.bmp', 'path': 'faces/HAM1.bmp'},
    {'name': 'faces/NEF6.bmp', 'path': 'faces/NEF6.bmp'},
    {'name': 'faces/SAF2.bmp', 'path': 'faces/SAF2.bmp'},
    {'name': 'faces/SAF3.bmp', 'path': 'faces/SAF3.bmp'},
    {'name': 'faces/SAM1.bmp', 'path': 'faces/SAM1.bmp'},
    {'name': 'faces/NEF9.bmp', 'path': 'faces/NEF9.bmp'},
    {'name': 'faces/SAM6.bmp', 'path': 'faces/SAM6.bmp'},
    {'name': 'faces/NEM4.bmp', 'path': 'faces/NEM4.bmp'},
    {'name': 'faces/HAF59.bmp', 'path': 'faces/HAF59.bmp'},
    {'name': 'faces/HAF107.bmp', 'path': 'faces/HAF107.bmp'},
    {'name': 'faces/HAM9.bmp', 'path': 'faces/HAM9.bmp'},
    {'name': 'faces/NEM5.bmp', 'path': 'faces/NEM5.bmp'},
    {'name': 'faces/HAM38.bmp', 'path': 'faces/HAM38.bmp'},
    {'name': 'faces/HAF110.bmp', 'path': 'faces/HAF110.bmp'},
    {'name': 'faces/SAM7.bmp', 'path': 'faces/SAM7.bmp'},
    {'name': 'faces/NEF35.bmp', 'path': 'faces/NEF35.bmp'},
    {'name': 'faces/NEM6.bmp', 'path': 'faces/NEM6.bmp'},
    {'name': 'faces/SAF20.bmp', 'path': 'faces/SAF20.bmp'},
    {'name': 'faces/NEM15.bmp', 'path': 'faces/NEM15.bmp'},
    {'name': 'faces/NEM59.bmp', 'path': 'faces/NEM59.bmp'},
    {'name': 'faces/SAF32.bmp', 'path': 'faces/SAF32.bmp'},
    {'name': 'loop_block.xlsx', 'path': 'loop_block.xlsx'},
    {'name': 'block_1.xlsx', 'path': 'block_1.xlsx'},
    {'name': 'faces/SAF20.bmp', 'path': 'faces/SAF20.bmp'},
    {'name': 'faces/NEF15.bmp', 'path': 'faces/NEF15.bmp'},
    {'name': 'faces/HAF118.bmp', 'path': 'faces/HAF118.bmp'},
    {'name': 'faces/HAM1.bmp', 'path': 'faces/HAM1.bmp'},
    {'name': 'faces/NEM11.bmp', 'path': 'faces/NEM11.bmp'},
    {'name': 'faces/HAM2.bmp', 'path': 'faces/HAM2.bmp'},
    {'name': 'faces/HAF122.bmp', 'path': 'faces/HAF122.bmp'},
    {'name': 'faces/SAM10.bmp', 'path': 'faces/SAM10.bmp'},
    {'name': 'faces/NEM14.bmp', 'path': 'faces/NEM14.bmp'},
    {'name': 'faces/NEF35.bmp', 'path': 'faces/NEF35.bmp'},
    {'name': 'faces/HAF1.bmp', 'path': 'faces/HAF1.bmp'},
    {'name': 'faces/NEF45.bmp', 'path': 'faces/NEF45.bmp'},
    {'name': 'faces/NEM15.bmp', 'path': 'faces/NEM15.bmp'},
    {'name': 'faces/SAM29.bmp', 'path': 'faces/SAM29.bmp'},
    {'name': 'faces/NEF60.bmp', 'path': 'faces/NEF60.bmp'},
    {'name': 'faces/SAF31.bmp', 'path': 'faces/SAF31.bmp'},
    {'name': 'faces/SAF32.bmp', 'path': 'faces/SAF32.bmp'},
    {'name': 'faces/HAM5.bmp', 'path': 'faces/HAM5.bmp'},
    {'name': 'faces/NEF62.bmp', 'path': 'faces/NEF62.bmp'},
    {'name': 'block_2.xlsx', 'path': 'block_2.xlsx'},
    {'name': 'faces/HAF8.bmp', 'path': 'faces/HAF8.bmp'},
    {'name': 'faces/NEF66.bmp', 'path': 'faces/NEF66.bmp'},
    {'name': 'faces/SAM30.bmp', 'path': 'faces/SAM30.bmp'},
    {'name': 'faces/SAF33.bmp', 'path': 'faces/SAF33.bmp'},
    {'name': 'faces/NEM29.bmp', 'path': 'faces/NEM29.bmp'},
    {'name': 'faces/SAM3.bmp', 'path': 'faces/SAM3.bmp'},
    {'name': 'faces/SAF34.bmp', 'path': 'faces/SAF34.bmp'},
    {'name': 'faces/HAF42.bmp', 'path': 'faces/HAF42.bmp'},
    {'name': 'faces/NEM37.bmp', 'path': 'faces/NEM37.bmp'},
    {'name': 'faces/NEM40.bmp', 'path': 'faces/NEM40.bmp'},
    {'name': 'faces/HAF59.bmp', 'path': 'faces/HAF59.bmp'},
    {'name': 'faces/NEM59.bmp', 'path': 'faces/NEM59.bmp'},
    {'name': 'faces/NEF83.bmp', 'path': 'faces/NEF83.bmp'},
    {'name': 'faces/SAM9.bmp', 'path': 'faces/SAM9.bmp'},
    {'name': 'faces/HAM9.bmp', 'path': 'faces/HAM9.bmp'},
    {'name': 'faces/HAM10.bmp', 'path': 'faces/HAM10.bmp'},
    {'name': 'faces/SAF48.bmp', 'path': 'faces/SAF48.bmp'},
    {'name': 'faces/HAM17.bmp', 'path': 'faces/HAM17.bmp'},
    {'name': 'block_3.xlsx', 'path': 'block_3.xlsx'},
    {'name': 'faces/HAF70.bmp', 'path': 'faces/HAF70.bmp'},
    {'name': 'faces/SAF2.bmp', 'path': 'faces/SAF2.bmp'},
    {'name': 'faces/NEM76.bmp', 'path': 'faces/NEM76.bmp'},
    {'name': 'faces/NEF99.bmp', 'path': 'faces/NEF99.bmp'},
    {'name': 'faces/SAM6.bmp', 'path': 'faces/SAM6.bmp'},
    {'name': 'faces/NEM95.bmp', 'path': 'faces/NEM95.bmp'},
    {'name': 'faces/NEF107.bmp', 'path': 'faces/NEF107.bmp'},
    {'name': 'faces/HAF82.bmp', 'path': 'faces/HAF82.bmp'},
    {'name': 'faces/SAM7.bmp', 'path': 'faces/SAM7.bmp'},
    {'name': 'faces/SAF3.bmp', 'path': 'faces/SAF3.bmp'},
    {'name': 'faces/HAM38.bmp', 'path': 'faces/HAM38.bmp'},
    {'name': 'faces/SAF15.bmp', 'path': 'faces/SAF15.bmp'},
    {'name': 'faces/NEM98.bmp', 'path': 'faces/NEM98.bmp'},
    {'name': 'faces/HAF86.bmp', 'path': 'faces/HAF86.bmp'},
    {'name': 'faces/HAF94.bmp', 'path': 'faces/HAF94.bmp'},
    {'name': 'faces/HAM39.bmp', 'path': 'faces/HAM39.bmp'},
    {'name': 'faces/NEM4.bmp', 'path': 'faces/NEM4.bmp'},
    {'name': 'faces/HAM49.bmp', 'path': 'faces/HAM49.bmp'},
    {'name': 'block_4.xlsx', 'path': 'block_4.xlsx'},
    {'name': 'faces/NEM5.bmp', 'path': 'faces/NEM5.bmp'},
    {'name': 'faces/NEF6.bmp', 'path': 'faces/NEF6.bmp'},
    {'name': 'faces/HAM50.bmp', 'path': 'faces/HAM50.bmp'},
    {'name': 'faces/HAF99.bmp', 'path': 'faces/HAF99.bmp'},
    {'name': 'faces/HAM78.bmp', 'path': 'faces/HAM78.bmp'},
    {'name': 'faces/HAF101.bmp', 'path': 'faces/HAF101.bmp'},
    {'name': 'faces/NEM6.bmp', 'path': 'faces/NEM6.bmp'},
    {'name': 'faces/HAF102.bmp', 'path': 'faces/HAF102.bmp'},
    {'name': 'faces/HAM95.bmp', 'path': 'faces/HAM95.bmp'},
    {'name': 'faces/NEM8.bmp', 'path': 'faces/NEM8.bmp'},
    {'name': 'faces/SAM12.bmp', 'path': 'faces/SAM12.bmp'},
    {'name': 'faces/SAM13.bmp', 'path': 'faces/SAM13.bmp'},
    {'name': 'faces/NEF8.bmp', 'path': 'faces/NEF8.bmp'},
    {'name': 'faces/HAM98.bmp', 'path': 'faces/HAM98.bmp'},
    {'name': 'faces/NEF9.bmp', 'path': 'faces/NEF9.bmp'},
    {'name': 'block_5.xlsx', 'path': 'block_5.xlsx'},
    {'name': 'faces/HAM112.bmp', 'path': 'faces/HAM112.bmp'},
    {'name': 'faces/SAM15.bmp', 'path': 'faces/SAM15.bmp'},
    {'name': 'faces/HAM114.bmp', 'path': 'faces/HAM114.bmp'},
    {'name': 'faces/SAM31.bmp', 'path': 'faces/SAM31.bmp'},
    {'name': 'faces/HAF103.bmp', 'path': 'faces/HAF103.bmp'},
    {'name': 'faces/HAF107.bmp', 'path': 'faces/HAF107.bmp'},
    {'name': 'block_6.xlsx', 'path': 'block_6.xlsx'},
    {'name': 'faces/HAF110.bmp', 'path': 'faces/HAF110.bmp'},
    {'name': 'faces/HAF115.bmp', 'path': 'faces/HAF115.bmp'},
    {'name': 'block_7.xlsx', 'path': 'block_7.xlsx'},
    {'name': 'faces/SAM11.bmp', 'path': 'faces/SAM11.bmp'},
    {'name': 'block_8.xlsx', 'path': 'block_8.xlsx'},
    {'name': 'faces/SAM1.bmp', 'path': 'faces/SAM1.bmp'},
    {'name': 'block_9.xlsx', 'path': 'block_9.xlsx'},
    {'name': 'block_10.xlsx', 'path': 'block_10.xlsx'},
    {'name': 'faces/SAM5.bmp', 'path': 'faces/SAM5.bmp'},
    {'name': 'block_11.xlsx', 'path': 'block_11.xlsx'},
    {'name': 'faces/SAF16.bmp', 'path': 'faces/SAF16.bmp'},
    {'name': 'block_12.xlsx', 'path': 'block_12.xlsx'},
    {'name': 'block_13.xlsx', 'path': 'block_13.xlsx'},
    {'name': 'block_14.xlsx', 'path': 'block_14.xlsx'},
    {'name': 'block_15.xlsx', 'path': 'block_15.xlsx'},
    {'name': 'block_16.xlsx', 'path': 'block_16.xlsx'},
    {'name': 'faces/SAF24.bmp', 'path': 'faces/SAF24.bmp'},
    {'name': 'block_17.xlsx', 'path': 'block_17.xlsx'},
    {'name': 'block_18.xlsx', 'path': 'block_18.xlsx'},
    {'name': 'block_19.xlsx', 'path': 'block_19.xlsx'},
    {'name': 'block_20.xlsx', 'path': 'block_20.xlsx'},
    {'name': 'block_21.xlsx', 'path': 'block_21.xlsx'},
    {'name': 'block_22.xlsx', 'path': 'block_22.xlsx'},
    {'name': 'block_23.xlsx', 'path': 'block_23.xlsx'},
    {'name': 'block_24.xlsx', 'path': 'block_24.xlsx'},
    {'name': 'block_25.xlsx', 'path': 'block_25.xlsx'},
    {'name': 'stimuli/welcome.png', 'path': 'stimuli/welcome.png'},
    {'name': 'stimuli/practice_instruct.png', 'path': 'stimuli/practice_instruct.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'stimuli/continue_check.png', 'path': 'stimuli/continue_check.png'},
    {'name': 'stimuli/welcome_primary.png', 'path': 'stimuli/welcome_primary.png'},
    {'name': 'faces/HAF1.bmp', 'path': 'faces/HAF1.bmp'},
    {'name': 'faces/HAF8.bmp', 'path': 'faces/HAF8.bmp'},
    {'name': 'faces/HAF42.bmp', 'path': 'faces/HAF42.bmp'},
    {'name': 'faces/HAF59.bmp', 'path': 'faces/HAF59.bmp'},
    {'name': 'faces/HAF70.bmp', 'path': 'faces/HAF70.bmp'},
    {'name': 'faces/HAF82.bmp', 'path': 'faces/HAF82.bmp'},
    {'name': 'faces/HAF86.bmp', 'path': 'faces/HAF86.bmp'},
    {'name': 'faces/HAF94.bmp', 'path': 'faces/HAF94.bmp'},
    {'name': 'faces/HAF99.bmp', 'path': 'faces/HAF99.bmp'},
    {'name': 'faces/HAF101.bmp', 'path': 'faces/HAF101.bmp'},
    {'name': 'faces/HAF102.bmp', 'path': 'faces/HAF102.bmp'},
    {'name': 'faces/HAF103.bmp', 'path': 'faces/HAF103.bmp'},
    {'name': 'faces/HAF107.bmp', 'path': 'faces/HAF107.bmp'},
    {'name': 'faces/HAF110.bmp', 'path': 'faces/HAF110.bmp'},
    {'name': 'faces/HAF115.bmp', 'path': 'faces/HAF115.bmp'},
    {'name': 'faces/HAF118.bmp', 'path': 'faces/HAF118.bmp'},
    {'name': 'faces/HAF122.bmp', 'path': 'faces/HAF122.bmp'},
    {'name': 'faces/HAM1.bmp', 'path': 'faces/HAM1.bmp'},
    {'name': 'faces/HAM2.bmp', 'path': 'faces/HAM2.bmp'},
    {'name': 'faces/HAM5.bmp', 'path': 'faces/HAM5.bmp'},
    {'name': 'faces/HAM9.bmp', 'path': 'faces/HAM9.bmp'},
    {'name': 'faces/HAM10.bmp', 'path': 'faces/HAM10.bmp'},
    {'name': 'faces/HAM17.bmp', 'path': 'faces/HAM17.bmp'},
    {'name': 'faces/HAM38.bmp', 'path': 'faces/HAM38.bmp'},
    {'name': 'faces/HAM39.bmp', 'path': 'faces/HAM39.bmp'},
    {'name': 'faces/HAM49.bmp', 'path': 'faces/HAM49.bmp'},
    {'name': 'faces/HAM50.bmp', 'path': 'faces/HAM50.bmp'},
    {'name': 'faces/HAM78.bmp', 'path': 'faces/HAM78.bmp'},
    {'name': 'faces/HAM89.bmp', 'path': 'faces/HAM89.bmp'},
    {'name': 'faces/HAM95.bmp', 'path': 'faces/HAM95.bmp'},
    {'name': 'faces/HAM98.bmp', 'path': 'faces/HAM98.bmp'},
    {'name': 'faces/HAM112.bmp', 'path': 'faces/HAM112.bmp'},
    {'name': 'faces/HAM114.bmp', 'path': 'faces/HAM114.bmp'},
    {'name': 'faces/NEF6.bmp', 'path': 'faces/NEF6.bmp'},
    {'name': 'faces/NEF8.bmp', 'path': 'faces/NEF8.bmp'},
    {'name': 'faces/NEF9.bmp', 'path': 'faces/NEF9.bmp'},
    {'name': 'faces/NEF15.bmp', 'path': 'faces/NEF15.bmp'},
    {'name': 'faces/NEF35.bmp', 'path': 'faces/NEF35.bmp'},
    {'name': 'faces/NEF36.bmp', 'path': 'faces/NEF36.bmp'},
    {'name': 'faces/NEF45.bmp', 'path': 'faces/NEF45.bmp'},
    {'name': 'faces/NEF60.bmp', 'path': 'faces/NEF60.bmp'},
    {'name': 'faces/NEF62.bmp', 'path': 'faces/NEF62.bmp'},
    {'name': 'faces/NEF66.bmp', 'path': 'faces/NEF66.bmp'},
    {'name': 'faces/NEF83.bmp', 'path': 'faces/NEF83.bmp'},
    {'name': 'faces/NEF99.bmp', 'path': 'faces/NEF99.bmp'},
    {'name': 'faces/NEF107.bmp', 'path': 'faces/NEF107.bmp'},
    {'name': 'faces/NEM4.bmp', 'path': 'faces/NEM4.bmp'},
    {'name': 'faces/NEM5.bmp', 'path': 'faces/NEM5.bmp'},
    {'name': 'faces/NEM6.bmp', 'path': 'faces/NEM6.bmp'},
    {'name': 'faces/NEM8.bmp', 'path': 'faces/NEM8.bmp'},
    {'name': 'faces/NEM11.bmp', 'path': 'faces/NEM11.bmp'},
    {'name': 'faces/NEM14.bmp', 'path': 'faces/NEM14.bmp'},
    {'name': 'faces/NEM15.bmp', 'path': 'faces/NEM15.bmp'},
    {'name': 'faces/NEM29.bmp', 'path': 'faces/NEM29.bmp'},
    {'name': 'faces/NEM37.bmp', 'path': 'faces/NEM37.bmp'},
    {'name': 'faces/NEM40.bmp', 'path': 'faces/NEM40.bmp'},
    {'name': 'faces/NEM59.bmp', 'path': 'faces/NEM59.bmp'},
    {'name': 'faces/NEM76.bmp', 'path': 'faces/NEM76.bmp'},
    {'name': 'faces/NEM95.bmp', 'path': 'faces/NEM95.bmp'},
    {'name': 'faces/NEM98.bmp', 'path': 'faces/NEM98.bmp'},
    {'name': 'faces/SAF2.bmp', 'path': 'faces/SAF2.bmp'},
    {'name': 'faces/SAF3.bmp', 'path': 'faces/SAF3.bmp'},
    {'name': 'faces/SAF15.bmp', 'path': 'faces/SAF15.bmp'},
    {'name': 'faces/SAF16.bmp', 'path': 'faces/SAF16.bmp'},
    {'name': 'faces/SAF20.bmp', 'path': 'faces/SAF20.bmp'},
    {'name': 'faces/SAF24.bmp', 'path': 'faces/SAF24.bmp'},
    {'name': 'faces/SAF31.bmp', 'path': 'faces/SAF31.bmp'},
    {'name': 'faces/SAF32.bmp', 'path': 'faces/SAF32.bmp'},
    {'name': 'faces/SAF33.bmp', 'path': 'faces/SAF33.bmp'},
    {'name': 'faces/SAF34.bmp', 'path': 'faces/SAF34.bmp'},
    {'name': 'faces/SAF48.bmp', 'path': 'faces/SAF48.bmp'},
    {'name': 'faces/SAM1.bmp', 'path': 'faces/SAM1.bmp'},
    {'name': 'faces/SAM3.bmp', 'path': 'faces/SAM3.bmp'},
    {'name': 'faces/SAM5.bmp', 'path': 'faces/SAM5.bmp'},
    {'name': 'faces/SAM6.bmp', 'path': 'faces/SAM6.bmp'},
    {'name': 'faces/SAM7.bmp', 'path': 'faces/SAM7.bmp'},
    {'name': 'faces/SAM9.bmp', 'path': 'faces/SAM9.bmp'},
    {'name': 'faces/SAM10.bmp', 'path': 'faces/SAM10.bmp'},
    {'name': 'faces/SAM11.bmp', 'path': 'faces/SAM11.bmp'},
    {'name': 'faces/SAM12.bmp', 'path': 'faces/SAM12.bmp'},
    {'name': 'faces/SAM13.bmp', 'path': 'faces/SAM13.bmp'},
    {'name': 'faces/SAM15.bmp', 'path': 'faces/SAM15.bmp'},
    {'name': 'faces/SAM29.bmp', 'path': 'faces/SAM29.bmp'},
    {'name': 'faces/SAM30.bmp', 'path': 'faces/SAM30.bmp'},
    {'name': 'faces/SAM31.bmp', 'path': 'faces/SAM31.bmp'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var welcomeClock;
var image_welcome;
var key_resp_welcome;
var refreshClock;
var text_refresh;
var practice_instructClock;
var image_practice_instruct;
var key_resp_practice_instruct;
var fixationClock;
var text_fixation;
var block_practiceClock;
var image_block_practice;
var key_resp_block_practice;
var answer_block_practiceClock;
var text_answer_block_practice;
var textbox_answer_block_practice;
var button_text_block_practice;
var mouse_block_practice;
var feedback_text;
var feedback_block_practiceClock;
var text_feedback_block_practice;
var text_feedback_note_practice;
var key_resp;
var continue_checkClock;
var image_continue_check;
var key_resp_continue_check;
var primary_task_welcomeClock;
var image_primary_welcome;
var key_resp_primary_welcome;
var blockClock;
var image_block;
var key_resp_block;
var answer_blockClock;
var text_answer_block;
var textbox_answer_block;
var button_answer_block;
var mouse_answer_block;
var feedback_text_primary;
var feedback_blockClock;
var text_feedback_block;
var text_feedback_block_note;
var key_resp_feedback_block;
var continue_check_blockClock;
var text_continue_check_block;
var block_counter;
var text_continue_prompt;
var key_resp_contiue_check_block;
var goodbyeClock;
var text_goodbye;
var key_resp_goodbye;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  image_welcome = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_welcome', units : undefined, 
    image : 'stimuli/welcome.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [1.1, 0.825],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_welcome = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "refresh"
  refreshClock = new util.Clock();
  text_refresh = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_refresh',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "practice_instruct"
  practice_instructClock = new util.Clock();
  image_practice_instruct = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_practice_instruct', units : undefined, 
    image : 'stimuli/practice_instruct.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [1.1, 0.825],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_practice_instruct = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  text_fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_fixation',
    text: '+',
    font: 'Noto Sans SC',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.2,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "block_practice"
  block_practiceClock = new util.Clock();
  image_block_practice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_block_practice', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.36, 0.41535],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_block_practice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "answer_block_practice"
  answer_block_practiceClock = new util.Clock();
  text_answer_block_practice = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_answer_block_practice',
    text: '请按如下顺序输入答案（数字中间无间隔或任何字符）：\n\n快乐-平静-悲伤',
    font: 'Noto Sans SC',
    units: undefined, 
    pos: [0, 0.3], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  textbox_answer_block_practice = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_answer_block_practice',
    text: '',
    placeholder: undefined,
    font: 'Noto Sans SC',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  button_text_block_practice = new visual.TextStim({
    win: psychoJS.window,
    name: 'button_text_block_practice',
    text: '点击这里继续',
    font: 'Noto Sans SC',
    units: undefined, 
    pos: [0, (- 0.35)], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  mouse_block_practice = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_block_practice.mouseClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  feedback_text = "";
  
  // Initialize components for Routine "feedback_block_practice"
  feedback_block_practiceClock = new util.Clock();
  text_feedback_block_practice = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_feedback_block_practice',
    text: '',
    font: 'Noto Sans SC',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_feedback_note_practice = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_feedback_note_practice',
    text: '请按空格键继续',
    font: 'Noto Sans SC',
    units: undefined, 
    pos: [0, (- 0.25)], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "continue_check"
  continue_checkClock = new util.Clock();
  image_continue_check = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_continue_check', units : undefined, 
    image : 'stimuli/continue_check.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [1.1, 0.825],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_continue_check = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "primary_task_welcome"
  primary_task_welcomeClock = new util.Clock();
  image_primary_welcome = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_primary_welcome', units : undefined, 
    image : 'stimuli/welcome_primary.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [1.1, 0.825],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_primary_welcome = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "block"
  blockClock = new util.Clock();
  image_block = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_block', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.36, 0.41535],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_block = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "answer_block"
  answer_blockClock = new util.Clock();
  text_answer_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_answer_block',
    text: '请按如下顺序输入答案（数字中间无间隔或任何字符）：\n\n快乐-平静-悲伤',
    font: 'Noto Sans SC',
    units: undefined, 
    pos: [0, 0.3], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  textbox_answer_block = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_answer_block',
    text: '',
    placeholder: undefined,
    font: 'Noto Sans SC',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  button_answer_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'button_answer_block',
    text: '点击这里继续',
    font: 'Noto Sans SC',
    units: undefined, 
    pos: [0, (- 0.35)], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  mouse_answer_block = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_answer_block.mouseClock = new util.Clock();
  // Run 'Begin Experiment' code from code_answer_block
  feedback_text_primary = "";
  
  // Initialize components for Routine "feedback_block"
  feedback_blockClock = new util.Clock();
  text_feedback_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_feedback_block',
    text: '',
    font: 'Noto Sans SC',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_feedback_block_note = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_feedback_block_note',
    text: '请按空格键继续',
    font: 'Noto Sans SC',
    units: undefined, 
    pos: [0, (- 0.25)], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_feedback_block = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "continue_check_block"
  continue_check_blockClock = new util.Clock();
  text_continue_check_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_continue_check_block',
    text: '',
    font: 'Noto Sans SC',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Run 'Begin Experiment' code from code_progress_report
  block_counter = 0;
  
  text_continue_prompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_continue_prompt',
    text: '请按空格键继续。',
    font: 'Noto Sans SC',
    units: undefined, 
    pos: [0, (- 0.25)], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_contiue_check_block = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "goodbye"
  goodbyeClock = new util.Clock();
  text_goodbye = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_goodbye',
    text: '测试结束。\n\n感谢您参与本测试，祝生活愉快！',
    font: 'Noto Sans SC',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_goodbye = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var welcomeMaxDurationReached;
var _key_resp_welcome_allKeys;
var welcomeMaxDuration;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcome' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    welcomeClock.reset();
    routineTimer.reset();
    welcomeMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_welcome.keys = undefined;
    key_resp_welcome.rt = undefined;
    _key_resp_welcome_allKeys = [];
    psychoJS.experiment.addData('welcome.started', globalClock.getTime());
    welcomeMaxDuration = null
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(image_welcome);
    welcomeComponents.push(key_resp_welcome);
    
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcome' ---
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_welcome* updates
    if (t >= 0.0 && image_welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_welcome.tStart = t;  // (not accounting for frame time here)
      image_welcome.frameNStart = frameN;  // exact frame index
      
      image_welcome.setAutoDraw(true);
    }
    
    
    // *key_resp_welcome* updates
    if (t >= 0.0 && key_resp_welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_welcome.tStart = t;  // (not accounting for frame time here)
      key_resp_welcome.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_welcome.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_welcome.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_welcome.clearEvents(); });
    }
    
    if (key_resp_welcome.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_welcome.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_welcome_allKeys = _key_resp_welcome_allKeys.concat(theseKeys);
      if (_key_resp_welcome_allKeys.length > 0) {
        key_resp_welcome.keys = _key_resp_welcome_allKeys[_key_resp_welcome_allKeys.length - 1].name;  // just the last key pressed
        key_resp_welcome.rt = _key_resp_welcome_allKeys[_key_resp_welcome_allKeys.length - 1].rt;
        key_resp_welcome.duration = _key_resp_welcome_allKeys[_key_resp_welcome_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcome' ---
    for (const thisComponent of welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_welcome.corr, level);
    }
    psychoJS.experiment.addData('key_resp_welcome.keys', key_resp_welcome.keys);
    if (typeof key_resp_welcome.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_welcome.rt', key_resp_welcome.rt);
        psychoJS.experiment.addData('key_resp_welcome.duration', key_resp_welcome.duration);
        routineTimer.reset();
        }
    
    key_resp_welcome.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var refreshMaxDurationReached;
var refreshMaxDuration;
var refreshComponents;
function refreshRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'refresh' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    refreshClock.reset(routineTimer.getTime());
    routineTimer.add(0.200000);
    refreshMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('refresh.started', globalClock.getTime());
    refreshMaxDuration = null
    // keep track of which components have finished
    refreshComponents = [];
    refreshComponents.push(text_refresh);
    
    for (const thisComponent of refreshComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function refreshRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'refresh' ---
    // get current time
    t = refreshClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_refresh* updates
    if (t >= 0.0 && text_refresh.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_refresh.tStart = t;  // (not accounting for frame time here)
      text_refresh.frameNStart = frameN;  // exact frame index
      
      text_refresh.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_refresh.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_refresh.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of refreshComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function refreshRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'refresh' ---
    for (const thisComponent of refreshComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('refresh.stopped', globalClock.getTime());
    if (refreshMaxDurationReached) {
        refreshClock.add(refreshMaxDuration);
    } else {
        refreshClock.add(0.200000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_instructMaxDurationReached;
var _key_resp_practice_instruct_allKeys;
var practice_instructMaxDuration;
var practice_instructComponents;
function practice_instructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_instruct' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice_instructClock.reset();
    routineTimer.reset();
    practice_instructMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_practice_instruct.keys = undefined;
    key_resp_practice_instruct.rt = undefined;
    _key_resp_practice_instruct_allKeys = [];
    psychoJS.experiment.addData('practice_instruct.started', globalClock.getTime());
    practice_instructMaxDuration = null
    // keep track of which components have finished
    practice_instructComponents = [];
    practice_instructComponents.push(image_practice_instruct);
    practice_instructComponents.push(key_resp_practice_instruct);
    
    for (const thisComponent of practice_instructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practice_instructRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_instruct' ---
    // get current time
    t = practice_instructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_practice_instruct* updates
    if (t >= 0.0 && image_practice_instruct.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_practice_instruct.tStart = t;  // (not accounting for frame time here)
      image_practice_instruct.frameNStart = frameN;  // exact frame index
      
      image_practice_instruct.setAutoDraw(true);
    }
    
    
    // *key_resp_practice_instruct* updates
    if (t >= 0.0 && key_resp_practice_instruct.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_practice_instruct.tStart = t;  // (not accounting for frame time here)
      key_resp_practice_instruct.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_practice_instruct.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_practice_instruct.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_practice_instruct.clearEvents(); });
    }
    
    if (key_resp_practice_instruct.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_practice_instruct.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_practice_instruct_allKeys = _key_resp_practice_instruct_allKeys.concat(theseKeys);
      if (_key_resp_practice_instruct_allKeys.length > 0) {
        key_resp_practice_instruct.keys = _key_resp_practice_instruct_allKeys[_key_resp_practice_instruct_allKeys.length - 1].name;  // just the last key pressed
        key_resp_practice_instruct.rt = _key_resp_practice_instruct_allKeys[_key_resp_practice_instruct_allKeys.length - 1].rt;
        key_resp_practice_instruct.duration = _key_resp_practice_instruct_allKeys[_key_resp_practice_instruct_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_instructComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_instructRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_instruct' ---
    for (const thisComponent of practice_instructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_instruct.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_practice_instruct.corr, level);
    }
    psychoJS.experiment.addData('key_resp_practice_instruct.keys', key_resp_practice_instruct.keys);
    if (typeof key_resp_practice_instruct.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_practice_instruct.rt', key_resp_practice_instruct.rt);
        psychoJS.experiment.addData('key_resp_practice_instruct.duration', key_resp_practice_instruct.duration);
        routineTimer.reset();
        }
    
    key_resp_practice_instruct.stop();
    // the Routine "practice_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var loop_practice;
function loop_practiceLoopBegin(loop_practiceLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_practice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 99, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'loop_block_practice.xlsx',
      seed: undefined, name: 'loop_practice'
    });
    psychoJS.experiment.addLoop(loop_practice); // add the loop to the experiment
    currentLoop = loop_practice;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoop_practice of loop_practice) {
      snapshot = loop_practice.getSnapshot();
      loop_practiceLoopScheduler.add(importConditions(snapshot));
      loop_practiceLoopScheduler.add(fixationRoutineBegin(snapshot));
      loop_practiceLoopScheduler.add(fixationRoutineEachFrame());
      loop_practiceLoopScheduler.add(fixationRoutineEnd(snapshot));
      const loop_block_practiceLoopScheduler = new Scheduler(psychoJS);
      loop_practiceLoopScheduler.add(loop_block_practiceLoopBegin(loop_block_practiceLoopScheduler, snapshot));
      loop_practiceLoopScheduler.add(loop_block_practiceLoopScheduler);
      loop_practiceLoopScheduler.add(loop_block_practiceLoopEnd);
      loop_practiceLoopScheduler.add(answer_block_practiceRoutineBegin(snapshot));
      loop_practiceLoopScheduler.add(answer_block_practiceRoutineEachFrame());
      loop_practiceLoopScheduler.add(answer_block_practiceRoutineEnd(snapshot));
      loop_practiceLoopScheduler.add(refreshRoutineBegin(snapshot));
      loop_practiceLoopScheduler.add(refreshRoutineEachFrame());
      loop_practiceLoopScheduler.add(refreshRoutineEnd(snapshot));
      loop_practiceLoopScheduler.add(feedback_block_practiceRoutineBegin(snapshot));
      loop_practiceLoopScheduler.add(feedback_block_practiceRoutineEachFrame());
      loop_practiceLoopScheduler.add(feedback_block_practiceRoutineEnd(snapshot));
      loop_practiceLoopScheduler.add(refreshRoutineBegin(snapshot));
      loop_practiceLoopScheduler.add(refreshRoutineEachFrame());
      loop_practiceLoopScheduler.add(refreshRoutineEnd(snapshot));
      loop_practiceLoopScheduler.add(continue_checkRoutineBegin(snapshot));
      loop_practiceLoopScheduler.add(continue_checkRoutineEachFrame());
      loop_practiceLoopScheduler.add(continue_checkRoutineEnd(snapshot));
      loop_practiceLoopScheduler.add(refreshRoutineBegin(snapshot));
      loop_practiceLoopScheduler.add(refreshRoutineEachFrame());
      loop_practiceLoopScheduler.add(refreshRoutineEnd(snapshot));
      loop_practiceLoopScheduler.add(loop_practiceLoopEndIteration(loop_practiceLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var loop_block_practice;
function loop_block_practiceLoopBegin(loop_block_practiceLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_block_practice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: block_practice_file,
      seed: undefined, name: 'loop_block_practice'
    });
    psychoJS.experiment.addLoop(loop_block_practice); // add the loop to the experiment
    currentLoop = loop_block_practice;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoop_block_practice of loop_block_practice) {
      snapshot = loop_block_practice.getSnapshot();
      loop_block_practiceLoopScheduler.add(importConditions(snapshot));
      loop_block_practiceLoopScheduler.add(block_practiceRoutineBegin(snapshot));
      loop_block_practiceLoopScheduler.add(block_practiceRoutineEachFrame());
      loop_block_practiceLoopScheduler.add(block_practiceRoutineEnd(snapshot));
      loop_block_practiceLoopScheduler.add(refreshRoutineBegin(snapshot));
      loop_block_practiceLoopScheduler.add(refreshRoutineEachFrame());
      loop_block_practiceLoopScheduler.add(refreshRoutineEnd(snapshot));
      loop_block_practiceLoopScheduler.add(loop_block_practiceLoopEndIteration(loop_block_practiceLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function loop_block_practiceLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_block_practice);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loop_block_practiceLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function loop_practiceLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_practice);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loop_practiceLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var loop_primary;
function loop_primaryLoopBegin(loop_primaryLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_primary = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'loop_block.xlsx',
      seed: undefined, name: 'loop_primary'
    });
    psychoJS.experiment.addLoop(loop_primary); // add the loop to the experiment
    currentLoop = loop_primary;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoop_primary of loop_primary) {
      snapshot = loop_primary.getSnapshot();
      loop_primaryLoopScheduler.add(importConditions(snapshot));
      loop_primaryLoopScheduler.add(fixationRoutineBegin(snapshot));
      loop_primaryLoopScheduler.add(fixationRoutineEachFrame());
      loop_primaryLoopScheduler.add(fixationRoutineEnd(snapshot));
      const loop_blockLoopScheduler = new Scheduler(psychoJS);
      loop_primaryLoopScheduler.add(loop_blockLoopBegin(loop_blockLoopScheduler, snapshot));
      loop_primaryLoopScheduler.add(loop_blockLoopScheduler);
      loop_primaryLoopScheduler.add(loop_blockLoopEnd);
      loop_primaryLoopScheduler.add(answer_blockRoutineBegin(snapshot));
      loop_primaryLoopScheduler.add(answer_blockRoutineEachFrame());
      loop_primaryLoopScheduler.add(answer_blockRoutineEnd(snapshot));
      loop_primaryLoopScheduler.add(refreshRoutineBegin(snapshot));
      loop_primaryLoopScheduler.add(refreshRoutineEachFrame());
      loop_primaryLoopScheduler.add(refreshRoutineEnd(snapshot));
      loop_primaryLoopScheduler.add(feedback_blockRoutineBegin(snapshot));
      loop_primaryLoopScheduler.add(feedback_blockRoutineEachFrame());
      loop_primaryLoopScheduler.add(feedback_blockRoutineEnd(snapshot));
      loop_primaryLoopScheduler.add(refreshRoutineBegin(snapshot));
      loop_primaryLoopScheduler.add(refreshRoutineEachFrame());
      loop_primaryLoopScheduler.add(refreshRoutineEnd(snapshot));
      loop_primaryLoopScheduler.add(continue_check_blockRoutineBegin(snapshot));
      loop_primaryLoopScheduler.add(continue_check_blockRoutineEachFrame());
      loop_primaryLoopScheduler.add(continue_check_blockRoutineEnd(snapshot));
      loop_primaryLoopScheduler.add(refreshRoutineBegin(snapshot));
      loop_primaryLoopScheduler.add(refreshRoutineEachFrame());
      loop_primaryLoopScheduler.add(refreshRoutineEnd(snapshot));
      loop_primaryLoopScheduler.add(loop_primaryLoopEndIteration(loop_primaryLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var loop_block;
function loop_blockLoopBegin(loop_blockLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_block = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: block_file,
      seed: undefined, name: 'loop_block'
    });
    psychoJS.experiment.addLoop(loop_block); // add the loop to the experiment
    currentLoop = loop_block;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoop_block of loop_block) {
      snapshot = loop_block.getSnapshot();
      loop_blockLoopScheduler.add(importConditions(snapshot));
      loop_blockLoopScheduler.add(blockRoutineBegin(snapshot));
      loop_blockLoopScheduler.add(blockRoutineEachFrame());
      loop_blockLoopScheduler.add(blockRoutineEnd(snapshot));
      loop_blockLoopScheduler.add(refreshRoutineBegin(snapshot));
      loop_blockLoopScheduler.add(refreshRoutineEachFrame());
      loop_blockLoopScheduler.add(refreshRoutineEnd(snapshot));
      loop_blockLoopScheduler.add(loop_blockLoopEndIteration(loop_blockLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function loop_blockLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_block);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loop_blockLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function loop_primaryLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_primary);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loop_primaryLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var fixationMaxDurationReached;
var fixationMaxDuration;
var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    fixationClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    fixationMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('fixation.started', globalClock.getTime());
    fixationMaxDuration = null
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(text_fixation);
    
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation' ---
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_fixation* updates
    if (t >= 0.0 && text_fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_fixation.tStart = t;  // (not accounting for frame time here)
      text_fixation.frameNStart = frameN;  // exact frame index
      
      text_fixation.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_fixation.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation' ---
    for (const thisComponent of fixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fixation.stopped', globalClock.getTime());
    if (fixationMaxDurationReached) {
        fixationClock.add(fixationMaxDuration);
    } else {
        fixationClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var block_practiceMaxDurationReached;
var _key_resp_block_practice_allKeys;
var block_practiceMaxDuration;
var block_practiceComponents;
function block_practiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'block_practice' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    block_practiceClock.reset();
    routineTimer.reset();
    block_practiceMaxDurationReached = false;
    // update component parameters for each repeat
    image_block_practice.setImage(stimulus);
    key_resp_block_practice.keys = undefined;
    key_resp_block_practice.rt = undefined;
    _key_resp_block_practice_allKeys = [];
    psychoJS.experiment.addData('block_practice.started', globalClock.getTime());
    block_practiceMaxDuration = null
    // keep track of which components have finished
    block_practiceComponents = [];
    block_practiceComponents.push(image_block_practice);
    block_practiceComponents.push(key_resp_block_practice);
    
    for (const thisComponent of block_practiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function block_practiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'block_practice' ---
    // get current time
    t = block_practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_block_practice* updates
    if (t >= 0.0 && image_block_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_block_practice.tStart = t;  // (not accounting for frame time here)
      image_block_practice.frameNStart = frameN;  // exact frame index
      
      image_block_practice.setAutoDraw(true);
    }
    
    
    // *key_resp_block_practice* updates
    if (t >= 0.0 && key_resp_block_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_block_practice.tStart = t;  // (not accounting for frame time here)
      key_resp_block_practice.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_block_practice.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_block_practice.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_block_practice.clearEvents(); });
    }
    
    if (key_resp_block_practice.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_block_practice.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_block_practice_allKeys = _key_resp_block_practice_allKeys.concat(theseKeys);
      if (_key_resp_block_practice_allKeys.length > 0) {
        key_resp_block_practice.keys = _key_resp_block_practice_allKeys[_key_resp_block_practice_allKeys.length - 1].name;  // just the last key pressed
        key_resp_block_practice.rt = _key_resp_block_practice_allKeys[_key_resp_block_practice_allKeys.length - 1].rt;
        key_resp_block_practice.duration = _key_resp_block_practice_allKeys[_key_resp_block_practice_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of block_practiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function block_practiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'block_practice' ---
    for (const thisComponent of block_practiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('block_practice.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_block_practice.corr, level);
    }
    psychoJS.experiment.addData('key_resp_block_practice.keys', key_resp_block_practice.keys);
    if (typeof key_resp_block_practice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_block_practice.rt', key_resp_block_practice.rt);
        psychoJS.experiment.addData('key_resp_block_practice.duration', key_resp_block_practice.duration);
        routineTimer.reset();
        }
    
    key_resp_block_practice.stop();
    // the Routine "block_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var answer_block_practiceMaxDurationReached;
var gotValidClick;
var answer_block_practiceMaxDuration;
var answer_block_practiceComponents;
function answer_block_practiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'answer_block_practice' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    answer_block_practiceClock.reset();
    routineTimer.reset();
    answer_block_practiceMaxDurationReached = false;
    // update component parameters for each repeat
    textbox_answer_block_practice.setText('');
    textbox_answer_block_practice.refresh();
    // setup some python lists for storing info about the mouse_block_practice
    // current position of the mouse:
    mouse_block_practice.x = [];
    mouse_block_practice.y = [];
    mouse_block_practice.leftButton = [];
    mouse_block_practice.midButton = [];
    mouse_block_practice.rightButton = [];
    mouse_block_practice.time = [];
    mouse_block_practice.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from code
    psychoJS.window.mouseVisible = true;
    
    psychoJS.experiment.addData('answer_block_practice.started', globalClock.getTime());
    answer_block_practiceMaxDuration = null
    // keep track of which components have finished
    answer_block_practiceComponents = [];
    answer_block_practiceComponents.push(text_answer_block_practice);
    answer_block_practiceComponents.push(textbox_answer_block_practice);
    answer_block_practiceComponents.push(button_text_block_practice);
    answer_block_practiceComponents.push(mouse_block_practice);
    
    for (const thisComponent of answer_block_practiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
var _pj;
var allowed_chars;
var text;
var filtered_text;
function answer_block_practiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'answer_block_practice' ---
    // get current time
    t = answer_block_practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_answer_block_practice* updates
    if (t >= 0.0 && text_answer_block_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_answer_block_practice.tStart = t;  // (not accounting for frame time here)
      text_answer_block_practice.frameNStart = frameN;  // exact frame index
      
      text_answer_block_practice.setAutoDraw(true);
    }
    
    
    // *textbox_answer_block_practice* updates
    if (t >= 0.0 && textbox_answer_block_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_answer_block_practice.tStart = t;  // (not accounting for frame time here)
      textbox_answer_block_practice.frameNStart = frameN;  // exact frame index
      
      textbox_answer_block_practice.setAutoDraw(true);
    }
    
    
    // *button_text_block_practice* updates
    if (t >= 0.0 && button_text_block_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_text_block_practice.tStart = t;  // (not accounting for frame time here)
      button_text_block_practice.frameNStart = frameN;  // exact frame index
      
      button_text_block_practice.setAutoDraw(true);
    }
    
    // *mouse_block_practice* updates
    if (t >= 0.0 && mouse_block_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_block_practice.tStart = t;  // (not accounting for frame time here)
      mouse_block_practice.frameNStart = frameN;  // exact frame index
      
      mouse_block_practice.status = PsychoJS.Status.STARTED;
      mouse_block_practice.mouseClock.reset();
      prevButtonState = mouse_block_practice.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_block_practice.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_block_practice.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_block_practice.clickableObjects = eval(button_text_block_practice)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_block_practice.clickableObjects)) {
              mouse_block_practice.clickableObjects = [mouse_block_practice.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_block_practice.clickableObjects) {
              if (obj.contains(mouse_block_practice)) {
                  gotValidClick = true;
                  mouse_block_practice.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              mouse_block_practice.clicked_name.push(null);
          }
          _mouseXYs = mouse_block_practice.getPos();
          mouse_block_practice.x.push(_mouseXYs[0]);
          mouse_block_practice.y.push(_mouseXYs[1]);
          mouse_block_practice.leftButton.push(_mouseButtons[0]);
          mouse_block_practice.midButton.push(_mouseButtons[1]);
          mouse_block_practice.rightButton.push(_mouseButtons[2]);
          mouse_block_practice.time.push(mouse_block_practice.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // Run 'Each Frame' code from code
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    allowed_chars = "0123456789";
    text = textbox_answer_block_practice.text;
    filtered_text = "";
    for (var i, _pj_c = 0, _pj_a = util.range(text.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        if (_pj.in_es6(text[i], allowed_chars)) {
            filtered_text += text[i];
        }
        if ((filtered_text.length >= 3)) {
            break;
        }
    }
    textbox_answer_block_practice.setText(filtered_text);
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of answer_block_practiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var correct_answer_current;
var participant_response;
var num_correct;
function answer_block_practiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'answer_block_practice' ---
    for (const thisComponent of answer_block_practiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('answer_block_practice.stopped', globalClock.getTime());
    psychoJS.experiment.addData('textbox_answer_block_practice.text',textbox_answer_block_practice.text)
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_block_practice.x', mouse_block_practice.x);
    psychoJS.experiment.addData('mouse_block_practice.y', mouse_block_practice.y);
    psychoJS.experiment.addData('mouse_block_practice.leftButton', mouse_block_practice.leftButton);
    psychoJS.experiment.addData('mouse_block_practice.midButton', mouse_block_practice.midButton);
    psychoJS.experiment.addData('mouse_block_practice.rightButton', mouse_block_practice.rightButton);
    psychoJS.experiment.addData('mouse_block_practice.time', mouse_block_practice.time);
    psychoJS.experiment.addData('mouse_block_practice.clicked_name', mouse_block_practice.clicked_name);
    
    // Run 'End Routine' code from code
    correct_answer_current = correct_answer;
    correct_answer_current = correct_answer_current.toString();
    participant_response = textbox_answer_block_practice.text.strip();
    num_correct = util.sum(function () {
        var _pj_a = [], _pj_b = util.range(3);
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var i = _pj_b[_pj_c];
            if ((participant_response[i] === correct_answer_current[i])) {
                _pj_a.push(1);
            }
        }
        return _pj_a;
    }
    .call(this));
    psychoJS.experiment.addData("num_correct", num_correct);
    feedback_text = `你答对了${num_correct}种表情的面孔数目。`;
    psychoJS.window.mouseVisible = false;
    
    // the Routine "answer_block_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_block_practiceMaxDurationReached;
var _key_resp_allKeys;
var feedback_block_practiceMaxDuration;
var feedback_block_practiceComponents;
function feedback_block_practiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_block_practice' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_block_practiceClock.reset();
    routineTimer.reset();
    feedback_block_practiceMaxDurationReached = false;
    // update component parameters for each repeat
    text_feedback_block_practice.setText(feedback_text);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('feedback_block_practice.started', globalClock.getTime());
    feedback_block_practiceMaxDuration = null
    // keep track of which components have finished
    feedback_block_practiceComponents = [];
    feedback_block_practiceComponents.push(text_feedback_block_practice);
    feedback_block_practiceComponents.push(text_feedback_note_practice);
    feedback_block_practiceComponents.push(key_resp);
    
    for (const thisComponent of feedback_block_practiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_block_practiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_block_practice' ---
    // get current time
    t = feedback_block_practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_feedback_block_practice* updates
    if (t >= 0.0 && text_feedback_block_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_feedback_block_practice.tStart = t;  // (not accounting for frame time here)
      text_feedback_block_practice.frameNStart = frameN;  // exact frame index
      
      text_feedback_block_practice.setAutoDraw(true);
    }
    
    
    // *text_feedback_note_practice* updates
    if (t >= 0.0 && text_feedback_note_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_feedback_note_practice.tStart = t;  // (not accounting for frame time here)
      text_feedback_note_practice.frameNStart = frameN;  // exact frame index
      
      text_feedback_note_practice.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_block_practiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedback_block_practiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_block_practice' ---
    for (const thisComponent of feedback_block_practiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_block_practice.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "feedback_block_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var continue_checkMaxDurationReached;
var _key_resp_continue_check_allKeys;
var continue_checkMaxDuration;
var continue_checkComponents;
function continue_checkRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'continue_check' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    continue_checkClock.reset();
    routineTimer.reset();
    continue_checkMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_continue_check.keys = undefined;
    key_resp_continue_check.rt = undefined;
    _key_resp_continue_check_allKeys = [];
    // Run 'Begin Routine' code from code_continue_check
    loop_practice.finished = false;
    
    psychoJS.experiment.addData('continue_check.started', globalClock.getTime());
    continue_checkMaxDuration = null
    // keep track of which components have finished
    continue_checkComponents = [];
    continue_checkComponents.push(image_continue_check);
    continue_checkComponents.push(key_resp_continue_check);
    
    for (const thisComponent of continue_checkComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function continue_checkRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'continue_check' ---
    // get current time
    t = continue_checkClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_continue_check* updates
    if (t >= 0.0 && image_continue_check.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_continue_check.tStart = t;  // (not accounting for frame time here)
      image_continue_check.frameNStart = frameN;  // exact frame index
      
      image_continue_check.setAutoDraw(true);
    }
    
    
    // *key_resp_continue_check* updates
    if (t >= 0.0 && key_resp_continue_check.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_continue_check.tStart = t;  // (not accounting for frame time here)
      key_resp_continue_check.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_continue_check.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_continue_check.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_continue_check.clearEvents(); });
    }
    
    if (key_resp_continue_check.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_continue_check.getKeys({keyList: ['space', 'Q', 'q'], waitRelease: false});
      _key_resp_continue_check_allKeys = _key_resp_continue_check_allKeys.concat(theseKeys);
      if (_key_resp_continue_check_allKeys.length > 0) {
        key_resp_continue_check.keys = _key_resp_continue_check_allKeys[_key_resp_continue_check_allKeys.length - 1].name;  // just the last key pressed
        key_resp_continue_check.rt = _key_resp_continue_check_allKeys[_key_resp_continue_check_allKeys.length - 1].rt;
        key_resp_continue_check.duration = _key_resp_continue_check_allKeys[_key_resp_continue_check_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of continue_checkComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function continue_checkRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'continue_check' ---
    for (const thisComponent of continue_checkComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('continue_check.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_continue_check.corr, level);
    }
    psychoJS.experiment.addData('key_resp_continue_check.keys', key_resp_continue_check.keys);
    if (typeof key_resp_continue_check.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_continue_check.rt', key_resp_continue_check.rt);
        psychoJS.experiment.addData('key_resp_continue_check.duration', key_resp_continue_check.duration);
        routineTimer.reset();
        }
    
    key_resp_continue_check.stop();
    // Run 'End Routine' code from code_continue_check
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (_pj.in_es6("Q", key_resp_continue_check.keys)) {
        loop_practice.finished = false;
    } else {
        if (_pj.in_es6("space", key_resp_continue_check.keys)) {
            loop_practice.finished = true;
        }
    }
    
    // the Routine "continue_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var primary_task_welcomeMaxDurationReached;
var _key_resp_primary_welcome_allKeys;
var primary_task_welcomeMaxDuration;
var primary_task_welcomeComponents;
function primary_task_welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'primary_task_welcome' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    primary_task_welcomeClock.reset();
    routineTimer.reset();
    primary_task_welcomeMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_primary_welcome.keys = undefined;
    key_resp_primary_welcome.rt = undefined;
    _key_resp_primary_welcome_allKeys = [];
    psychoJS.experiment.addData('primary_task_welcome.started', globalClock.getTime());
    primary_task_welcomeMaxDuration = null
    // keep track of which components have finished
    primary_task_welcomeComponents = [];
    primary_task_welcomeComponents.push(image_primary_welcome);
    primary_task_welcomeComponents.push(key_resp_primary_welcome);
    
    for (const thisComponent of primary_task_welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function primary_task_welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'primary_task_welcome' ---
    // get current time
    t = primary_task_welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_primary_welcome* updates
    if (t >= 0.0 && image_primary_welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_primary_welcome.tStart = t;  // (not accounting for frame time here)
      image_primary_welcome.frameNStart = frameN;  // exact frame index
      
      image_primary_welcome.setAutoDraw(true);
    }
    
    
    // *key_resp_primary_welcome* updates
    if (t >= 0.0 && key_resp_primary_welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_primary_welcome.tStart = t;  // (not accounting for frame time here)
      key_resp_primary_welcome.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_primary_welcome.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_primary_welcome.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_primary_welcome.clearEvents(); });
    }
    
    if (key_resp_primary_welcome.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_primary_welcome.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_primary_welcome_allKeys = _key_resp_primary_welcome_allKeys.concat(theseKeys);
      if (_key_resp_primary_welcome_allKeys.length > 0) {
        key_resp_primary_welcome.keys = _key_resp_primary_welcome_allKeys[_key_resp_primary_welcome_allKeys.length - 1].name;  // just the last key pressed
        key_resp_primary_welcome.rt = _key_resp_primary_welcome_allKeys[_key_resp_primary_welcome_allKeys.length - 1].rt;
        key_resp_primary_welcome.duration = _key_resp_primary_welcome_allKeys[_key_resp_primary_welcome_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of primary_task_welcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function primary_task_welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'primary_task_welcome' ---
    for (const thisComponent of primary_task_welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('primary_task_welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_primary_welcome.corr, level);
    }
    psychoJS.experiment.addData('key_resp_primary_welcome.keys', key_resp_primary_welcome.keys);
    if (typeof key_resp_primary_welcome.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_primary_welcome.rt', key_resp_primary_welcome.rt);
        psychoJS.experiment.addData('key_resp_primary_welcome.duration', key_resp_primary_welcome.duration);
        routineTimer.reset();
        }
    
    key_resp_primary_welcome.stop();
    // the Routine "primary_task_welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var blockMaxDurationReached;
var _key_resp_block_allKeys;
var blockMaxDuration;
var blockComponents;
function blockRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'block' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    blockClock.reset();
    routineTimer.reset();
    blockMaxDurationReached = false;
    // update component parameters for each repeat
    image_block.setImage(stimulus);
    key_resp_block.keys = undefined;
    key_resp_block.rt = undefined;
    _key_resp_block_allKeys = [];
    psychoJS.experiment.addData('block.started', globalClock.getTime());
    blockMaxDuration = null
    // keep track of which components have finished
    blockComponents = [];
    blockComponents.push(image_block);
    blockComponents.push(key_resp_block);
    
    for (const thisComponent of blockComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function blockRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'block' ---
    // get current time
    t = blockClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_block* updates
    if (t >= 0.0 && image_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_block.tStart = t;  // (not accounting for frame time here)
      image_block.frameNStart = frameN;  // exact frame index
      
      image_block.setAutoDraw(true);
    }
    
    
    // *key_resp_block* updates
    if (t >= 0.0 && key_resp_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_block.tStart = t;  // (not accounting for frame time here)
      key_resp_block.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_block.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_block.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_block.clearEvents(); });
    }
    
    if (key_resp_block.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_block.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_block_allKeys = _key_resp_block_allKeys.concat(theseKeys);
      if (_key_resp_block_allKeys.length > 0) {
        key_resp_block.keys = _key_resp_block_allKeys[_key_resp_block_allKeys.length - 1].name;  // just the last key pressed
        key_resp_block.rt = _key_resp_block_allKeys[_key_resp_block_allKeys.length - 1].rt;
        key_resp_block.duration = _key_resp_block_allKeys[_key_resp_block_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blockComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blockRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'block' ---
    for (const thisComponent of blockComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('block.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_block.corr, level);
    }
    psychoJS.experiment.addData('key_resp_block.keys', key_resp_block.keys);
    if (typeof key_resp_block.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_block.rt', key_resp_block.rt);
        psychoJS.experiment.addData('key_resp_block.duration', key_resp_block.duration);
        routineTimer.reset();
        }
    
    key_resp_block.stop();
    // the Routine "block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var answer_blockMaxDurationReached;
var answer_blockMaxDuration;
var answer_blockComponents;
function answer_blockRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'answer_block' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    answer_blockClock.reset();
    routineTimer.reset();
    answer_blockMaxDurationReached = false;
    // update component parameters for each repeat
    textbox_answer_block.setText('');
    textbox_answer_block.refresh();
    // setup some python lists for storing info about the mouse_answer_block
    // current position of the mouse:
    mouse_answer_block.x = [];
    mouse_answer_block.y = [];
    mouse_answer_block.leftButton = [];
    mouse_answer_block.midButton = [];
    mouse_answer_block.rightButton = [];
    mouse_answer_block.time = [];
    mouse_answer_block.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from code_answer_block
    psychoJS.window.mouseVisible = true;
    
    psychoJS.experiment.addData('answer_block.started', globalClock.getTime());
    answer_blockMaxDuration = null
    // keep track of which components have finished
    answer_blockComponents = [];
    answer_blockComponents.push(text_answer_block);
    answer_blockComponents.push(textbox_answer_block);
    answer_blockComponents.push(button_answer_block);
    answer_blockComponents.push(mouse_answer_block);
    
    for (const thisComponent of answer_blockComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function answer_blockRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'answer_block' ---
    // get current time
    t = answer_blockClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_answer_block* updates
    if (t >= 0.0 && text_answer_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_answer_block.tStart = t;  // (not accounting for frame time here)
      text_answer_block.frameNStart = frameN;  // exact frame index
      
      text_answer_block.setAutoDraw(true);
    }
    
    
    // *textbox_answer_block* updates
    if (t >= 0.0 && textbox_answer_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_answer_block.tStart = t;  // (not accounting for frame time here)
      textbox_answer_block.frameNStart = frameN;  // exact frame index
      
      textbox_answer_block.setAutoDraw(true);
    }
    
    
    // *button_answer_block* updates
    if (t >= 0.0 && button_answer_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_answer_block.tStart = t;  // (not accounting for frame time here)
      button_answer_block.frameNStart = frameN;  // exact frame index
      
      button_answer_block.setAutoDraw(true);
    }
    
    // *mouse_answer_block* updates
    if (t >= 0.0 && mouse_answer_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_answer_block.tStart = t;  // (not accounting for frame time here)
      mouse_answer_block.frameNStart = frameN;  // exact frame index
      
      mouse_answer_block.status = PsychoJS.Status.STARTED;
      mouse_answer_block.mouseClock.reset();
      prevButtonState = mouse_answer_block.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_answer_block.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_answer_block.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_answer_block.clickableObjects = eval(button_answer_block)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_answer_block.clickableObjects)) {
              mouse_answer_block.clickableObjects = [mouse_answer_block.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_answer_block.clickableObjects) {
              if (obj.contains(mouse_answer_block)) {
                  gotValidClick = true;
                  mouse_answer_block.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              mouse_answer_block.clicked_name.push(null);
          }
          _mouseXYs = mouse_answer_block.getPos();
          mouse_answer_block.x.push(_mouseXYs[0]);
          mouse_answer_block.y.push(_mouseXYs[1]);
          mouse_answer_block.leftButton.push(_mouseButtons[0]);
          mouse_answer_block.midButton.push(_mouseButtons[1]);
          mouse_answer_block.rightButton.push(_mouseButtons[2]);
          mouse_answer_block.time.push(mouse_answer_block.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // Run 'Each Frame' code from code_answer_block
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    allowed_chars = "0123456789";
    text = textbox_answer_block.text;
    filtered_text = "";
    for (var i, _pj_c = 0, _pj_a = util.range(text.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        if (_pj.in_es6(text[i], allowed_chars)) {
            filtered_text += text[i];
        }
        if ((filtered_text.length >= 3)) {
            break;
        }
    }
    textbox_answer_block.setText(filtered_text);
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of answer_blockComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var correct_answer_primary_current;
function answer_blockRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'answer_block' ---
    for (const thisComponent of answer_blockComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('answer_block.stopped', globalClock.getTime());
    psychoJS.experiment.addData('textbox_answer_block.text',textbox_answer_block.text)
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_answer_block.x', mouse_answer_block.x);
    psychoJS.experiment.addData('mouse_answer_block.y', mouse_answer_block.y);
    psychoJS.experiment.addData('mouse_answer_block.leftButton', mouse_answer_block.leftButton);
    psychoJS.experiment.addData('mouse_answer_block.midButton', mouse_answer_block.midButton);
    psychoJS.experiment.addData('mouse_answer_block.rightButton', mouse_answer_block.rightButton);
    psychoJS.experiment.addData('mouse_answer_block.time', mouse_answer_block.time);
    psychoJS.experiment.addData('mouse_answer_block.clicked_name', mouse_answer_block.clicked_name);
    
    // Run 'End Routine' code from code_answer_block
    correct_answer_primary_current = correct_answer;
    correct_answer_primary_current = correct_answer_primary_current.toString();
    participant_response = textbox_answer_block.text.strip();
    num_correct = util.sum(function () {
        var _pj_a = [], _pj_b = util.range(3);
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var i = _pj_b[_pj_c];
            if ((participant_response[i] === correct_answer_primary_current[i])) {
                _pj_a.push(1);
            }
        }
        return _pj_a;
    }
    .call(this));
    psychoJS.experiment.addData("num_correct", num_correct);
    feedback_text_primary = `你答对了${num_correct}种表情的面孔数目。`;
    psychoJS.window.mouseVisible = false;
    
    // the Routine "answer_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_blockMaxDurationReached;
var _key_resp_feedback_block_allKeys;
var feedback_blockMaxDuration;
var feedback_blockComponents;
function feedback_blockRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_block' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_blockClock.reset();
    routineTimer.reset();
    feedback_blockMaxDurationReached = false;
    // update component parameters for each repeat
    text_feedback_block.setText(feedback_text_primary);
    key_resp_feedback_block.keys = undefined;
    key_resp_feedback_block.rt = undefined;
    _key_resp_feedback_block_allKeys = [];
    psychoJS.experiment.addData('feedback_block.started', globalClock.getTime());
    feedback_blockMaxDuration = null
    // keep track of which components have finished
    feedback_blockComponents = [];
    feedback_blockComponents.push(text_feedback_block);
    feedback_blockComponents.push(text_feedback_block_note);
    feedback_blockComponents.push(key_resp_feedback_block);
    
    for (const thisComponent of feedback_blockComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_blockRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_block' ---
    // get current time
    t = feedback_blockClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_feedback_block* updates
    if (t >= 0.0 && text_feedback_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_feedback_block.tStart = t;  // (not accounting for frame time here)
      text_feedback_block.frameNStart = frameN;  // exact frame index
      
      text_feedback_block.setAutoDraw(true);
    }
    
    
    // *text_feedback_block_note* updates
    if (t >= 0.0 && text_feedback_block_note.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_feedback_block_note.tStart = t;  // (not accounting for frame time here)
      text_feedback_block_note.frameNStart = frameN;  // exact frame index
      
      text_feedback_block_note.setAutoDraw(true);
    }
    
    
    // *key_resp_feedback_block* updates
    if (t >= 0.0 && key_resp_feedback_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_feedback_block.tStart = t;  // (not accounting for frame time here)
      key_resp_feedback_block.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_feedback_block.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_feedback_block.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_feedback_block.clearEvents(); });
    }
    
    if (key_resp_feedback_block.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_feedback_block.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_feedback_block_allKeys = _key_resp_feedback_block_allKeys.concat(theseKeys);
      if (_key_resp_feedback_block_allKeys.length > 0) {
        key_resp_feedback_block.keys = _key_resp_feedback_block_allKeys[_key_resp_feedback_block_allKeys.length - 1].name;  // just the last key pressed
        key_resp_feedback_block.rt = _key_resp_feedback_block_allKeys[_key_resp_feedback_block_allKeys.length - 1].rt;
        key_resp_feedback_block.duration = _key_resp_feedback_block_allKeys[_key_resp_feedback_block_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_blockComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedback_blockRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_block' ---
    for (const thisComponent of feedback_blockComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_block.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_feedback_block.corr, level);
    }
    psychoJS.experiment.addData('key_resp_feedback_block.keys', key_resp_feedback_block.keys);
    if (typeof key_resp_feedback_block.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_feedback_block.rt', key_resp_feedback_block.rt);
        psychoJS.experiment.addData('key_resp_feedback_block.duration', key_resp_feedback_block.duration);
        routineTimer.reset();
        }
    
    key_resp_feedback_block.stop();
    // the Routine "feedback_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var continue_check_blockMaxDurationReached;
var _key_resp_contiue_check_block_allKeys;
var continue_check_blockMaxDuration;
var continue_check_blockComponents;
function continue_check_blockRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'continue_check_block' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    continue_check_blockClock.reset();
    routineTimer.reset();
    continue_check_blockMaxDurationReached = false;
    // update component parameters for each repeat
    text_continue_check_block.setText('');
    // Run 'Begin Routine' code from code_progress_report
    block_counter += 1;
    if ((block_counter === 6)) {
        text_continue_check_block.text = "\u60a8\u5df2\u7ecf\u5b8c\u6210\u4e86\u56db\u5206\u4e4b\u4e00\u3002";
    } else {
        if ((block_counter === 13)) {
            text_continue_check_block.text = "\u60a8\u5df2\u7ecf\u5b8c\u6210\u4e86\u4e00\u534a\u3002";
        } else {
            if ((block_counter === 19)) {
                text_continue_check_block.text = "\u60a8\u5df2\u7ecf\u5b8c\u6210\u4e86\u56db\u5206\u4e4b\u4e09\u3002";
            } else {
                text_continue_check_block.text = "\u5982\u679c\u60a8\u89c9\u5f97\u7d2f\u4e86\uff0c\u53ef\u4ee5\u4f11\u606f\u4e00\u4f1a\u513f\u3002";
            }
        }
    }
    
    key_resp_contiue_check_block.keys = undefined;
    key_resp_contiue_check_block.rt = undefined;
    _key_resp_contiue_check_block_allKeys = [];
    psychoJS.experiment.addData('continue_check_block.started', globalClock.getTime());
    continue_check_blockMaxDuration = null
    // keep track of which components have finished
    continue_check_blockComponents = [];
    continue_check_blockComponents.push(text_continue_check_block);
    continue_check_blockComponents.push(text_continue_prompt);
    continue_check_blockComponents.push(key_resp_contiue_check_block);
    
    for (const thisComponent of continue_check_blockComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function continue_check_blockRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'continue_check_block' ---
    // get current time
    t = continue_check_blockClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_continue_check_block* updates
    if (t >= 0.0 && text_continue_check_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_continue_check_block.tStart = t;  // (not accounting for frame time here)
      text_continue_check_block.frameNStart = frameN;  // exact frame index
      
      text_continue_check_block.setAutoDraw(true);
    }
    
    
    // *text_continue_prompt* updates
    if (t >= 0.0 && text_continue_prompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_continue_prompt.tStart = t;  // (not accounting for frame time here)
      text_continue_prompt.frameNStart = frameN;  // exact frame index
      
      text_continue_prompt.setAutoDraw(true);
    }
    
    
    // *key_resp_contiue_check_block* updates
    if (t >= 0.0 && key_resp_contiue_check_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_contiue_check_block.tStart = t;  // (not accounting for frame time here)
      key_resp_contiue_check_block.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_contiue_check_block.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_contiue_check_block.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_contiue_check_block.clearEvents(); });
    }
    
    if (key_resp_contiue_check_block.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_contiue_check_block.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_contiue_check_block_allKeys = _key_resp_contiue_check_block_allKeys.concat(theseKeys);
      if (_key_resp_contiue_check_block_allKeys.length > 0) {
        key_resp_contiue_check_block.keys = _key_resp_contiue_check_block_allKeys[_key_resp_contiue_check_block_allKeys.length - 1].name;  // just the last key pressed
        key_resp_contiue_check_block.rt = _key_resp_contiue_check_block_allKeys[_key_resp_contiue_check_block_allKeys.length - 1].rt;
        key_resp_contiue_check_block.duration = _key_resp_contiue_check_block_allKeys[_key_resp_contiue_check_block_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of continue_check_blockComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function continue_check_blockRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'continue_check_block' ---
    for (const thisComponent of continue_check_blockComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('continue_check_block.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_contiue_check_block.corr, level);
    }
    psychoJS.experiment.addData('key_resp_contiue_check_block.keys', key_resp_contiue_check_block.keys);
    if (typeof key_resp_contiue_check_block.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_contiue_check_block.rt', key_resp_contiue_check_block.rt);
        psychoJS.experiment.addData('key_resp_contiue_check_block.duration', key_resp_contiue_check_block.duration);
        routineTimer.reset();
        }
    
    key_resp_contiue_check_block.stop();
    // the Routine "continue_check_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var goodbyeMaxDurationReached;
var _key_resp_goodbye_allKeys;
var goodbyeMaxDuration;
var goodbyeComponents;
function goodbyeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'goodbye' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    goodbyeClock.reset();
    routineTimer.reset();
    goodbyeMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_goodbye.keys = undefined;
    key_resp_goodbye.rt = undefined;
    _key_resp_goodbye_allKeys = [];
    psychoJS.experiment.addData('goodbye.started', globalClock.getTime());
    goodbyeMaxDuration = null
    // keep track of which components have finished
    goodbyeComponents = [];
    goodbyeComponents.push(text_goodbye);
    goodbyeComponents.push(key_resp_goodbye);
    
    for (const thisComponent of goodbyeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function goodbyeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'goodbye' ---
    // get current time
    t = goodbyeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_goodbye* updates
    if (t >= 0.0 && text_goodbye.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_goodbye.tStart = t;  // (not accounting for frame time here)
      text_goodbye.frameNStart = frameN;  // exact frame index
      
      text_goodbye.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_goodbye.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_goodbye.setAutoDraw(false);
    }
    
    
    // *key_resp_goodbye* updates
    if (t >= 0.0 && key_resp_goodbye.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_goodbye.tStart = t;  // (not accounting for frame time here)
      key_resp_goodbye.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_goodbye.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_goodbye.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_goodbye.clearEvents(); });
    }
    
    if (key_resp_goodbye.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_goodbye.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_goodbye_allKeys = _key_resp_goodbye_allKeys.concat(theseKeys);
      if (_key_resp_goodbye_allKeys.length > 0) {
        key_resp_goodbye.keys = _key_resp_goodbye_allKeys[_key_resp_goodbye_allKeys.length - 1].name;  // just the last key pressed
        key_resp_goodbye.rt = _key_resp_goodbye_allKeys[_key_resp_goodbye_allKeys.length - 1].rt;
        key_resp_goodbye.duration = _key_resp_goodbye_allKeys[_key_resp_goodbye_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of goodbyeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function goodbyeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'goodbye' ---
    for (const thisComponent of goodbyeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('goodbye.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_goodbye.corr, level);
    }
    psychoJS.experiment.addData('key_resp_goodbye.keys', key_resp_goodbye.keys);
    if (typeof key_resp_goodbye.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_goodbye.rt', key_resp_goodbye.rt);
        psychoJS.experiment.addData('key_resp_goodbye.duration', key_resp_goodbye.duration);
        routineTimer.reset();
        }
    
    key_resp_goodbye.stop();
    // the Routine "goodbye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
