## js8bbs ##
Python-based framework for building a Bulletin Board System using JS8Call as the modem.  This is intended as a conceptual development, and it would be good for a "real" programmer to take this on and write more sophisticated code than what I'm capable of.

This is a fork of the help_text.py script developed by Paul VandenBosch, KC8WBK.
Thanks Paul for your wx_server and help_text projects!
See Paul's projects at https://github.com/skyl4rk/

Instructions and examples for setting up the system can be found in the settings.py file.

<b>NOTE:</b>  This project is only intended to be a proof of concept.  I do not intend to further develop or provide support for it, but would like to see someone with programming skill and patience develop a JS8Call BBS back-end.  Such BBS tools can be useful for fun, but could also be useful for emergency communications support.

73,<br>
-Joe-<br>
K0OG<br>

=====<br>
Original JS8Help By Paul VandenBosch - KC8WBK

Modified by Joseph A. Counsil - K0OG - 6/24/2022
 * Added user paramater block
 * Added a second trigger to execute an external program
    specifying an executable file and an output file
    to read and report back to requesting station's inbox.
    If no output is generated, a "CMD COMPLETE" message
    is sent to requester's RX Text window (not to inbox).
    
Modified - K0OG - 6/27/2022
 * Added external settings file settings.py
 * Modified trigger command routine to execute multiple triggers
 * Moved HELP? trigger to use the functional triggers.
 * Limited triggers to be the first word after the callsigns.

 With this framework, and crude JS8Call BBS can be built.

----- NEXT STEPS -----
* The next step is to allow the remote station to pass parameters
  to the server to modify queries.
* Add an output log file of commands received, date, time
  requesting station callsign, and response data.
  
=====
