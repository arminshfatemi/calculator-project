# basic-calculator-project
A Simple calculator built with python tkinter

### How to Run

1. First clone the project and cd calculator-project
```commandline
git clone <url of the project>
cd calculator-project
```
2. Make a python virtual env
```commandline
python3 -m venv <name of your venv>
```
3. Activate your venv
#### on linux
```commandline
source ./venv/bin/activate
```
#### on windows
```commandline
venv/bin/activate
```

4. Install the python packages
```commandline
pip install -r requirements.txt
```
5. Run the file
```commandline
python main.py
```

### Error
if you have error like this :

ERROR: Could not find a version that satisfies the requirement tkinter (from versions: none)

ERROR: No matching distribution found for tkinter

first make sure you have installed packages and venv is activated 
if it didn't fixed do below command 

```commandline
 sudo dnf install python3.<your version>-tkinter  
```

and i hope it fixed 

Enjoy.