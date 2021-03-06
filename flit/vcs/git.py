import os
from subprocess import check_output

name = 'git'

def list_tracked_files(directory):
    outb = check_output(['git', 'ls-files', '--recurse-submodules'],
                        cwd=str(directory))
    return [os.fsdecode(l) for l in outb.strip().splitlines()]

def list_untracked_deleted_files(directory):
    outb = check_output(['git', 'ls-files', '--deleted', '--others',
                         '--exclude-standard'],
                        cwd=str(directory))
    return [os.fsdecode(l) for l in outb.strip().splitlines()]
