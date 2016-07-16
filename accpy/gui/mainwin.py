# -*- coding: utf-8 -*-
''' accpy.gui.menu
author:     felix.kramer(at)physik.hu-berlin.de
'''
from __future__ import division
try:
    from Tkinter import Menu
    from ttk import Frame
except:
    from tkinter import Menu
    from tkinter.ttk import Frame
from .file import latticeeditor, settings, defaults
from .simulate import (gui_twisstrack, gui_parttrack, gui_ramp,
                       gui_quadscansim)
from .measure import (tunes, chromaticity, quadscanmeas, achroscan)
from .optimize import (emittex, twissmatch)
from .help import (documentation, about)
from ..visualize.figures import plotstandards
from ..dataio.hdf5 import confload


def mainwindow(root, version):
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry('{}x{}'.format(w, h))
    root.wm_title("ACCPY gui {}".format(version))
    bar, frame = menubar(root, version, w, h)
    root.config(menu=bar)
    return


def menubar(root, version, w, h):
    def clear(frame):
        # destroy all widgets in fram/tab
        for widget in frame.winfo_children():
            widget.destroy()

    bar = Menu(root)

    # FILE MENU
    FM = Menu(bar, tearoff=0)
    FML = ['Lattice editor',
           'Settings',
           'Quit']

    def File_newlat():
        root.wm_title('accpy gui - lattice editor')
        clear(frame)
        latticeeditor(frame, w, h)
    FM.add_command(label=FML[0], command=File_newlat)

    FM.add_separator()

    def File_settings():
        settings(w, h)
    FM.add_command(label=FML[1], command=File_settings)

    FM.add_separator()

    def File_quit():
        root.quit()     # stops mainloop
        root.destroy()
    FM.add_command(label=FML[2], command=File_quit)
    bar.add_cascade(label="File", menu=FM)

    # SIMULATION MENU
    SM = Menu(bar, tearoff=0)
    SML = ['Betamatrix and dispersion tracking',
           'Particle tracking',
           'Ramp',
           'Quadrupole scan']

    def Simu_twisstrack():
        root.wm_title('accpy gui - simulations: {}'.format(SML[0]))
        clear(frame)
        gui_twisstrack(frame, w, h)
    SM.add_command(label=SML[0], command=Simu_twisstrack)

    def Simu_parttrack():
        root.wm_title('accpy gui - simulations: {}'.format(SML[1]))
        clear(frame)
        gui_parttrack(frame, w, h)
    SM.add_command(label=SML[1], command=Simu_parttrack)

    def Simu_hframp():
        root.wm_title('accpy gui - simulations: {}'.format(SML[2]))
        clear(frame)
        gui_ramp(frame, w, h)
    SM.add_command(label=SML[2], command=Simu_hframp)

    def Simu_quadscan():
        root.wm_title('accpy gui - simulations: {}'.format(SML[2]))
        clear(frame)
        gui_quadscansim(frame, w, h)
    SM.add_command(label=SML[3], command=Simu_quadscan)
    bar.add_cascade(label='Simulation', menu=SM)

    # MEASUREMENT MENU
    MM = Menu(bar, tearoff=0)
    MML = ['Tunes',
           'Chromaticity',
           'Quadrupole scan',
           'Achromat scan']

    def Meas_tunes():
        root.wm_title('accpy gui - measurements: {}'.format(MML[0]))
        clear(frame)
        tunes(frame, w, h)
    MM.add_command(label=MML[0], command=Meas_tunes)

    def Meas_chrom():
        root.wm_title('accpy gui - measurements: {}'.format(MML[1]))
        clear(frame)
        chromaticity(frame, w, h)
    MM.add_command(label=MML[1], command=Meas_chrom)

    def Meas_QuadScan():
        root.wm_title('accpy gui - measurements: {}'.format(MML[2]))
        clear(frame)
        quadscanmeas(frame, w, h)
    MM.add_command(label=MML[2], command=Meas_QuadScan)

    def Meas_AchroScan():
        root.wm_title('accpy gui - measurements: {}'.format(MML[3]))
        clear(frame)
        achroscan(frame, w, h)
    MM.add_command(label=MML[3], command=Meas_AchroScan)
    bar.add_cascade(label='Measurement', menu=MM)

    # Entries for Optimization menu
    OM = Menu(bar, tearoff=0)
    OML = ['Find Transverse emittance exchange section',
           'Twiss matching']

    def Opti_emittex():
        root.wm_title('accpy gui - optimizations: {}'.format(OML[0]))
        clear(frame)
        emittex(frame, w, h)
    OM.add_command(label=OML[0], command=Opti_emittex)

    def Opti_twissmatch():
        root.wm_title('accpy gui - measurements: {}'.format(OML[1]))
        clear(frame)
        twissmatch(frame, w, h)
    OM.add_command(label=OML[1], command=Opti_twissmatch)
    bar.add_cascade(label='Optimization', menu=OM)

    # Entries for Help menu
    HM = Menu(bar, tearoff=0)
    HML = ['Documentation',
           'About ACCPY...']

    def Help_docs():
        documentation(version, w, h)
    HM.add_command(label=HML[0], command=Help_docs)

    def Help_about():
        about(version, w, h)
    HM.add_command(label=HML[1], command=Help_about)
    bar.add_cascade(label="Help", menu=HM)

    frame = Frame(root)
    frame.pack(expand=True)

    # load settings
    try:
        varlist, vallist = confload('./settings.conf')
    except:
        varlist, vallist = defaults('./settings.conf')
    plotstandards(varlist, vallist, w, h)
    return bar, frame
