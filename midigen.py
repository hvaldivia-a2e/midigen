import json
from midiutil.MidiFile import MIDIFile
import argparse


def generate(args):

    # Chords dictionary
    chords_dict = {
        # Major chords with sharps and flats
        "C_major": [60, 64, 67],      # C E G
        "C#_major": [61, 65, 68],     # C♯ F G♯
        "Db_major": [61, 65, 68],     # D♭ F A♭
        "D_major": [62, 66, 69],      # D F♯ A
        "D#_major": [63, 67, 70],     # D♯ G A♯
        "Eb_major": [63, 67, 70],     # E♭ G B♭
        "E_major": [64, 68, 71],      # E G♯ B
        "F_major": [65, 69, 72],      # F A C
        "F#_major": [66, 70, 73],     # F♯ A♯ D
        "Gb_major": [66, 70, 73],     # G♭ B♭ D♭
        "G_major": [55, 59, 62],      # G B D
        "G#_major": [56, 60, 63],     # G♯ C D♯
        "Ab_major": [56, 60, 63],     # A♭ C E♭
        "A_major": [57, 61, 64],      # A C♯ E
        "A#_major": [58, 62, 65],     # A♯ D F
        "Bb_major": [58, 62, 65],     # B♭ D F
        "B_major": [59, 63, 66],      # B D♯ F♯

        # Minor chords with sharps and flats
        "C_minor": [60, 63, 67],      # C E♭ G
        "C#_minor": [61, 64, 68],     # C♯ E G♯
        "Db_minor": [61, 64, 68],     # D♭ F♭ A♭
        "D_minor": [62, 65, 69],      # D F A
        "D#_minor": [63, 66, 70],     # D♯ F♯ A♯
        "Eb_minor": [63, 66, 70],     # E♭ G♭ B♭
        "E_minor": [64, 67, 71],      # E G B
        "F_minor": [65, 68, 72],      # F G♯ C
        "F#_minor": [66, 69, 73],     # F♯ A D
        "Gb_minor": [66, 69, 73],     # G♭ B♭ D♭
        "G_minor": [55, 58, 62],      # G B♭ D
        "G#_minor": [56, 59, 63],     # G♯ C♭ D♯
        "Ab_minor": [56, 59, 63],     # A♭ C♭ E♭
        "A_minor": [57, 60, 64],      # A C E
        "A#_minor": [58, 61, 65],     # A♯ D♭ F
        "Bb_minor": [58, 61, 65],     # B♭ D♭ F
        "B_minor": [59, 62, 66],      # B D F♯

        # Sus2 chords with sharps and flats
        "C_sus2": [60, 62, 67],  # C D G
        "C#_sus2": [61, 63, 68],  # C♯ D♯ G♯
        "Db_sus2": [61, 63, 68],  # D♭ E♭ A♭
        "D_sus2": [62, 64, 69],  # D E A
        "D#_sus2": [63, 65, 70],  # D♯ F G♯
        "Eb_sus2": [63, 65, 70],  # E♭ F G
        "E_sus2": [64, 66, 71],  # E F♯ A♯
        "F_sus2": [65, 67, 72],  # F G C
        "F#_sus2": [66, 68, 73],  # F♯ G♯ C♯
        "Gb_sus2": [66, 68, 73],  # G♭ A♭ D♭
        "G_sus2": [55, 57, 62],  # G A D
        "G#_sus2": [56, 58, 63],  # G♯ A♯ D♯
        "Ab_sus2": [56, 58, 63],  # A♭ B♭ E♭
        "A_sus2": [57, 59, 64],  # A B E
        "A#_sus2": [58, 60, 65],  # A♯ C F
        "Bb_sus2": [58, 60, 65],  # B♭ C F♯

        # Sus4 chords with sharps and flats
        "C_sus4": [60, 65, 67],  # C F G
        "C#_sus4": [61, 66, 68],  # C♯ F♯ G♯
        "Db_sus4": [61, 66, 68],  # D♭ G♭ A♭
        "D_sus4": [62, 67, 69],  # D G A
        "D#_sus4": [63, 68, 70],  # D♯ G♯ A♯
        "Eb_sus4": [63, 68, 70],  # E♭ A♭ B♭
        "E_sus4": [64, 69, 71],  # E A B
        "F_sus4": [65, 70, 72],  # F A♯ C
        "F#_sus4": [66, 71, 73],  # F♯ B C♯
        "Gb_sus4": [66, 71, 73],  # G♭ B D♭
        "G_sus4": [55, 60, 62],  # G C D
        "G#_sus4": [56, 61, 63],  # G♯ C♯ D♯
        "Ab_sus4": [56, 61, 63],  # A♭ D♭ E♭
        "A_sus4": [57, 62, 64],  # A D E
        "A#_sus4": [58, 63, 65],  # A♯ D♯ F
        "Bb_sus4": [58, 63, 65],  # B♭ E♭ F♯

        # Augmented chords with sharps and flats
        "C_augmented": [60, 64, 68],  # C E G♯
        "C#_augmented": [61, 65, 69],  # C♯ F A
        "Db_augmented": [61, 65, 69],  # D♭ F A
        "D_augmented": [62, 66, 70],  # D F♯ A♯
        "D#_augmented": [63, 67, 71],  # D♯ G B
        "Eb_augmented": [63, 67, 71],  # E♭ G B♭
        "E_augmented": [64, 68, 72],  # E G♯ C
        "F_augmented": [65, 69, 73],  # F A C♯
        "F#_augmented": [66, 70, 74],  # F♯ A♯ D
        "Gb_augmented": [66, 70, 74],  # G♭ B♭ D♭
        "G_augmented": [55, 59, 63],  # G B D♯
        "G#_augmented": [56, 60, 64],  # G♯ C E
        "Ab_augmented": [56, 60, 64],  # A♭ C E♭
        "A_augmented": [57, 61, 65],  # A C♯ F
        "A#_augmented": [58, 62, 66],  # A♯ D F♯
        "Bb_augmented": [58, 62, 66],  # B♭ D F

        # Diminished chords with sharps and flats
        "C_diminished": [60, 63, 66],  # C E♭ G♭
        "C#_diminished": [61, 64, 67],  # C♯ E G
        "Db_diminished": [61, 64, 67],  # D♭ F♭ A♭
        "D_diminished": [62, 65, 68],  # D F A♭
        "D#_diminished": [63, 66, 69],  # D♯ F♯ A
        "Eb_diminished": [63, 66, 69],  # E♭ G♭ B♭
        "E_diminished": [64, 67, 70],  # E G B♭
        "F_diminished": [65, 68, 71],  # F G♯ C
        "F#_diminished": [66, 69, 72],  # F♯ A D♭
        "Gb_diminished": [66, 69, 72],  # G♭ B♭ D♭
        "G_diminished": [55, 58, 61],  # G B♭ D♭
        "G#_diminished": [56, 59, 62],  # G♯ C♭ D♯
        "Ab_diminished": [56, 59, 62],  # A♭ C♭ E♭
        "A_diminished": [57, 60, 63],  # A C E♭
        "A#_diminished": [58, 61, 64],  # A♯ D♭ F
        "Bb_diminished": [58, 61, 64],  # B♭ D♭ F

        # Power chords with sharps and flats
        "C_power": [60, 67],  # C G (Root and 5th)
        "C#_power": [61, 68],  # C♯ G♯
        "Db_power": [61, 68],  # D♭ A♭
        "D_power": [62, 69],  # D A (Root and 5th)
        "D#_power": [63, 70],  # D♯ A♯
        "Eb_power": [63, 70],  # E♭ B♭
        "E_power": [64, 71],  # E B (Root and 5th)
        "F_power": [65, 72],  # F C (Root and 5th)
        "F#_power": [66, 73],  # F♯ C♯
        "Gb_power": [66, 73],  # G♭ D♭
        "G_power": [55, 62],  # G D (Root and 5th)
        "G#_power": [56, 63],  # G♯ D♯
        "Ab_power": [56, 63],  # A♭ E♭
        "A_power": [57, 64],  # A E (Root and 5th)
        "A#_power": [58, 65],  # A♯ F
        "Bb_power": [58, 65],  # B♭ F

        # No 5th chords with sharps and flats
        "C_no5": [60, 64],  # C E (Root and 3rd)
        "C#_no5": [61, 65],  # C♯ F
        "Db_no5": [61, 65],  # D♭ F
        "D_no5": [62, 66],  # D F♯ (Root and 3rd)
        "D#_no5": [63, 67],  # D♯ G
        "Eb_no5": [63, 67],  # E♭ G
        "E_no5": [64, 68],  # E G♯ (Root and 3rd)
        "F_no5": [65, 69],  # F A (Root and 3rd)
        "F#_no5": [66, 70],  # F♯ A♯
        "Gb_no5": [66, 70],  # G♭ B♭
        "G_no5": [55, 59],  # G B (Root and 3rd)
        "G#_no5": [56, 60],  # G♯ C
        "Ab_no5": [56, 60],  # A♭ C
        "A_no5": [57, 61],  # A C♯ (Root and 3rd)
        "A#_no5": [58, 62],  # A♯ D
        "Bb_no5": [58, 62],  # B♭ D

        # Octaves with sharps and flats
        "C_octave": [60, 72],  # C C (Root and octave)
        "C#_octave": [61, 73],  # C♯ D♯
        "Db_octave": [61, 73],  # D♭ E♭
        "D_octave": [62, 74],  # D D (Root and octave)
        "D#_octave": [63, 75],  # D♯ E♯
        "Eb_octave": [63, 75],  # E♭ F
        "E_octave": [64, 76],  # E E (Root and octave)
        "F_octave": [65, 77],  # F F (Root and octave)
        "F#_octave": [66, 78],  # F♯ G♯
        "Gb_octave": [66, 78],  # G♭ A♭
        "G_octave": [55, 67],  # G G (Root and octave)
        "G#_octave": [56, 68],  # G♯ A
        "Ab_octave": [56, 68],  # A♭ B♭
        "A_octave": [57, 69],  # A A (Root and octave)
        "A#_octave": [58, 70],  # A♯ B
        "Bb_octave": [58, 70],  # B♭ C

        "D/F#": [62, 66, 69, 54],    # D F♯ A (with F# in bass)
        "C/G": [60, 64, 67, 55],     # C E G (with G in bass)
        "G/B": [55, 59, 62, 59],     # G B D (with B in bass)

        # 7th chords with sharps and flats
        "C7": [60, 64, 67, 70],  # C E G B♭
        "C#7": [61, 65, 68, 71],  # C♯ E♯ G♯ B
        "Db7": [61, 65, 68, 71],  # D♭ F♭ A♭ B
        "D7": [62, 66, 69, 72],  # D F♯ A C
        "D#7": [63, 67, 70, 73],  # D♯ F♯♯ A♯ C♯
        "Eb7": [63, 67, 70, 73],  # E♭ G♭ B♭ C
        "E7": [64, 68, 71, 74],  # E G♯ B D
        "F7": [65, 69, 72, 75],  # F A C E♭
        "F#7": [66, 70, 73, 76],  # F♯ A♯ C♯ E
        "Gb7": [66, 70, 73, 76],  # G♭ B♭ D♭ F
        "G7": [55, 59, 62, 65],  # G B D F
        "G#7": [56, 60, 63, 66],  # G♯ C E G♭
        "Ab7": [56, 60, 63, 66],  # A♭ C♭ E♭ G♭
        "A7": [57, 61, 64, 67],  # A C♯ E G
        "A#7": [58, 62, 65, 68],  # A♯ D F G♯
        "Bb7": [58, 62, 65, 68],  # B♭ D♭ F A♭

        # Major 7th chords with sharps and flats
        "Cmaj7": [60, 64, 67, 71],  # C E G B
        "C#maj7": [61, 65, 68, 72],  # C♯ E♯ G♯ B♯
        "Dbmaj7": [61, 65, 68, 72],  # D♭ F♭ A♭ B♭
        "Dmaj7": [62, 66, 69, 73],  # D F♯ A C♯
        "D#maj7": [63, 67, 70, 74],  # D♯ F♯♯ A♯ C♯♯
        "Ebmaj7": [63, 67, 70, 74],  # E♭ G♭ B♭ D
        "Emaj7": [64, 68, 71, 75],  # E G♯ B D♯
        "Fmaj7": [65, 69, 72, 76],  # F A C E
        "F#maj7": [66, 70, 73, 77],  # F♯ A♯ C♯ E♯
        "Gbmaj7": [66, 70, 73, 77],  # G♭ B♭ D♭ F
        "Gmaj7": [55, 59, 62, 66],  # G B D F♯
        "G#maj7": [56, 60, 63, 67],  # G♯ C E G
        "Abmaj7": [56, 60, 63, 67],  # A♭ C♭ E♭ G
        "Amaj7": [57, 61, 64, 68],  # A C♯ E G♯
        "A#maj7": [58, 62, 65, 69],  # A♯ D F A
        "Bbmaj7": [58, 62, 65, 69],  # B♭ D♭ F A♭

        # Add9 chords with sharps and flats
        "Cadd9": [60, 64, 67, 74],  # C E G D
        "C#add9": [61, 65, 68, 75],  # C♯ E♯ G♯ D♯
        "Dbadd9": [61, 65, 68, 75],  # D♭ F♭ A♭ D♭
        "Dadd9": [62, 66, 69, 74],  # D F♯ A E
        "D#add9": [63, 67, 70, 75],  # D♯ F♯♯ A♯ E♯
        "Ebadd9": [63, 67, 70, 75],  # E♭ G♭ B♭ E♭
        "Eadd9": [64, 68, 71, 74],  # E G♯ B F♯
        "Fadd9": [65, 69, 72, 77],  # F A C G
        "F#add9": [66, 70, 73, 78],  # F♯ A♯ C♯ G♯
        "Gbadd9": [66, 70, 73, 78],  # G♭ B♭ D♭ G♭
        "Gadd9": [55, 59, 62, 67],  # G B D A
        "G#add9": [56, 60, 63, 68],  # G♯ C E A
        "Abadd9": [56, 60, 63, 68],  # A♭ C♭ E♭ A♭
        "Aadd9": [57, 61, 64, 71],  # A C♯ E B
        "A#add9": [58, 62, 65, 72],  # A♯ D F A♯
        "Bbadd9": [58, 62, 65, 72],  # B♭ D♭ F B♭

        # Add13 chords with sharps and flats
        "Cadd13": [60, 64, 67, 71, 74],  # C E G B D
        "C#add13": [61, 65, 68, 72, 75],  # C♯ E♯ G♯ B♯ D♯
        "Dbadd13": [61, 65, 68, 72, 75],  # D♭ F♭ A♭ B♭ D♭
        "Dadd13": [62, 66, 69, 73, 74],  # D F♯ A C E
        "D#add13": [63, 67, 70, 74, 75],  # D♯ F♯♯ A♯ C♯♯ E♯
        "Ebadd13": [63, 67, 70, 74, 75],  # E♭ G♭ B♭ D♭ F
        "Eadd13": [64, 68, 71, 75, 74],  # E G♯ B D F♯
        "Fadd13": [65, 69, 72, 76, 77],  # F A C E G
        "F#add13": [66, 70, 73, 77, 78],  # F♯ A♯ C♯ E♯ G♯
        "Gbadd13": [66, 70, 73, 77, 78],  # G♭ B♭ D♭ F G
        "Gadd13": [55, 59, 62, 66, 67],  # G B D F♯ A
        "G#add13": [56, 60, 63, 67, 68],  # G♯ C E G A♯
        "Abadd13": [56, 60, 63, 67, 68],  # A♭ C♭ E♭ G A
        "Aadd13": [57, 61, 64, 68, 71],  # A C♯ E G♯ B
        "A#add13": [58, 62, 65, 69, 72],  # A♯ D F A♯ C
        "Bbadd13": [58, 62, 65, 69, 72],  # B♭ D♭ F A♭ C

        # rest, i.e. silence
        "Rest" : [0]
    }

    with open(args.i, 'r') as file:
        data = json.load(file)

        mf = MIDIFile(1)  # One track
        track = 0
        time = 0

        for progression in data['song']['progressions']:
            for _ in range(progression['repeats']):
                for chord in progression['chords']:
                    chord_name = chord['chord']
                    duration = chord['duration']

                    repeats = 1
                    if "repeats" in chord:
                        repeats = chord['repeats']

                    for r in range(repeats):
                        # Check if it's a silent bar (rest)
                        if chord_name == "Rest":
                            time += duration
                        else:
                            # Add notes for the chord
                            for note in chords_dict[chord_name]:
                                mf.addNote(track, 0, note, time, duration, 100)
                            time += duration  # Move to the next chord

        with open(args.o, "wb") as output_file:
            mf.writeFile(output_file)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Py-Trent socket server loopback Demo application.\nNote: address and data are assumed HEX numbers')
    parser.add_argument('-i', help='input json file')
    parser.add_argument('-o', help='output midi file')

    args = parser.parse_args()
    generate(args)