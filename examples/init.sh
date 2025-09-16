#!/bin/bash -e

d=$1
if [ $d != "" ]; then

  mkdir $d

  sed "s/template/$d/g" <.template/template.markdown >$d.markdown
  sed "s/template/$d/g" <.template/template/template.py >$d/$d.py

fi

