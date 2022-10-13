#!/bin/bash
#set -x

# Usage ./remove-gettext.sh
# run this from the same directory as config.txt.tmpl

# It will remove all $gettext strings (lang variables) from the template files
# that are used in WeeWX 4.6.0, and later versions, to enable language
# translations. The php scripts since WXgraphic v0.6.6 use the lang feature.
# If you use a WeeWX version earlier than 4.6.0 they will cause the php scripts
# to fail (no image).

# The modified files - config.txt.tmpl and DATA/wxgraphic_weewx.txt.tmpl - will
# be backed up with a .lang.bup-epoch_timestamp suffix and the originals will
# then work for the versions earlier than this.

# This script is a wrapper around two sed commands...
# sed -i -e 's/:\")/:/g' -e  's/\$gettext(\"//g' ./config.txt.tmpl
# sed -i -e 's/y\")/y\"/g' -e  's/\$gettext(\"/\"/g' DATA/wxgraphic_weewx.txt.tmpl
# Using the script makes a backup, checks the files


stamp=`date +"%s"`
file1="./config.txt.tmpl"
file2="DATA/wxgraphic_weewx.txt.tmpl"
bup=".lang.bup-$stamp"

echo -e "Continuing will remove the lang features from the wxgraphic template files"
read -n 1 -p "'y' to continue" continue

if [ "$continue"x != 'yx' ]
then
    exit 0
fi

if [ -f $file1 ]
then
    `cp $file1 ${file1}$bup` && echo -e "Backup file ${file1}$bup created" || echo "Failed to write file!"
    grep $file1 -e gettext > /dev/null 2>&1
    if [ $? = 0 ]
    then
        echo -e "\n\$gettext string/s found, replacing all strings\n"
        echo -e "    $file1 has been cleansed!\n"
        echo -e "   Use it in WeeWX versions older than 4.6.0\n"
        sed -i -e 's/:\")/:/g' -e  's/\$gettext(\"//g' $file1
    else
        echo -e "\nNo \$gettext string found in $file1\n"
        echo -e "        It's done already?\n"
        #exit 2
    fi
else
    echo -e "\n$file1 - file not found - Exiting!\n"
    #exit 1
fi

# Rinse , repeat for 2nd file

if [ -f $file2 ]
then
    `cp $file2 ${file2}$bup` && echo -e "Backup file ${file2}$bup created" || echo "Failed to write file!"
    grep $file2 -e gettext > /dev/null 2>&1
    if [ $? = 0 ]
    then
        echo -e "\n\$gettext string/s found, replacing all strings\n"
        echo -e "    $file2 has been cleansed!\n"
        echo -e "   Use it in WeeWX versions older than 4.6.0\n"
        sed -i -e 's/y\")/y\"/g' -e  's/\$gettext(\"/\"/g' $file2
    else
        echo -e "\nNo \$gettext string found in $file2\n"
        echo -e "        It's done already?\n"
        exit 2
    fi
else
    echo -e "\n$file2 - file not found - Exiting!\n"
    exit 1
fi

exit 0
