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

cd "$parent_path"
python3 ../manage.py migrate
