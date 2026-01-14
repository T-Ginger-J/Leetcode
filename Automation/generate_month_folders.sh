#!/bin/bash

MONTH=$1

declare -A MONTHS=(
  [1]="January 31"
  [2]="February 28"
  [3]="March 31"
  [4]="April 30"
  [5]="May 31"
  [6]="June 30"
  [7]="July 31"
  [8]="August 31"
  [9]="September 30"
  [10]="October 31"
  [11]="November 30"
  [12]="December 31"
)

if [[ -z "${MONTHS[$MONTH]}" ]]; then
  echo "Usage: ./generate_month_folders.sh <1-12>"
  exit 1
fi

read MONTH_NAME DAYS <<< "${MONTHS[$MONTH]}"

mkdir -p "$MONTH_NAME"

for (( i=1; i<=DAYS; i++ ))
do
  mkdir -p "$MONTH_NAME/$i"
done

echo "Created $MONTH_NAME with $DAYS day folders."
