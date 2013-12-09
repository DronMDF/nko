#!/bin/bash

NAME=$1
FILES=`find $NAME -name "*.html"`

for f in $FILES; do
	echo ${f/.*/}
	sed -e 's/;=""//' $f | xsltproc --html --encoding cp1251 -o ${f/.*/}.txt nko.xslt - 
done

