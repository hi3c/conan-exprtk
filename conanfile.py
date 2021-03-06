from conans import ConanFile, CMake, tools
import os


class ExprtkConan(ConanFile):
    name = "exprtk"
    version = "5d0dd1b_1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    generators = "cmake"

    def source(self):
        tools.download("https://github.com/ArashPartow/exprtk/raw/{}/exprtk.hpp".format(self.version.split("_")[0]), "exprtk.hpp")

    def package(self):
        self.copy("*.hpp", dst="include/Exprtk", src=".")

    def package_info(self):
        self.cpp_info.libs = []
