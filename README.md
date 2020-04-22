# Diversion Monitor
Monitor diversionary airfield METARs and TAFs and alert user to 
change of colour states and TAF status.

Data is provided by the Met Office MetDB.
If you get a message 'Error retrieving data - will retry...'  it means that the
app cannot access the data server. 

To use the app just enter up to 10 ICAOs and press 'Start Monitoring'. 
You can press 'Update Now' at anytime to check for more recent data. In
addition ICAOs can be added/deleted/changed on the fly (though obviously you will need
at least two METAR reports before previous colour state can be displayed).

The Windows executable was built using PyInstaller with a Python 3 environment 
wrapped up in the executable (so need to even install Python). 

