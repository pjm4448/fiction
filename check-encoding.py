#!/usr/bin/env python3
# -*- coding: utf-8 -*-

file_path = r"c:\Users\pjm35\source\repos\fiction\dark-fantasy\mythara\mythara-world-bible.md"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Check lines 50-55 for the actual characters
for i in range(49, 55):
    line = lines[i]
    if "Mythara" in line or "classes" in line:
        print(f"Line {i+1}: {repr(line[:100])}")
        # Find and show the bytes around the problematic characters
        for j, char in enumerate(line):
            if ord(char) > 127:
                print(f"  Position {j}: {repr(char)} (U+{ord(char):04X})")
