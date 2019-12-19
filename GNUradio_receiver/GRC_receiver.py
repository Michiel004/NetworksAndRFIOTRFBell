#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Grc Receiver
# Generated: Sat Dec 14 12:31:37 2019
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import logpwrfft
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import numbersink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import module1
import osmosdr
import time
import wx


class GRC_receiver(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Grc Receiver")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.value = value = -55
        self.station_frequency = station_frequency = 88000000
        self.samp_rate = samp_rate = 2000000

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_numbersink2_0_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit='Units',
        	minval=-100,
        	maxval=100,
        	factor=1.0,
        	decimal_places=10,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=2000000,
        	average=False,
        	avg_alpha=None,
        	label='Number Plot',
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_0_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=88000000,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.rtlsdr_source_1 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_1.set_sample_rate(samp_rate)
        self.rtlsdr_source_1.set_center_freq(100e6, 0)
        self.rtlsdr_source_1.set_freq_corr(0, 0)
        self.rtlsdr_source_1.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_1.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_1.set_gain_mode(False, 0)
        self.rtlsdr_source_1.set_gain(10, 0)
        self.rtlsdr_source_1.set_if_gain(20, 0)
        self.rtlsdr_source_1.set_bb_gain(20, 0)
        self.rtlsdr_source_1.set_antenna('', 0)
        self.rtlsdr_source_1.set_bandwidth(0, 0)

        self.module1_comparator_py_f_0 = module1.comparator_py_f(value)
        self.logpwrfft_x_0 = logpwrfft.logpwrfft_c(
        	sample_rate=samp_rate,
        	fft_size=512,
        	ref_scale=2,
        	frame_rate=30,
        	avg_alpha=1.0,
        	average=False,
        )
        self.blocks_max_xx_0 = blocks.max_ff(512,1)
        self.band_pass_filter_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	1, samp_rate, 1000, 10000, 10000, firdes.WIN_HAMMING, 6.76))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.logpwrfft_x_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.module1_comparator_py_f_0, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.wxgui_numbersink2_0_0, 0))
        self.connect((self.logpwrfft_x_0, 0), (self.blocks_max_xx_0, 0))
        self.connect((self.rtlsdr_source_1, 0), (self.band_pass_filter_0, 0))

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_station_frequency(self):
        return self.station_frequency

    def set_station_frequency(self, station_frequency):
        self.station_frequency = station_frequency

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.rtlsdr_source_1.set_sample_rate(self.samp_rate)
        self.logpwrfft_x_0.set_sample_rate(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 1000, 10000, 10000, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=GRC_receiver, options=None):
    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
