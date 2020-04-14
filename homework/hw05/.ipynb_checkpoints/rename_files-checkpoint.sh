#!/bin/bash
cd data/university/

old_characters=$1
new_characters=$2

for str in $(ls ${1}*)
do
	mv "$str" "${str/$old_characters/$new_characters}"
done
