<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="content-type" content="application/xhtml+xml; charset=iso-8859-1" />
    <meta http-equiv="Pragma" content="no-cache" />
    <meta http-equiv="Expires" content="-1" />
    <meta name="author" content="Larry Boyd" />
    <meta name="generator" content="Notetab" />

    <title>PHP Verification</title>

    <style type="text/css">
    body {color: black; background-color: rgb(255,255,255); font-family: arial, tahoma, verdana, helvetica, sans-serif; font-size: 10pt; padding: 10;}
    .container-solid {color: #000; background-color: #FF9; border: 1px solid #080; padding: 5px;}
    h1 {font-size: 150%; font-weight: bold; text-align: left; border-top: 1px solid rgb(216,210,195);}
    .red {color: #f00;}
    .green {color: #090;}
    </style>

  </head>

  <body>
  <h1 class="green" style="text-align:center">PHP Verification Test</h1>
  <p>
   This page provides a test of PHP support for your server. To use it upload this file to your server and call it with a URL:<br />
   http://your.domain.com/PHP_verify.php
  </p>
  <p>
  If your server supports PHP, you should see some information in the yellow boxes below. If the boxes are empty, your server most likely does not support PHP, but you should contact your hosting company to be sure as some may require different a file extension instead of ".php".
  </p>
  <h1 class="green">IS PHP SUPPPORTED ON THIS SERVER?</h1>
  <div class="container-solid">
    <?php
    echo "Yes, it is!<br />\n";
    echo "PHP Version: " . phpversion();
    ?>
  </div>
  <p>
  If the yellow box above is empty, your would appear your server does not support PHP.
  </p>

  <h1 class="green">IS PHP INSTALLED WITH GD SUPPORT?</h1>
  <div class="container-solid">
    <?php
    function yesNo($bool){ 
      if($bool){
        return "<span class=\"green\">Yes</span>";
      } // end if 
      else {
           return "<span class=\"red\">NO</span>"; 
      } 
    } // end function yesNo
    echo "GD support: "; 
    if(function_exists("gd_info")){ 
       echo "<span class=\"green\">Yes</span>"; 
       echo "<ul style=\"list-style-type: none\"><li>"; 
       $info = gd_info(); 
       $keys = array_keys($info); 
       for($i=0; $i<count($keys); $i++) { 
          if(is_bool($info[$keys[$i]])) {
            echo "</li>\n<li>" . $keys[$i] .": " . yesNo($info[$keys[$i]]);
          } //end if
          else {
               echo "</li>\n<li>" . $keys[$i] .": " . $info[$keys[$i]]; 
          } // end else
       } // end for
       echo "</li></ul>";
    } // end if
    else { 
         echo "<span class=\"red\">NO</span>"; 
    } //end else
    ?>
  </div>
  <p>
  If the yellow box above is empty, it would appear your server does not support GD. If GD is supported the box will contain data about the GD install including whether or not it support FreeType (TrueType) fonts.
  </p>

  <h1 class="green">DETAILED PHP INSTALL INFORMATION</h1>
  <?php
  phpinfo();
  ?>
  <p>
  If PHP is installed you should see a long list of information about the different modules it contains immediately above this line.
  </p>

  </body>
</html>
 