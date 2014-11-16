# -*- coding: utf-8 -*-
"""
Utilities for converting RGB values from the Tableau web site to hex values
and generating demo plots
"""

import numpy as np
import matplotlib.pyplot as plt


tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127),
             (199, 199, 199), (188, 189, 34), (219, 219, 141), (23, 190, 207),
             (158, 218, 229)]

tableau10 = [(31, 119, 180), (255, 127, 14), (44, 160, 44), (214, 39, 40),
             (148, 103, 189), (140, 86, 75), (227, 119, 194), (127, 127, 127),
             (188, 189, 34), (23, 190, 207)]

tableau_cb10 = [(0, 107, 164), (255, 128, 14), (171, 171, 171), (89, 89, 89),
                (95, 158, 209), (200, 82, 0), (137, 137, 137), (162, 200, 236),
                (255, 188, 121), (207, 207, 207)]


def make_plot(N):
    """ plot N sine waves"""
    x = np.linspace(0, 2*np.pi, 255)
    for i in range(N):
        plt.plot(x, np.sin(x - i*np.pi/N))

    plt.show()


def rgb_to_hex(rgb):
    """convert rgb tuple to hex"""
    print('{:02x}{:02x}{:02x}'.format(*rgb))


def convert_list(colors):
    """convert list or rgb colors into hex"""
    for rgb in colors:
        rgb_to_hex(rgb)


if __name__ == '__main__':
    plt.style.use('fivethirtyeight')
    plt.style.use('./tableau_cb10.mplstyle')
    make_plot(10)
#    convert_list(tableau_cb10)
