#!/bin/bash
#READ stdin with sepeperate ' ', first input will be orig_language, second input will be orig_text
IFS=' '

read -r orig_lang orig_text
#echo $orig_text
echo $orig_text | sh /opt/joshua-v6.0.1/prepare_lang.sh $orig_lang| nc localhost 5674
