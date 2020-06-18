from conans import ConanFile, CMake, tools
import os

class ZipConan(ConanFile):
    name = "zip"
    license = "The Unlicense"
    author = "Kuba Podgorski"
    url = "https://github.com/kuba--/zip"
    description = "Provides simple zip and unzip functionality"
    settings = "os", "compiler", "arch", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    exports = ["UNLICENSE"]
    generators = "cmake"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        os.rename(self.name + "-" + self.version, self._source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_DISABLE_TESTING"] = "On"
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src=self._source_subfolder, keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.dll", dst="lib", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy('*.so*', dst='lib', keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["zip"]

