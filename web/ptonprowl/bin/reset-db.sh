#!/bin/bash

echo "WARNING! This script overwrites your database."

read -r -p 'Do you want to continue? (Y/N)' choice
    case "$choice" in
      y|Y) echo 'Running...';;
      n|N|*) return;;
    esac
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

mysql -u root -p -e "DROP DATABASE IF EXISTS prowl_db; CREATE DATABASE
prowl_db;"
python3 "$parent_path"/../manage.py makemigrations
python3 "$parent_path"/../manage.py migrate
