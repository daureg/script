#! /bin/bash
exec pylint -f html $@ > code.html
