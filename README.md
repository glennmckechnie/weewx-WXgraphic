
**26th Sept 2022**

This repo consists of a wrapper to install wxgraphic-6.3, a "Weather Graphic" image generator that was originally available at [anolecomputer.com/wxgraphic](https://web.archive.org/web/20130105094954/http://scripts.anolecomputer.com/wxgraphic/). That original file is also available at [Saratoga-Weather.org](https://saratoga-weather.org/wxtemplates/plugins.php)
This repo is concerned with wrapping that original package into an easly installable skin for weewx. It uses the wee_extension script to install a working version to an existing weewx installation. Some configuration will no doubt be needed to suit your setup - colors, fonts, branding etc. You also need a php and GD enabled webserver!


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

1. Knowing your paths is still relevant, but the installer will handle that.
2. The installer will also take care of generating a template file
3. You still need to know how to include an image file on a web page!

The script still works for the original file formats - clientraw.txt if you have that being generated then adjust the script topoint to that.

Otherwise a simple weewx skin will create a template that generates a suitable file to feed wxgraphic, which will be installed on a local webserver, or secure remote server.
Currently, the icons are not available from this template. That may change.




# Install, then configure


   1. Fetch the archive
   
      ```wget -o weewx-WXgraphic-main.zip https://github.com/glennmckechnie/weewx-WXgraphic/archive/refs/heads/main.zip```

   2. Use wee_extension to install it
   
      ```sudo wee_extension --install=weewx-WXgraphic-main.zip```

   3. Restart weewx

      ```sudo /etc/init.d/weewx stop```

      ```sudo /etc/init.d/weewx start```

This will install a skin named WXgraphic under the skins directory and will also enable it in weewx.conf

   4. Configure your webserver.
    
It requires that your webserver runs php, and has access to GD.
There is a file named PHP_verify.php within the new (www)wxgraphic server directory. Access that from your browser and it should present a html page that will hopefully announce your successful web server setup, if not install php for your webserver, or satisfy its other needs.

When the weewx report cycle runs it will copy the www/wxgraphic directory to your webserver once, and once only. It will be named wxgraphic and will be in your weewx root directory (weewx/wxgraphic) by default.

   5. Configure the php script

Within that wxgraphic directory is a file named config.txt  That will require editing to change the configuration to suit your taste, set up.    
You have your choice of banner, banner_big, avatar or if nothing is selected, a default image. Only the *.png files are copied over. If you want the other formats (jpeg, gif) thats a manual job for you to perform.

The data to feed wxgraphic will be transferred at each weewx report cycle to (www) wxgraphic/DATA/weewx-wxgraphic.txt via the skins/WXgraphic/DATA/weewx-graphic.txt.tmpl
Currently no editing is required within the skin.conf file - that may change later.

The original script wxgraphic.php has been renamed as index.php. Currently, that's the only change to the original source. However, this installation does not install every file from the wxgraphic_6.3 source. They are available in the master file , or the github repo if you want them.

6. Usage:-

```http://your_weewx_servers_name/weewx/wxgraphic/```

Or as embedded html.

```<img src="http://your_weewx_servers_name/weewx/wxgraphic/" alt="wxgraphics weather image">```


# To Do - perhaps...

   Extract the title, and units and populate the config.txt from weewx.conf or supplied skin.conf values. Also the current conditions icons need to be incorporated.


