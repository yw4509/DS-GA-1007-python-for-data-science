#!/bin/bash

# echo ${0};

# head -n ${1} "planets.txt" | tail -n ${2}

head_number=${1};

shift;

tail_number=${1}

head -n ${head_number} "planets.txt" | tail -n ${tail_number}

