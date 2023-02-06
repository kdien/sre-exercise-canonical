# SRE Automation Exercise

## Requirements
Debian uses *deb packages to deploy and upgrade software. The packages are stored in repositories and each repository contains the so called ["Contents index"](https://wiki.debian.org/RepositoryFormat#A.22Contents.22_indices).

The task is to develop a Python command line tool that takes the architecture (amd64, arm64, mips, etc.) as an argument and downloads the compressed Contents file associated with it from a [Debian mirror](http://ftp.uk.debian.org/debian/dists/stable/main/). The program should parse the file and output the statistics of the top 10 packages that have the most files associated with them.

Example output:
```
./package_statistics.py amd64


1. <package name 1> <number of files>
2. <package name 2> <number of files>
......
10. <package name 10> <number of files>
```

## Results
Having basically no experience with Python, this has been a challenging yet very interesting exercise. I really enjoyed learning several common use-cases with Python: argument parsing, making web requests to download file, opening file in different modes, dealing with lists and dictionaries, etc.

### Total time spent
Almost **4 hours**, with a significant portion spent on learning the language and looking up libraries commonly used to achieve certain tasks broken down from the main requirements (see [commit history](https://github.com/kdien/sre-exercise-canonical/commits/main) for more details).

### Done
The script works and fulfills the requested features, with quite decently-formatted console output.

### TODO
Potential unit tests. For now, I'm not sure how to approach this for the purpose of this script, and since I've spent quite a bit more than the suggested 2 hours, this will need to ship as `v0.1`.

