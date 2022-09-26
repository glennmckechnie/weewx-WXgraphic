
**26th Sept 2022**

This repo consists of a wrapper to install wxgraphic-6.3, a "Weather Graphic" image generator that was originally available at [anolecomputer.com/wxgraphic](https://web.archive.org/web/20130105094954/http://scripts.anolecomputer.com/wxgraphic/). The original is also available at [Saratoga-Weather.org](https://saratoga-weather.org/wxtemplates/plugins.php)
The rest of this repo is a skin to enable weewx to install a working version on your weewx installation. Some configuration will no doubt be needed to suit your setup - colors, fonts, branding etc.


## What is wxgraphic

In the words of the original author, anolecomputer.com...


"First a disclaimer. I am not a programmer. Anyone who is and looks at this code will instantly recognize that. This script was basically begun as a way to teach myself some PHP and image manipulation. I am well aware that there are probably numerous ways to do what I've done here much more efficiently and I encourage the real programmers out there who look at this script and see a way to make it better to provide some input. Now that that is out of the way....

This script generates a graphical weather image in GIF, PNG or JPG format created from a user supplied background image and data file. This script supports true type fonts and built-in GD fonts.

To utilize this script you should understand the following basic concepts:

  1.  What file paths are, absolute and relative.
  2.  How to make your weather station software parse and upload a template file.
  3.  How to include an image file on a web page.

            Additionally, if you wish to modify the text locations, customize the data points displayed, etc., you should have at least a basic understanding of PHP scripting, and a basic understanding of x,y coordinates within images."

## And as of now?

Well, it seems to have stood the test of time so a little tweaking to suit weewx is in order.

The script still works for the original file formats - clientraw.txt etc.

A simple weewx skin and its template can generate a suitable file to feed wxgraphic installed on a local webserver.




# Install, then configure


    stop weewx

    wget -O weewx-wxgraphic.zip https://github.com/glennmckechnie/weewx-wxgraphic/archive/master.zip
    wee_extension --install weewx-wxgraphic.zip

    start weewx

    This will install a skin named WXgraphic under the skins directory and it will be enabled in weewx.conf

    It requires that your webserver runs php, and has access to GD. There is a file named PHP_verify.php within the new (www)wxgraphic server directory. Access that from your browser and it should present a html page that will hopefully announce your successful web server setup, if not install php for your webserver, or satisfy its other needs.

    iWhen the weewx report cycle runs it will copy the www/wxgraphic directory to your webserver once, and once only. It will be named wxgraphic and will be in your weewx root directory (weewx/wxgraphic) by default. Within that wxgraphic directory is a file named config.txt. That will require editing to change the configuration to suit your taste, set up. You have your choice of banner, banner_big, avatar or if nothing is selected, a default image. Only the *.png files are copied over. If you want the other formats (jpeg, gif) thats a manual job for you to perform.
    
    The data to feed wxgraphic will be transferred at each weewx report cycle to (www) wxgraphic/DATA/weewx-wxgraphic.txt via the skins/WXgraphic/DATA/weewx-graphic.txt.tmpl
    Currently no editing is required within the skin.conf file - that may change later.


