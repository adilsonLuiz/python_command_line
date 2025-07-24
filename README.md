# Python CLI Software 

# createArray

`createArray` is a utility intended to be used from the terminal. To use it globally from any directory, make sure to add the source file to your system's `PATH`.

The goal of `createArray` is to generate an array from a string-based data source.

---

## Input Format

A valid data source is a single string with elements separated by commas.
You Can call the script by the prompt line commander

**Example 01: Call the script with Python interpreter first.**

`python CreateArray.py --break 3 'Mouse, Keyboard, Monitor, Webcam, Headset, Microphone, Chair, Desk'`

**Example 02: If you configure the PATH in your system, you can call the script only by the name**
`CreateArray.py --break 3 'Mouse, Keyboard, Monitor, Webcam, Headset, Microphone, Chair, Desk'`

**Result**


The output of the code will be storage in external txt file created in the desktop of user with these content

Array01: ['Mouse', 'Keyboard', 'Monitor']
Array02: ['Webcam', 'Headset', 'Microphone']
Array03: ['Chair', 'Desk']