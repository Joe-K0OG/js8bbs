##############################################
# Settings file for the js8bbs python script #
##############################################

# Triggers may be upper or lower case but MUST have a "?" at the end.

# This specifies external executables which produce output, if desired.
# The trigger labels must be of the form as shown below.
# Leave output blank if no output is needed to send back to requester.
#
# You may add as many sets as you like - there is no practical limit.
# All three parameters must be specified, even if a null "" is used
# for the outfile parameter for executables which generate no output.
# Quotations for the parameters may be either ' or " marks, but both
# on the same line must be the same mark type for the outer quotations.
#
# With this framework, a crude bulletin-board-system could be built.

# Moved the helpfile function to the functional triggers.
# Notice that the executable file is null, so this just reads
# a text file.
trigger_1 = "HELP?"
exefile_1 = ""
outfile_1 = "help.txt"

# Run script to download and report current solar conditions.
trigger_2 = 'SOLAR?'
exefile_2 = './solarget'
outfile_2 = 'solaroutput'

# Can even use system commands and redirect to
# an output file for a report.
trigger_3 = 'DATE?'
exefile_3 = 'date +%T > date.txt ; ./solarget ; cat solaroutput >> date.txt'
outfile_3 = 'date.txt'

# Here is a trigger with no output data, as an example.
# This will pop up a message window in Linux.  When you close the
# message box, it will send a success notice to requester.
trigger_4 = 'ruthere?'
exefile_4 = 'xmessage "Someone is asking if you are at the JS8 keyboard."'
outfile_4 = ''
