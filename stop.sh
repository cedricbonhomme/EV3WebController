#! /usr/bin/env bash

kill -9 `ps -A | grep -i atom | grep -oE '^[0-9]+' | tr '\n' ' '`
