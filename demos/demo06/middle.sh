#!/bin/bash
cd data-shell/molecules/

head -n 10 "octane.pdb" | tail -n 5

# head -n 10 "${1}" | tail -n 5

# head -n ${2} "${1}" | tail -n ${3}

# head -n ${2} "${1}" | tail -n $((${2} - ${3} + 1))

# for filename in ${@}
#  do 
#     echo ${filename};
#     head -n 10 "${filename}" | tail -n 5;
#  done

upper=${1};
shift;

lower=${1}
shift;

if [ "$1" != "0" ]; then
    echo ${1};
    head -n ${upper} "${1}" | tail -n ${lower};
    shift;
else
    echo "all done!"
fi