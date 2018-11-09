from conans import ConanFile, CMake, tools
import os

class ZlibConan(ConanFile):
    name = "MySQLClient"
    version = "6.1.9"
    author = "Ralph-Gordon Paul (gordon@rgpaul.com)"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "android_ndk": "ANY", "android_stl_type":["c++_static", "c++_shared"]}
    default_options = "shared=False", "android_ndk=None", "android_stl_type=c++_static"
    description = "A MySQL-Client library for C development."
    url = "https://github.com/Manromen/conan-mysql-c-client-scripts"
    license = "GPL-2.0-only"
    exports_sources = "cmake-modules/*"

    # download sources
    def source(self):
        url = "https://dev.mysql.com/get/Downloads/Connector-C/mysql-connector-c-%s-src.tar.gz" % self.version
        tools.get(url)

    # compile using cmake
    def build(self):
        cmake = CMake(self)
        library_folder = "%s/mysql-connector-c-%s-src" % (self.source_folder, self.version)
        cmake.verbose = True

        if self.settings.os == "Macos":
            cmake.definitions["CMAKE_OSX_ARCHITECTURES"] = tools.to_apple_arch(self.settings.arch)

        cmake.configure(source_folder=library_folder)
        cmake.build()
        cmake.install()

        lib_dir = os.path.join(self.package_folder,"lib")

        if self.settings.os == "Macos":
            # delete shared artifacts for static builds and the static library for shared builds
            if self.options.shared == False:
                for f in os.listdir(lib_dir):
                    if f.endswith(".dylib"):
                        os.remove(os.path.join(lib_dir,f))
            else:
                for f in os.listdir(lib_dir):
                    if f.endswith(".a"):
                        os.remove(os.path.join(lib_dir,f))

    def package(self):
        self.copy("*", dst="include", src='include')
        self.copy("*.lib", dst="lib", src='lib', keep_path=False)
        self.copy("*.dll", dst="bin", src='bin', keep_path=False)
        self.copy("*.so", dst="lib", src='lib', keep_path=False)
        self.copy("*.dylib", dst="lib", src='lib', keep_path=False)
        self.copy("*.a", dst="lib", src='lib', keep_path=False)
        
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.includedirs = ['include']

    def config_options(self):
        # remove android specific option for all other platforms
        if self.settings.os != "Android":
            del self.options.android_ndk
            del self.options.android_stl_type
