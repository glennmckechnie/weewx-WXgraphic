###############################################################################
#  Localization File WXgraphic https://github.com/glennmckechnie/weewx-uradmon#
#  English                                                                    #
# Copyright (c) 2018-2021 Tom Keffer <tkeffer@gmail.com> and Matthew Wall     #
# Copyright (c) 2021 Johanna Karen Roedenbeck                                 #
#                                                                             #
# See the file LICENSE.txt for your rights.                                   #
###############################################################################
#
# https://weewx.com/docs/customizing.htm#localization

# Generally want the US system for the English language.
unit_system = us

[Units]

    [[Labels]]

        # These are singular, plural
        meter             = " meter",  " meters"
        day               = " day",    " days"
        hour              = " hour",   " hours"
        minute            = " minute", " minutes"
        second            = " second", " seconds"

    [[Ordinates]]

        # Ordinal directions. The last one should be for no wind direction
        directions = N, NNE, NE, ENE, E, ESE, SE, SSE, S, SSW, SW, WSW, W, WNW, NW, NNW, N/A


[Labels]

[Texts]
    "Language" = "English"
    # as per Seasons skin ?
    # From config.txt.tmpl
    "Temp:" = "XTemp:"
    "Wind Chill:" = "XWind Chill:"
    "Heat Idx:" = "XHeat Idx:"
    "Humidity:" = "XHumidity:"
    "Wind:" = "XWind:"
    "Gust:" = "XGust:"
    "Calm" = "XCalm"
    "Rain:" = "XRain:"
    "Dew Pt:" = "XDew Pt:"

    # from wxgraphic_weewx.txt.tmpl
    "Rising_Rapidly" = "XRising_Rapidly"_
    "Rising_Slowly" = "XRising_Slowly"
    "Falling_Slowly" = "XFalling_Slowly"
    "Steady" = "XSteady"
