#!/usr/bin/env python3
# -*- coding: utf-8 -*-

file_path = r"c:\Users\pjm35\source\repos\fiction\dark-fantasy\mythara\mythara-world-bible.md"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The malformed sequence is: apostrophe + euro sign + right double quote
bad_sequence = "'\u20ac\u201d"  # '€"
count = content.count(bad_sequence)
print(f"Found {count} instances of malformed em-dash to replace")

# Fix encoding issues
content = content.replace(bad_sequence, "\u2014")  # Unicode em-dash (—)
content = content.replace("peakSilk", "peak\u2014Silk")
content = content.replace("scrollsavailable", "scrolls\u2014available")
content = content.replace("holding*require", "holding*\u2014require")
content = content.replace("healing*available", "healing*\u2014available")

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully fixed {count} encoding issues!")
print("Replaced malformed sequence '€\" with proper em-dash (—)")
print("Fixed spacing issues: peakSilk, scrollsavailable, holding*require, healing*available")
