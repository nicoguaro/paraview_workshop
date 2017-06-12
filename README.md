# Paraview Tutorial

This is the repository for a Paraview Tutorial data.

Instructor: Nicolas Guarin-Zapta

- email: nicoguarin@gmail.com
- twitter: @nicoguaro
- github: nicoguaro

## Installation Instructions

**Note:** The instruction is going to use version 5.2, but any version newer than 5.0 should work for all the examples in the workshop.

The preferred method of installation is to use an installer for your particular operative system.

**Official download link:** [http://www.paraview.org/download/](http://www.paraview.org/download/)


### Windows

You can download the most recent version of ParaView in the [Official website](http://www.paraview.org/download/) (32 or 64 bits) and just run the installer in your machine.

### Mac OS

You can download the most recent version of ParaView in the [Official website](http://www.paraview.org/download/).

### Linux

For major Linux distributions you will find a binary version of ParaView in your software manager. For example, in Ubuntu and Linux Mint you can find version 5.0. It is suggested to use this version.

You can also, download the most recent version of ParaView in the [Official website](http://www.paraview.org/download/), then extract the file with

    mkdir paraview-5.1.2
    tar -xvf ParaView-5.1.2-Qt4-OpenGL2-MPI-Linux-64bit.tar.gz -C paraview-5.1.2 --strip-components=1

or just use your favorite file manager. You can run ParaView using the executable
in ``bin/paraview``. You might need to create a link to this file for future use.


## Downloading the Tutorial Materials
You can clone the repo using:

    git clone https://github.com/nicoguaro/paraview_workshop.git

## Slides
The slides for the tutorial are in the folder [``slides``](./slides) in the ``slides.html`` file. They were written in the ``slides.md`` file, and compiled with

     pandoc -t slidy --css style.css -s slides.md -o slides.html

## License

The content of this project itself is licensed under the [Creative Commons Attribution 4.0 license](http://choosealicense.com/licenses/cc-by-4.0/), and the source code that accompany the content is licensed under the [MIT license](https://opensource.org/licenses/mit-license.php).

[Data files](./data) ``headsq.vti``, ``can.ex2``, and ``disk_out_ref.ex2`` are under Creative Commons Attribution 2.5 Generic by Kitware.
