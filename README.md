# Diversion Monitor
Monitor diversionary airfield METARs and TAFs and alert user to 
change of colour states and TAF status.

Data is provided by a web features server (WFS) running on a Visual Weather
sandbox within the Met Office DMZ. Note that this server cannot be accessed 
via DirectAccess connections only via a 'green cable' connection.
If you get a message 'Error retrieving data - will retry...'  it means that the
app cannot access the data server. 

To use the app just enter up to 10 ICAOs and press 'Start Monitoring'. 
You can press 'Update Now' at anytime to check for more recent data. In
addition ICAOs can be added/deleted/changed on the fly (though obviously you will need
at least two METAR reports before previous colour state can be displayed).

The Windows executable was built using PyInstaller with a Python 3.5 environment 
wrapped up in the executable (so need to even install Python). 


##### Version History:

- v1.0b 15/08/17: At the moment alert messages will not take the top focus from 
other windows but it may possible to change this behaviour can be changed if required 
in the future.
 

