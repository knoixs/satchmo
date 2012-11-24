#!/bin/bash
set -x
MANAGE=`which django-admin.py`
DIRS=`find . -name locale`
for dir in $DIRS
do
    pushd $dir
    cd ..
    echo $PWD
    ${MANAGE} makemessages -l de -e html,txt,rml
    ${MANAGE} compilemessages
    popd
done

#-exec sh -c 'cd $0 && cd ../ && ${MANAGE} makemessages -l de -e html,txt,rml' {} \;
#find . -name locale -exec sh -c 'cd $0 && cd ../ && ${MANAGE} compilemessages' {} \;
