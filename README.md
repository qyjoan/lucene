PyLucene Installation

    Installing pylucene needs some patience, but you will get it...eventually.

My installation is on OS X Yosemite Version 10.10.2.

A couple of ways that I explored before finally succeeded. I will list them out in
decending order of time.

Option 1: Brew (what led me to successfully installed PyLucene)

    brew install python 
    brew cask install java7
    brew install pylucene

I reinstall python using brew to ensure that the compiler is consistent. More on this
in option 2. Java >=1.7 is required for installing PyLucene. Homebrew will refuse to 
install pylucene if it cannot find java. One way to check
is to see if

    /Library/Java/JavaVirtualMachines/

contains jdk1.7.xxx.jdk. It happened to me that although I had jdk1.8, homebrew was not
able to find it (because I downloaded it directly). I did not find a solution to solve
this, so brew installed java, and removed the previously installed jkd1.8.

Note: the benefit of using brew install is that Apache Ant, which is a requirement for
PyLucene will be installed automatically, and brew will also handle JCC build for you.

If installation is successful, you should see jcc/ and lucene/ directories under:

    /usr/local/lib/python2.7/site-packages/

If you are using a Python distribution, such as Spyder or Canopy, most likely your 
site-packages path does not contain where homebrew install pylucene

    echo 'import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")' >> /Your/default/python/site-packages/homebrew.pth
    export JAVA_HOME=`/usr/libexec/java_home`

Option 2: follow the official Lucene site

    https://lucene.apache.org/pylucene/install.html

Check list:

    1. Java Development Kit (JDK) >=7
    2. Apache Ant 
        http://stackoverflow.com/questions/3222804/how-can-i-install-apache-ant-on-mac-os-x
    3. setuptools is recommended
        https://pypi.python.org/pypi/setuptools
    4. JCC
        https://lucene.apache.org/pylucene/jcc/install.html
        Note:
           JCC was the step where I failed. Here's the error that I was getting:
           http://stackoverflow.com/questions/26570125/error-installing-pylucene-jcc-on-osx
           but I haven't quite figured out how to remove the -x tag.
           Another helpful note is that the compiler that builds Python has to be the same
           as the one you use to build JCC. If not, you need to rebuild Python or it's 
           likely that you will have a clang/gcc mismatch.

    Once JCC is successfully built, the rest should be straightforward by following pylucene
    official installation link listed above.
