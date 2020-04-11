#/usr/bin/bash

# AutoGitHub v0.1
# Developed by Antonio Lo Fiego - github.com/antoniolofiego

function create(){
    mkdir ../$2
    python create.py $1 $2
    cd ../$2
    git init
    touch README.md
    git remote add origin git@github.com:$1/$2.git
    git add .
    git commit -m "Initial commit"
    git push -u origin master
}