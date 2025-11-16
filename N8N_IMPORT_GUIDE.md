# n8n Import Instructions

## Step-by-Step Guide to Import Workflows

### Prerequisites
- n8n must be running (either locally or cloud instance)
- Access to n8n web interface

### Method 1: Import via n8n Web UI

1. **Open n8n**
   - Local: Usually at http://localhost:5678
   - Cloud: Your n8n cloud URL

2. **Navigate to Workflows**
   - Click on "Workflows" in the left sidebar
   - Or go directly to the workflows page

3. **Import the Master Workflow**
   - Click the "+" button or "Add workflow"
   - Look for an "Import from file" or "Import from URL" option
   - OR click the menu (three dots) and select "Import from file"

4. **Select the workflow file**
   - Browse to: `workflows/house-music-master.json`
   - Click "Open" or "Import"

5. **Save the workflow**
   - Click "Save" button
   - Name it something like "House Music MIDI Generator"

6. **Repeat for individual generators** (optional)
   - `workflows/drum-generator.json`
   - `workflows/bass-generator.json`
   - `workflows/chord-generator.json`

### Method 2: Copy-Paste JSON

1. **Copy the workflow JSON**
   ```bash
   cat workflows/house-music-master.json
   ```

2. **In n8n:**
   - Create a new workflow
   - Click the menu (three dots) in the top right
   - Select "Import from URL" or "Import from Clipboard"
   - Paste the JSON content
   - Click "Import"

### Method 3: Using n8n CLI (if installed)

```bash
# If you have n8n CLI installed locally
n8n import:workflow --input=workflows/house-music-master.json

# Import all workflows
n8n import:workflow --input=workflows/drum-generator.json
n8n import:workflow --input=workflows/bass-generator.json
n8n import:workflow --input=workflows/chord-generator.json
```

## After Import

### Test the Workflow

1. **Open the imported workflow**
   - Click on "House Music MIDI Generator" in your workflows list

2. **Configure parameters** (optional)
   - Click on the "Start - Configure Track" node
   - Modify the test data:
     ```json
     {
       "bpm": 128,
       "bars": 16,
       "key": "A",
       "scale": "minor"
     }
     ```

3. **Execute the workflow**
   - Click the "Execute Workflow" button (play icon)
   - Watch the nodes light up as they execute

4. **Check the output**
   - Click on the "Output Result" node
   - View the generated MIDI data in the output panel
   - You should see event counts, BPM, key, and other metadata

### Troubleshooting

**If nodes show errors:**
- Check that all Code nodes are using JavaScript (not Python)
- Verify node connections are intact
- Re-import the workflow if nodes are missing

**If execution fails:**
- Check the error message in the node
- Verify BPM is between 120-140
- Ensure key and scale are valid values

**If you can't find the import option:**
- n8n version might be different
- Try: Workflows > Three-dot menu > Import
- Or: Create new workflow > Three-dot menu > Import from URL

## Next Steps

Once imported and tested:
1. Save the JSON output to a file
2. Use the Python script to convert to MIDI:
   ```bash
   python scripts/midi-export.py output.json
   ```
3. Import the MIDI file into your DAW

---

Need help with a specific step? Let me know!
