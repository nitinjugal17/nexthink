#
# Author : Jugal Kishore <jugalk1993@gmail.com>
# Homepage : https://nitinjugal17.github.io/
# License : BSD http://en.wikipedia.org/wiki/BSD_license
# Copyright (c) 2023, Jugal Kishore
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met: 
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer. 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution. 
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Purpose : This script aims to gather all memory profiling for a windows process and log them in a csv file within execution directory, with appropriate memory leak indicators

import tracemalloc
 
# list to store memory snapshots
snaps = []
 
def snapshot():
	snaps.append(tracemalloc.take_snapshot())
 
 
def display_stats():
	strret = "\n*** top 5 stats grouped by filename *** \n"
	stats = snaps[0].statistics('filename')
	# print("\n*** top 5 stats grouped by filename ***")
	for s in stats[:10]:
		#print(s)
		strret += str(s) + '\n'
	return strret
 
 
def compare():
	first = snaps[0]
	strret = "\n*** top 10 stats ***\n"
	for snapshot in snaps[1:]:
		stats = snapshot.compare_to(first, 'lineno')
		# print("\n*** top 10 stats ***\n")
		for s in stats[:10]:
			#print(s)
			strret += str(s) + '\n'
	return strret
 
 
def print_trace():
	# pick the last saved snapshot, filter noise
	snapshot = snaps[-1].filter_traces((
    	    tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
    	    tracemalloc.Filter(False, "<frozen importlib._bootstrap_external>"),
    	    tracemalloc.Filter(False, "<unknown>"),
	))
	largest = snapshot.statistics("traceback")[0]
 
	strret = f"*** Trace for largest memory block - ({largest.count} blocks, {largest.size/1024} Kb) ***"
	for l in largest.traceback.format():
		#print(l)
		strret += str(l) + '\n'
	
	return strret