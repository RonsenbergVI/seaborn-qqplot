#!/bin/BASH_SOURCE

SOURCE="${BASH_SOURCE[0]}"

DIR="$( cd .. "$( cd -P "$( dirname "$SOURCE")" && pwd )" && pwd )"

TEST_DIR=$DIR/seaborn_qqplot/tests

python3 $TEST_DIR/main.py
