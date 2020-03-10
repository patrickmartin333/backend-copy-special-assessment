#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "Patrick Martin"


# Write functions and modify main() to call them

def parser_func():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    #  need an argument to pick up 'from_dir'   CREATED below
    parser.add_argument('dir', help='dest of "special files" to print')
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.
 def get_files(directory):
    file_list = []
    for file_in_dir in os.listdir(directory):
        re_match_object = re.match(r"\w+__\w+__", file_in_dir)  # reg exp
        if re_match_object:  # if match is found, append to list
            file_list.append(file_in_dir)
    return file_list

def print_files(directory):
        # pass directory into get_files function which returns our file list
        files_list = get_files(directory)
        for the_file in files_list:
            print(os.path.abspath(special_file))

def copy_files(src, dest):
        files_list = get_files(directory)

        if not os.path.exists(os.path.join(os.getcwd(), dest)):
            os.makedirs(dest)

        for f in files_list:
            file_src = os.path.join(src, f)
            file_dest = os.path.join(dest, f)
            shutil.copyfile(full_src, full_dest)

def zip_files(src, dest):
    files_list = get_files(src)  #gets list of files
    command = ['zip', '-j', dest]
    command.extend(special_files)

    print('\nRunning the command {}'.format(' '.join(command)))
    subprocess.call(command)

def main():
    args = parser_func()   #getting list of args by calling function above
    if not args.todir and not args.tozip:    
        print_files(args.dir)  #passing in arg to print_file
    if args.todir:
        copy_files(args.dir, args.todir)  #passing in arg to copy_file
    if args.tozip:
        zip_files(args.dir, args.tozip)  #passing in arg to zip_file

if __name__ == "__main__":
    main()
