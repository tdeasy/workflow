# Quick Start Guide

Get started with the House Music MIDI Generator in 5 minutes!

## Prerequisites

- n8n installed (self-hosted or cloud account)
- Optional: Python 3.x for MIDI file export

## Step 1: Import Workflow to n8n

1. Open your n8n instance
2. Click on "Workflows" in the sidebar
3. Click "Import from File"
4. Select `workflows/house-music-master.json`
5. Click "Import"

## Step 2: Configure Your Track

1. Click on the "Start - Configure Track" node
2. Modify the parameters:

```json
{
  "bpm": 128,      // 120-140 for house music
  "bars": 16,      // Number of bars to generate
  "key": "A",      // Musical key (C, D, E, F, G, A, B, with # or b)
  "scale": "minor" // minor, major, dorian, phrygian
}
```

### Recommended Settings by Style

**Deep House**:
```json
{ "bpm": 122, "bars": 32, "key": "F", "scale": "minor" }
```

**Tech House**:
```json
{ "bpm": 128, "bars": 16, "key": "G", "scale": "dorian" }
```

**Progressive House**:
```json
{ "bpm": 126, "bars": 64, "key": "C", "scale": "major" }
```

## Step 3: Execute the Workflow

1. Click "Execute Workflow" button
2. Wait for the workflow to complete (usually < 1 second)
3. Check the "Output Result" node for the generated MIDI data

## Step 4: View the Output

The workflow generates:

- **Multi-track MIDI data** with drums, bass, and chords
- **Metadata** including BPM, key, duration, and event counts
- **Filename suggestion** for saving

### Example Output:

```
=== House Music MIDI Generated ===
File: house_music_A_minor_128bpm_16bars.mid
BPM: 128
Key: A minor
Bars: 16
Duration: 30.00s
Total MIDI Events: 453
Tracks: Drums (256 events), Bass (128 events), Chords (69 events)
```

## Step 5: Export to MIDI File (Optional)

### Option A: Using Python Script

1. Install requirements:
```bash
pip install -r scripts/requirements.txt
```

2. Save the JSON output from n8n to a file (e.g., `output.json`)

3. Run the export script:
```bash
python scripts/midi-export.py output.json
```

4. Find your MIDI file in the `output/` directory

### Option B: Add File Write Node in n8n

1. Add a "Write Binary File" node after "Output Result"
2. Configure it to save the MIDI data
3. Connect and execute

## Step 6: Use in Your DAW

1. Import the generated MIDI file into your DAW:
   - **Ableton Live**: Drag and drop the .mid file
   - **FL Studio**: File > Import > MIDI File
   - **Logic Pro**: File > Import > MIDI File
   - **Cubase**: File > Import > MIDI File

2. Assign instruments:
   - **Track 1 (Channel 9)**: Drum kit
   - **Track 2 (Channel 0)**: Bass synth
   - **Track 3 (Channel 1)**: Pad/chord synth

3. Start producing! 🎵

## Customization Tips

### Adjust Drum Pattern

Open `workflows/drum-generator.json` and modify:
- Velocity values (how hard notes are hit)
- Note timing for different grooves
- Add extra percussion elements

### Modify Bass Groove

Open `workflows/bass-generator.json` and edit:
- `bassPatterns` array for different rhythms
- `progressionDegrees` for chord progression
- Note durations for staccato/legato

### Change Chord Voicings

Open `workflows/chord-generator.json` and modify:
- `progression` for different chord sequences
- `rhythmPatterns` for various playing styles
- `voicing` parameter for spread

## Troubleshooting

### BPM outside range?
The workflow automatically clamps BPM to 120-140. If you need different tempos, modify the validation in the "Validate Parameters" node.

### Wrong key?
Ensure the key parameter uses proper notation:
- Sharps: `C#`, `D#`, `F#`, `G#`, `A#`
- Flats: `Db`, `Eb`, `Gb`, `Ab`, `Bb`

### Need more bars?
Simply increase the `bars` parameter. 16-32 bars is typical for a loop, 64+ for full arrangements.

## Next Steps

- Mix and match individual generators (drums only, bass only, etc.)
- Combine multiple generated patterns for a full song structure
- Add melody generators (coming soon!)
- Experiment with different scales and progressions

## Support

Check the main [README.md](README.md) for detailed documentation.

Happy producing! 🎧
