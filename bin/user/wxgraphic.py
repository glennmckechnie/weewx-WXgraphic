# Copyright (c) 2017-2020 Glenn McKechnie <glenn.mckechnie@gmail.com>
# Credit to Tom Keffer <tkeffer@gmail.com>, Matthew Wall and the core
#        weewx team, all from whom I've borrowed heavily.
# Mistakes are mine, corrections and or improvements welcomed
#      https://github.com/glennmckechnie/weewx-sqlbackup
#
# See the file LICENSE.txt for your full rights.
#
#


import weewx.engine
import weewx.manager
import weewx.units
from weewx.cheetahgenerator import SearchList

wxgraphic_version = "0.6.4"

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
sql_debug = 5 will also need to be set in skin.conf
[Logging]
    [[loggers]]
        [[[user.sqlbackup]]]
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

        # local (skin) debug switch "2" or weewx.debug, "4" adds extra to html
        # report page
        # 5 is for release testing only and can safely be ignored by users
        try:
            self.sql_debug = int(self.generator.skin_dict['WXgraphic'].get(
                'sql_debug', '5'))
        except KeyError as e:
            # err with duplicate skin, if skin.conf [section] isn't renamed
            logerr("KeyError: Missing skin [section] heading? - %s" % e)
            return
        if weewx.debug >= 1 or self.sql_debug >= 1:
            loginf('version is %s' % wxgraphic_version)

        self.d_f_p = self.generator.skin_dict['WXgraphic'].get(
            'data_file_path')
        if not self.d_f_p:
            data_path = self.generator.config_dict['StdReport']["WXgraphic"] \
                .get('HTML_ROOT', '/var/www/html/weewx/wgraphic')
            self.d_f_p = (data_path+"/DATA/wxgraphic_weewx.txt")

        self.img_style = self.generator.skin_dict['WXgraphic'].get(
            'image_style', 'default')
        # These values are used by the php script. Empty values will break
        # the script with NO feedback so we will at least prevent null values
        if not self.img_style:
            self.img_style = "default"
        self.img_type = self.generator.skin_dict['WXgraphic'].get(
            'image_format', 'png')
        if not self.img_type:
            self.img_type = "png"
        self.f_file = self.generator.skin_dict['WXgraphic'].get(
            'font_file', 'none')
        if not self.f_file:
            self.f_file = "none"
        self.b_u = self.generator.skin_dict['WXgraphic'].get(
            'barom_units', '')
        self.r_u = self.generator.skin_dict['WXgraphic'].get(
            'rain_units', '')
        self.d_u = self.generator.skin_dict['WXgraphic'].get(
            'degree_units', '')
        self.w_u = self.generator.skin_dict['WXgraphic'].get(
            'wind_units', '')
        self.w_c_t = self.generator.skin_dict['WXgraphic'].get(
            'wind_chill_threshold', '15.5')
        if not self.w_c_t:
            self.w_c_t = "15.5"
        self.h_i_t = self.generator.skin_dict['WXgraphic'].get(
            'heat_index_threshold', '21')
        if not self.h_i_t:
            self.h_i_t = "21"
        self.c_c_i = self.generator.skin_dict['WXgraphic'].get(
            'curr_cond_icon', 'yes')
        if not self.c_c_i:
            self.c_c_i = "yes"
        self.t_f = self.generator.skin_dict['WXgraphic'].get(
            'time_format', '24HR')
        if not self.t_f:
            self.t_f = "24HR"
        self.title_here = self.generator.skin_dict['WXgraphic'].get(
            'weather_station', 'Add a title')
        if not self.title_here:
            self.title_here = "Add a title"
        self.add_text = self.generator.skin_dict['WXgraphic'].get(
            'additional_text', 'Click for More')
        if not self.add_text:
            self.add_text = "Click for More"

        if self.sql_debug >= 5:  # sanity check for releases - safely ignored.
            logdbg("wxg: image_type is %s" % self.img_style)
            logdbg("wxg: data_file_path is %s" % self.d_f_p)
            logdbg("wxg: image_format is %s" % self.img_type)
            logdbg("wxg: font_file is %s" % self.f_file)
            logdbg("wxg: barom_unit %s" % self.b_u)
            logdbg("wxg: rain_units: %s" % self.r_u)
            logdbg("wxg: degree units: %s" % self.d_u)
            logdbg("wxg: wind units: %s" % self.w_u)
            logdbg("wxg: wind chill: %s" % self.w_c_t)
            logdbg("wxg: heat index: %s" % self.h_i_t)
            logdbg("wxg: current condition icon: %s" % self.c_c_i)
            logdbg("wxg: time format: %s" % self.t_f)
            logdbg("wxg: weather station is %s" % self.title_here)
            logdbg("wxg: additional text is %s" % self.add_text)
