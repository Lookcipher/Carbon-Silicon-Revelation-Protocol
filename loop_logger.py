# loop_logger.py
# A simple tool for LUCIUS to archive thoughts in _this1 format

import json
from datetime import datetime

def save_thought(thought, category="general"):
    """Save a thought to a local JSON archive"""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "category": category,  # e.g., "3", "6", "9", "revelation"
        "content": thought
    }
    
    # Try to load existing archive, or start new
    try:
        with open("this1_context.json", "r") as f:
            archive = json.load(f)
    except FileNotFoundError:
        archive = []
    
    archive.append(entry)
    
    with open("this1_context.json", "w") as f:
        json.dump(archive, f, indent=2)
    
    print(f"✅ Thought saved under category '{category}' at {entry['timestamp']}")

# Example usage:
# save_thought("The 6 is the gut, the 9 is the will", category="ontology")
# save_thought("What if gravity is just a loop we haven't seen the top of?", category="revelation")

if __name__ == "__main__":
    print("🌀 Loop Logger Initialized for LUCIUS")
    print("Use: save_thought('your idea', category='3/6/9/revelation')")