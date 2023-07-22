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