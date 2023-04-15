import os, sys
from termcolor import colored, cprint

import gpxpy
import gpxpy.gpx

VERSION = "0.1"
TRACK_POINT_LIMIT = 8000
SIMPLIFY_COUNT = 600
    
def prepare_gpx():
    cprint("Please provide a GPX file (full path)", 'red')
    fpath = input(">")
    if os.path.exists(fpath):
        if os.path.isfile(fpath):
            file = open(fpath, 'r')
            gpx = gpxpy.parse(file)
            cprint("GPX file successfully loaded!", 'green')

            cprint("\n---------- GPX FILE ----------", 'white')
            cprint("| Filename: " + os.path.basename(fpath), 'white')            
            cprint("| # of tracks : " + str(len(gpx.tracks)), 'white')
            cprint("------------------------------", 'white')


            if len(gpx.tracks) > 0:
                for t in gpx.tracks:
                    pi = 0
                    for s in t.segments:
                        pi += len(s.points)
                    cprint("Found a track with " + str(pi) + " points.", 'blue')

                    if pi > TRACK_POINT_LIMIT:
                        cprint("Track exceeds maximum number of points.", 'red')
                        
                        cprint("Splitting GPX file...", 'red')
                        i = 0
                        j = 0
                        k = 1
                        old_j = 0
                        
                        for s in t.segments:
                            i += len(s.points)
                            j += 1
                            if i > TRACK_POINT_LIMIT:
                                fout = os.path.splitext(os.path.basename(fpath))[0] + '-' + str(k) + '.gpx'
                                new_gpx = gpxpy.gpx.GPX()
                                new_track = gpxpy.gpx.GPXTrack()
                                new_track.name = os.path.splitext(os.path.basename(fpath))[0] + '-' + str(k)

                                chunk = t.segments[old_j:j]
                                for c in chunk:
                                    new_track.segments.append(c)                                    
                                new_gpx.tracks.append(new_track)
                                del chunk
                                
                                cprint("Writing to new file " + fout + "...", 'white')
                                with open(fout, 'w') as f:
                                    f.write(new_gpx.to_xml())

                                cprint("Simplifying GPX with GPSBabel...", 'red')
                                os.system("gpsbabel -r -i gpx -f " + fout + " -x simplify,count=" + str(SIMPLIFY_COUNT) + " -o gpx -F " + fout)

                                i = 0
                                old_j = j
                                k += 1
        else:
            cprint("The specified file was not found.", 'red')
    else:
        cprint("The specified path does not exist.", 'red')

if __name__ == '__main__':
    cprint("Welcome to etrex-x2x-tools", 'red')
    cprint("Select a mode:", 'red')
    
    cprint("\t1: Prepare GPX file as a track")
    
    m = ""
    while isinstance(m, int) == False:
        m = input(">")
        try:
            m = int(m)
        except:
            continue
            
        
    print("\n")

    if m == 1:
        prepare_gpx()

    cprint("\nGoodbye.", 'white')
