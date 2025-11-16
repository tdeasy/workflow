#!/usr/bin/env python3
"""
House Music MIDI Exporter
Converts JSON MIDI data from n8n workflows to actual MIDI files
"""

import json
import sys
from pathlib import Path

try:
    from mido import MidiFile, MidiTrack, Message, MetaMessage
except ImportError:
    print("Error: mido library not found.")
    print("Install with: pip install mido")
    sys.exit(1)


def json_to_midi(json_data, output_path):
    """
    Convert JSON MIDI data to a MIDI file

    Args:
        json_data: Dictionary containing MIDI data from n8n workflow
        output_path: Path to save the MIDI file
    """
    midi_data = json_data.get('midiData', {})

    # Create MIDI file
    mid = MidiFile(type=midi_data.get('format', 1), ticks_per_beat=midi_data.get('ticksPerBeat', 480))

    # Get BPM
    bpm = midi_data.get('bpm', 128)
    tempo = int(60000000 / bpm)  # Convert BPM to microseconds per beat

    # Process each track
    for track_data in midi_data.get('tracksData', []):
        track = MidiTrack()
        mid.tracks.append(track)

        # Add track name
        track.append(MetaMessage('track_name', name=track_data['name'], time=0))

        # Add tempo (only on first track)
        if len(mid.tracks) == 1:
            track.append(MetaMessage('set_tempo', tempo=tempo, time=0))

        # Sort events by tick
        events = sorted(track_data.get('events', []), key=lambda e: e['tick'])

        # Convert events to MIDI messages
        current_tick = 0
        note_offs = []  # Track note off messages

        for event in events:
            tick = event['tick']
            delta_time = tick - current_tick

            # Add any pending note_off messages that should come before this event
            while note_offs and note_offs[0]['tick'] <= tick:
                off_event = note_offs.pop(0)
                off_delta = off_event['tick'] - current_tick
                track.append(Message('note_off',
                                   note=off_event['note'],
                                   velocity=0,
                                   channel=off_event['channel'],
                                   time=off_delta))
                current_tick = off_event['tick']
                delta_time = tick - current_tick

            # Add note on message
            track.append(Message('note_on',
                               note=event['note'],
                               velocity=event['velocity'],
                               channel=event['channel'],
                               time=delta_time))
            current_tick = tick

            # Schedule note off
            note_off_tick = tick + event['duration']
            note_offs.append({
                'tick': note_off_tick,
                'note': event['note'],
                'channel': event['channel']
            })
            note_offs.sort(key=lambda e: e['tick'])

        # Add remaining note off messages
        for off_event in note_offs:
            off_delta = off_event['tick'] - current_tick
            track.append(Message('note_off',
                               note=off_event['note'],
                               velocity=0,
                               channel=off_event['channel'],
                               time=off_delta))
            current_tick = off_event['tick']

        # End of track
        track.append(MetaMessage('end_of_track', time=0))

    # Save MIDI file
    mid.save(output_path)
    print(f"✓ MIDI file saved: {output_path}")

    # Print summary
    metadata = json_data.get('metadata', {})
    print(f"\nTrack Info:")
    print(f"  BPM: {metadata.get('bpm', bpm)}")
    print(f"  Key: {metadata.get('key', 'Unknown')} {metadata.get('scale', '')}")
    print(f"  Bars: {metadata.get('bars', 'Unknown')}")
    print(f"  Duration: {metadata.get('durationSeconds', 0):.2f}s")
    print(f"  Total Events: {metadata.get('totalEvents', 'Unknown')}")
    print(f"  Tracks: {len(midi_data.get('tracksData', []))}")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python midi-export.py <json_file> [output_file]")
        print("\nExample:")
        print("  python midi-export.py house_music.json")
        print("  python midi-export.py house_music.json output.mid")
        sys.exit(1)

    json_file = Path(sys.argv[1])

    if not json_file.exists():
        print(f"Error: File not found: {json_file}")
        sys.exit(1)

    # Load JSON data
    try:
        with open(json_file, 'r') as f:
            json_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        sys.exit(1)

    # Determine output path
    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        # Use filename from JSON or generate one
        filename = json_data.get('filename', json_file.stem + '.mid')
        if not filename.endswith('.mid'):
            filename += '.mid'
        output_path = Path('output') / filename

    # Create output directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Convert and save
    print(f"Converting {json_file} to MIDI...")
    json_to_midi(json_data, output_path)


if __name__ == '__main__':
    main()
