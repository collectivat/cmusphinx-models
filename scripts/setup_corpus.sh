#!/bin/bash

NOT_FOUND="ERROR: Could not find the sphinxtrain libraries locally. Make sure sphinxtrain is installed in your system.
    try: which sphinxtrain

After installation rerun the script or replace the PROJECT_PATH and SPHINX_LIB_PATH variables manually in the PROJECT_PATH/etc/sphinx_train.cfg file."

MODEL="ca-ca-0.1"

# download encrypted tar file
wget https://transfer.sh/ZPZ0C/$MODEL.gpg
# check download

# extract tar file
gpg --decrypt < $MODEL.gpg | tar xzf -
# check directory

# get local absolute path of the script
#SOURCE="${BASH_SOURCE[0]}"
#DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
DIR="$(pwd)"

# get the path of the sphinxtrain bin and lib
LOCAL_SPHINXTRAIN="$(which sphinxtrain)"
SUBSTRING='/bin/sphinxtrain'
MATCH=`expr match "$LOCAL_SPHINXTRAIN" '.*\('"$SUBSTRING"'\)'`

# if found, replace the variables in the configuration file
if [ "$MATCH" == "$SUBSTRING" ]
then
    LIB_SPHINXTRAIN="${LOCAL_SPHINXTRAIN%$SUBSTRING}"
    CFG_FILE=$DIR/$MODEL/etc/sphinx_train.cfg
    echo "PROJECT_PATH is "$DIR
    echo "SPHINX_LIB_PATH is "$LIB_SPHINXTRAIN
    echo "filling the config file "$CFG_FILE
    sed 's|SPHINX_LIB_PATH|'"$LIB_SPHINXTRAIN"'|g' $CFG_FILE | sed 's|PROJECT_PATH|'"$DIR"'|g' > dummy
    cp dummy $CFG_FILE
    rm dummy
else
    echo "SPHINX_LIB_PATH is "$LOCAL_SPHINXTRAIN
    echo $MATCH" is not equal to "$SUBSTRING
    echo "$NOT_FOUND"
fi
