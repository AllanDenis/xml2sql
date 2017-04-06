#!/bin/sh
# Approximate count of lines in huge text files
# Author: Allan Denis <allancomll@gmail.com>

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 FILE NLINES" >&2
  exit 1
fi
if ! [ -e "$1" ]; then
  echo "$1 not found." >&2
  exit 1
fi

tempFile=/tmp/head
filebytes=$(stat --printf="%s" $1)
headbytes=$(head -n $2 $1 > $tempFile && stat --printf="%s" $tempFile)
echo "$2 * $filebytes / $headbytes" | bc
