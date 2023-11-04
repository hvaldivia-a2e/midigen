# midigen

Simple Python midi file generator software.

## Background 

As a hobbyist musician I wanted to easily create synth pads that could be imported in any DAW and used with VST synths. I had experimented with the midiutil python package before to create 100s of files to be used as inspiration for guitar riffs. I came across a post in a FB group for Reaper DAW users where someone asked for a way to create midi files from a text file with a list of chords and so my idea of computer generated guitar riffs took on a different route to be a dictionary of chords that could be used with an input json file to produce midi files, mostly to be used with synth pads.

## SW requirements

* [https://www.python.org/ ]Python 3 (3.8, 3.10, 3.11...)

Install required python packages from the command line with:

` >pip install -r requirements.txt`

## song.json file

The input to the generator is a json file with a list of chord progressions (or sections of a song), 

```
{
     "song" : {
        "progressions" : [
            {
                "chords" : [
                    { "chord" : "G_major", "duration" : 1 },
                    { "chord" : "Rest", "duration" : 2 },
                    { "chord" : "G_major", "duration" : 0.25, "repeats": 4 },
                    { "chord" : "C_major", "duration" : 4 },
                    { "chord" : "D_major", "duration" : 8 }
                ],
                "repeats" : 8
            }
        ]
    }
}
```


Each progression can have 1 or more "chords", each must have a specified "duration" in number of beats. fractional beats are supported (0.5 for half notes, 0.25 for quarter notes, etc.). The optional "repeats" param specifies the number of times this chord is to be added to the progression, when not specified, the chord is added once. The "repeats" param in the progression specifies how many times the progression is played.

> NOTE: chord names must match an entry in the dictionary in the script. For silence we use "Rest" as the chord name.

## running the generator

To run the generator, from a command line run:

` > python midigen -i my_song.json -o my_song.mid`

where:
* my_song.json specifies the input file describing the song
* my_song.mid speficies the filename for the generated file


