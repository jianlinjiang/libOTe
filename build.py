import os
import sys


folder = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(folder+"/cryptoTools/CMakeLists.txt") == False:
    os.system("git submodule update --init")

import cryptoTools.build


def replace(argv, find, rep):
    return cryptoTools.build.replace(argv, find, rep)


if __name__ == "__main__":

    argv = sys.argv
    # only to build silent vole
    replace(argv, "--bitpolymul", "-DENABLE_SILENT_VOLE=ON -DENABLE_BITPOLYMUL=ON -DENABLE_SOFTSPOKEN_OT=ON -DENABLE_MRR_TWIST=ON -DENABLE_SSE=ON -DENABLE_SILENTOT=ON -DNO_SILVER_WARNING=ON")
    cryptoTools.build.main("libOTe", argv[1:])
