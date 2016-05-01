'''
loadEphysData.py
Load ephys events
author: Billy Walker
'''



from jaratoolbox import loadopenephys
from jaratoolbox import loadbehavior
from jaratoolbox import spikesanalysis
import numpy as np
from pylab import * #I SHOULD CHANGE THIS. EFFECTS ARGSORT
import os

###########################
#ASSUMPTIONS
#There is a sound onset in every trial
###########################

#####################################################################################################################################################################
#PARAMETERS
#####################################################################################################################################################################

outputDir = '/home/billywalker/Pictures/psyCurve/'

timeLabeling = 'Time from sound Onset (sec)'

ephysRoot='/home/billywalker/data/ephys/test014/psyCurve/'
ephysSessionArray = ['2015-01-07_17-37-14','2015-01-08_16-14-41','2015-01-09_16-41-49','2015-01-10_21-45-52','2015-01-11_16-15-53','2015-01-12_17-10-52','2015-01-13_15-17-35','2015-01-14_16-04-16','2015-01-15_14-38-04','2015-01-16_17-13-23','2015-01-17_18-29-02','2015-01-18_21-33-33','2015-01-19_16-46-59','2015-01-20_16-06-16']#['2014-12-19_14-36-45','2014-12-22_11-42-00','2014-12-23_15-50-14','2014-12-24_17-11-53','2014-12-26_18-07-12']#'2014-12-20_22-37-24','2014-12-26_18-07-12'

subject = 'test014'
experimenter = 'santiago'
paradigm = '2afc'
sessionstrArray = ['20150107a','20150108a','20150109a','20150110a','20150111a','20150112a','20150113a','20150114a','20150115a','20150116a','20150117a','20150118a','20150119a','20150120a']#['20141219a','20141222a','20141223a','20141224a','20141226a']#'20141220a','20141226a'

#tetrodeID = 1 #Which tetrode to plot
responseRange = [0.10,0.40] #range of time to count spikes in after event onset
timeRange=[-0.5,1] #In seconds. Time range for rastor plot to plot spikes (around some event onset as 0)
binTime = 0.1 #Size of each bin in histogram in seconds
nametrialsToUse = "HighFreq"
Frequency = 0 #This chooses which frequency to look at, numbered out of possible frequencies starting with the lowest frequency as number 0
eventID = 0 #THIS IS THE CHANNEL THAT YOU CARE ABOUT. for example, channel 0 could be the sound presentation and channel 1 could be the trial period
#####################################################################################################################################################################
#####################################################################################################################################################################


# -- Global variables --
SAMPLING_RATE=30000.0


for indDate, ephysSession in enumerate(ephysSessionArray):
	
	#Load name of behavior session 
	sessionstr = sessionstrArray[indDate]
	
	for tetrodeID in range(1,9):

	# -- Load Behavior Data --
		behaviorFilename = loadbehavior.path_to_behavior_data(subject,experimenter,paradigm,sessionstr)
		bdata = loadbehavior.BehaviorData(behaviorFilename)

		numberOfTrials = len(bdata['choice'])
		targetFreqs = bdata['targetFrequency']

		#This gives an array of all frequencies presented
		possibleFreq = np.unique(bdata['targetFrequency'])

		#This gives an array with true and indices where the mouse made a correct decision
		correct = bdata['outcome']==bdata.labels['outcome']['correct']
		#This gives an array with true and indices where the mouse made a incorrect decision
		incorrect = bdata['outcome']==bdata.labels['outcome']['error']

		#This gives an array with true at indices of trials that are correct and went right
		rightward = bdata['choice']==bdata.labels['choice']['right']
		correctRightward = correct*rightward

		#This gives an array with true at indices of trials that are correct and went left
		leftward = bdata['choice']==bdata.labels['choice']['left']
		correctLeftward = correct*leftward

		#This gives an array with true at indices of trials that are incorrect and went right
		incorrectRightward = incorrect*rightward

		#This gives an array with true at indices of trials that are incorrect and went left
		incorrectLeftward = incorrect*leftward

		###############################################################################################################################################################################
		trialsToUse1 = incorrectLeftward #This is an array of 1's and 0's to decide which trials to count spikes in and compare to the other trials
		trialsToUse2 = correctRightward #This is an array of 1's and 0's to decide which trials to count spikes in and compare to the other trials
		##################################################################################################################################################################################



		# -- Load event data and convert event timestamps to ms --
		ephysDir = os.path.join(ephysRoot, ephysSession)
		eventFilename=os.path.join(ephysDir, 'all_channels.events')
		events = loadopenephys.Events(eventFilename) # Load events data
		eventTimes=np.array(events.timestamps)/SAMPLING_RATE #get array of timestamps for each event and convert to seconds by dividing by sampling rate (Hz). matches with eventID and 
		multipleEventOnset=np.array(events.eventID)  #loads the onset times of all events (matches up with eventID to say if event 1 went on (1) or off (0)
		eventChannel = np.array(events.eventChannel) #loads the ID of the channel of the event. For example, 0 is sound event, 1 is trial event, 2 ...

		# -- Load spike data and convert spike timestamps to ms --
		spike_filename=os.path.join(ephysDir, 'Tetrode{0}.spikes'.format(tetrodeID)) #make a path to ephys spike data of specified tetrode tetrodeID
		spikeData=loadopenephys.DataSpikes(spike_filename) #load spike data from specified tetrode tetrodeID
		spkTimeStamps=np.array(spikeData.timestamps)/SAMPLING_RATE #array of timestamps for each spike in seconds (thats why you divide by sampling rate)



		# -- Only use event onset times of one event --
		oneEvent = eventChannel==eventID #This picks out which channel you care about if there is more that one event
		eventOnset = multipleEventOnset*oneEvent #This keeps the correct size of the array to match eventTimes and picks out the onset of the channel you want

		while (numberOfTrials < np.sum(eventOnset)):
			eventOnset = eventOnset[:-1]

		eventOnsetTimes = eventTimes[eventOnset == 1] #This gives only the times of the onset of the channel you want

		eventOnsetTimesTrials1 = eventOnsetTimes[trialsToUse1==1]
		eventOnsetTimesTrials2 = eventOnsetTimes[trialsToUse2==1]



		# -- Convert spike data into np.array's --
		(spikeTimesFromEventOnset,trialIndexForEachSpike,indexLimitsEachTrial) = spikesanalysis.eventlocked_spiketimes(spkTimeStamps,eventOnsetTimes,timeRange)
		(spikeTimesFromEventOnsetTrials1,trialIndexForEachSpikeTrials1,indexLimitsEachTrialTrials1) = spikesanalysis.eventlocked_spiketimes(spkTimeStamps,eventOnsetTimesTrials1,timeRange)
		(spikeTimesFromEventOnsetTrials2,trialIndexForEachSpikeTrials2,indexLimitsEachTrialTrials2) = spikesanalysis.eventlocked_spiketimes(spkTimeStamps,eventOnsetTimesTrials2,timeRange)
		''' spikesanalysis.eventlocked_spiketimes
		    Create a vector with the spike timestamps w.r.t. events onset.

		    (spikeTimesFromEventOnset,trialIndexForEachSpike,indexLimitsEachTrial) = 
			eventlocked_spiketimes(timeStamps,eventOnsetTimes,timeRange)

		    timeStamps: (np.array) the time of each spike.
		    eventOnsetTimes: (np.array) the time of each instance of the event to lock to.
		    timeRange: (list or np.array) two-element array specifying time-range to extract around event.

		    spikeTimesFromEventOnset: 1D array with time of spikes locked to event.
		    trialIndexForEachSpike: 1D array with the trial corresponding to each spike.
		       The first spike index is 0.
		    indexLimitsEachTrial: [2,nTrials] range of spikes for each trial. Note that
		       the range is from firstSpike to lastSpike+1 (like in python slices)
		    spikeIndices
		'''


		# -- Make np.array of time ranges for bins
		startTime = float(timeRange[0]) #makes sure that these are floats so division works as expected
		endTime = float(timeRange[1])
		fullTime = endTime - startTime
		numberOfBins = int((fullTime//binTime)+1)
		binTimeRanges = np.empty([numberOfBins,2]) #Gives np.array of time ranges for each bin
		xCoordinatesPlot = np.empty(numberOfBins)
		for indBin in range(0,numberOfBins):
		    xCoordinatesPlot[indBin]=startTime+indBin*binTime
		    binTimeRanges[indBin]=np.array([(startTime+indBin*binTime),(startTime+(indBin+1)*binTime)])

		# -- Find the number of spikes in each bin --
		spikeNumberInBinPerTrial = np.empty([numberOfBins,numberOfTrials])
		for i,binRange in enumerate(binTimeRanges):
		    spikeNumberInBinPerTrial[i] = spikesanalysis.count_spikes_in_range(spikeTimesFromEventOnset,indexLimitsEachTrial,binRange) #array of the number of spikes in range for each trial
		''' spikesanalysis.count_spikes_in_range
		    Count number of spikes on each trial in a given time range.

		       spikeTimesFromEventOnset: vector of spikes timestamps with respect
			 to the onset of the event.
		       indexLimitsEachTrial: each column contains [firstInd,lastInd+1] of the spikes on a trial.
		       timeRange: time range to evaluate. Spike times exactly at the limits are not counted.

		       returns nSpikes
		'''

		##############################
		#THIS COULD BE A SEPARATE MODULE
		##############################

		######################################################################################################################
		#THIS IS FOR ALL FREQUENCIES
		# -- Pick which trials you care about in counting spikes --
		spikeMeanInBin1 = np.empty(numberOfBins) #This will hold the mean number of spikes in each bin or time range for the trialsToUse1
		spikeMeanInBin2 = np.empty(numberOfBins) #This will hold the mean number of spikes in each bin or time range for the trialsToUse2
		for indBin, spikeCounts in enumerate(spikeNumberInBinPerTrial):
		    spikeMeanInBin1[indBin] = np.mean(np.append(spikeCounts[trialsToUse1==1],0))  #The append 0 is just for the edge case that there are no trials to use so np.mean does not give a nan.
		    spikeMeanInBin2[indBin] = np.mean(np.append(spikeCounts[trialsToUse2==1],0))
		######################################################################################################################
		'''
		######################################################################################################################
		#THIS IS FOR ONE FREQUENCY
		# -- Pick which trials you care about in counting spikes --
		trialsOfFreq = targetFreqs==possibleFreq[Frequency] #array of booleans that is true if the frequency chosen was played in that trial
		trialToUseWithFreq1 = trialsToUse1*trialsOfFreq  #array with 1 is this is a trial to use and of the frequency chosen and 0 if not
		trialToUseWithFreq2 = trialsToUse2*trialsOfFreq  #array with 1 is this is a trial to use and of the frequency chosen and 0 if not
		spikeMeanInBin1 = np.empty(numberOfBins) #This will hold the mean number of spikes in each bin or time range for the trialsToUse1 for the frequency chosen
		spikeMeanInBin2 = np.empty(numberOfBins) #This will hold the mean number of spikes in each bin or time range for the trialsToUse2 for the frequency chosen
		for indBin, spikeCounts in enumerate(spikeNumberInBinPerTrial):
		    spikeMeanInBin1[indBin] = np.mean(np.append(spikeCounts[trialToUseWithFreq1==1],0)) #The append 0 is just for the edge case that there are no trials to use with this frequency so np.mean does not give a nan.
		    spikeMeanInBin2[indBin] = np.mean(np.append(spikeCounts[trialToUseWithFreq2==1],0))
		######################################################################################################################
		'''






		###################################################################################################################################################################################
		#####################################################THIS IS FOR THE RASTOR PLOT###################################################################################################
		###################################################################################################################################################################################

		targetFreqsTrials1 = targetFreqs[trialsToUse1==1]
		targetFreqsTrials2 = targetFreqs[trialsToUse2==1]


		sortedTrials1 = [] #array that sorts trials for different frequencies
		numTrialsEachFreq1 = []  #Used to plot lines after each group of sorted trials
		for indf1,oneFreq1 in enumerate(possibleFreq): #indf is index of this freq and oneFreq is the frequency
		    indsThisFreq1 = np.flatnonzero(targetFreqsTrials1==oneFreq1) #this gives indices of this frequency
		    sortedTrials1 = np.concatenate((sortedTrials1,indsThisFreq1)) #adds all indices to a list called sortedTrials
		    numTrialsEachFreq1.append(len(indsThisFreq1)) #finds number of trials each frequency has
		sortingIndsTrials1 = argsort(sortedTrials1) #gives array of indices that would sort the sortedTrials

		sortedIndexForEachSpikeTrials1 = sortingIndsTrials1[trialIndexForEachSpikeTrials1] #Takes values of trialIndexForEachSpike and finds value of sortingInds at that index and makes array. This array gives an array with the sorted index of each trial for each spike

		sortedTrials2 = [] #array that sorts trials for different frequencies
		numTrialsEachFreq2 = []  #Used to plot lines after each group of sorted trials
		for indf2,oneFreq2 in enumerate(possibleFreq): #indf is index of this freq and oneFreq is the frequency
		    indsThisFreq2 = np.flatnonzero(targetFreqsTrials2==oneFreq2) #this gives indices of this frequency
		    sortedTrials2 = np.concatenate((sortedTrials2,indsThisFreq2)) #adds all indices to a list called sortedTrials
		    numTrialsEachFreq2.append(len(indsThisFreq2)) #finds number of trials each frequency has
		sortingIndsTrials2 = argsort(sortedTrials2) #gives array of indices that would sort the sortedTrials

		sortedIndexForEachSpikeTrials2 = sortingIndsTrials2[trialIndexForEachSpikeTrials2] #Takes values of trialIndexForEachSpike and finds value of sortingInds at that index and makes array. This array gives an array with the sorted index of each trial for each spike

		###############################################################################################################################################################################################
		#This is for standard deviation analysis
		nSpikesTrials1 = spikesanalysis.count_spikes_in_range(spikeTimesFromEventOnsetTrials1,indexLimitsEachTrialTrials1,responseRange) #array of the number of spikes in range for each trial
		nSpikesTrials2 = spikesanalysis.count_spikes_in_range(spikeTimesFromEventOnsetTrials2,indexLimitsEachTrialTrials2,responseRange) #array of the number of spikes in range for each trial		
		'''Count number of spikes on each trial in a given time range.

		       spikeTimesFromEventOnset: vector of spikes timestamps with respect
			 to the onset of the event.
		       indexLimitsEachTrial: each column contains [firstInd,lastInd+1] of the spikes on a trial.
		       timeRange: time range to evaluate. Spike times exactly at the limits are not counted.

		       returns nSpikes
		'''
		standardDev1 = np.std(nSpikesTrials1)
		standardDev2 = np.std(nSpikesTrials2)
		#This analysis can also be done for each bin if we put the np.std into the bin nspike for loop
		##################################################################################################################################################################################################
		
		'''
		# -- Calculate average firing for each freq --
		#This is just used for plotting frequency in raster plots
		meanSpikesEachFrequencyTrials1 = np.empty(len(possibleFreq))
		for indf,oneFreq in enumerate(possibleFreq):
		    meanSpikesEachFrequencyTrials1[indf] = np.mean(nSpikesTrials1[indf])
		meanSpikesEachFrequencyTrials2 = np.empty(len(possibleFreq))
		for indf,oneFreq in enumerate(possibleFreq):
		    meanSpikesEachFrequencyTrials2[indf] = np.mean(nSpikesTrials2[indf])
		'''

                #The cumulative sum of the list of specific frequency presentations, used below for plotting the lines across the figure. 
		numTrialsTrials1 = cumsum(numTrialsEachFreq1)
		numTrialsTrials2 = cumsum(numTrialsEachFreq2)

		'''
		#This is to plot frequency tuning without comparisons
		clf()
		rastorFreq1 = plt.subplot2grid((3,4), (0, 0), colspan=3, rowspan=2)
		plot(spikeTimesFromEventOnset, sortedIndexForEachSpike, '.', ms=1)
		axvline(x=0, ymin=0, ymax=1, color='r')

		#The cumulative sum of the list of specific frequency presentations, 
		#used below for plotting the lines across the figure. 
		numTrials = cumsum(numTrialsEachFreq)

		#Plot the lines across the figure in between each group of sorted trials
		for indf, num in enumerate(numTrials):
		    rastorFreq1.axhline(y = num, xmin = 0, xmax = 1, color = '0.90', zorder = 0)

		tickPositions = numTrials - mean(numTrialsEachFreq)/2
		tickLabels = ["%0.2f" % (possibleFreq[indf]/1000.0) for indf in range(len(possibleFreq))]
		rastorFreq1.set_yticks(tickPositions)
		rastorFreq1.set_yticklabels(tickLabels)
		ylabel('Frequency Presented (kHz), {} total trials'.format(numTrials[-1]))
		title(ephysSession+' TT{0}'.format(tetrodeID))
		xlabel('Time (sec)')


		rastorFreq2 = plt.subplot2grid((3,4), (0, 3), colspan=1, rowspan=2)
		rastorFreq2.set_xscale('log')
		plot(possibleFreq,meanSpikesEachFrequency,'o-')
		ylabel('Avg spikes in window {0}-{1} sec'.format(*responseRange))
		xlabel('Frequency')
		'''

		clf()
		rastorFreq1 = plt.subplot2grid((3,4), (0, 0), colspan=2, rowspan=2)
		plot(spikeTimesFromEventOnsetTrials1, sortedIndexForEachSpikeTrials1, '.', ms=1)
		axvline(x=0, ymin=0, ymax=1, color='r')
		
		#This is used to plot frequency tick marks on side of raster plot.
		tickPossibleFreq1 = np.empty(0)
		tickNumTrialsTrials1 = np.empty(0)
		tickNumTrialsEachFreq1 = np.empty(0)
		for indf in range(len(possibleFreq)):
			if (numTrialsEachFreq1[indf]!=0):
				tickPossibleFreq1 = np.append(tickPossibleFreq1,possibleFreq[indf])
				tickNumTrialsTrials1 = np.append(tickNumTrialsTrials1,numTrialsTrials1[indf])
				tickNumTrialsEachFreq1 = np.append(tickNumTrialsEachFreq1,numTrialsEachFreq1[indf])
		tickPositions = tickNumTrialsTrials1 - mean(tickNumTrialsEachFreq1)/2
		tickLabels = ["%0.2f" % (tickPossibleFreq1[indf]/1000.0) for indf in range(len(tickPossibleFreq1))]
		rastorFreq1.set_yticks(tickPositions)
		rastorFreq1.set_yticklabels(tickLabels)
		ylabel('Frequency Presented (kHz), {} total trials'.format(numTrialsTrials1[-1]))
		title(ephysSession+' TT{0}'.format(tetrodeID))
		xlabel(timeLabeling)

		rastorFreq2 = plt.subplot2grid((3,4), (0, 2), colspan=2, rowspan=2)
		plot(spikeTimesFromEventOnsetTrials2, sortedIndexForEachSpikeTrials2, '.', ms=1)
		axvline(x=0, ymin=0, ymax=1, color='r')

	        #This is used to plot frequency tick marks on side of raster plot.
		tickPossibleFreq2 = np.empty(0)
		tickNumTrialsTrials2 = np.empty(0)
		tickNumTrialsEachFreq2 = np.empty(0)
		for indf in range(len(possibleFreq)):
			if (numTrialsEachFreq2[indf]!=0):
				tickPossibleFreq2 = np.append(tickPossibleFreq2,possibleFreq[indf])
				tickNumTrialsTrials2 = np.append(tickNumTrialsTrials2,numTrialsTrials2[indf])
				tickNumTrialsEachFreq2 = np.append(tickNumTrialsEachFreq2,numTrialsEachFreq2[indf])
		tickPositions = tickNumTrialsTrials2 - mean(tickNumTrialsEachFreq2)/2
		tickLabels = ["%0.2f" % (tickPossibleFreq2[indf]/1000.0) for indf in range(len(tickPossibleFreq2))]
		rastorFreq2.set_yticks(tickPositions)
		rastorFreq2.set_yticklabels(tickLabels)
		ylabel('Frequency Presented (kHz), {} total trials'.format(numTrialsTrials2[-1]))
		title(ephysSession+' TT{0}'.format(tetrodeID))
		xlabel(timeLabeling)



		###################################################################################################################################################################################
		#####################################################THIS IS FOR THE HISTOGRAM#####################################################################################################
		###################################################################################################################################################################################

		histogram3 = plt.subplot2grid((3,4), (2, 0), colspan=2)
		bar(xCoordinatesPlot,spikeMeanInBin1, width=binTime)
		ylabel('trialsToUse1, Average number of spikes in bin size {} sec'.format(binTime))
		xlabel(timeLabeling)

		histogram4 = plt.subplot2grid((3,4), (2, 2), colspan=2)
		bar(xCoordinatesPlot,spikeMeanInBin2, width=binTime)
		ylabel('trialsToUse2, Average number of spikes in bin size {} sec'.format(binTime))
		xlabel(timeLabeling)

		#show()
		
		tetrodeName = 'TT'+str(tetrodeID)
		plt.gcf().set_size_inches((8.5,11))
		figformat = 'png' #'png' #'pdf' #'svg'
		filename = 'psyCurve_%s_%s_%s_%s.%s'%(subject,sessionstr,tetrodeName,nametrialsToUse,figformat)
		fulloutputDir = outputDir+subject+'/'
		fullFileName = os.path.join(fulloutputDir,filename)
		print 'saving figure to %s'%fullFileName
		plt.gcf().savefig(fullFileName,format=figformat)
