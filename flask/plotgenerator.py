#Plot generation code for the Jaraviewer web framework
#By: James Vargas-Witherell
import matplotlib.pyplot as plt
from jaratoolbox import behavioranalysis
#the following are only needed for the test function. Can delete later
from jaratoolbox import loadbehavior
from jaratoolbox import settings
'''
INPUT CONVENTIONS:
plotList should be a list of dictionaries, each dictionary with the following parameters:
'type' : Contains the requested type of plot as a string. Accepted values are "psychometric", "summary", or "dynamics" 
'filename' : Contains the filename as the string. The filename should be in the format "mousename_YYYYMMDD_plotType.svg"
'data': Contains the raw data gained from the loadbehavior.FlexCategBehaviorData(behavFile,readmode='full') function in jaratoolbox

A parameter may be added that contains the filepath to the graph storage folder. Need to discuss
'''
#need to make a global path variable
def Generate(plotList):
#plotList is the list of plot dictionaries as specified above
    for plot in plotList:
        #get the data from the dictionary
        plotData = plot['data']
        #check what the plot type is and run the coorisponding method
        #basis for method calls taken from "test032_example_read_bdata.py" by Santiago Jaramillo
        if plot['type'] is "psychometric":
            #As mentioned by Santiago: parameters returned from psychometric plot are not used. Were put in place for improvments that were never finished
            (pline, pcaps, pbars, pdots) = behavioranalysis.plot_frequency_psycurve(plotData,fontsize=14)
        elif plot['type'] is "summary":
            freqsToUse = [plotData['lowFreq'][-1],plotData['highFreq'][-1]]
            behavioranalysis.plot_summary(plotData,fontsize=14,soundfreq=freqsToUse)
        elif plot['type'] is "dynamics":
            freqsToUse = [plotData['lowFreq'][-1],plotData['highFreq'][-1]]
            behavioranalysis.plot_dynamics(plotData,winsize=40,fontsize=14,soundfreq=freqsToUse)
        else:
            #ERROR case: plot type invalid
            return False
        #save the plot under the given filename (need to edit with filepath)
        #NOTE: Current savefig will save to whatever directory the code is run in. Be warned
        plt.savefig(plot['filename'])
    return True 

def Test():
    #Test function: Used to test code without needing the other modules
    # NOTE: this text function will be a mini version of what the backend will be doing each time
    #code from "test032_example_read_bdata.py" by Santiago Jaramillo
    EXPERIMENTER = settings.DEFAULT_EXPERIMENTER
    paradigm = '2afc'
    subject = 'adap021'
    session = '20160310a' # This is the date formatted as YYYYMMDD and one more character (usually 'a')

    # -- Find the data filename and load the data into a data object (similar to a Python dict) --
    behavFile = loadbehavior.path_to_behavior_data(subject,EXPERIMENTER,paradigm,session)
    behavData = loadbehavior.FlexCategBehaviorData(behavFile,readmode='full')
    #end Santiago's code
    #make each dictionary (for test, 1 per graph type) and append them to the list
    graphList = []
    graphDict1 = {'type' : "psychometric", 'filename' : "adap021_20160310_psychometric.svg", 'data' : behavData}
    graphList.append(graphDict1)
    graphDict2 = {'type' : "summary", 'filename' : "adap021_20160310_summary.svg", 'data' : behavData}
    graphList.append(graphDict2)
    graphDict3 = {'type' : "dynamic", 'filename' : "adap021_20160310_dynamic.svg", 'data' : behavData}
    graphList.append(graphDict3)
    Generate(graphList)

