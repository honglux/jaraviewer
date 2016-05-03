'''
Additional function for modifying plots.
'''


import matplotlib.pyplot as plt
import numpy as np
import os

def boxoff(ax,keep='left',yaxis=True):
    '''
    Hide axis lines, except left and bottom.
    You can specify to keep instead right and bottom with keep='right'
    '''
    ax.spines['top'].set_visible(False)
    if keep=='left':
        ax.spines['right'].set_visible(False)
    else:
        ax.spines['left'].set_visible(False)        
    xtlines = ax.get_xticklines()
    ytlines = ax.get_yticklines()
    for t in xtlines[1::2]+ytlines[1::2]:
        t.set_visible(False)
    if not yaxis:
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ytlines = ax.get_yticklines()
        for t in ytlines:
            t.set_visible(False)

def set_axes_color(ax,axColor):
    '''
    Change the color of axes, ticks and labels.
    '''
    import matplotlib
    for child in ax.get_children():
        if isinstance(child, matplotlib.axis.XAxis) or isinstance(child, matplotlib.axis.YAxis):
            for gchild in child.get_children():
                try:
                    gchild.set_color(axColor)
                except AttributeError:
                    for ggchild in gchild.get_children():
                        ggchild.set_color(axColor)
        if isinstance(child, matplotlib.spines.Spine):
            child.set_color(axColor)

def set_ticks_fontsize(ax,fontSize):
    '''
    Set fontsize of axis tick labels
    '''
    plt.setp(ax.get_xticklabels(),fontsize=fontSize)
    plt.setp(ax.get_yticklabels(),fontsize=fontSize)


def trials_each_cond_inds(trialsEachCond,nTrials):
    '''
    Create trialsEachCond as a list of indexes with trials for each condition.
    '''
    if isinstance(trialsEachCond,np.ndarray):
        # -- Convert boolean matrix to list of trial indexes --
        trialsEachCond = [np.flatnonzero(trialsEachCond[:,ind]) for ind in range(trialsEachCond.shape[1])]
    if trialsEachCond==[]:
        nCond=1
        #trialsEachCond = [np.arange(indexLimitsEachTrial.shape[1])]
        trialsEachCond = [np.arange(nTrials)]
    else:
        nCond = len(trialsEachCond)
    nTrialsEachCond = [len(x) for x in trialsEachCond]
    return (trialsEachCond,nTrialsEachCond,nCond)


def raster_plot(spikeTimesFromEventOnset,indexLimitsEachTrial,timeRange,trialsEachCond=[],
                colorEachCond=None,fillWidth=None,labels=None):
    '''
    Plot spikes raster plot grouped by condition
    Returns (pRaster,hcond)
    First trial is plotted at y=0

    trialsEachCond can be a list of lists of indexes, or a boolean array of shape [nTrials,nConditions]
    '''
    nTrials = len(indexLimitsEachTrial[0])
    (trialsEachCond,nTrialsEachCond,nCond) = trials_each_cond_inds(trialsEachCond,nTrials)

    if colorEachCond is None:
        colorEachCond = ['0.5','0.75']*np.ceil(nCond/2.0)

    if fillWidth is None:
        fillWidth = 0.05*np.diff(timeRange)

    nSpikesEachTrial = np.diff(indexLimitsEachTrial,axis=0)[0]
    nSpikesEachTrial = nSpikesEachTrial*(nSpikesEachTrial>0) # Some are negative
    trialIndexEachCond = []
    spikeTimesEachCond = []
    for indcond,trialsThisCond in enumerate(trialsEachCond):
        spikeTimesThisCond = np.empty(0,dtype='float64')
        trialIndexThisCond = np.empty(0,dtype='int')
        for indtrial,thisTrial in enumerate(trialsThisCond):
            indsThisTrial = slice(indexLimitsEachTrial[0,thisTrial],
                                  indexLimitsEachTrial[1,thisTrial])
            spikeTimesThisCond = np.concatenate((spikeTimesThisCond,
                                                 spikeTimesFromEventOnset[indsThisTrial]))
            trialIndexThisCond = np.concatenate((trialIndexThisCond,
                                                 np.repeat(indtrial,nSpikesEachTrial[thisTrial])))
        trialIndexEachCond.append(np.copy(trialIndexThisCond))
        spikeTimesEachCond.append(np.copy(spikeTimesThisCond))

    xpos = timeRange[0]+np.array([0,fillWidth,fillWidth,0])
    lastTrialEachCond = np.cumsum(nTrialsEachCond)
    firstTrialEachCond = np.r_[0,lastTrialEachCond[:-1]]

    hcond=[]
    pRaster = []
    ax = plt.gca()
    zline = plt.axvline(0,color='0.75',zorder=-10)
    plt.hold(True)

    for indcond in range(nCond):
        pRasterOne, = plt.plot(spikeTimesEachCond[indcond],
                            trialIndexEachCond[indcond]+firstTrialEachCond[indcond],'.k',
                            rasterized=True)
        pRaster.append(pRasterOne)
        ypos = np.array([firstTrialEachCond[indcond],firstTrialEachCond[indcond],
                         lastTrialEachCond[indcond],lastTrialEachCond[indcond]])-0.5
        hcond.extend(plt.fill(xpos,ypos,ec='none',fc=colorEachCond[indcond]))
        hcond.extend(plt.fill(xpos+np.diff(timeRange)-fillWidth,ypos,ec='none',
                              fc=colorEachCond[indcond]))
    plt.hold(False)
    plt.xlim(timeRange)
    plt.ylim(-0.5,lastTrialEachCond[-1]-0.5)

    if labels:
        labelsPos = (lastTrialEachCond+firstTrialEachCond)/2.0 -0.5
        ax.set_yticks(labelsPos)
        ax.set_yticklabels(labels)

    return(pRaster,hcond,zline)


def plot_psth(spikeCountMat,smoothWinSize,binsStartTime,trialsEachCond=[],
              colorEachCond=None,linestyle=None,linewidth=3,downsamplefactor=1):
    '''
    TODO: 
    - Check if the windowing is non-causal
    - Check the units of the vertical axis (is it spikes/sec?)
    '''

    #from scipy.signal import hanning
    #winShape = hanning(smoothWinSize) # Hanning
    #winShape = np.ones(smoothWinSize) # Square (non-causal)
    winShape = np.concatenate((np.zeros(smoothWinSize),np.ones(smoothWinSize))) # Square (causal)
    winShape = winShape/np.sum(winShape)


    nTrials = spikeCountMat.shape[0]
    (trialsEachCond,nTrialsEachCond,nCond) = trials_each_cond_inds(trialsEachCond,nTrials)

    if colorEachCond is None:
        colorEachCond = ['0.5']*nCond
    if linestyle is None:
        linestyle = ['-']*nCond
    pPSTH = []
    for indc in range(nCond):
        thisCondCounts = spikeCountMat[trialsEachCond[indc],:]
        thisPSTH = np.mean(thisCondCounts,axis=0)
        smoothPSTH = np.convolve(thisPSTH,winShape,mode='same')
        sSlice = slice(0,len(smoothPSTH),downsamplefactor)
        ph, = plt.plot(binsStartTime[sSlice],smoothPSTH[sSlice],ls=linestyle[indc])
        pPSTH.append(ph)
        pPSTH[-1].set_linewidth(linewidth)
        pPSTH[-1].set_color(colorEachCond[indc])    
        plt.hold(True)
    return pPSTH



def plot_psychometric(possibleValues,fractionHitsEachValue,ciHitsEachValue=None,xTicks=None,xTickPeriod=1000):
    if ciHitsEachValue is not None:
        upperWhisker = ciHitsEachValue[1,:]-fractionHitsEachValue
        lowerWhisker = fractionHitsEachValue-ciHitsEachValue[0,:]
        (pline, pcaps, pbars) = plt.errorbar(possibleValues, 100*fractionHitsEachValue, 
                                             yerr = [100*lowerWhisker, 100*upperWhisker],color='k')
    else:
        pline = plt.plot(possibleValues, 100*fractionHitsEachValue,'k')
        pcaps = None
        pbars = None
    pdots = plt.plot(possibleValues, 100*fractionHitsEachValue, 'o',mec='none',mfc='k',ms=8)
    plt.setp(pline,lw=2)
    plt.axhline(y=50, color = '0.5',ls='--')
    ax=plt.gca()
    ax.set_xscale('log')
    if xTicks is None:
        xTicks = [possibleValues[0],possibleValues[-1]]
    ax.set_xticks(xTicks)
    ax.set_xticks(np.arange(possibleValues[0],possibleValues[-1],xTickPeriod),minor=True)
    from matplotlib.ticker import ScalarFormatter
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_major_formatter(ScalarFormatter())

    plt.ylim([0,100])
    plt.xlim([possibleValues[0]/1.2,possibleValues[-1]*1.2])
    #plt.xlabel('Frequency (kHz)')
    #plt.ylabel('Rightward trials (%)')
    return (pline, pcaps, pbars, pdots)


def set_log_ticks(ax,tickValues,axis='x'):
    tickLogValues = np.log10(tickValues);
    tickLabels = ['%d'%(1e-3*xt) for xt in tickValues];
    if axis=='x':
        ax.set_xticks(tickLogValues)
        ax.set_xticklabels(tickLabels)
    else:
        ax.set_yticks(tickLogValues)
        ax.set_yticklabels(tickLabels)


def save_figure(filename, fileformat, figsize, outputDir='./'):
    plt.gcf().set_size_inches(figsize)
    figName = filename+'.{0}'.format(fileformat)
    fullName = os.path.join(outputDir,figName)
    print 'Saving figure to %s'%fullName
    plt.gcf().set_frameon(False)
    plt.savefig(fullName,format=fileformat,facecolor='none')
    plt.gcf().set_frameon(True)
    print '... figure saved.'


class FlipThrough(object):
    def __init__(self, plotter, data):
        '''
        Allow flipping through data plots.
        Args:
            plotter (function): function that plots data.
            data (list): list of tuples containing the parameters for the plotter function.
        '''
        self.plotter = plotter
        self.data = data
        self.counter = 0
        self.maxDataInd = len(data)-1
        self.fig = plt.gcf()
        self.redraw() # Plot data
        self.kpid = self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)

    def redraw(self):
        self.fig.clf()
        if isinstance(self.data[self.counter], tuple):
            # FIXME: this will fail if the function requires a tuple as input
            self.plotter(*self.data[self.counter])
        else:
            self.plotter(self.data[self.counter])
        plt.suptitle('{}/{}: Press < or > to flip through data'.format(self.counter+1,
                                                                       self.maxDataInd+1))
        self.fig.show()

    def on_key_press(self, event):
        '''
        Method to listen for keypresses and flip to next/previous view
        '''
        if event.key=='<' or event.key==',' or event.key=='left':
            if self.counter>0:
                self.counter -= 1
            else:
                self.counter = self.maxDataInd
            self.redraw()
        elif event.key=='>' or event.key=='.' or event.key=='right':
            if self.counter<self.maxDataInd:
                self.counter += 1
            else:
                self.counter = 0
            self.redraw()


if __name__=='__main__':
    rdata = np.random.randint(0,9,(10,3,3))
    dataList = [(m,) for m in rdata]
    ft=FlipThrough(plt.imshow,dataList)

