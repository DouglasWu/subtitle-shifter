# subtitle-shifter

A tool that helps you shift the timeline of srt subtitle files.

# Usage
Clone this project.
```
$ git clone https://github.com/DouglasWu/subtitle-shifter.git
$ cd subtitle-shifter/
```

Run the program with arguments:
```
$ python main.py <inputfile> <outputfile> <seconds>
```
```<seconds>``` is the amount to shift in seconds. It can be a positive or a negative integer.

For example:
```
$ python main.py input.srt output.srt -12
```
When finished, ```output.srt``` would be a file whose time has been shifted 12 seconds backwards compared with ```input.srt```.
