Weather graphic generator v6.3
Copyright (C) 2005 Anole Computer Services, LLC
scripts@anolecomputer.com

License
-------

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

===============================================================================

****************************************************************************
***                                                                      ***
*** NOTE: for more detailed information about this script, please visit: ***
*** http://scripts.anolecomputer.com/wxgraphic/                          *** 
***                                                                      ***
****************************************************************************

General Description
-------------------

First a disclaimer. I am not a programmer. Anyone who is and looks at this
code will instantly recognize that. This script was basically begun as a way
to teach myself some PHP and image manipulation. I am well aware that there
are probably numerous ways to do what I've done here in much more efficient
ways and I am encourage the real programmers out there who look at this 
script and see a way to make it better to provide some input. Now that that
is out of the way....

This script generates an image in GIF, PNG or JPG format created from a user 
supplied background image and data file. If no background image is used a 
simple box with a one pixel black frame is created. This script supports true 
type fonts and built-in GD fonts.

Obviously, since this is a PHP script, your server needs to support PHP.

To utilize this script you should understand the following basic concepts:

  1) What file paths are, absolute and relative.
  2) How to make your weather station software parse and upload a template
     file.
  3) How to include an image file on a web page.

Additionally, if you wish to modify the text locations, customize the data 
points displayed, etc., you should have at least a basic understanding of PHP
scripting, and a basic understanding of x,y coordinates within images.

===============================================================================

Requirements
-------------------

This script requires the following to function:

PHP release 4.3.0 or higher with GD support.
GD release 2.0.28 or higher (provides GIF support).

===============================================================================

Installing the script
---------------------

To install the script:

  1) Unpack/unzip the archive.
 
  2) Copy the appropriate data template file to the location that suits the
     weather station software you use.

  3) Enable processing and upload of the file to the location you want on the 
     server.

  4) Verify that the file is being processed an uploaded to the server.

  5) Create a directory on your server that can be accessed with a URL, 
     ie, in your document root or subdirectory of it. The file can be placed
     in an existing directory if desired.

  6) Set the following parameters in the file config.txt to match your specific 
     configuration. Refer to the Notes section for details:

       $data_file
       $image_format
       $font_file
       $barom_units
       $rain_units
       $degree_units
       $wind_units
       $wind_chill_threshold
       $heat_index_threshold
       $curr_cond_icon 

      ** YOU MUST SET $data_file, $image_format AND $font_file PROPERLY OR THE 
      ** SCRIPT WILL NOT WORK!!!
      
      If you are using Weather Display clientraw.txt additional
      parameters should be defined. If you are not using clientraw.txt
      you do not need to set these parameters:

        $time_format
        $temp_conv
        $temp_prec
        $wind_conv
        $wind_prec 
        $barom_conv
        $rain_conv
        $rain_prec

  7) Copy the following files to the directory you want to run the script from:

       wxgraphic.php
       config.txt
       default.gif, default.png, or default.jpg 
       banner.gif, banner.png, or banner.jpg
       banner_big.gif, banner_big.png, or banner_big.jpg
       The font file you want to use if using a TrueType font.
       
       Copy current conditions icons to a subdirectory called "/icons" if you are 
       using them.


===============================================================================

Using The Script
----------------
Once installed you use the script by calling it in an <img> tag with the 
appropriate URL. The default graphic type is a 150px X 150px square. To 
generate the banners or avatar, add a type value to the URL query string:

To display the default graphic:
<img src="http://your.domain.com/url/to/script/wxgraphic.php">

To display the banner graphic:
<img src="http://your.domain.com/url/to/script/wxgraphic.php?type=banner">

To display the big banner graphic:
<img src="http://your.domain.com/url/to/script/wxgraphic.php?type=banner_big">

To display the avatar graphic:
<img src="http://your.domain.com/url/to/script/wxgraphic.php?type=avatar">

===============================================================================

Image Format
------------
The script supports image creation in the following formats:
GIF, PNG, and JPEG.

Select the image format by setting $image_format in config.txt to one of the 
following values:

GIF: 
$image_format = 'gif';

PNG:
$image_format = 'png';

JPEG:
$image_format = 'jpeg';

Your background and icon images must match the selected format. Copies of all
background and icon images in all three formats are provided in the archive.

===============================================================================

Data File
---------
The script requires a text data file in the following format:
 
time,date,temp,heat index,wind chill,humidity,dew point,barometer,barometer trend,wind speed,wind direction,todays rain

VWS users should use the following format if they wish to include a current
conditions icon:
time,date,temp,heatindex,wind chill,humidity,dew point,barometer,barometer trend,wind speed,wind direction,todays rain,currentconditions,sunrise,sunset

The currentconditions parameter must be one of the ^climate_ccondsx^ tags 
from VWS. The default in the provided example template is ^climate_cconds1^.

Weather Display users have the option of using the clientraw.txt file directly.
If using clientraw.txt no additional template file is required.

Data is written into an array called $data. Individual data points are
then referenced as $data[0] for time, $data[1] for date, etc., so adding
additional parameters is a matter of adding them to your template and
then calling them with the proper reference. 

NOTE: If you add additional parameters to the graphics you will need to add
the parameter names to the following global declaration of the following 
functions in config.txt:
  write_default() at line 186
  write_banner() at line 230
  write_banner_big() at line 274
  write_avatar() at line 318

clientraw.txt data points are referenced by their order in the clientraw.txt
file. See the clientrawdescription.txt file included with Weather Display for 
more information.

Data file templates are provided in the archive for most of the popular
weather station software packages.

$data_file defines the path to the data file. This path is NOT A URL!! 
To avoid confusion it is recommended that you use an absolute file path.
If you are comfortable with the concept, a relative path can be used as 
well.

If the script is unable to get the data file it will output an image in the 
proper format indicating that no data was available. The text of this message
can be modified at line 68 of wxgraphic.php

===============================================================================

Weather Display clientraw.txt Functionality
-------------------------------------------
As noted above, if you are using Weather Display's clientraw.txt file as your
data source, there are additional parameters you must configure in the script.
This is necessary because unlike the html tags generated by the various weather
software packages (including Weather Display), clientraw.txt does not take into
account your unit preference settings. For example, temperature readings in
clientraw.txt are always in C even if your have your Weather Display preferences 
set to display in F. 

In order to make it possible to make the values appear in the units you desire 
you must therefore set those units in the script. Additionally, because the 
units are converted via mathematical functions, you must specify the precision
(number of decimal places) you wish to see in the final display. Keep in mind 
that these values represent the maximum number of decimal places to display. If
a precision is set to '2' and there is only one decimal place in the value, only
one decimal place will be displayed.

Do not confuse these settings with the unit settings $barom_units, $rain_units,
$degree_units, and $wind_units! The unit settings do not control conversion.
They are there to make it possible for you display, or not display units as 
you choose.

===============================================================================

Background Images
-----------------
The script assumes the following background images are available:

 1) 150px X 150px background image for the default named "default.gif"
    "default.png", or "default.jpeg"

 2) 468px X 60px background image for the standard banner named "banner.gif"
    "banner.png", or "banner.jpeg"

 3) 500px X 80px background image for the big banner named "banner_big.gif"
    "banner_big.png", or "banner_big.jpeg"

 4) 100px X 100px background image for the avatar named "avatar.gif"
    "avatar.png", or "avatar.jpeg"

To change the size of the image, simply create a new background image in the
dimensions you want then pload the resized background image to your script 
directory. You will most likely have to move the text around on the image
to make it fit the new size properly.

You can move items around on the images by modifying the writing functions
write_default(), write_banner(), write_banner_big(), and write_avatar(), in 
config.txt. If you are using the current conditions icon feature you must also
account for the space that the icon will occupy. Please refer to the section: 
"Current Conditions Icons" below for more details.

If the background image does not meet the above criteria for blank space
you will have to make changes to config.txt in the sections that draw
the data onto the background image.

===============================================================================

Current Conditions Icons
------------------------
* NOTE: This feature is currently only works if you are using Weather Display
* clientraw.txt as your data file, or a VWS version that includes the 
* ^climate_cconds1^ tag.

All graphics support the inclusion of a current conditions icon embedded within
the generated graphic. Current conditions iconsare 25px X 25px in size. Icon 
position is controlled by the following parameters in config.txt:
$default_icon_x
$default_icon_y
$banner_icon_x 
$banner_icon_y
$banner_big_icon_x
$banner_big_icon_y
$avatar_icon_x 
$avatar_icon_y

These values represent the location upper left pixel of the icon within the
graphics. For example:

$default_icon_x = '2';
$default_icon_y = '2';

will place the icon on the default image with the upper left pixel located at
x = 2 and y = 2 on the default background image. Since the icon image is 
25px X 25px the icon will fill a square on the image whose corners will be 
located at:

UL: x = 2, y = 2
UR: x = 27, y = 2
LL: x = 2, y = 27
LR: x = 27, y = 27

Keep the boundaries of the icon in mind so that the icon does not overwrite
any of your data on the image.

If you wish to use the current conditions icon on your graphic,
$curr_cond_icon in config.txt should be set to: 

$curr_cond_icon = 'yes';

Setting to any other value or leaving it blank will turn off the current
conditions icon.

A group of default icons has been provided in the script archive. You are free
to substitute your own icons. While some of them are decent, I'm no graphics 
artist so it certainly won't hurt my feelings if you don't want to use them! :)

Icons should be 25px X 25px and should be saved in GIF, PNG or JPEG format to
match the format selected in config.txt and should use the same names as the 
provided icons. If you wish to make them a different size, format, or name them
something else you will need to make modifications to the script.

Below is a list of the included icon images:

day_clear.gif, day_clear.png, day_clear.jpeg
day_cloudy.gif, day_cloudy.png, day_cloudy.jpeg
day_heavy_rain.gif, day_heavy_rain.png, day_heavy_rain.jpeg
day_light_rain.gif, day_light_rain.png, day_light_rain.jpeg
day_mostly_sunny.gif, day_mostly_sunny.png, day_mostly_sunny.jpeg
day_partly_cloudy.gif, day_partly_cloudy.png, day_partly_cloudy.jpeg
day_rain.gif, day_rain.png, day_rain.jpeg
day_snow.gif, day_snow.png, day_snow.jpeg
day_tstorm.gif, day_tstorm.png, day_tstorm.jpeg
night_clear.gif, night_clear.png, night_clear.jpeg
night_cloudy.gif, night_cloudy.png, night_cloudy.jpeg
night_heavy_rain.gif, night_heavy_rain.png, night_heavy_rain.jpeg
night_light_rain.gif, night_light_rain.png, night_light_rain.jpeg
night_partly_cloudy.gif, night_partly_cloudy.png, night_partly_cloudy.jpeg
night_rain.gif, night_rain.png, night_rain.jpeg
night_snow.gif, night_snow.png, night_snow.jpeg
night_tstorm.gif, night_tstorm.png, night_tstorm.jpeg
fog.gif, fog.png, fog.jpeg
haze.gif, haze.png, haze.jpeg
mist.gif, mist.png, mist.jpeg
sleet.gif, sleet.png, sleet.jpeg
snow.gif, snow.png, snow.jpeg
tornado.gif, tornado.png, tornado.jpeg
windy.gif, windy.png, windy.jpeg

Which icon is displayed for WD clientraw is defined in the section of 
wxgraphic.php at line 197 marked:
   // CURRENT CONDITIONS ICONS FOR clientraw.txt

Which icon is displayed for VWS is defined in the section of 
wxgraphic.php at line 276 marked:
     // CURRENT CONDITIONS ICONS FOR VWS
===============================================================================

TrueType Fonts
--------------
The script can use TTF fonts or the built-in default fonts found in the 
GD image manipulation library. Use of TTF font requires the user to provide
a valid path to the font file. If the file does not currently exist on the
server it must be uploaded. Be sure to upload the font file as binary!

The script checks to verify that the PHP installation supports TrueType fonts
and applies the user defined font to text written to the image. If TrueType
is not supported in the PHP installation, or no font has been specified, the
script defaults to the built-in GD fonts.

The font is determined by the setting for $font_file.  This parameter has one
special value: none. If defined as:

$font_file = 'none'; 

the script will use the default GD fonts.

$font_file should be defined as a path to the appropriate TTF font file that
you want to use. As with $data_file this value is NOT A URL!! The file can be 
located anywhere on your server, but the script has to be able to find it. 
If you place the font file in the same directory as the script, it can be 
defined with the following relative path:

$font_file = './arial.ttf';  

substituting the desired font file name for "arial.ttf". 

===============================================================================

Wind Chill and Heat Index
-------------------------
The script takes the wind chill and heat index parameters from the data file
and determines whether to output them based upon the values set for
$wind_chill_threshold and $heat_index_threshold. 

If the wind chill value is <= $wind_chill_threshold, wind chill will be 
included in the graphic.

If the heat index value is >= $heat_index_threshold, heat index will be
included in the graphic.

If neither criteria is met no data is written into that area of the graphic.

===============================================================================

The Text Writing Functions and Parameters
----------------------------------------
The text writing functions are found in the config.txt file.

If you wish to move things around on the image you need to understand how the
text writing function works. The function that writes the text onto 
the background image is imagecenteredtext(). It takes the supplied x,y 
coordinates, and centers the supplied text on them. So the x,y position you
provide represents the center of the image.
imagecenteredtext() must be passed the following parameters in the following order:

imagecenteredtext(x, y, text, font size (GD default), TTF font size, color, angle)

where: 
 
x = x coordinate where the text will be centered (horizontal placement)
y = y coordinate where the text will be centered (vertical placement)
text = the text to be written
size = font size for built-in GD fonts (1,2,3,4, or 5)
ttfsize = font size for ttf fonts.  8 = 8pt
color = color as defined in the allocate colors section. Default colors available 
        are red, green, blue, black, and white.
angle = for ttf fonts, determines the angle (direction) for the text.

You must pass all parameters! If you aren't using a parameter, just plug a ''
into it's position. 

If you wish to add additional parameters to the graphics, you must also add 
those parameters to the global declarations in the writing functions in 
config.txt at the following locations:
  write_default() at line 220
  write_banner() at line 265
  write_banner_big() at line 310
  write_avatar() at line 354

===============================================================================

Colors
------

Colors are defined in config.txt in the define_colors() function. By default
there are five colors defined as follows:

$color1: red
$color2: green
$color3: blue
$color4: black
$color5: white

Colors are defined in define_colors() using the imagecolorallocate() function
as follows:

imagecolorallocate(image, red, green, blue);
where:
image = image variable. Will always be "$img".
red = red component 0-255
green = green component 0-255
blue = blue component 0-255

You can modify the existing colors by simply changing the rgb components for
the $color1 - $color5 variables.

You may add additional colors if you like but you will need to add the new
variables to the global declarations in both the define_colors() function and
the image writing functions (see above for locations).

===============================================================================

Transparency
------------

The script supports the use of transparent backgrounds for GIF and PNG images.
Transparency is not supported for JPEG.

To use transparency set the value of the color in the background image that you
want to be transparent using it's RGB values in the define_colors() function
found in config.txt

IMPORTANT!
Do not set the transparency in your source image. The image should be saved in
your image editor without any transparency. If you set the transparency in the
source image you will get strange results. The script will set the color you
chose in the variable "$trans_color" as the transparent color of the output
image.

Anti-aliasing and transparency
------------------------------
Anti-aliasing for the purposes of this script refers to smoothing of the text
that is written onto the graphic. Anti-aliasing and transparency often don't 
play well together becuase of the way that anti-aliasing works. In very simple
terms, anti-aliasing of black text on a white background "blends" the black
of the text into the white of the background. This isn't a big deal if the
background of the web page that the transparent image appears on is the same
or close to the transparent color (background) of the image. If it's not you
see a "halo" affect which makes your graphic look bad and in some case the text
unreadable.

The real problem here is that graphics drawing engine the script uses (GD), 
always anti-aliases TrueType fonts by default. If you aren't using a TrueType
font, this is a non-issue since the built-in fonts are not anti-aliased.

To help you avoid this problem you can turn off the anti-aliasing by setting 
the parameter $anti_alias to 'off':
$anti_alias = 'off';

There is a trade-off in doing this though. Your text will look not be as smooth
or look as good. The severity of this degradation is dependent upon the
font being used but all fonts will exhibit some amount of degradation.

To see some examples of the various affects of transparency and anti-aliasing
you can visit: 
http://scripts.anolecomputer.com/wxgraphic/

===============================================================================

Release Notes
-------------

6.3 - Bug Fix: Fixed a bug that caused failure of generation of the \
      "Data Currently Unavailble" image.

      Bug Fix: Replaced mb_convert_case with strtoupper due to compatibilty
      issues seen by some users. 

6.2 - Bug Fix: Fixed a bug that was seen when running PHP5 that caused all
      images to use the settings for the default text locations

6.1 - Consolidated base image creation into a simpler function.

6.0 - The script has been renamed to respect the registered trademark 
      "Weather Sticker" which belongs to Weather Underground. 
      
      Transparency is now turned off by default.

5.5 - Bug Fix: corrected typo in config.txt where "$anti-alias" should have 
      been "$anti_alias"

5.4 - Added transparency support. This support adds two new parameters:
      $trans_color
      $anti_alias
      
      Modified the clientraw precision values so that they will have an impact
      on non-converted values.

      Corrected avatar.jpeg file name in archive.

5.3 - Added PHP_verify.php to archive to facilitate verification of PHP 
      installations on user servers.
      
      Created new web site with additional script information located at:
      http://scripts.anolecomputer.com/wxgraphic/ 

5.2 - Added a 100px X 100px image size for forum avatars. 

5.1 - Fixed a problem (typo) for some of the VWS current conditions icon paths.

5.0 - Moved the icon placement parameters out into the config.txt file to make
      it easier to control placement of the icon. I meant to do this in 4.0
      but somehow overlooked it.
      
      Made it possible to choose your image format with a single parameter in
      config.txt. Options are gif, png, or jpeg.
      
      Current conditions icons now supported for VWS! To use this feature 
      the following tags are added to the template file:
      ^climate_cconds1^,^vst144^,^vst145^
      Thanks to Gordon C. @ oldlineweather.com for coming up with the
      list of possible values for ^climate_cconds1^ and making this possible!

      Added some functionality to handle conditions where the data file is not
      present. Since its possible that the data file could be in the process of
      being uploaded at the time we try to get it, we can end up with a
      situation where we have no data. This can result in either script errors
      or blank images. The script is now much more robust in dealing with 
      problems pulling the data file. Specifically:
        * If the data file is not found on the first attempt it will try again
          after a two second sleep.
        * If the data file is not found on the second attempt it will try again
          after another two second sleep.
        * If the data file is not found on the third attempt an image in the 
          appropriate size (default, banner, banner_big) will be output 
          indicating that there was no data available.

      Corrected some problems with icon images names.

      Corrected text locations in the default images so they'll look a bit
      better initially.

4.1 - Changed the banner size to the standard 468px X 60px ad banner size.
      The larger 500px X 80px banner is still retained but is now called with:
      "type=banner_big".

      Moved the image text color definitions into the config.txt to make them 
      easier to modify.

      Corrected requirements to reflect PHP release 4.3.0 or higher.

      Bug Fix: corrected typo on windy.gif icon mapping.

4.0 - Broke configuration out into a separate file: config.txt
      This should make modification and updating the script a bit easier.
      The config.txt file also contains the data writing functions to make
      modifying them a bit easier.
      
      Bug Fix: Corrected clientraw.txt wind conversions. Values were being
      converted from MPH when they should have been converted from knots. 
      I knew the values were knots but for some reason I was in a fit of 
      "braindeadness" when writing those functions.

      Bug Fix: fixed misplaced ";" in case statement

      Bug Fix: fixed issue relating to not quoting $_REQUEST globals seen in 
      PHP 5.X

      Bug Fix: removed a line I left in by accident that was outputting:
      St. James City, FL Current Weather Conditions on the banner. (Oops!)

      Slight modification to barometric trends for WD clientraw.txt slightly to 
      line it up better with WD values.
      
      Added a "Requirements" section to README.txt

3.1 - Bug Fix: fixed a minor bug that was causing error log entries if current
      conditions icon was not being used.

3.0 - Added support for Weather Display clientraw.txt file. Because of the
      nature of the clientraw.txt file additional user configuration parameters
      specific to it have been added to handle unit and time conversion. 
      
      Added a changing current conditions icon. This currently only works if
      using Weather Display clientraw.txt

      Bug Fix: Fixed a failure to destroy one of the temporary images used for
      final image creation.

2.4 - Changed provided default.gif and banner.gif to remove the sun and 
      cloud from the images. The sun and cloud image that was included on
      those images was created by Kevin Reed at TNET Services, Inc. and were
      not part of the public domain. It was never my intention to create the
      impression that I created that graphic nor was it my intention to 
      violate Mr. Reed's rights with regard to that image so it has been
      removed to avoid any appearance of such.

2.3 - Added two new parameters to make controlling wind chill and heat index
      display easier. Code slightly modified to accommodate this.

2.2 - Bug fix: Still wasn't happy with the way wind units were being handled
      so it was "robustified". Wind units now display if type is banner, but
      don't display if type is default to conserve horizontal space.

      Added gust values to default image creation and data template files.

2.1 - Bug fix: Fixed color allocation issue if gif pallette is already filled.

      Bug fix: Fixed problem where "Calm" was showing as "Calmmph".

      Slight modification to internal functionality to make expansion a bit
      easier.

2.0 - Added support for TrueType fonts.

      Added wind units parameter.

      Made positioning text a little more intuitive by changing the method to
      center both horizontally and vertically on the supplied x,y coordinates.

1.1 - Added user definable measurement unit parameters.

      Eliminated white space between values and units to make display a bit
      more compact.

      Tweaked value locations on banner style graphic.

1.0 - Initial Release

