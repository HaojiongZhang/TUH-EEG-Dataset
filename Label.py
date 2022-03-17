#!/usr/bin/env python

# usage:
#  nedc_print_labels.py *.lbl *.tse
#
# This script loads an annotation and displays it to stdout.
#------------------------------------------------------------------------------

# import system modules
#
import os
import sys

# import NEDC modules
#
import sys_tools.nedc_cmdl_parser as ncp
import sys_tools.nedc_file_tools as nft
import sys_tools.nedc_ann_tools as nat

#------------------------------------------------------------------------------
#
# global variables are listed here
#
#------------------------------------------------------------------------------

# determine script location
#
SCRIPT_LOC = os.path.dirname(os.path.realpath(__file__))

# define path to help and usage files
#
HELP_FILE = SCRIPT_LOC + "/help/nedc_print_labels.help"
USAGE_FILE = SCRIPT_LOC + "/help/nedc_print_labels.usage"

# define a line width
#
LINE_WIDTH = int(80)

#------------------------------------------------------------------------------
#
# the main program starts here
#
#------------------------------------------------------------------------------

# main: nedc_print_labels
#
def main(argv):

    # declare local variables
    #
    lev = int(0)
    sub = int(0)
    ann = nat.Annotations()
    num_files_att = int(0)
    num_files_proc = int(0)
    files = []
    
    # create a command line parser
    #
    parser = ncp.CommandLineParser(USAGE_FILE, HELP_FILE)
    parser.add_argument("files", type = str, nargs = '*')
    parser.add_argument("-level", type = float)
    parser.add_argument("-sublevel", type = float)
    parser.add_argument("-help", action="help")

    # parse the command line
    #
    args = parser.parse_args()

    if len(args.files) == 0:
        parser.print_usage()
        exit(-1)

    # set option and argument values
    #
    if args.level is not None:
        lev = int(args.level)

    if args.sublevel is not None:
        sub = int(args.sublevel)

    # loop over all arguments
    #                 
    for ifile in args.files:

        # reset flag
        #
        is_list = True

        # if version check passes, ifile is not a list
        #
        for vers in nat.VERSIONS:

            # get full path to file, and get it's version
            #
            if nft.get_version(nft.get_fullpath(ifile)) == vers:
                is_list = False
                break

        if is_list is True:
            files += nft.get_flist(ifile)
        else:
            files.append(ifile)

    # loop over all files
    #
    for fname in files:

        # increment the counter for files attempted
        #
        num_files_att += 1
        print "%s" % ("-" * LINE_WIDTH)
        print "%d: %s" % (num_files_att, fname)

        # get full path to fname, and load
        #
        status = ann.load(nft.get_fullpath(fname))
        if status == False:
            print "%s (%s: %s): error loading label file (%s)" % \
                (sys.argv[0], __name__, "main", fname)

        # display the annotation
        #
        if status is True:
            status = ann.display(lev, sub)
            if status is True:
                num_files_proc += 1
        print ""

        # get the annotations
        #
        channel = -1
        annotations = ann.get(lev, sub, channel)

        # process as needed
        # ...
        
    #
    # end of loop

    # display the results
    #
    print "%s" % ("-" * LINE_WIDTH)
    print "Summary:"
    print " %s: processed %d out of %d files successfully>" % \
        (sys.argv[0], num_files_proc, num_files_att)
    print ""
#
# exit gracefully

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv[0:])

#
# end of file
