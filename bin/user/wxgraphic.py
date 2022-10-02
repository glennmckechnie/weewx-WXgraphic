# Copyright (c) 2017-2020 Glenn McKechnie <glenn.mckechnie@gmail.com>
# Credit to Tom Keffer <tkeffer@gmail.com>, Matthew Wall and the core
#        weewx team, all from whom I've borrowed heavily.
#
# Mistakes are mine, corrections and or improvements welcomed at
#      https://github.com/glennmckechnie/weewx-WXgraphic
#
# See the file LICENSE.txt for your full rights.
#
#


import weewx.engine
import weewx.manager
import weewx.units
from weewx.cheetahgenerator import SearchList

wxgraphic_version = "0.6.5"

try:
    # Test for new-style weewx logging by trying to import weeutil.logger
    import weeutil.logger
    import logging
    log = logging.getLogger(__name__)

    def logdbg(msg):
        log.debug(msg)

    def loginf(msg):
        log.info(msg)

    def logerr(msg):
        log.error(msg)

except ImportError:
    # Old-style weewx logging
    import syslog

    def logmsg(level, msg):
        syslog.syslog(level, 'wxgraphic: %s:' % msg)

    def logdbg(msg):
        logmsg(syslog.LOG_DEBUG, msg)

    def loginf(msg):
        logmsg(syslog.LOG_INFO, msg)

    def logerr(msg):
        logmsg(syslog.LOG_ERR, msg)

"""
add to weewx.conf if debug output is required
wxg_debug = 5 will also need to be set in skin.conf
[Logging]
    [[loggers]]
        [[[user.wxgraphic]]]
            level = DEBUG
            handlers = syslog,
            propagate = 0

"""


class WXgraphic (SearchList):
    """ Notes and WARNINGS
    # only because I can never remember
    # date -d "11-june-2017 21:00:00" +'%s'
    # 1497178800
    #
    # date +"%s"
    # returns  current epoch time
    """

    def __init__(self, generator):
        SearchList.__init__(self, generator)

        # local (skin) debug switch "2" or weewx.debug
        # 5 is for release testing only and can safely be ignored by users
        self.wxg_debug = int(self.generator.skin_dict['WXgraphic'].get(
                'wxg_debug', '0'))
        if weewx.debug >= 1 or self.wxg_debug >= 1:
            loginf('version is %s' % wxgraphic_version)

        self.d_f_p = self.generator.skin_dict['WXgraphic']['Clientraw'].get(
            'data_file_path')
        if not self.d_f_p:
            data_path = self.generator.config_dict['StdReport']["WXgraphic"] \
                .get('HTML_ROOT', '/var/www/html/weewx/wgraphic')
            self.d_f_p = (data_path+"/DATA/wxgraphic_weewx.txt")

        self.title_here = self.generator.skin_dict['WXgraphic'].get(
            'weather_station')
        if not self.title_here:
            self.title_here = self.generator.config_dict['Station'].get('location')

        self.img_style = self.generator.skin_dict['WXgraphic'].get(
            'image_style', 'default')
        # These values are used by the php script. Empty values will break
        # the script with NO feedback so we will at least prevent null values
        self.img_type = self.generator.skin_dict['WXgraphic'].get(
            'image_format', 'png')
        self.f_file = self.generator.skin_dict['WXgraphic'].get(
            'font_file', 'none')
        self.ttf_on = self.generator.skin_dict['WXgraphic'].get(
            'anti_alias', 'on')
        self.w_c_t = self.generator.skin_dict['WXgraphic'].get(
            'wind_chill_threshold', '15')
        self.h_i_t = self.generator.skin_dict['WXgraphic'].get(
            'heat_index_threshold', '21')
        self.c_c_i = self.generator.skin_dict['WXgraphic'].get(
            'curr_cond_icon', 'yes')
        self.add_text = self.generator.skin_dict['WXgraphic'].get(
            'additional_text', 'Click for More')

        # settings specific to the clientraw.txt file
        self.b_u = self.generator.skin_dict['WXgraphic']['Clientraw'].get(
            'barom_units', '')
        self.r_u = self.generator.skin_dict['WXgraphic']['Clientraw'].get(
            'rain_units', '')
        self.d_u = self.generator.skin_dict['WXgraphic']['Clientraw'].get(
            'degree_units', '')
        self.w_u = self.generator.skin_dict['WXgraphic']['Clientraw'].get(
            'wind_units', '')
        self.t_f = self.generator.skin_dict['WXgraphic']['Clientraw'].get(
            'time_format', '24HR')

        if self.wxg_debug >= 5:  # sanity check for releases - safely ignored.
            loginf("wxg: image_type is %s" % self.img_style)
            loginf("wxg: data_file_path is %s" % self.d_f_p)
            loginf("wxg: image_format is %s" % self.img_type)
            loginf("wxg: font_file is %s" % self.f_file)
            loginf("wxg: anti_alias is %s" % self.ttf_on)
            loginf("wxg: wind chill: %s" % self.w_c_t)
            loginf("wxg: heat index: %s" % self.h_i_t)
            loginf("wxg: current condition icon: %s" % self.c_c_i)
            loginf("wxg: weather station is %s" % self.title_here)
            loginf("wxg: additional text is %s" % self.add_text)
            loginf("wxg: time format: %s" % self.t_f)
            loginf("wxg: wxg_debug: %s" % self.wxg_debug)
            #loginf("wxg: barom_units: %s" % self.b_u)
            #loginf("wxg: rain_units: %s" % self.r_u)
            #loginf("wxg: degree units: %s" % self.d_u)
            #loginf("wxg: wind units: %s" % self.w_u)
