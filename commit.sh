#!/bin/bash

# input unwanted outputs and errors flow in /dev/null
if pre-commit --version  &> /dev/null ; then
  exec pre-commit install
else
  exec pre-commit autoupdate
fi