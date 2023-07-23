
## 🚀 About Me
An Automation Engineer [SDET] , Providing Test Solutions Since 2014...

- [Jugal Kishore](https://nitinjugal17.github.io/)
## Author Details

- [@nitinjugal17](https://www.github.com/nitinjugal17)

- [@jugalk](https://www.linkedin.com/in/jugalk/)

# Process resources monitoring app

A console application in Python that, for a given Process Name.


## Features

• Periodically gathers process metrics (for a specified amount of time).

• Creates a report of the gathered process metrics (in CSV format).

• Outputs the average for each process metric.

• Detects possible memory leaks and raises a warning 
 





## Installation & Requirements

•Install Python 3.11.3 or Higher

**Tested on Environment:**

• Windows 11 Home Edition 64 Bit

• Developed on VS Studio Code


```cmd
  cd my-project
  pip install ./requirements.txt
  
```
**Requirements :**

•psutil==5.9.5 or Higher

•pywin32==306 or Higher

•WMI==1.5.1 or Higher

** Note : Some Functions are not supported on Python Version 3.10 or below, Suggested Installation to be used is Python 3.11 or Higher.
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/nitinjugal17/nexthink.git
```

Go to the project directory

```bash
  cd nexthink
```

Install dependencies

```bash
  pip install ./requirements.txt
```

Start Memory Profiling with Process name

```bash
  python nexthink.py chrome.exe
```
Start Memory Profiling with Process name using :

•Param (-n[process_name])

•Param (-d[duration]) - Default Value : 5

•Param (-ct[cpu threshold increase in %]) - Default Value : 5

•Param (-mt[Priv Memory threshold increase in %]) -Default Value:10
```bash
  python nexthink.py -n chrome.exe
```
Start Memory Profiling with Process name using:

•Param (-n[process_name])

•Param (-d[duration])

•Param (-ct[cpu threshold increase in %]) - Default Value : 5

•Param (-mt[Priv Memory threshold increase in %]) -Default Value:10
```bash
  python nexthink.py -n chrome.exe -d 100 
```
Start Memory Profiling with Process name using:

•Param (-n[process_name])

•Param (-d[duration])

•Param (-ct[cpu threshold increase])

•Param (-mt[Priv Memory threshold increase in %]) -Default Value:10
```bash
  python nexthink.py -n chrome.exe -d 100 -ct 5
```
Start Memory Profiling with Process name using:

•Param (-n[process_name])

•Param (-d[duration])

•Param (-ct[cpu threshold increase in %])

•Param (-mt[Priv Memory threshold increase in %])
```bash
  python nexthink.py -n chrome.exe -d 100 -ct 5 -mt 10
```
## Parameter Reference

#### Usage without param
```http
  python nextthink.py chrome.exe
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `` | `string` | **Required**. Your Process Name |

```http
 python nextthink.py -p -d -ct -mt
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `-p` | `string` | **Required**. Your Process Name |
| `-d` | `int` | **Not Required**. Duration Of Profiling |
| `-ct` | `int` | **Not Required**. Your API key |
| `-mt` | `int` | **Not Required**. Your API key |
#### Get item

```http
  python nextthink.py -p -d -ct -mt
```

| Parameter | Usage     | Default Value                       |
| :-------- | :------- | :-------------------------------- |
| `-p` | `Process Name` | **None**. *Mandatory* |
| `-d` | `Duration in secs` | **Not Required**. *5* |
| `-ct` | `Cpu Leak Indentifier in %` | **Not Required**. *5*|
| `-mt` | `Priv Mem Leak Indentifier in %` | **Not Required**. *10* |

#### python nexthink.py chrome.exe

1. **Checks for Chrome.exe Process** in executed environment.
2. Dumping of **PID,Name,CPU Usage %, Total Mem Usage %,Priv Mem Usage in Mb, File Handles Count** to **process.data.csv** within same execution directory.
3. **-ct** Helps to decide Memory-Leak check due to Cpu Increase % by Using Input.
4. **-mt** Helps to decide Memory-Leak check due to Private Memory Usage % by Using *User Input*.


## License

[Pywin32](https://github.com/mhammond/pywin32/blob/main/Pythonwin/License.txt) - Lic. [PSF 2.0](https://spdx.org/licenses/PSF-2.0.html)

[WMI](https://github.com/tjguk/wmi) - Lic. [MIT](http://www.opensource.org/licenses/mit-license.php)

[Psutil](https://github.com/giampaolo/psutil/blob/master/LICENSE) - Lic. [BSD3](https://docs.eggplantsoftware.com/performance/license-psutil-bsd/)



## Screenshots & Output

![App Screenshot](https://github.com/nitinjugal17/nexthink/blob/main/screenshots/Screenshot_without_param.png)

```http
 PS C:\Git\nexthink> python .\nexthink.py -p chrome.exe -d 100 
********Using Params Duration in sec: 100 | Process Name: chrome.exe | WITH Leak Memory Threshold : 10% | WITH CPU Threshold : 5%*******
Memory Sampling for Process id : 17432 : chrome.exe
 Capture with Duration 100s in Progress used Process Name: chrome.exe | █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
 The average memory % usage of the process name chrome.exe is 1.84 % | Average Memory Used : 295.54328125 MB | Average CPU Usage : 0.0% | Start Time :Sun Jul 23 08:50:20 2023 | End Time: Sun Jul 23 08:51:29 2023
******Parameterized Memory Leak Check in Percentage 10 | Memory Threshold Should Not Exceed :298.92MB, Memory Leak Indicator Value Increase Param: 3.38MB, Avg Priv Mem Usage: 295.54******
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:35 2023 | Actual Memory Usage: 299.52 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:35 2023 | Actual Memory Usage: 299.35 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:36 2023 | Actual Memory Usage: 299.41 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:42 2023 | Actual Memory Usage: 299.92 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:43 2023 | Actual Memory Usage: 301.56 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:44 2023 | Actual Memory Usage: 301.57 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:44 2023 | Actual Memory Usage: 301.09 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:45 2023 | Actual Memory Usage: 300.85 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning: 
Application Leaks at Point Time: Sun Jul 23 08:50:45 2023 | Actual Memory Usage: 300.43 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:46 2023 | Actual Memory Usage: 300.24 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:47 2023 | Actual Memory Usage: 300.23 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:48 2023 | Actual Memory Usage: 300.23 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:49 2023 | Actual Memory Usage: 302.05 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:50 2023 | Actual Memory Usage: 300.18 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:51 2023 | Actual Memory Usage: 300.18 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:51 2023 | Actual Memory Usage: 302.16 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:52 2023 | Actual Memory Usage: 304.02 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:53 2023 | Actual Memory Usage: 304.45 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:50:53 2023 | Actual Memory Usage: 301.27 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
C:\Git\nexthink\nexthink.py:83: UserWarning:
Application Leaks at Point Time: Sun Jul 23 08:51:29 2023 | Actual Memory Usage: 299.07 | Average Memory of Execution is : 295.54
  warnings.warn(outxt)
******Parameterized Cpu Leak Check in Percentage 5 | CPU Usage Threshold Should Not Exceed :5.0%, CPU Spike Indicator Value Increasing Param :5.0%, Avg Cpu Usage:0.0******
PS C:\Git\nexthink>
```