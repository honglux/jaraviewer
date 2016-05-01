'''
List of all isolated units from one animal
'''

from jaratoolbox import celldatabase_quality as celldatabase
eSession = celldatabase.EphysSessionInfo  # Shorter name to simplify code


cellDB = celldatabase.CellDatabase()

oneES = eSession(animalName='test055',
                 ephysSession = '2015-06-04_15-02-05',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[3,3,5,3,2,4,2,3,3,4,2,2],2:[3,1,2,1,4,3,4,4,5,4,3,2],3:[3,4,1,2,4,3,3,1,4,2,4,2],4:[3,3,1,3,4,2,2,2,2,2,4,4],5:[3,2,4,3,2,2,3,2,2,4,4,2],6:[2,0,0,0,0,0,0,0,0,0,0,0],7:[3,2,4,5,2,1,4,2,3,3,2,2],8:[3,3,2,2,1,2,1,4,2,4,3,4]},
		 behavSession = '20150604a')
cellDB.append_session(oneES) 

oneES = eSession(animalName='test055',
                 ephysSession = '2015-06-02_13-32-18',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[3,1,2,3,2,2,1,2,1,1,2,2],2:[3,3,3,2,2,3,2,7,2,2,3,1],3:[3,2,1,2,3,5,1,2,2,2,2,2],4:[3,2,2,4,2,2,6,1,4,1,1,3],5:[3,1,2,2,2,2,2,3,2,4,3,2],6:[9,0,0,0,0,0,0,0,0,0,0,0],7:[3,2,2,1,2,2,3,4,4,1,2,2],8:[3,4,1,1,1,2,1,1,6,2,3,1]},
		 behavSession = '20150602a')
cellDB.append_session(oneES) 

oneES = eSession(animalName='test055',
                 ephysSession = '2015-06-01_12-51-07',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[3,4,4,2,2,3,4,1,2,2,7,0],2:[3,2,3,2,2,2,2,3,3,7,2,2],3:[3,1,1,1,2,2,2,2,1,2,4,4],4:[3,2,7,2,1,7,4,2,1,2,2,2],5:[3,3,1,2,2,1,2,2,1,1,6,2],6:[9,0,0,0,0,0,0,0,0,0,0,0],7:[3,1,1,3,4,2,1,1,1,1,1,0],8:[3,1,4,1,6,3,2,1,1,1,4,2]},
		 behavSession = '20150601a')
cellDB.append_session(oneES) 

oneES = eSession(animalName='test055',
                 ephysSession = '2015-05-30_15-51-45',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[3,2,7,2,2,6,7,3,6,2,7,2],2:[3,2,2,3,2,2,3,2,3,2,6,2],3:[3,2,2,2,1,1,2,3,2,2,2,2],4:[3,1,2,2,1,2,3,2,2,2,4,7],5:[3,3,3,2,2,2,2,3,3,1,2,2],6:[9,0,0,0,0,0,0,0,0,0,0,0],7:[3,3,1,2,3,4,1,2,1,2,4,1],8:[3,2,7,4,4,3,6,1,1,4,1,1]},
		 behavSession = '20150530a')
cellDB.append_session(oneES) 

'''
oneES = eSession(animalName='test055',
                 ephysSession = '2015-05-29_14-00-38',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:[1],7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[]},
                 behavSession = '20150529a')
cellDB.append_session(oneES)
'''

oneES = eSession(animalName='test055',
                 ephysSession = '2015-05-28_12-49-35',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[3,1,6,6,2,4,4,2,3,3,1,6],2:[3,3,4,2,3,2,3,1,3,3,3,2],3:[3,2,2,2,2,2,2,2,3,3,1,2],4:[3,3,3,3,2,6,2,2,7,1,2,2],5:[3,1,3,1,3,3,2,2,2,2,3,3],6:[9,0,0,0,0,0,0,0,0,0,0,0],7:[3,1,3,1,1,4,1,2,3,3,3,1],8:[3,4,3,1,2,2,3,1,2,3,6,6]},
		 behavSession = '20150528a')
cellDB.append_session(oneES) 

oneES = eSession(animalName='test055',
                 ephysSession = '2015-05-27_12-20-52',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[3,6,2,3,3,7,1,6,6,2,3,2],2:[3,2,3,1,2,3,8,2,1,2,8,3],3:[3,2,4,1,2,3,2,1,4,1,4,2],4:[3,2,2,1,4,2,2,1,3,2,3,1],5:[3,2,3,2,5,2,1,2,3,3,8,2],6:[9,0,0,0,0,0,0,0,0,0,0,0],7:[3,1,1,5,1,3,3,1,2,1,1,1],8:[3,2,4,3,3,2,7,4,2,3,4,3]},
                 behavSession = '20150527a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-05-26_13-19-02',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[3,2,3,2,2,6,2,3,1,2,2,3],2:[3,2,2,3,7,3,1,3,3,2,6,2],3:[3,3,2,2,2,2,3,2,4,1,1,0],4:[3,2,2,3,1,2,1,1,3,1,1,2],5:[3,3,2,3,2,2,2,2,2,1,3,3],6:[3,0,0,0,0,0,0,0,0,0,0,0],7:[3,3,8,3,2,1,3,1,2,1,1,1],8:[3,7,2,7,2,3,2,3,1,3,2,2]},
                 behavSession = '20150526a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-05-19_12-54-16',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[3,2,6,2,1,1,6,2,6,3,6,6],2:[3,2,3,3,2,2,2,7,4,1,2,3],3:[3,3,2,4,1,1,2,2,2,2,1,2],4:[3,2,2,4,2,4,3,2,1,2,1,7],5:[3,3,4,2,2,2,3,2,4,3,2,2],6:[9,0,0,0,0,0,0,0,0,0,0,0],7:[3,3,1,3,1,1,1,1,1,2,1,2],8:[3,6,1,3,1,1,1,1,2,1,1,2]},
                 behavSession = '20150519a')
cellDB.append_session(oneES)
'''
oneES = eSession(animalName='test055',
                 ephysSession = '2015-05-18_13-13-02',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[
                 behavSession = '20150518a')
cellDB.append_session(oneES)
'''
oneES = eSession(animalName='test055',
                 ephysSession = '2015-05-17_18-01-31',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[3,3,2,1,2,7,2,1,1,1,8,1],2:[3,3,1,6,3,2,3,1,2,2,2,6],3:[3,3,2,1,2,4,6,1,2,2,6,2],4:[3,1,2,2,8,2,2,2,4,3,2,1],5:[3,2,8,3,2,2,2,2,2,2,1,3],6:[9,0,0,0,0,0,0,0,0,0,0,0],7:[3,1,2,1,1,1,1,1,1,3,1,4],8:[3,1,1,3,6,1,1,1,1,1,2,1]},
                 behavSession = '20150517a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-05-15_12-05-23',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[3,3,6,2,3,6,1,6,1,2,2,3],2:[3,2,2,2,2,3,5,6,3,3,7,3],3:[3,2,4,2,3,2,2,2,2,7,1,2],4:[3,2,4,2,1,2,1,3,1,1,1,1],5:[3,4,2,4,2,2,5,2,2,3,5,2],6:[3,0,0,0,0,0,0,0,0,0,0,0],7:[3,4,2,2,4,4,3,1,2,1,1,2],8:[3,1,6,1,2,1,1,1,3,1,1,1]},
                 behavSession = '20150515a')
cellDB.append_session(oneES)

'''
oneES = eSession(animalName='test055',#########################################
                 ephysSession = '2015-05-14_12-46-29',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[
                 behavSession = '20150514a')
cellDB.append_session(oneES)
'''

oneES = eSession(animalName='test055',
                 ephysSession = '2015-05-13_13-07-12',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[3,6,7,6,1,3,3,2,2,2,1,6],2:[3,2,3,2,2,2,3,1,2,3,3,7],3:[3,2,2,2,2,3,2,2,4,2,2,1],4:[3,2,1,3,2,2,4,4,4,2,2,4],5:[3,2,2,3,1,2,2,2,3,3,8,3],6:[2,0,0,0,0,0,0,0,0,0,0,0],7:[3,1,7,3,1,2,4,4,4,3,2,1],8:[3,1,1,4,1,1,3,1,1,1,1,2]},
                 behavSession = '20150513a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-05-12_13-01-27',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[3,1,2,4,1,1,7,3,2,2,2,4],2:[3,2,3,2,2,2,1,1,3,1,2,3],3:[3,2,4,2,2,1,2,2,3,1,2,2],4:[3,2,1,2,2,2,3,1,1,2,2,2],5:[3,8,2,8,3,4,5,2,2,2,2,1],6:[9,0,0,0,0,0,0,0,0,0,0,0],7:[3,2,1,3,1,4,4,1,1,1,2,1],8:[3,1,1,1,1,3,1,1,1,1,7,1]},
                 behavSession = '20150512a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-05-11_15-31-25',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[3,4,1,2,1,2,1,2,2,1,1,4],2:[9,0,0,0,0,0,0,0,0,0,0,0],3:[3,2,2,2,2,3,2,2,2,2,1,2],4:[3,1,2,4,1,3,2,2,4,2,4,8],5:[3,2,3,4,5,2,2,3,3,2,4,2],6:[3,3,2,4,2,1,1,2,3,2,2,2],7:[3,1,2,3,1,6,2,2,1,1,2,4],8:[3,1,4,4,3,1,2,1,1,1,4,3]},
                 behavSession = '20150511a')
cellDB.append_session(oneES)
'''
oneES = eSession(animalName='test055',###########################################
                 ephysSession = '2015-05-10_23-03-22',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[
                 behavSession = '20150510a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',############################################
                 ephysSession = '2015-05-09_20-39-25',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[
                 behavSession = '20150509a')
cellDB.append_session(oneES)
'''
oneES = eSession(animalName='test055',
                 ephysSession = '2015-05-08_17-17-43',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[3,1,1,1,6,7,2,2,2,1,1,0],2:[2,0,0,0,0,0,0,0,0,0,0,0],3:[3,2,2,4,2,2,3,2,2,2,6,2],4:[3,4,2,2,2,4,1,1,6,2,4,6],5:[3,2,8,5,2,2,2,2,3,2,4,2],6:[3,1,2,3,1,3,2,2,2,2,2,3],7:[3,3,1,2,2,1,2,3,2,4,1,1],8:[3,4,2,3,4,1,4,1,1,1,1,2]},
                 behavSession = '20150508a')
cellDB.append_session(oneES)
'''
oneES = eSession(animalName='test055',
                 ephysSession = '2015-05-06_12-38-47',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[
                 behavSession = '20150506a')
cellDB.append_session(oneES)
'''
oneES = eSession(animalName='test055',
                 ephysSession = '2015-05-05_12-55-25',
                 clustersEachTetrode = {1:range(1,13),2:range[1],3:range(1,12),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[3,1,2,1,2,1,4,6,6,1,1,1],2:[9,0,0,0,0,0,0,0,0,0,0,0],3:[3,2,3,2,2,1,2,4,1,2,2,0],4:[3,2,6,4,3,2,6,2,6,2,2,6],5:[3,2,2,8,6,2,3,1,3,6,2,0],6:[3,3,1,3,2,2,2,3,3,3,2,2],7:[3,4,2,2,2,2,3,2,3,1,1,4],8:[3,2,1,4,1,3,1,1,1,4,4,6]},
                 behavSession = '20150505a')
cellDB.append_session(oneES)
'''
oneES = eSession(animalName='test055',########################################
                 ephysSession = '2015-05-01_12-59-12',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:[1],7:range(1,12),8:range(1,13)},
                 clusterQuality = {1:[4,2,3,1,1,4,1,2,3,3,2,3],2:[4,3,4,3,4,5,4,3,2,2,3,3],3:[4,3,3,3,5,3,3,2,2,4,3,4],4:[4,2,3,5,3,3,5,5,5,5,3,4],5:[4,4,5,5,5,3,5,5,3,5,3,3],6:[4],7:[4,2,4,3,3,2,3,3,3,5,3,3],8:[4,1,2,1,4,3,2,1,2,2,1,3]},
                 behavSession = '20150501a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-29_12-48-20',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:[1],7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,2,3,3,2,3,2,2,1,3,3,4],2:[4,2,3,2,4,1,3,3,3,3,3,4],3:[4,3,3,3,3,3,5,3,3,3,4,3],4:[4,3,3,4,3,3,2,1,5,3,5,3],5:[4,5,3,5,3,5,3,5,3,5,3,3],6:[3],7:[4,3,4,3,3,3,3,3,3,3,5,3],8:[4,4,3,2,2,4,3,2,1,2,1,2]},
                 behavSession = '20150429a')
cellDB.append_session(oneES)

#HAS TWO SKIPPED TRIALS
oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-28_12-46-13',
                 clustersEachTetrode = {1:range(1,13),2:range(1,12),3:range(1,13),4:range(1,13),5:range(1,13),6:[1],7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,4,2,2,2,1,1,3,1,3,3,1],2:[4,3,2,4,3,1,3,2,2,3,3],3:[4,3,3,3,3,3,3,3,3,3,4,3],4:[4,5,3,1,4,5,5,3,3,5,3,3],5:[4,3,4,3,5,3,3,3,5,3,5,5],6:[3],7:[4,3,3,3,3,4,3,5,3,5,3,5],8:[4,2,2,2,1,2,4,3,2,2,1,1]},
                 behavSession = '20150428a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-27_15-41-55',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:[1],7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,2,1,4,1,1,1,2,1,2,1,2],2:[4,1,4,3,2,2,4,4,3,2,4,2],3:[4,3,4,3,4,2,2,2,2,2,4,3],4:[4,5,3,3,2,3,4,3,2,2,2,3],5:[4,5,3,3,5,4,4,4,4,4,2,3],6:[4],7:[4,2,1,4,4,4,4,3,2,2,3,4],8:[4,2,1,2,2,2,2,1,1,4,2,2]},
                 #soundResponse = {1:[4,6,6,4,6,1,1,2,6,1,2,6],2:[4,6,4,5,1,6,4,4,6,6,5,1],3:[4,1,4,6,4,4,6,5,4,5,4,3],4:[4,1,3,6,3,3,4,6,6,6,6,6],5:[4,5,5,6,6,4,4,4,4,4,3,6],6:[6],7:[5,6,6,4,4,4,4,6,6,5,3,4],8:[4,1,1,1,1,5,2,1,3,4,1,1]},
                 behavSession = '20150427a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-23_13-08-26',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:[1],7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,2,2,2,1,2,2,1,4,2,3,2],2:[4,3,3,2,4,3,4,4,2,3,3,1],3:[4,3,2,3,3,1,1,3,4,3,3,2],4:[4,5,4,5,3,3,3,5,5,5,5,3],5:[4,2,3,2,5,3,3,4,4,5,5,3],6:[4],7:[4,2,3,1,3,2,4,3,1,1,1,3],8:[4,2,2,3,4,2,2,2,2,1,2,2]},
                 #soundResponse = {1:[5,2,1,2,1,2,3,1,3,1,6,6],2:[5,6,5,1,5,5,3,4,3,1,5,5],3:[5,6,2,1,5,6,3,3,4,3,6,5],4:[5,2,4,6,3,3,3,1,3,3,3,3],5:[5,5,5,3,5,6,6,3,5,6,5,5],6:[3],7:[5,2,3,6,2,5,4,3,6,6,6,6],8:[5,1,1,1,4,1,1,1,1,1,5,1]},
                 behavSession = '20150423a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-22_13-47-04',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,12),4:[1],5:range(1,12),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,1,3,3,4,3,3,2,2,1,2,2],2:[4,1,1,2,3,2,1,4,3,4,3,2],3:[4,3,3,2,3,2,3,3,3,1,3],4:[5],5:[4,1,3,4,3,5,3,5,5,3,3],6:[4,2,4,4,4,4,3,2,3,3,3,4],7:[4,3,3,3,3,3,1,3,4,4,3,3],8:[4,4,2,2,2,3,1,3,1,2,2,2]},
                 #soundResponse = {1:[5,1,6,6,4,2,6,2,2,1,6,5],2:[5,6,6,6,3,3,6,4,3,5,3,5],3:[5,3,6,1,3,3,3,5,6,6,1,5],4:[1],5:[5,6,6,5,6,6,6,5,5,5,5,5],6:[5,3,3,5,4,5,3,5,6,3,5,5],7:[5,6,2,3,1,3,3,6,3,4,3,5],8:[5,4,6,6,1,2,1,6,2,1,1,1]},
                 behavSession = '20150422a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',###################################
                 ephysSession = '2015-04-21_13-43-00',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:[1],5:range(1,13),6:range(1,12),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,4,2,1,1,1,1,3,2,2,2,2],2:[4,1,4,3,4,1,3,4,3,1,3,4],3:[4,2,2,1,2,3,3,4,2,1,1,2],4:[2],5:[4,3,2,4,5,3,3,5,1,4,3,5],6:[4,2,3,2,2,4,3,3,2,4,2],7:[4,3,3,4,2,3,2,2,4,2,2,3],8:[4,4,1,2,2,2,1,1,2,1,2,3]},
                 #soundResponse = {1:[5,4,2,1,1,5,6,3,3,1,2,2],2:[5,6,3,6,5,2,6,3,3,6,1,5],3:[5,1,6,6,5,3,6,4,1,1,3,3],4:[1],5:[5,6,6,5,6,6,3,5,5,4,6,5],6:[5,3,6,5,3,5,6,6,5,4,5,5],7:[5,6,2,4,5,5,2,6,5,5,5,5],8:[5,4,6,1,6,1,1,1,1,1,1,6]},
                 behavSession = '20150421a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-20_13-31-52',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,12),4:[1],5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,2,2,2,3,2,2,3,2,2,2,4],2:[4,3,3,2,4,2,2,3,4,4,3,2],3:[4,3,3,1,3,3,2,3,2,2,4],4:[2],5:[4,3,5,1,3,2,4,3,5,3,1,4],6:[4,3,3,3,4,3,2,3,3,3,3,4],7:[4,3,1,2,4,3,4,3,3,3,1,4],8:[4,2,2,2,2,2,2,4,2,3,1,3]},
                 #soundResponse = {1:[5,6,6,1,3,1,1,1,3,2,1,4],2:[5,6,5,3,5,6,2,1,4,5,2,3],3:[5,3,3,1,6,3,1,6,3,6,4,5],4:[1],5:[5,5,6,2,6,5,5,6,5,5,5,4],6:[5,6,3,5,4,6,1,5,3,2,5,5],7:[5,1,6,4,1,2,3,5,6,1,6,3],8:[5,1,6,1,1,1,1,4,1,6,1,2]},
                 behavSession = '20150420a')
cellDB.append_session(oneES)


oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-19_15-12-02',
                 clustersEachTetrode = {1:range(1,13),2:range(1,12),3:range(1,13),4:range(1,13),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,1,1,4,1,2,2,3,2,2,2,2],2:[4,4,3,3,3,2,4,3,4,2,3],3:[4,2,3,2,4,2,3,4,2,3,2,2],4:[4,1,5,4,5,2,2,2,3,5,5,5],5:[2],6:[4,4,4,4,3,4,4,2,4,4,4,3],7:[4,3,4,4,4,1,1,3,1,4,2,3],8:[4,2,3,1,2,4,1,2,2,2,2,2]},
                 behavSession = '20150419a')
cellDB.append_session(oneES)


oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-18_15-43-54',
                 clustersEachTetrode = {1:range(1,12),2:range(1,13),3:range(1,13),4:range(1,13),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,2,1,2,2,4,3,2,1,2,3],2:[4,3,2,3,4,3,4,5,4,2,1,3],3:[4,2,3,2,1,2,2,4,2,2,3,3],4:[4,1,1,2,2,4,2,3,2,5,2,3],5:[4],6:[4,4,3,3,3,4,3,4,2,3,3,4],7:[4,3,2,3,4,3,3,3,4,5,5,4],8:[4,2,2,2,1,4,2,2,3,4,2,2]},
                 #soundResponse = {1:[5,6,6,6,5,4,3,6,1,3,1,5],2:[5,6,5,5,5,5,5,5,4,3,5,5],3:[5,5,3,3,6,3,3,4,3,1,6,3],4:[5,6,3,5,6,3,1,3,6,1,3,6],5:[6],6:[5,3,3,5,2,5,5,5,3,3,3,5],7:[5,6,3,3,5,5,1,1,4,6,2,5],8:[5,1,1,1,1,4,1,1,2,5,6,1]},
                 behavSession = '20150418a')
cellDB.append_session(oneES)


#THIS SESSION IS MESSED UP
oneES = eSession(animalName='test055',######################################
                 ephysSession = '2015-04-17_16-21-33',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150417a')
cellDB.append_session(oneES)


oneES = eSession(animalName='test055',#######################################
                 ephysSession = '2015-04-16_13-38-38',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,1,2,1,2,3,4,4,4,2,2,2],2:[4,4,4,3,4,4,2,4,4,3,4,2],3:[4,2,1,4,4,2,2,3,1,3,2,1],4:[4,2,5,3,5,2,4,3,3,2,2,5],5:[4],6:[4,4,3,4,4,4,2,4,4,3,4,2],7:[4,4,4,3,4,3,4,4,2,4,3,3],8:[4,2,2,2,2,4,1,2,1,2,2,4]},
                 #soundResponse = {1:[5,1,6,1,2,1,4,5,5,6,6,2],2:[5,5,5,5,5,5,6,5,4,6,5,5],3:[5,6,1,3,3,3,1,3,3,3,2,6],4:[5,2,6,3,5,3,5,6,6,3,3,6],5:[6],6:[5,5,6,5,5,5,1,4,5,5,5,3],7:[5,5,5,6,5,1,5,5,3,4,5,6],8:[5,1,1,1,5,5,2,1,6,1,1,4]},
                 behavSession = '20150416a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-15_12-29-45',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,12),4:range(1,13),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,3,5,2,2,4,1,4,2,2,3,2],2:[4,4,4,2,4,4,4,4,3,4,3,2],3:[4,2,5,4,2,2,1,3,1,1,2],4:[4,2,2,4,4,5,3,5,3,2,5,3],5:[4],6:[4,4,4,4,2,4,1,4,3,4,3,4],7:[4,3,3,2,4,2,4,4,4,4,4,2],8:[4,2,2,4,1,4,4,2,5,2,2,4]},
                 #soundResponse = {1:[5,6,6,2,2,6,1,4,6,5,6,2],2:[5,4,3,6,4,4,5,4,6,4,2,6],3:[5,6,2,4,2,3,1,6,6,3,1,5],4:[5,6,3,4,4,5,6,6,6,6,3,2],5:[6],6:[5,5,4,5,6,3,1,4,4,4,6,4],7:[5,2,2,1,4,6,4,4,4,4,4,1],8:[5,1,1,4,6,4,4,6,6,6,1,4]},
                 behavSession = '20150415a')
cellDB.append_session(oneES)


oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-14_12-09-18',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150414a')
cellDB.append_session(oneES)


oneES = eSession(animalName='test055',################################################
                 ephysSession = '2015-04-13_15-54-20',
                 clustersEachTetrode = {1:range(1,12),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:[1],7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,1,2,2,1,3,2,4,2,1,1],2:[4,1,4,4,2,3,3,4,1,4,1,4],3:[4,3,1,3,2,3,2,2,2,4,2,2],4:[4,3,5,5,3,2,4,4,5,5,3,2],5:[4,4,3,4,3,5,3,3,4,5,3,3],6:[2],7:[4,2,3,4,4,2,3,1,3,1,4,3],8:[4,2,1,2,1,2,5,1,1,4,2,1]},
                 #soundResponse = {1:[5,6,5,6,1,5,2,4,2,2,1,5],2:[5,5,3,5,5,3,6,5,6,5,6,3],3:[5,6,3,3,1,3,1,6,3,4,3,6],4:[5,3,3,1,3,3,4,5,5,3,6,6],5:[5,5,5,5,6,5,5,5,3,5,6,6],6:[3],7:[5,5,1,5,4,1,3,5,3,1,3,6],8:[5,1,1,1,1,1,1,6,1,4,6,1]},
                 behavSession = '20150413a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-13_00-14-37',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150412a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-11_18-30-24',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,2,1,2,2,2,2,1,3,1,1,4],2:[4,2,1,1,2,3,4,4,4,2,2,2],3:[4,4,1,3,3,2,5,2,1,3,4,2],4:[4,5,3,5,4,2,4,5,2,4,3,3],5:[2],6:[4,4,4,4,4,4,4,4,3,3,4,4],7:[4,2,3,4,2,4,4,4,4,2,4,3],8:[4,1,2,3,1,2,2,2,5,4,1,1]},
                 #soundResponse = {1:[5,1,1,6,6,6,3,2,1,6,1,4],2:[5,1,6,2,3,3,5,4,5,1,6,5],3:[5,4,3,3,6,1,6,2,6,3,5,5],4:[5,1,6,5,5,5,5,3,3,5,3,3],5:[6],6:[5,5,5,4,5,5,3,5,5,6,5,5],7:[5,1,6,3,2,4,5,5,5,6,5,3],8:[5,1,1,3,1,1,1,1,1,4,3,1]},
                 behavSession = '20150411a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-10_12-34-00',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150410a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-09_12-17-28',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,2,1,1,1,2,1,4,2,2,2,2],2:[4,1,1,1,1,2,2,4,4,1,2,3],3:[4,5,4,3,3,3,2,1,1,4,3,3],4:[4,1,1,5,3,2,5,5,5,4,1,1],5:[4],6:[4,4,4,3,2,4,3,2,3,4,3,3],7:[4,3,3,2,3,2,4,1,4,3,3,1],8:[4,2,1,4,1,2,2,1,1,2,3,2]},
                 #soundResponse = {1:[5,6,6,2,5,1,5,4,5,5,6,5],2:[5,1,6,5,1,6,5,5,4,6,6,1],3:[5,3,4,6,4,3,2,6,6,5,3,6],4:[5,1,5,6,3,3,6,6,3,3,3,6],5:[1],6:[5,5,5,5,5,3,5,5,6,4,5,6],7:[5,6,5,5,5,5,5,1,4,6,6,6],8:[5,6,1,4,1,6,1,6,5,6,6,1]},
                 behavSession = '20150409a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-08_12-12-18',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150408a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-07_19-08-51',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150407a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-04-06_15-15-25',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150406a')
cellDB.append_session(oneES)

#THIS MAY HAVE TWO SKIPPED TRIALS
oneES = eSession(animalName='test055',####################################################
                 ephysSession = '2015-04-03_15-03-35',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,4,3,2,2,1,2,2,2,2,4,3],2:[4,4,2,3,1,2,3,4,4,4,3,3],3:[4,3,4,2,3,4,2,5,3,4,2,3],4:[4,2,2,3,4,3,2,2,4,2,2,4],5:[2],6:[4,4,3,4,4,4,4,3,4,4,3,2],7:[4,4,4,3,3,3,4,4,5,4,4,4],8:[4,4,1,3,2,2,2,2,1,2,4,1]},
                 behavSession = '20150403a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',######################################################
                 ephysSession = '2015-04-01_13-04-43',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:[1],6:range(1,13),7:range(1,13),8:range(1,12)},
                 clusterQuality = {1:[4,1,2,1,2,1,4,3,1,4,2,2],2:[4,2,4,3,2,4,4,3,1,2,1,3],3:[4,3,2,2,3,4,2,3,4,2,2,4],4:[4,2,3,2,2,2,4,4,2,1,3,2],5:[4],6:[4,4,3,4,4,4,3,4,3,4,4,4],7:[4,2,2,3,4,3,2,4,2,4,4,4],8:[4,3,2,2,2,2,1,4,2,2,2]},
                 #soundResponse = {1:[5,2,1,6,6,3,2,3,6,4,1,6],2:[5,6,4,2,6,5,5,6,2,5,5,5],3:[5,6,5,5,3,4,5,4,5,2,1,5],4:[5,5,6,6,1,1,4,5,1,6,6,1],5:[5],6:[5,4,5,5,5,5,2,4,5,5,5,5],7:[5,5,5,5,5,6,1,5,1,5,4,4],8:[5,1,2,3,2,6,1,4,1,1,6,5]},
                 behavSession = '20150401a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-31_11-50-55',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150331a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-30_12-32-26',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150330a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',####################################################
                 ephysSession = '2015-03-29_23-16-17',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:[1],6:range(1,12),7:range(1,12),8:range(1,13)},
                 clusterQuality = {1:[4,1,3,1,2,2,1,2,4,2,1,1],2:[4,2,1,2,2,2,3,2,2,1,2,3],3:[4,3,3,2,5,3,3,2,2,5,3,4],4:[4,1,1,1,2,2,4,1,1,1,3,3],5:[3],6:[4,4,4,3,4,3,4,3,3,3,3],7:[4,2,3,3,3,3,2,2,3,3,4],8:[4,2,2,2,3,2,2,1,4,1,2,2]},
                 #soundResponse = {1:[5,2,1,1,1,2,6,6,4,3,3,3],2:[5,1,1,3,1,2,1,5,6,1,4,1],3:[5,2,5,5,5,1,1,2,1,5,6,4],4:[5,6,6,5,1,1,1,1,1,1,6,1],5:[1],6:[5,5,4,1,5,5,5,1,6,5,1,5],7:[5,5,6,1,5,5,1,1,1,6,4,5],8:[5,1,1,2,1,1,1,1,1,2,1,1]},
                 behavSession = '20150329a')
cellDB.append_session(oneES)

#THIS SESSION IS MESSED UP
oneES = eSession(animalName='test055',####################################################
                 ephysSession = '2015-03-28_20-36-26',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150328a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-27_12-31-11',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150327a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-26_11-18-10',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,12),4:range(1,13),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,2,2,2,1,1,1,2,1,3,2,4],2:[4,3,4,1,2,1,1,1,2,2,2,1],3:[4,2,5,5,3,3,4,3,4,2,3],4:[4,4,2,2,2,2,1,2,1,3,2,3],5:[4],6:[4,3,3,3,2,3,3,4,2,4,2,3],7:[4,3,2,4,3,4,4,2,3,3,3,3],8:[4,2,2,1,2,1,3,2,4,2,2,1]},
                 #soundResponse = {1:[5,5,1,3,3,1,1,1,1,1,2,4],2:[5,1,4,6,6,2,1,2,1,6,1,3],3:[5,5,5,2,6,5,5,1,4,6,1,5],4:[5,4,5,1,5,1,5,1,6,1,1,1],5:[3],6:[5,5,1,5,5,5,5,5,5,4,5,5],7:[5,1,1,5,1,4,4,5,1,5,1,5],8:[5,1,1,6,1,1,1,1,4,1,1,1]},
                 behavSession = '20150326a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-25_12-44-37',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,2,2,3,2,3,4,2,1,2,2,1],2:[4,2,1,2,1,3,2,1,2,2,1,4],3:[4,3,4,2,3,2,3,3,5,3,3,4],4:[4,2,2,2,4,2,1,1,3,2,1,1],5:[4],6:[4,2,3,3,3,3,3,2,4,2,2,3],7:[4,2,3,2,3,4,4,2,3,3,2,3],8:[4,2,1,1,2,3,1,2,2,2,2,2]},
                 #soundResponse = {1:[5,1,2,3,1,1,4,1,1,6,3,1],2:[5,5,1,1,1,1,1,1,6,6,6,4],3:[5,5,4,5,5,1,1,1,1,1,5,4],4:[5,1,1,1,4,5,1,6,1,1,1,1],5:[1],6:[5,4,5,6,1,6,5,3,4,5,5,1],7:[5,1,1,5,1,5,4,5,1,1,5,1],8:[4,1,2,2,1,1,3,2,1,1,1,1]},
                 behavSession = '20150325a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-24_12-33-05',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,2,4,1,2,2,3,3,2,1,4,4],2:[4,3,2,2,2,1,1,2,1,2,2,2],3:[4,2,3,4,3,3,3,2,3,3,2,4],4:[4,2,2,1,1,1,1,3,2,2,1,3],5:[1],6:[4,4,3,2,3,3,2,3,3,4,2,3],7:[4,3,3,3,2,3,3,3,3,4,2,3],8:[4,2,1,2,2,2,2,1,1,2,2,2]},
                 #soundResponse = {1:[5,6,3,1,1,5,6,1,1,1,4,5],2:[5,1,3,2,1,1,2,1,1,1,2,2],3:[5,2,5,4,1,1,5,5,1,5,5,5],4:[5,1,1,1,6,2,1,1,1,6,1,1],5:[1],6:[5,5,5,6,2,5,6,1,1,4,5,1],7:[5,1,5,1,1,1,1,1,5,4,1,1],8:[5,2,1,1,1,2,1,2,2,1,4,1]},
                 behavSession = '20150324a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-23_12-39-08',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,1,1,3,2,2,4,2,2,1,2,2],2:[4,2,2,2,2,2,2,2,4,2,2,2],3:[4,2,2,3,4,4,2,3,3,3,2,3],4:[4,2,3,2,1,2,2,2,3,2,3,1],5:[4],6:[4,2,3,3,4,2,4,2,3,3,2,4],7:[4,4,3,2,2,3,2,3,3,3,4,3],8:[4,2,2,1,1,2,3,3,2,4,1,1]},
                 #soundResponse = {1:[5,6,1,1,6,6,4,3,3,6,1,2],2:[5,5,2,2,1,2,1,3,6,2,2,1],3:[5,1,1,5,4,5,5,6,5,6,6,1],4:[5,5,1,6,3,1,1,5,1,5,5,5],5:[1],6:[5,2,1,5,4,5,5,3,1,2,5,5],7:[5,4,1,5,6,1,5,1,1,5,5,1],8:[5,3,1,6,1,1,1,1,6,4,3,6]},
                 behavSession = '20150323a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-22_19-01-22',
                 clustersEachTetrode = {1:range(1,13),2:range(1,12),3:range(1,13),4:range(1,13),5:range(1,13),6:[1],7:range(1,12),8:range(1,13)},
                 clusterQuality = {1:[4,1,3,2,2,2,2,2,4,2,2,2],2:[4,2,2,2,4,1,3,2,2,2,2],3:[4,3,1,3,3,3,3,2,2,4,3,1],4:[4,3,1,2,1,4,2,2,3,2,2,3],5:[4,3,3,2,3,3,2,2,4,3,3,4],6:[2],7:[4,1,3,3,2,3,4,3,2,4,2],8:[4,2,1,2,2,2,2,1,4,1,1,3]},
                 #soundResponse = {1:[5,1,1,1,6,6,3,1,4,1,3,5],2:[5,6,1,2,4,1,6,6,6,1,1,5],3:[5,5,1,6,6,6,5,5,1,4,6,5],4:[5,1,6,6,5,4,5,1,1,5,1,1],5:[5,5,1,5,5,5,1,5,5,5,6,4],6:[2],7:[5,1,1,1,5,1,5,1,5,5,5,5],8:[5,6,1,3,1,2,1,1,4,1,6,2]},
                 behavSession = '20150322a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-21_15-33-38',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,2,2,2,1,3,2,4,2,3,2,2],2:[4,4,3,4,2,2,2,2,2,3,2,2],3:[4,2,2,2,3,2,4,3,5,4,2,3],4:[4,2,2,2,2,1,3,2,3,5,2,4],5:[4],6:[4,2,2,4,3,4,2,2,3,4,3,4],7:[4,3,2,2,1,3,4,3,4,3,2,2],8:[4,2,2,3,4,3,1,2,1,2,2,2]},
                 #soundResponse = {1:[5,6,6,3,1,2,3,4,3,1,3,2],2:[5,4,6,4,3,6,1,2,3,3,2,3],3:[5,5,1,6,1,6,5,1,3,4,1,6],4:[5,1,5,1,6,1,1,6,1,1,6,5],5:[6],6:[5,1,3,3,1,5,5,5,1,4,2,5],7:[5,5,1,5,1,1,5,1,4,1,1,1],8:[5,1,1,6,4,1,2,1,2,1,2,1]},
                 behavSession = '20150321a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',###########################################################
                 ephysSession = '2015-03-20_11-34-22',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,12),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,3,2,2,2,2,1,2,2,2,3,4],2:[4,2,4,2,2,2,1,2,3,2,2,2],3:[4,2,4,2,2,3,2,4,3,3,3,3],4:[4,3,2,2,2,2,3,3,2,1,2],5:[3],6:[4,1,3,4,2,1,3,2,3,1,2,4],7:[4,1,3,2,3,3,3,4,2,4,2,3],8:[4,2,2,2,2,2,2,4,3,2,1,2]},
                 #soundResponse = {1:[5,2,2,6,1,1,3,3,1,2,1,4],2:[5,2,4,1,3,2,2,1,6,1,6,1],3:[5,3,5,1,1,1,5,4,5,5,5,5],4:[5,1,5,1,1,6,1,1,5,1,6,5],5:[1],6:[5,6,1,5,5,1,1,5,5,1,5,4],7:[5,1,1,1,1,6,1,5,1,4,3,1],8:[5,6,1,1,6,1,1,4,1,1,6,2]},
                 behavSession = '20150320a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-19_15-04-52',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,12),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,2,2,2,2,4,2,3,3,2,2,4],2:[4,3,2,2,2,3,2,4,2,2,2,2],3:[4,2,3,4,3,3,2,4,3,2,3,4],4:[4,1,1,3,3,2,4,2,2,2,2],5:[4],6:[4,4,2,2,2,2,2,1,3,2,4,3],7:[4,2,2,3,3,4,3,3,1,3,2,2],8:[4,2,2,3,2,4,1,2,2,2,2,2]},
                 #soundResponse = {1:[5,1,2,1,1,4,6,1,1,3,1,3],2:[5,6,1,1,1,6,1,4,1,2,1,5],3:[5,1,5,4,1,6,5,5,1,5,1,4],4:[5,1,1,1,1,2,5,1,6,1,6,5],5:[1],6:[5,4,2,5,5,5,5,5,1,2,5,5],7:[5,1,2,6,1,4,1,1,1,1,2,1],8:[5,1,6,1,1,4,1,1,6,6,6,1]},
                 behavSession = '20150319a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-18_15-42-32',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,2,3,4,2,2,2,2,2,2,3,2],2:[4,3,2,1,3,2,2,4,1,2,3,2],3:[4,3,3,3,3,3,2,3,3,1,2,4],4:[4,2,3,2,3,3,4,2,2,2,3,2],5:[2],6:[4,1,2,3,2,4,2,2,3,2,4,2],7:[4,3,1,2,1,3,3,2,3,2,3,4],8:[4,2,2,2,2,1,3,3,4,2,2,2]},
                 #soundResponse = {1:[5,1,3,4,2,1,6,1,1,1,6,3],2:[5,1,1,2,6,6,5,4,1,6,1,1],3:[4,1,1,2,6,5,1,1,1,1,1,1],4:[5,1,3,1,1,1,4,1,6,1,6,1],5:[3],6:[5,3,5,1,2,5,5,1,5,5,4,3],7:[5,1,1,2,1,6,1,3,1,5,1,4],8:[5,1,1,1,1,6,1,1,4,6,1,6]},
                 behavSession = '20150318a')
cellDB.append_session(oneES)

#THIS SESSION IS MESSED UP
oneES = eSession(animalName='test055',############################################################
                 ephysSession = '2015-03-17_12-21-27',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150317a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-16_11-20-30',
                 clustersEachTetrode = {1:range(1,13),2:range(1,12),3:range(1,13),4:range(1,13),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,2,1,2,2,3,2,2,4,2,3,3],2:[4,3,3,4,3,1,1,3,1,3,3],3:[4,4,3,4,2,3,3,3,2,3,2,4],4:[4,3,2,3,2,3,2,2,3,2,3,4],5:[4],6:[4,2,3,1,2,4,2,2,2,2,2,3],7:[4,2,2,1,2,2,3,3,4,2,3,1],8:[4,3,2,2,2,2,2,2,2,2,4,2]},
                 #soundResponse = {1:[5,3,6,1,1,3,1,2,4,3,6,5],2:[5,1,5,4,1,5,6,5,2,1,3,5],3:[5,4,1,4,1,1,5,5,5,5,1,5],4:[5,1,1,1,5,5,5,1,5,1,1,4],5:[1],6:[5,5,5,1,5,4,1,1,3,5,5,1],7:[5,2,2,1,6,5,1,1,4,6,1,1],8:[5,1,1,1,6,1,1,1,1,2,4,1]},
                 behavSession = '20150316a')
cellDB.append_session(oneES)


oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-15_13-08-56',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,12),4:range(1,12),5:[1],6:range(1,13),7:range(1,13),8:range(1,13)},
                 clusterQuality = {1:[4,2,2,2,3,2,2,3,4,2,3,3],2:[4,2,3,2,3,2,1,2,4,3,2,1],3:[4,3,3,2,3,4,3,2,2,3,2],4:[4,2,2,3,2,2,3,4,3,3,3],5:[2],6:[4,2,1,3,2,3,2,4,1,2,2,3],7:[4,2,1,2,2,2,1,3,2,3,4,2],8:[4,2,2,2,2,2,2,3,3,2,2,1]},
                 #soundResponse = {1:[4,6,1,1,3,2,1,1,4,6,6,5],2:[5,1,5,5,1,6,2,3,4,3,5,3],3:[5,5,1,6,1,4,5,5,1,5,5,5],4:[5,1,1,6,5,2,1,4,5,1,6,5],5:[1],6:[5,5,3,1,5,1,5,4,3,3,5,6],7:[5,1,1,2,1,2,3,1,1,1,4,1],8:[4,2,3,3,2,1,2,1,1,1,2,1]},
                 behavSession = '20150315a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-13_11-53-29',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150313a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-12_11-39-19',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150312a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-11_13-23-02',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150311a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-10_14-08-40',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150310a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-09_15-15-58',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150309a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',############################################################
                 ephysSession = '2015-03-08_21-05-54',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150308a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-07_21-00-17',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150307a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-06_12-30-25',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150306a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',#################################################################
                 ephysSession = '2015-03-05_14-12-36',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150305a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-04_13-02-28',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150304a')
cellDB.append_session(oneES)
oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-03_11-42-14',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150303a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-02_13-35-20',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150302a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-03-01_16-53-27',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150301a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-02-28_19-02-10',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150228a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',##################################################
                 ephysSession = '2015-02-27_13-15-39',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150227a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-02-26_13-06-01',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150226a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-02-25_12-38-09',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150225a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',###############################################################
                 ephysSession = '2015-02-24_13-19-06',
                 clustersEachTetrode = {1:range(1,13)},#,2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150224a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-02-23_13-23-03',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150223a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-02-22_22-42-06',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150222a')
cellDB.append_session(oneES)

#THIS BEHAVIOR SESSION IS MESSED UP
oneES = eSession(animalName='test055',#######################################################################
                 ephysSession = '2015-02-21_18-38-13',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150221a')
cellDB.append_session(oneES)

oneES = eSession(animalName='test055',
                 ephysSession = '2015-02-20_11-42-48',
                 clustersEachTetrode = {1:range(1,13),2:range(1,13),3:range(1,13),4:range(1,13),5:range(1,13),6:range(1,13),7:range(1,13),8:range(1,13)},
                 behavSession = '20150220a')
cellDB.append_session(oneES)
'''
