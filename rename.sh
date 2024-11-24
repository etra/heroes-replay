#!/bin/bash

# Directory containing the files
directory="ui/public/img/assets/heroes"

# Loop through each file in the directory
for file in "$directory"/*_small.png; do
    # Extract the base name of the file
    filename=$(basename "$file")
    
    newname=$(echo "$filename" | sed -e 's/Hero_//' -e 's/_small//' | tr '[:upper:]' '[:lower:]')
    
    # Rename the file
    mv "$file" "$directory/$newname"
done