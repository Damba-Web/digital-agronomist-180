# Day 3: Git Basics I

## Today’s Focus

Today I learned the basic Git workflow for tracking changes in my Digital Agronomist project.

The basic workflow is:

edit file → check status → add file → commit → push

## Basic Git Commands

### 1. git status

`git status` shows the current state of my repository. It tells me which files have changed, which files are untracked, and which files are ready to be committed.

### 2. git add

`git add` stages a file for the next commit. This means I am telling Git which changes I want to include in the next saved checkpoint.

Example:

```bash
git add learning_log/day_03_git_basics.md