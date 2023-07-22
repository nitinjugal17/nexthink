import sys , csv, getopt, time
import wmi
import psutil
import gc
import tracemalloc
from collections import defaultdict 
import profiler , warnings

def __get_pid_by_name_windows(process_name, filename):
  """
  Args:
    process_name: The name of the process.

  Returns:
    The process ID.
  """
  try:
    process = wmi.WMI().Win32_Process()
    fileclear = open(filename, "w+")
    writer = csv.writer(fileclear, delimiter=",")
    writer.writerow([""])
    fileclear.close()
    for p in process:
      # fileclear = open(filename, "a")
      # writer = csv.writer(fileclear, delimiter=",")
      # writer.writerow([p.Name])
      if process_name in p.Name:
        if process_name == p.Name:
          return p.ProcessId
        else:
          raise Exception

    return 0
  except Exception as ex:
    print(ex)
    print("## YOU HAVE ENTERED A WRONG PROCESS NAME : {}  WAS NOT FOUND , ARE YOU TRYING TO FIND : {} \n  \
          ********#############  PLEASE RETRY WITH CORRECT PARAMETERS | Ex. | python nexthink.py -d 10 -n chrome ###########***********".format(process_name, p.Name) )
    return 0
  finally:
    pass

def __detect_leak(filename, mem_dict, cpu_dict, memaverage, cpuavg, leakpercent: int, leakpercent2: int ):
  val_increase = round(leakpercent/round(memaverage,3) * 100,3)
  leakmem_indi = round(memaverage + val_increase, 3)
  # print(val_increase, leakmem_indi)
  for t, mem in mem_dict.items():
    # print(t,mem)
    if leakmem_indi < round(mem, 3):
      outxt = '\nApplication Leaks at Point Time: {} | Actual Memory Usage: {} | Average Memory of Execution is : {}'.format(time.ctime(t), round(mem, 3), round(memaverage, 3))
      # print(outxt)
      warnings.warn(outxt)
      fileclear = open(filename, "a")
      writer = csv.writer(fileclear, delimiter=",")
      writer.writerow(['WARNING !! POSSIBLE MEMORY LEAK !!', outxt, '\nWARNING !! POSSIBLE MEMORY LEAK !!'])
    else:
      pass

  # print(leakpercent2, cpuavg)
  # cpu_val = round(leakpercent2/round(cpuavg,4) * 100, 3)
  # leakcpu_indi = round(cpuavg + cpu_val, 3)

  cpu_val = round(cpuavg, 3) + leakpercent2
  leakcpu_indi = round(cpuavg + cpu_val, 3)
  # print(cpu_val, leakcpu_indi)
  for ti, per in cpu_dict.items():
    # print(ti,per)
    if leakcpu_indi < round(per, 3):
      otxt = '\nApplication Leaks at Point Time: {} | Actual CPU Usage: {} | Average CPU Usage of Execution is : {}'.format(time.ctime(ti), round(per, 3), round(cpuavg, 3))
      # print(otxt)
      warnings.warn(otxt)
      fileclear = open(filename, "a")
      writer = csv.writer(fileclear, delimiter=",")
      writer.writerow(['WARNING !! POSSIBLE CPU LEAK DUE TO MEMORY MISMAGEMENT !!', otxt, '\nWARNING !! POSSIBLE MEMORY LEAK !!'])
    else:
      pass



def dump_process_data_to_csv(process_name, filename, duration, cputhres, memthres, bars=80):
  """Dumps the process data for the process with the given PID to a CSV file."""
  """Monitors the process with the given PID for the given duration and finds the average memory usage of the process."""

  start_time = time.time()
  mem_usage = 0
  mem_mb = 0
  cpu_usage = 0
  mem_usage_dict = defaultdict(int) #value type tracking and mapping with time 
  cpu_usage_dict = defaultdict(int) #value type tracking and mapping with time
  pid = __get_pid_by_name_windows(process_name, filename)
  print("Memory Sampling for Process id : {} : {}".format(pid, process_name))
  if pid != 0:
    fileclear = open(filename, "a")
    writer = csv.writer(fileclear, delimiter=",")
    writer.writerow(["PID", "Name", "CPU Use", "Mem Usage", "Priv Mem Usage", "File Handles"])
    fileclear.close()
    for x in range(0,duration):
      time_bar = '█' * int(x * bars/30) + '->' * (bars - int(x * bars))
      process = psutil.Process(pid)
      mem_usage += process.memory_percent()
      mem_mb += process.memory_info().rss / (1024 ** 2)
      mem_usage_dict[time.time()] += process.memory_info().rss / (1024 ** 2)
      cpu_usage += process.cpu_percent()
      cpu_usage_dict[time.time()] += process.cpu_percent()
      with open(filename, "a", newline="") as csvfile:
          writer = csv.writer(csvfile, delimiter=",")
          # writer.writerow(["PID", "Name", "CPU %", "Mem Usage %", "Priv Mem Usage", "File Handles"])
          process = psutil.Process(pid)
          writer.writerow([process.pid, process_name, process.cpu_percent(), process.memory_percent(), process.memory_info().rss / (1024 ** 2), process.num_handles()])
      print('\r Capture with Duration {}s in Progress used Process Name: {} | {}  \n'.format(duration, process_name, time_bar), end='\r')
      time.sleep(.6)
    end_time = time.time()
    avg_mem_usage = mem_usage / duration
    avg_mem_mb = mem_mb / duration
    cpu_avg = cpu_usage / duration
    str_out = "The average memory % usage of the process name {} is {} % | Average Memory Used : {} MB | Average CPU Usage : {}% | Start Time :{} | End Time: {}".format(process_name, round(avg_mem_usage,3), avg_mem_mb,round(cpu_avg, 3), time.ctime(start_time), time.ctime(end_time)) 
    print(str_out)
    with open(filename, "a", newline="") as csvfile:
      writer = csv.writer(csvfile, delimiter=",")
      writer.writerow([str_out])
    __detect_leak(filename, mem_usage_dict, cpu_usage_dict, avg_mem_mb, cpu_avg, cputhres, memthres)
  else:
    fileclear = open(filename, "a")
    writer = csv.writer(fileclear, delimiter=",")
    strout = "Please Enter Correct Process Name or Check Permission of Script Unable to find Process: {} , PID : {} | PLEASE RETRY WITH CORRECT PROCESS NAME".format(process_name , pid)
    print(strout)
    writer.writerow([strout])
    exit

if __name__ == "__main__":
  process_name = ""
  filename = "./process_data.csv"
  duration = 5 # default duration
  cputhres = 5 # default cpu threshold for leak check
  memthres = 10 # default mem threshold for leak check
  strret = '\n*** Python Script Self Execution Memory Profiling ****'
  opts, args = getopt.getopt(sys.argv[1:], "d:n:ct:mt:", ['duration', 'process_name', 'cputhres', 'memthres'])
  if sys.argv[1]:
    process_name = sys.argv[1]
  for opt, arg in opts:
    if opt == '-d':
      duration = arg
    if opt == '-n':
      process_name = arg
    if opt == '-ct':
      cputhres = arg
    if opt == '-mt':
      memthres = arg

  # Self Memory Profiling and outputing as csv data
  tracemalloc.start(10)
  print("Using Params Duration in sec: {} | Process Name: {} | Leak Memory Threshold with : {}% | CPU Threshold Increase: {}%".format(duration, process_name, memthres, cputhres))
  dump_process_data_to_csv(process_name, filename, int(duration), int(cputhres), int(memthres))
  gc.collect()
  profiler.snapshot()
  strret += profiler.display_stats()
  strret += profiler.compare() + '\n'
  strret += profiler.print_trace() + '\n'
  with open(filename, "a", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow([strret])
  

