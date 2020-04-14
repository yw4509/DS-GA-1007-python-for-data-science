#!/bin/bash

head -n ${2} "${1}" | tail -n $((${2} - ${3} + 1))
