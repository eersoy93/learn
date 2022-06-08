# NumPy Learning Example main script
# Copyright (C) 2022 Erdem Ersoy (eersoy93)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def printLine():
    print("-" * 80)

def main(args):
    print(np.__version__)
    arr = np.array([1, 2, 3, 4, 5], ndmin=5, dtype="int64")
    print(arr[0, 0, 0, 0, 2:4])
    print(arr.shape)

    printLine()

    arr2 = np.array([1, 2, 3, 4, 5])
    x = np.random.choice(arr2, p=[0.2, 0.4, 0.1, 0.25, 0.05], size=(100))
    print(x)

    printLine()

    sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
    plt.show()

    printLine()

    x = np.random.normal(loc=1, scale=2, size=(2, 5))
    print(x)

    printLine()

    x = sns.distplot(np.random.normal(size=1000), hist=False)
    plt.show()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
