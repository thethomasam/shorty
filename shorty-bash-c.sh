#!/bin/bash

# Initialize variables
file_name=""
verbose=0

# Function to show usage
usage() {
    echo "Usage: $0 [-v] [-f filename]"
    echo "  -v    Verbose mode"
    echo "  -f    Specify file name"
    exit 1
}

# Parse command-line options
while getopts "vf:" opt; do
  case ${opt} in
    v )
      verbose=1
      ;;
    f )
      file_name=$OPTARG
      ;;
    \? )
      usage
      ;;
  esac
done
echo $file_name
# Check if file name is provided
if [ -z "$file_name" ]; then
    echo "$file_name"
    usage
fi

# Main script logic
if [ $verbose -eq 1 ]; then
    echo "Verbose mode is on."
    echo "File name is: $file_name"
fi

# Add the rest of the script logic here
