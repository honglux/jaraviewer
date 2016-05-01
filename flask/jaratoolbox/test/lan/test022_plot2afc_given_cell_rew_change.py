'''
Given the Tetrode, Plots ephys data during behavior (reward_change_freq_discrim paradigm), data split according to the type of block in behavior (more_left or more_right) and the choice (left or right). only plotting correct trials.
Try using loaders from celldatabase
Implemented: using santiago's methods to remove missing trials from behavior when ephys has skipped trials. -LG20160309
Lan Guo Feb-March 2016
'''
from jaratoolbox.test.nick.database import dataloader
from jaratoolbox import settings
from jaratoolbox import loadopenephys
from jaratoolbox import loadbehavior
from jaratoolbox import behavioranalysis
from jaratoolbox import celldatabase
from jaratoolbox import ephyscore
from jaratoolbox import behavioranalysis
from jaratoolbox import spikesanalysis
from jaratoolbox import extraplots
from jaratoolbox import spikesorting
import os
import numpy as np
import matplotlib.pyplot as plt

SAMPLING_RATE=30000.0
soundTriggerChannel = 0 # channel 0 is the sound presentation, 1 is the trial
binWidth = 0.010 # Size of each bin in histogram in seconds

#timeRange = [-0.2,0.8] # In seconds. Time range for rastor plot to plot spikes (around some event onset as 0)
#timeRange = [-0.25,1.0]
timeRange = [-0.4,1.2]


#experimenter='billy'
#experimenter='lan'


def load_ephys_per_cell(oneCell):
    '''
    Load spike and event data from one cell given a CellInfo object (from celldatabase)
    '''
    ###0301 should TRY spkData = ephyscore.CellData(oneCell)
    ephysDir = settings.EPHYS_PATH
    ephysData=ephyscore.CellData(oneCell) #ephyscore's CellData object uses loadopenephys.DataSpikes method, gets back a DataSpikes object that is stored in CellData.spikes, with fields: nSpikes, samples, timestamps(ephyscore already divides this by sampling rate),gain,samplingRate.
    spikeData=ephysData.spikes #so this is the DataSpikes object from loadopenephys
    spikeTimestamps = spikeData.timestamps #ephyscore already divided this by sampling rate so unit is in seconds
    waveforms = spikeData.samples.astype(float)-2**15 #This is specific to open Ephys
    waveforms = (1000.0/spikeData.gain[0,0]) * waveforms #converting to microvolt,specific to open Ephys

    fullEventFilename=os.path.join(ephysDir,oneCell.animalName,oneCell.ephysSession,'all_channels.events')
    eventData=loadopenephys.Events(fullEventFilename)
    
    eventData.timestamps = np.array(eventData.timestamps)/SAMPLING_RATE
    eventOnsetTimes=np.array(eventData.timestamps) #all events not just soundonset
    return (spikeTimestamps,waveforms,eventOnsetTimes,eventData)  

def plot_summary_per_cell(oneCell):
    #can plot wave-from, ISI, projections...
    pass

def load_tuning_behav_per_cell(oneCell):
    pass

def load_behav_per_cell(oneCell):
    '''
    Load behavioral data from one cell given a CellInfo object (from celldatabase)
    '''
    behavSession=oneCell.behavSession
    behavDir=settings.BEHAVIOR_PATH
    fullBehavName=oneCell.animalName+'_2afc_'+behavSession+'.h5'
    if oneCell.animalName=='adap015' or oneCell.animalName=='adap013' or oneCell.animalName=='adap017':
        experimenter = 'billy'
    else:
        experimenter = 'lan'
    behavFullFilePath = os.path.join(behavDir,experimenter,oneCell.animalName,fullBehavName)
    loadingClass = loadbehavior.FlexCategBehaviorData
    bdata = loadingClass(behavFullFilePath,readmode='full')
    return bdata

def plot_rew_change_per_cell(oneCell,trialLimit=[],alignment='sound'):
    '''
    Plots raster and PSTH for one cell during reward_change_freq_dis task, split by block; alignment parameter should be set to either 'sound', 'center-out', or 'side-in'.
    '''    
    bdata = load_behav_per_cell(oneCell)
    (spikeTimestamps,waveforms,eventOnsetTimes,eventData) = load_ephys_per_cell(oneCell)

    # -- Check to see if ephys has skipped trials, if so remove trials from behav data 
    soundOnsetEvents = (eventData.eventID==1) & (eventData.eventChannel==soundTriggerChannel)
    soundOnsetTimeEphys = eventOnsetTimes[soundOnsetEvents]
    soundOnsetTimeBehav = bdata['timeTarget']

    # Find missing trials
    missingTrials = behavioranalysis.find_missing_trials(soundOnsetTimeEphys,soundOnsetTimeBehav)
    # Remove missing trials
    bdata.remove_trials(missingTrials)

    currentBlock = bdata['currentBlock']
    blockTypes = [bdata.labels['currentBlock']['same_reward'],bdata.labels['currentBlock']['more_left'],bdata.labels['currentBlock']['more_right']]
    #blockLabels = ['more_left', 'more_right']
    if(not len(trialLimit)):
        validTrials = np.ones(len(currentBlock),dtype=bool)
    else:
        validTrials = np.zeros(len(currentBlock),dtype=bool)
        validTrials[trialLimit[0]:trialLimit[1]] = 1

    trialsEachType = behavioranalysis.find_trials_each_type(currentBlock,blockTypes)
    
        
    if alignment == 'sound':
        soundOnsetEvents = (eventData.eventID==1) & (eventData.eventChannel==soundTriggerChannel)
        EventOnsetTimes = eventOnsetTimes[soundOnsetEvents]
    elif alignment == 'center-out':
        soundOnsetEvents = (eventData.eventID==1) & (eventData.eventChannel==soundTriggerChannel)
        EventOnsetTimes = eventOnsetTimes[soundOnsetEvents]
        diffTimes=bdata['timeCenterOut']-bdata['timeTarget']
        EventOnsetTimes+=diffTimes
    elif alignment == 'side-in':
        soundOnsetEvents = (eventData.eventID==1) & (eventData.eventChannel==soundTriggerChannel)
        EventOnsetTimes = eventOnsetTimes[soundOnsetEvents]
        diffTimes=bdata['timeSideIn']-bdata['timeTarget']
        EventOnsetTimes+=diffTimes

    freqEachTrial = bdata['targetFrequency']
    possibleFreq = np.unique(freqEachTrial)
    
    rightward = bdata['choice']==bdata.labels['choice']['right']
    leftward = bdata['choice']==bdata.labels['choice']['left']
    invalid = bdata['outcome']==bdata.labels['outcome']['invalid']
        
    correct = bdata['outcome']==bdata.labels['outcome']['correct'] 
    incorrect = bdata['outcome']==bdata.labels['outcome']['error']  

    ######Split left and right trials into correct and  incorrect categories to look at error trials#########
    rightcorrect = rightward&correct&validTrials
    leftcorrect = leftward&correct&validTrials
    #righterror = rightward&incorrect&validTrials
    #lefterror = leftward&incorrect&validTrials

    rightcorrectBlockSameReward = rightcorrect&trialsEachType[:,0]
    rightcorrectBlockMoreLeft = rightcorrect&trialsEachType[:,1] 
    rightcorrectBlockMoreRight = rightcorrect&trialsEachType[:,2]
    leftcorrectBlockSameReward = leftcorrect&trialsEachType[:,0]
    leftcorrectBlockMoreLeft = leftcorrect&trialsEachType[:,1]
    leftcorrectBlockMoreRight = leftcorrect&trialsEachType[:,2]

    trialsEachCond = np.c_[leftcorrectBlockMoreLeft,rightcorrectBlockMoreLeft,leftcorrectBlockMoreRight,rightcorrectBlockMoreRight,leftcorrectBlockSameReward,rightcorrectBlockSameReward] 


    colorEachCond = ['g','r','m','b','y','darkgray']
    #trialsEachCond = np.c_[invalid,leftcorrect,rightcorrect,lefterror,righterror] 
    #colorEachCond = ['0.75','g','r','b','m'] 

    (spikeTimesFromEventOnset,trialIndexForEachSpike,indexLimitsEachTrial) = \
spikesanalysis.eventlocked_spiketimes(spikeTimestamps,EventOnsetTimes,timeRange)
    
    ###########Plot raster and PSTH#################
    plt.figure()
    ax1 = plt.subplot2grid((8,5), (0, 0), rowspan=4,colspan=5)
    extraplots.raster_plot(spikeTimesFromEventOnset,indexLimitsEachTrial,timeRange,trialsEachCond=trialsEachCond,colorEachCond=colorEachCond,fillWidth=None,labels=None)
    plt.ylabel('Trials')
    plt.xlim(timeRange)

    plt.title('{0}_{1}_TT{2}_c{3}_{4}'.format(oneCell.animalName,oneCell.behavSession,oneCell.tetrode,oneCell.cluster,alignment))

    timeVec = np.arange(timeRange[0],timeRange[-1],binWidth)
    spikeCountMat = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnset,indexLimitsEachTrial,timeVec)
    smoothWinSize = 3
    ax2 = plt.subplot2grid((8,5), (4, 0),colspan=5,rowspan=2,sharex=ax1)
    extraplots.plot_psth(spikeCountMat/binWidth,smoothWinSize,timeVec,trialsEachCond=trialsEachCond,colorEachCond=colorEachCond,linestyle=None,linewidth=3,downsamplefactor=1)
    plt.xlabel('Time from {0} onset (s)'.format(alignment))
    plt.ylabel('Firing rate (spk/sec)')
   
    # -- Plot ISI histogram --
    plt.subplot2grid((8,5), (6,0), rowspan=1, colspan=2)
    spikesorting.plot_isi_loghist(spikeTimestamps)
    plt.ylabel('c%d'%oneCell.cluster,rotation=0,va='center',ha='center')
    plt.xlabel('')

    # -- Plot waveforms --
    plt.subplot2grid((8,5), (7,0), rowspan=1, colspan=3)
    spikesorting.plot_waveforms(waveforms)

    # -- Plot projections --
    plt.subplot2grid((8,5), (6,2), rowspan=1, colspan=3)
    spikesorting.plot_projections(waveforms)

    # -- Plot events in time --
    plt.subplot2grid((8,5), (7,3), rowspan=1, colspan=2)
    spikesorting.plot_events_in_time(spikeTimestamps)

    plt.subplots_adjust(wspace = 0.7)
    
    #plt.show()
    #fig_path = 
    #fig_name = 'TT{0}Cluster{1}{2}.png'.format(tetrode, cluster, '_2afc plot_each_type')
    #full_fig_path = os.path.join(fig_path, fig_name)
    #print full_fig_path
    plt.gcf().set_size_inches((8.5,11))
    #plt.savefig(full_fig_path, format = 'png')


def plot_rew_change_per_cell_per_freq(oneCell,trialLimit=[],alignment='sound'):
    '''
    Plots raster and PSTH for one cell during reward_change_freq_dis task, split by block; alignment parameter should be set to either 'sound', 'center-out', or 'side-in'.
    '''    
    bdata = load_behav_per_cell(oneCell)
    (spikeTimestamps,waveforms,eventOnsetTimes,eventData) = load_ephys_per_cell(oneCell)

    # -- Check to see if ephys has skipped trials, if so remove trials from behav data 
    soundOnsetEvents = (eventData.eventID==1) & (eventData.eventChannel==soundTriggerChannel)
    soundOnsetTimeEphys = eventOnsetTimes[soundOnsetEvents]
    soundOnsetTimeBehav = bdata['timeTarget']

    # Find missing trials
    missingTrials = behavioranalysis.find_missing_trials(soundOnsetTimeEphys,soundOnsetTimeBehav)
    # Remove missing trials
    bdata.remove_trials(missingTrials)

    currentBlock = bdata['currentBlock']
    blockTypes = [bdata.labels['currentBlock']['more_left'],bdata.labels['currentBlock']['more_right']]
    #blockLabels = ['more_left', 'more_right']
    if(not len(trialLimit)):
        validTrials = np.ones(len(currentBlock),dtype=bool)
    else:
        validTrials = np.zeros(len(currentBlock),dtype=bool)
        validTrials[trialLimit[0]:trialLimit[1]] = 1

    trialsEachType = behavioranalysis.find_trials_each_type(currentBlock,blockTypes)
    
        
    if alignment == 'sound':
        soundOnsetEvents = (eventData.eventID==1) & (eventData.eventChannel==soundTriggerChannel)
        EventOnsetTimes = eventOnsetTimes[soundOnsetEvents]
    elif alignment == 'center-out':
        soundOnsetEvents = (eventData.eventID==1) & (eventData.eventChannel==soundTriggerChannel)
        EventOnsetTimes = eventOnsetTimes[soundOnsetEvents]
        diffTimes=bdata['timeCenterOut']-bdata['timeTarget']
        EventOnsetTimes+=diffTimes
    elif alignment == 'side-in':
        soundOnsetEvents = (eventData.eventID==1) & (eventData.eventChannel==soundTriggerChannel)
        EventOnsetTimes = eventOnsetTimes[soundOnsetEvents]
        diffTimes=bdata['timeSideIn']-bdata['timeTarget']
        EventOnsetTimes+=diffTimes

    freqEachTrial = bdata['targetFrequency']
    possibleFreq = sorted(np.unique(freqEachTrial))
    print possibleFreq
    ######Make a plot for each frequency presented######
    for ind,freq in enumerate(possibleFreq):
        trialsThisFreq= freqEachTrial==freq

        #rightwardThisFreq = bdata['choice']==bdata.labels['choice']['right']&trialsThisFreq
        #leftwardThisFreq = bdata['choice']==bdata.labels['choice']['left']&trialsThisFreq
        #invalid = bdata['outcome']==bdata.labels['outcome']['invalid']

        correct = bdata['outcome']==bdata.labels['outcome']['correct'] 
        correctThisFreq = correct&trialsThisFreq
        incorrect = bdata['outcome']==bdata.labels['outcome']['error']  

        ######Split left and right trials into correct and  incorrect categories to look at error trials#########
        #rightcorrectThisFreq = rightward&correct&validTrials
        #leftcorrectThisFreq = leftward&correct&validTrials
        #righterror = rightward&incorrect&validTrials
        #lefterror = leftward&incorrect&validTrials

        #rightcorrectBlockMoreLeft = rightcorrect&trialsEachType[:,0] 
        #rightcorrectBlockMoreRight = rightcorrect&trialsEachType[:,1]
        #leftcorrectBlockMoreLeft = leftcorrect&trialsEachType[:,0]
        #leftcorrectBlockMoreRight = leftcorrect&trialsEachType[:,1]

        correctMoreLeftThisFreq = correctThisFreq&trialsEachType[:,0]
        correctMoreRightThisFreq = correctThisFreq&trialsEachType[:,1]
        print freq, len(np.nonzero(correctMoreLeftThisFreq)[0]),len(np.nonzero(correctMoreRightThisFreq)[0])
        if ind==0:
            trialsEachCond = np.c_[correctMoreLeftThisFreq,correctMoreRightThisFreq]
        else:
            trialsEachCond = np.c_[trialsEachCond,correctMoreLeftThisFreq,correctMoreRightThisFreq] 


    colorEachCond = ['g','r','m','b','y','darkgray']
#trialsEachCond = np.c_[invalid,leftcorrect,rightcorrect,lefterror,righterror] 
    #colorEachCond = ['0.75','g','r','b','m'] 

    (spikeTimesFromEventOnset,trialIndexForEachSpike,indexLimitsEachTrial) = \
spikesanalysis.eventlocked_spiketimes(spikeTimestamps,EventOnsetTimes,timeRange)

    ###########Plot raster and PSTH#################
    plt.figure()
    ax1 = plt.subplot2grid((8,5), (0, 0), rowspan=4,colspan=5)
    extraplots.raster_plot(spikeTimesFromEventOnset,indexLimitsEachTrial,timeRange,trialsEachCond=trialsEachCond,colorEachCond=colorEachCond,fillWidth=None,labels=None)
    plt.ylabel('Trials')
    plt.xlim(timeRange)

    plt.title('{0}_{1}_TT{2}_c{3}_{4}'.format(oneCell.animalName,oneCell.behavSession,oneCell.tetrode,oneCell.cluster,alignment))

    timeVec = np.arange(timeRange[0],timeRange[-1],binWidth)
    spikeCountMat = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnset,indexLimitsEachTrial,timeVec)
    smoothWinSize = 3
    ax2 = plt.subplot2grid((8,5), (4, 0),colspan=5,rowspan=2,sharex=ax1)
    extraplots.plot_psth(spikeCountMat/binWidth,smoothWinSize,timeVec,trialsEachCond=trialsEachCond,colorEachCond=colorEachCond,linestyle=None,linewidth=3,downsamplefactor=1)
    plt.xlabel('Time from {0} onset (s)'.format(alignment))
    plt.ylabel('Firing rate (spk/sec)')

    # -- Plot ISI histogram --
    plt.subplot2grid((8,5), (6,0), rowspan=1, colspan=2)
    spikesorting.plot_isi_loghist(spikeTimestamps)
    plt.ylabel('c%d'%oneCell.cluster,rotation=0,va='center',ha='center')
    plt.xlabel('')

    # -- Plot waveforms --
    plt.subplot2grid((8,5), (7,0), rowspan=1, colspan=3)
    spikesorting.plot_waveforms(waveforms)

    # -- Plot projections --
    plt.subplot2grid((8,5), (6,2), rowspan=1, colspan=3)
    spikesorting.plot_projections(waveforms)

    # -- Plot events in time --
    plt.subplot2grid((8,5), (7,3), rowspan=1, colspan=2)
    spikesorting.plot_events_in_time(spikeTimestamps)

    plt.subplots_adjust(wspace = 0.7)

    plt.show()
    #fig_path = 
    #fig_name = 'TT{0}Cluster{1}{2}.png'.format(tetrode, cluster, '_2afc plot_each_type')
    #full_fig_path = os.path.join(fig_path, fig_name)
    #print full_fig_path
    plt.gcf().set_size_inches((8.5,11))
    #plt.savefig(full_fig_path, format = 'png')



def plot_rew_change_byblock_per_cell(oneCell,trialLimit=[],alignment='sound',choiceSide='both'):
    '''
    Plots ephys data during behavior (reward_change_freq_discrim paradigm), data split according to the block in behavior and the choice (left or right). only plotting correct trials.
    oneCell is an CellInfo object as in celldatabase.
    'trialLimit' (e.g. [0, 600]) is the indecies of trials wish to be plotted.
    'choiceSide' is a string, either 'left' or 'right', to plot leftward and rightward trials, respectively. If not provided, will plot both sides.
    'alignment' selects which event to align spike data to, should be 'sound', 'center-out', or 'side-in'.
    '''
    
    SAMPLING_RATE=30000.0
    soundTriggerChannel = 0 # channel 0 is the sound presentation, 1 is the trial
    binWidth = 0.010 # Size of each bin in histogram in seconds

    #timeRange = [-0.2,0.8] # In seconds. Time range for rastor plot to plot spikes (around some event onset as 0)
    #timeRange = [-0.25,1.0]
    timeRange = [-0.4,1.2]
    
    bdata = load_behav_per_cell(oneCell)
    (spikeTimestamps,waveforms,eventOnsetTimes,eventData)=load_ephys_per_cell(oneCell)

    # -- Check to see if ephys has skipped trials, if so remove trials from behav data 
    soundOnsetEvents = (eventData.eventID==1) & (eventData.eventChannel==soundTriggerChannel)
    soundOnsetTimeEphys = eventOnsetTimes[soundOnsetEvents]
    soundOnsetTimeBehav = bdata['timeTarget']

    # Find missing trials
    missingTrials = behavioranalysis.find_missing_trials(soundOnsetTimeEphys,soundOnsetTimeBehav)
    # Remove missing trials
    bdata.remove_trials(missingTrials)
                
    currentBlock = bdata['currentBlock']
    
    if(not len(trialLimit)):
        validTrials = np.ones(len(currentBlock),dtype=bool)
    else:
        validTrials = np.zeros(len(currentBlock),dtype=bool)
        validTrials[trialLimit[0]:trialLimit[1]] = 1

    bdata.find_trials_each_block()
    trialsEachBlock = bdata.blocks['trialsEachBlock']
    #print trialsEachBlock
    nBlocks = bdata.blocks['nBlocks']

    #blockLabels = ['more_left', 'more_right']
    rightward = bdata['choice']==bdata.labels['choice']['right']
    leftward = bdata['choice']==bdata.labels['choice']['left']
    invalid = bdata['outcome']==bdata.labels['outcome']['invalid']
    correct = bdata['outcome']==bdata.labels['outcome']['correct'] 
    incorrect = bdata['outcome']==bdata.labels['outcome']['error'] 
    ######Split left and right trials into correct and  incorrect categories to look at error trials#########
    rightcorrect = rightward&correct&validTrials
    leftcorrect = leftward&correct&validTrials
    #righterror = rightward&incorrect&validTrials
    #lefterror = leftward&incorrect&validTrials
    colorEachCond=[]
    
    ####construct trialsEachCond and colorEachCond for ploting####
    for block in range(nBlocks):
        rightcorrectThisBlock = rightcorrect&trialsEachBlock[:,block]
        leftcorrectThisBlock = leftcorrect&trialsEachBlock[:,block]
        #trialTypeVec = leftcorrect*1+rightcorrect*2
        #trialTypePossibleValues = [1,2] #1 stands for left correct, 2 stands for right correct

        firstIndexThisBlock=np.nonzero(trialsEachBlock[:,block])[0][0]
        if currentBlock[firstIndexThisBlock]==bdata.labels['currentBlock']['more_left']:
            if choiceSide=='right':
                colorThisCond='r'
            elif choiceSide=='left':
                colorThisCond='g'
            elif choiceSide=='both':
                colorThisCond=['g','r']
        if currentBlock[firstIndexThisBlock]==bdata.labels['currentBlock']['more_right']:
            if choiceSide=='right':
                colorThisCond='b'
            elif choiceSide=='left':
                colorThisCond='m'
            elif choiceSide=='both':
                colorThisCond=['m','b']
        if currentBlock[firstIndexThisBlock]==bdata.labels['currentBlock']['same_reward']:
            if choiceSide=='right':
                colorThisCond='darkgray'
            elif choiceSide=='left':
                colorThisCond='y'
            elif choiceSide=='both':
                colorThisCond=['y','darkgray']

        #trialsEachTypeEachBlock = behavioranalysis.find_trials_each_type_each_block(trialTypeVec, trialTypePossibleValues,currentBlock,blockTypes)
        
        if block==0:
            #trialsEachCond=np.c_[leftcorrectThisBlock,rightcorrectThisBlock] 
            if choiceSide=='right':
                trialsEachCond=np.c_[rightcorrectThisBlock]
            elif choiceSide=='left':
                trialsEachCond=np.c_[leftcorrectThisBlock]              
            elif choiceSide=='both':
                trialsEachCond=np.c_[leftcorrectThisBlock,rightcorrectThisBlock]

        else:
            if choiceSide=='right':
                trialsEachCond=np.c_[trialsEachCond,rightcorrectThisBlock]
            elif choiceSide=='left':
                trialsEachCond=np.c_[trialsEachCond,leftcorrectThisBlock]              
            elif choiceSide=='both':
                trialsEachCond=np.c_[trialsEachCond,leftcorrectThisBlock,rightcorrectThisBlock]

        colorEachCond.append(colorThisCond)


    if alignment == 'sound':
        soundOnsetEvents = (eventData.eventID==1) & (eventData.eventChannel==soundTriggerChannel)
        EventOnsetTimes = eventOnsetTimes[soundOnsetEvents]
    elif alignment == 'center-out':
        soundOnsetEvents = (eventData.eventID==1) & (eventData.eventChannel==soundTriggerChannel)
        EventOnsetTimes = eventOnsetTimes[soundOnsetEvents]
        diffTimes=bdata['timeCenterOut']-bdata['timeTarget']
        EventOnsetTimes+=diffTimes
    elif alignment == 'side-in':
        soundOnsetEvents = (eventData.eventID==1) & (eventData.eventChannel==soundTriggerChannel)
        EventOnsetTimes = eventOnsetTimes[soundOnsetEvents]
        diffTimes=bdata['timeSideIn']-bdata['timeTarget']
        EventOnsetTimes+=diffTimes
            
    freqEachTrial = bdata['targetFrequency']
    possibleFreq = np.unique(freqEachTrial)
            
    (spikeTimesFromEventOnset,trialIndexForEachSpike,indexLimitsEachTrial) = \
    spikesanalysis.eventlocked_spiketimes(spikeTimestamps,EventOnsetTimes,timeRange)

    plt.figure()
    ###########Plot raster and PSTH#################
    ax1 =  plt.subplot2grid((3,1), (0, 0), rowspan=2)
    pRaster,hcond,zline =extraplots.raster_plot(spikeTimesFromEventOnset,indexLimitsEachTrial,timeRange,trialsEachCond=trialsEachCond,
                       colorEachCond=colorEachCond,fillWidth=None,labels=None)
    #plt.setp(pRaster, ms=0.8)
    plt.ylabel('Trials')
    plt.xlim(timeRange)
    fig_title='{0}_{1}_TT{2}_c{3}_{4}_{5}'.format(oneCell.animalName,oneCell.behavSession,oneCell.tetrode,oneCell.cluster,alignment,choiceSide)
    plt.title(fig_title)

    timeVec = np.arange(timeRange[0],timeRange[-1],binWidth)

    spikeCountMat = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnset,indexLimitsEachTrial,timeVec)
    smoothWinSize = 3
    ax2 = plt.subplot2grid((3,1), (2, 0), sharex=ax1)
    extraplots.plot_psth(spikeCountMat/binWidth,smoothWinSize,timeVec,trialsEachCond=trialsEachCond,
                     colorEachCond=colorEachCond,linestyle=None,linewidth=1.5,downsamplefactor=1)

    plt.xlabel('Time from sound onset (s)')
    plt.ylabel('Firing rate (spk/sec)')
    #plt.show()
    
    #fig_path= 
    #full_fig_path = os.path.join(fig_path, fig_title)
    #print full_fig_path
    #plt.tight_layout()
    plt.gcf().set_size_inches((8.5,11))
    #plt.savefig(full_fig_path, format = 'png')


'''
oneCell=celldatabase.CellInfo(animalName='adap012',ephysSession='2016-02-04_12-41-31',behavSession='20160204a',tetrode=3,cluster=3,trialsToExclude=[])

plot_rew_change_per_cell(oneCell,trialLimit=[],alignment='sound')

plot_rew_change_per_cell(oneCell,trialLimit=[],alignment='center-out')

plot_rew_change_per_cell(oneCell,trialLimit=[],alignment='side-in')

subject='adap012'
processedDir = '/home/languo/data/ephys/'+subject+'/'+subject+'_stats'
sigModFilename = os.path.join(processedDir,'sigMod_soundOnset.txt')

sigModFile=open(sigModFilename, 'r')
for line in sigModFile:
    str=line.split(':')[1]
    cellID=str.split()[0]


oneCell=celldatabase.CellInfo(animalName='adap012',ephysSession='2016-03-08_13-29-12',behavSession='20160308a',tetrode=3,cluster=4,trialsToExclude=[])

plot_rew_change_per_cell_per_freq(oneCell,trialLimit=[],alignment='sound')

plot_rew_change_per_cell_per_freq(oneCell,trialLimit=[],alignment='center-out')

plot_rew_change_per_cell_per_freq(oneCell,trialLimit=[],alignment='side-in')

#plot_rew_change_byblock_per_cell(oneCell,trialLimit=[],alignment='sound',choiceSide='right')

oneCell=celldatabase.CellInfo(animalName='adap012',ephysSession='2016-03-08_13-29-12',behavSession='20160308a',tetrode=5,cluster=6,trialsToExclude=[])

plot_rew_change_per_cell_per_freq(oneCell,trialLimit=[],alignment='sound')

plot_rew_change_per_cell_per_freq(oneCell,trialLimit=[],alignment='center-out')

plot_rew_change_per_cell_per_freq(oneCell,trialLimit=[],alignment='side-in')
'''
