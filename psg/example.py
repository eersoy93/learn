# PySimpleGUI Learning Example main script
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
import PySimpleGUI as psg

def main(args):
    psg.theme("DarkBlue11")

    layout = [ [psg.Text("IT WILL BE A WASTELAND!!!")],
               [psg.Text("Enter the name:"), psg.InputText()],
               [psg.Button("Ok"), psg.Button("Cancel")] ]

    window = psg.Window("DESTROY THEM!!!", layout)

    while True:
        event, values = window.read()
        if event == psg.WINDOW_CLOSED or event == "Cancel":
            break
        print(f"This is a joke, {values[0]}!!!")

if __name__ == "__main__":
    sys.exit(main(sys.argv))
