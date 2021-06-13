The Unreal Engine source distribution ships with a tool called
`GitDependencies.exe`. This tool is intended to make it easy to get all the
dependencies you need to compile the Unreal Engine - and it does.

However, for packaging purposes, we would prefer to download the dependencies
separately, or install using a package manager.

This script is intended to parse the `Commit.gitdeps.xml` file, located in
`Engine/Build` subdirectory of the Unreal Engine source distribution.

It will create a URL for each item found, download it, extract the appropriate
"blob" from each "pack", and then save it to the correct location in the project
hiercarchy, with the correct filename.

Currently, it outputs to a hardcoded "output" directory.
