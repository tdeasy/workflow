# House Music MIDI Generator

A comprehensive n8n workflow-based system for generating house music MIDI patterns with drums, bass, and chords.

## Features

- **BPM Range**: 120-140 BPM (classic house music tempo)
- **Three Instrument Tracks**:
  - **Drums**: 4-on-the-floor kick, snare/clap, hi-hats, crash
  - **Bass**: Groovy basslines with syncopation and chord progression following
  - **Chords**: Lush chord progressions with multiple voicings and rhythms

## Workflows

### 1. Master Workflow (`house-music-master.json`)

The main workflow that generates a complete house music track with all three instruments.

**Parameters**:
- `bpm`: Tempo (120-140, default: 128)
- `bars`: Number of bars (default: 16)
- `key`: Musical key (default: 'A')
- `scale`: Scale type - 'minor', 'major', 'dorian' (default: 'minor')

**Output**: Multi-track MIDI data with drums, bass, and chords

### 2. Individual Generators

#### Drum Generator (`drum-generator.json`)
Generates classic house drum patterns:
- 4-on-the-floor kick drum
- Snare/clap on beats 2 and 4
- 8th note hi-hat patterns
- Crash cymbal accents

#### Bass Generator (`bass-generator.json`)
Creates groovy basslines:
- Root-focused patterns
- Syncopated rhythms
- Follows chord progression (I-VI-III-VII)
- Two alternating patterns for variation

#### Chord Generator (`chord-generator.json`)
Produces lush chord progressions:
- Classic house progressions (i7-VI7-IV7-VII7)
- Multiple rhythm patterns (sustained, stabs, syncopated)
- Open and closed voicings
- 7th chord extensions

## Usage

### In n8n

1. Import the workflow files into your n8n instance:
   - Go to n8n > Workflows > Import from File
   - Select `workflows/house-music-master.json`

2. Configure parameters in the "Start - Configure Track" node:
   ```json
   {
     "bpm": 128,
     "bars": 16,
     "key": "A",
     "scale": "minor"
   }
   ```

3. Execute the workflow

4. The output will contain:
   - MIDI event data
   - Track information
   - Metadata (BPM, key, duration, etc.)

### Standalone Usage

You can also import individual generators if you only need drums, bass, or chords:

```bash
# Import individual workflows
workflows/drum-generator.json
workflows/bass-generator.json
workflows/chord-generator.json
```

## Musical Theory

### Chord Progressions

The generator uses common house music progressions:

**Classic Progression** (default):
- i7 (Am7) → VI7 (FM7) → IV7 (DM7) → VII7 (G7)

**Uplifting Progression**:
- i7 → v7 → VI7 → IV7

**Deep House Progression**:
- i7 → IV sus2 → VII7 → i

### Scales Supported

- **Minor** (Natural Minor): Root, 2, ♭3, 4, 5, ♭6, ♭7
- **Major**: Root, 2, 3, 4, 5, 6, 7
- **Dorian**: Root, 2, ♭3, 4, 5, 6, ♭7 (popular in house music)
- **Phrygian**: Root, ♭2, ♭3, 4, 5, ♭6, ♭7

### Drum Mapping (General MIDI)

- Kick: C1 (MIDI 36)
- Snare: D1 (MIDI 38)
- Clap: D#1 (MIDI 39)
- Closed Hi-hat: F#1 (MIDI 42)
- Open Hi-hat: A#1 (MIDI 46)
- Crash: C#2 (MIDI 49)

## Output Format

The workflows output MIDI data in JSON format:

```json
{
  "format": 1,
  "tracks": 3,
  "ticksPerBeat": 480,
  "bpm": 128,
  "tracksData": [
    {
      "name": "Drums",
      "channel": 9,
      "events": [...]
    },
    {
      "name": "Bass",
      "channel": 0,
      "events": [...]
    },
    {
      "name": "Chords",
      "channel": 1,
      "events": [...]
    }
  ]
}
```

## Export to MIDI Files

To export the JSON output to actual MIDI files, you can:

1. Use the included Python script (see `scripts/midi-export.py`)
2. Use n8n's file writing capabilities
3. Process the JSON with your own MIDI library

## Examples

### Generate a Deep House Track

```json
{
  "bpm": 122,
  "bars": 32,
  "key": "F",
  "scale": "minor"
}
```

### Generate a Tech House Track

```json
{
  "bpm": 128,
  "bars": 16,
  "key": "G",
  "scale": "dorian"
}
```

### Generate a Progressive House Track

```json
{
  "bpm": 126,
  "bars": 64,
  "key": "C",
  "scale": "major"
}
```

## Customization

### Modify Drum Patterns

Edit the `Generate Drums` node in `drum-generator.json`:
- Adjust velocities for different dynamics
- Change hi-hat patterns (16th notes, etc.)
- Add percussion elements

### Modify Bass Patterns

Edit the `Generate Bass` node in `bass-generator.json`:
- Add new rhythm patterns to `bassPatterns` array
- Change progression in `progressionDegrees`
- Adjust note durations for staccato/legato feel

### Modify Chord Patterns

Edit the `Generate Chords` node in `chord-generator.json`:
- Add new progressions to `progressions` object
- Modify rhythm patterns in `rhythmPatterns`
- Change chord voicings

## Requirements

- n8n instance (self-hosted or cloud)
- Understanding of MIDI and music theory (helpful but not required)
- Optional: Python 3.x with `mido` library for MIDI file export

## License

MIT License - Feel free to use and modify for your projects!

## Contributing

Contributions welcome! Some ideas:
- Add more drum patterns (shuffle, breakbeat, etc.)
- Implement melody generators
- Add swing/humanization
- Support for different time signatures
- More complex chord voicings

## Credits

Built for house music producers and enthusiasts. Inspired by classic house, deep house, and tech house productions.
