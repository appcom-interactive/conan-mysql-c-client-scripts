# Conan MySQL C-Connector

This repository contains the conan receipe that is used to build the MySQLClient packages at appcom.

For Infos about the MySQL C-Connector please visit [dev.mysql.com](https://dev.mysql.com/downloads/connector/c/).
The library is licensed under the [GPL-2.0 License](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html).
This repository is licensed under the [MIT License](LICENSE).

## macOS

To create a package for macOS you can run the conan command like this:

`conan create . mysql-c-client/6.1.9@appcom/stable -s os=Macos -s os.version=10.14 -s arch=x86_64 -s build_type=Release -o shared=False`

### Requirements

* [CMake](https://cmake.org/)
* [Conan](https://conan.io/)
* [Xcode](https://developer.apple.com/xcode/)
