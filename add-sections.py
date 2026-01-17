#!/usr/bin/env python3
# Script to add two new sections to mythara-world-bible.md

filepath = r"c:\Users\pjm35\source\repos\fiction\dark-fantasy\mythara\mythara-world-bible.md"

# Read the file
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Task 1: Add Travel Pace Assumptions section
travel_pace_section = """
#### Travel Pace Assumptions

The base travel times assume a standard adventuring party (4–6 members) using common mounts or walking. Unusual circumstances modify these assumptions:

- **Large Groups**: Caravans exceeding 20 travelers or military columns move approximately 50% slower due to coordination difficulties and frequent stops.
- **Unusual Mounts**: Elephants (20 ft. movement) travel at half normal mounted speed (~2 miles/hour), while flying mounts vary dramatically—griffons and hippogriffs (80 ft. fly) achieve ~8 miles/hour, while giant eagles (16 miles/hour) match fast naval vessels. Flying bypasses terrain penalties but exposes riders to aerial predators and exhaustion limits.
- **Extreme Terrain**: The existing route times already incorporate typical terrain challenges. Particularly hazardous areas (e.g., Bleakmoor Fens, Death Hyena Plains) may add 25–50% additional travel time beyond listed values due to navigation challenges and forced detours.

"""

# Find the insertion point for Task 1
marker1 = "- **Caravan vs. Adventurer Pace**: Large merchant caravans move slower"
idx1 = content.find(marker1)
if idx1 != -1:
    # Find the end of this line
    end_of_line = content.find('\n', idx1)
    # Find the next line (which should be blank)
    next_line_start = end_of_line + 1
    # Insert after the blank line
    next_para = content.find('\n', next_line_start) + 1
    content = content[:next_para] + travel_pace_section + content[next_para:]
    print(f"✓ Added Travel Pace Assumptions section")
else:
    print("✗ Could not find insertion point for Travel Pace Assumptions")

# Task 2: Add The Unseeing Eye section
unseeing_eye_section = """
**The Unseeing Eye (Remote cavern system beneath the Coiled Barrier mountains)**  
A reality-thin wound in the deepest darkness where the Far Realm seeps through—an incomprehensible void that whispers maddening geometries to those who dare approach. The cavern walls pulse with bioluminescent patterns that shift into non-Euclidean angles, inducing vertigo and psychic damage (DC 15 Wisdom save or take 2d6 psychic damage and gain short-term madness). Great Old One warlocks pilgrimage here to commune with their patrons, emerging changed—some enlightened, most broken. Aberrations manifest sporadically: star spawn, intellect devourers, and nothics drawn to the rift like moths to flame. The site remains deliberately obscure, known only through cryptic verses in forbidden tomes and the raving testimonies of escaped madmen. Serpentis occultists occasionally dispatch expeditions seeking forbidden knowledge, though few return. Those who do bring back *ioun stones of insight* warped by alien energies, granting advantage on Arcana checks but causing prophetic nightmares. The Unseeing Eye represents cosmic horror incarnate—a place where reality fractures, sanity shatters, and the infinitesimal nature of mortal existence becomes unbearably clear.

"""

# Find the insertion point for Task 2
marker2 = "**The Sunken Planar Rift (Kraken Depths, offshore Inner Bay)**"
idx2 = content.find(marker2)
if idx2 != -1:
    # Find the end of the description paragraph (next blank line)
    para_start = idx2
    para_end = content.find('\n\n', para_start)
    if para_end != -1:
        # Insert after this paragraph
        content = content[:para_end + 2] + unseeing_eye_section + content[para_end + 2:]
        print(f"✓ Added The Unseeing Eye section")
    else:
        print("✗ Could not find paragraph end for The Sunken Planar Rift")
else:
    print("✗ Could not find insertion point for The Unseeing Eye")

# Write the modified content back
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ File updated successfully!")
