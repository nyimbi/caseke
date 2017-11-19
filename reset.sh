#!/usr/bin/env bash

echo "Dropping Database"
dropdb $1

echo "Creating Database"
createdb $1

echo "Creating tables and such ....."
fabmanager create-db
fabmanager create-admin

echo "About to run app "
read -n 1 -p "execute: fabmanager run? [Y/n]" yesno

case "$yesno" in
	[Yy]|[Yy][Ee][Ss]) echo "Running the app.";;
	*) exit 0;;
esac



#if [ "$(yesno)" == 'n' ]; then
#	exit 0
#else
#	fabmanager run
#f1
