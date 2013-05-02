/*  
    IE + ActiveX + EOLAS - Javascript workaround

	Author: 
		Thomas Rauscher <tr-web@gardengnomesoftware.com>
		http://gardengnomesoftware.com
		
	To embed a panorama just call one of these functions with 
	additional pairs for additional paramameters f.e:
	
	p2q_EmbedQuicktime('pano.mov','640','480','scale','tofit','background','#eeeeee');
	
	Use this file at your own risk
*/

window.p2q_Version	= 2.2;

function p2q_EmbedQuicktime(sFile,sWidth,sHeight) {
	document.writeln('<object classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B"');
	document.writeln('  codebase="http://www.apple.com/qtactivex/qtplugin.cab"');
	document.writeln('  width="' + sWidth + '" height="' + sHeight + '" >');
	document.writeln('  <param name="src" value="' + sFile + '">');
	for(i=3;i<arguments.length;i+=2) {
		document.writeln('  <param name="' + arguments[i] + '" value="' + arguments[i+1] + '">');
	}
	document.writeln('<embed width="' + sWidth + '" height="' + sHeight + '"');
	document.writeln('	pluginspage="http://www.apple.com/quicktime/download/"');
	document.writeln('	type="video/quicktime"');
	document.writeln('	src="' + sFile + '"');
	for(i=3;i<arguments.length;i+=2) {
		document.writeln('  ' + arguments[i] + '="' + arguments[i+1] + '"');
	}
	document.writeln('	/>');
	document.writeln('</object>');
}

function p2q_EmbedSPiV(sFile,sWidth,sHeight) {
	document.writeln('<object id="SPi-V_object"	classid="clsid:166B1BCA-3F9C-11CF-8075-444553540000"');
	document.writeln('  codebase="http://download.macromedia.com/pub/shockwave/cabs/director/sw.cab#version=8,5,1,0"');
	document.writeln('  width="' + sWidth + '" height="' + sHeight + '" >');
	document.writeln('	<param name="src" value="SPi-V.dcr">');
	document.writeln('	<param name="swStretchStyle" value="stage">');
	document.writeln('	<param name="swRemote"       value="swContextMenu=' + "'" + 'FALSE' + "'" + '">');
	document.writeln('	<param name="progress"       value="true">'); 
	document.writeln('	<param name="logo"           value="false">'); 

	document.writeln('  <param name="swURL" value="' + sFile + '">');
	for(i=3;i<arguments.length;i+=2) {
		document.writeln('  <param name="' + arguments[i] + '" value="' + arguments[i+1] + '">');
	}
	document.writeln('<embed name="SPi-V_object" width="' + sWidth + '" height="' + sHeight + '"');
	document.writeln('	pluginspage="http://www.macromedia.com/shockwave/download/"');
	document.writeln('	type="application/x-director" ');
	document.writeln('	swURL="' + sFile + '" ');
	document.writeln('	src="SPi-V.dcr" ');
	document.writeln('	swStretchStyle="stage" ');
	document.writeln('	swRemote="swContextMenu=' + "'" + 'FALSE' + "'" + '" ');
	document.writeln('	progress="true" ');
	document.writeln('	logo="false" ');
	for(i=3;i<arguments.length;i+=2) {
		document.writeln('  ' + arguments[i] + '="' + arguments[i+1] + '"');
	}
	document.writeln('	/>');
	document.writeln('</object>');
}

function p2q_EmbedDevalVR(sFile,sWidth,sHeight) {
	document.writeln('<object classid="clsid:5D2CF9D0-113A-476B-986F-288B54571614"');
	document.writeln('  codebase="http://www.devalvr.com/instalacion/plugin/devalocx.cab#version=0,2,9,0"');
	document.writeln('  width="' + sWidth + '" height="' + sHeight + '" >');
	document.writeln('  <param name="src" value="' + sFile + '">');
	for(i=3;i<arguments.length;i+=2) {
		document.writeln('  <param name="' + arguments[i] + '" value="' + arguments[i+1] + '">');
	}
	document.writeln('<embed width="' + sWidth + '" height="' + sHeight + '"');
	document.writeln('	pluginspage="http://www.devalvr.com/instalacion/plugin/install.html"');
	document.writeln('	type="application/x-devalvrx"');
	document.writeln('	src="' + sFile + '"');
	for(i=3;i<arguments.length;i+=2) {
		document.writeln('  ' + arguments[i] + '="' + arguments[i+1] + '"');
	}
	document.writeln('	/>');
	document.writeln('</object>');
}

function p2q_EmbedFlash(sFile,sWidth,sHeight) {
	document.writeln('<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"');
	document.writeln('  codebase="http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=8,0,0,0"');
	document.writeln('  width="' + sWidth + '" height="' + sHeight + '" >');
	document.writeln('  <param name="movie" value="' + sFile + '">');
	for(i=3;i<arguments.length;i+=2) {
		document.writeln('  <param name="' + arguments[i] + '" value="' + arguments[i+1] + '">');
	}
	document.writeln('<embed width="' + sWidth + '" height="' + sHeight + '"');
	document.writeln('	pluginspage="http://www.macromedia.com/go/getflashplayer"');
	document.writeln('	type="application/x-shockwave-flash"');
	document.writeln('	src="' + sFile + '"');
	for(i=3;i<arguments.length;i+=2) {
		document.writeln('  ' + arguments[i] + '="' + arguments[i+1] + '"');
	}
	document.writeln('	/>');
	document.writeln('</object>');
}

function p2q_EmbedFlashId(id,sFile,sWidth,sHeight) {
	document.writeln('<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"');
	document.writeln('  codebase="http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=8,0,0,0"');
	document.writeln('  id="' + id + '"');
	document.writeln('  width="' + sWidth + '" height="' + sHeight + '" >');
	document.writeln('  <param name="movie" value="' + sFile + '">');
	for(i=4;i<arguments.length;i+=2) {
		document.writeln('  <param name="' + arguments[i] + '" value="' + arguments[i+1] + '">');
	}
	document.writeln('<embed width="' + sWidth + '" height="' + sHeight + '"');
	document.writeln('	pluginspage="http://www.macromedia.com/go/getflashplayer"');
	document.writeln('	type="application/x-shockwave-flash"');
	document.writeln('	name="' + id + '"');
	document.writeln('	src="' + sFile + '"');
	for(i=4;i<arguments.length;i+=2) {
		document.writeln('  ' + arguments[i] + '="' + arguments[i+1] + '"');
	}
	document.writeln('	/>');
	document.writeln('</object>');
}


function p2q_EmbedPtviewer(sFile,sWidth,sHeight) {
	document.writeln('<applet code="ptviewer.class" archive="ptviewer.jar"'); 
	document.writeln('  width="' + sWidth + '" height="' + sHeight + '" >');
	document.writeln('	<param name="file" value="' + sFile + '">');
	for(i=3;i<arguments.length;i+=2) {
		document.writeln('  <param name="' + arguments[i] + '" value="' + arguments[i+1] + '">');
	}
	document.writeln('</applet>');
}

function htmlEncode(s) {
	var str = new String(s);
	str = str.replace(/&/g, "&amp;");
	str = str.replace(/</g, "&lt;");
	str = str.replace(/>/g, "&gt;");
	str = str.replace(/"/g, "&quot;");
	return str;
}

// Flash Player Version Detection - Rev 1.5
// Detect Client Browser type
// Copyright(c) 2005-2006 Adobe Macromedia Software, LLC. All rights reserved.
var isIE  = (navigator.appVersion.indexOf("MSIE") != -1) ? true : false;
var isWin = (navigator.appVersion.toLowerCase().indexOf("win") != -1) ? true : false;
var isOpera = (navigator.userAgent.indexOf("Opera") != -1) ? true : false;

function ControlVersion()
{
	var version;
	var axo;
	var e;

	// NOTE : new ActiveXObject(strFoo) throws an exception if strFoo isn't in the registry

	try {
		// version will be set for 7.X or greater players
		axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash.7");
		version = axo.GetVariable("$version");
	} catch (e) {
	}

	if (!version)
	{
		try {
			// version will be set for 6.X players only
			axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash.6");
			
			// installed player is some revision of 6.0
			// GetVariable("$version") crashes for versions 6.0.22 through 6.0.29,
			// so we have to be careful. 
			
			// default to the first public version
			version = "WIN 6,0,21,0";

			// throws if AllowScripAccess does not exist (introduced in 6.0r47)		
			axo.AllowScriptAccess = "always";

			// safe to call for 6.0r47 or greater
			version = axo.GetVariable("$version");

		} catch (e) {
		}
	}

	if (!version)
	{
		try {
			// version will be set for 4.X or 5.X player
			axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash.3");
			version = axo.GetVariable("$version");
		} catch (e) {
		}
	}

	if (!version)
	{
		try {
			// version will be set for 3.X player
			axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash.3");
			version = "WIN 3,0,18,0";
		} catch (e) {
		}
	}

	if (!version)
	{
		try {
			// version will be set for 2.X player
			axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash");
			version = "WIN 2,0,0,11";
		} catch (e) {
			version = -1;
		}
	}
	
	return version;
}

// JavaScript helper required to detect Flash Player PlugIn version information
function GetSwfVer(){
	// NS/Opera version >= 3 check for Flash plugin in plugin array
	var flashVer = -1;
	
	if (navigator.plugins != null && navigator.plugins.length > 0) {
		if (navigator.plugins["Shockwave Flash 2.0"] || navigator.plugins["Shockwave Flash"]) {
			var swVer2 = navigator.plugins["Shockwave Flash 2.0"] ? " 2.0" : "";
			var flashDescription = navigator.plugins["Shockwave Flash" + swVer2].description;			
			var descArray = flashDescription.split(" ");
			var tempArrayMajor = descArray[2].split(".");
			var versionMajor = tempArrayMajor[0];
			var versionMinor = tempArrayMajor[1];
			if ( descArray[3] != "" ) {
				tempArrayMinor = descArray[3].split("r");
			} else {
				tempArrayMinor = descArray[4].split("r");
			}
			var versionRevision = tempArrayMinor[1] > 0 ? tempArrayMinor[1] : 0;
			var flashVer = versionMajor + "." + versionMinor + "." + versionRevision;
		}
	}
	// MSN/WebTV 2.6 supports Flash 4
	else if (navigator.userAgent.toLowerCase().indexOf("webtv/2.6") != -1) flashVer = 4;
	// WebTV 2.5 supports Flash 3
	else if (navigator.userAgent.toLowerCase().indexOf("webtv/2.5") != -1) flashVer = 3;
	// older WebTV supports Flash 2
	else if (navigator.userAgent.toLowerCase().indexOf("webtv") != -1) flashVer = 2;
	else if ( isIE && isWin && !isOpera ) {
		flashVer = ControlVersion();
	}	
	return flashVer;
}

// When called with reqMajorVer, reqMinorVer, reqRevision returns true if that version or greater is available
function DetectFlashVer(reqMajorVer, reqMinorVer, reqRevision)
{
	versionStr = GetSwfVer();
	if (versionStr == -1 ) {
		return false;
	} else if (versionStr != 0) {
		if(isIE && isWin && !isOpera) {
			// Given "WIN 2,0,0,11"
			tempArray         = versionStr.split(" "); 	// ["WIN", "2,0,0,11"]
			tempString        = tempArray[1];			// "2,0,0,11"
			versionArray      = tempString.split(",");	// ['2', '0', '0', '11']
		} else {
			versionArray      = versionStr.split(".");
		}
		var versionMajor      = versionArray[0];
		var versionMinor      = versionArray[1];
		var versionRevision   = versionArray[2];

        	// is the major.revision >= requested major.revision AND the minor version >= requested minor
		if (versionMajor > parseFloat(reqMajorVer)) {
			return true;
		} else if (versionMajor == parseFloat(reqMajorVer)) {
			if (versionMinor > parseFloat(reqMinorVer))
				return true;
			else if (versionMinor == parseFloat(reqMinorVer)) {
				if (versionRevision >= parseFloat(reqRevision))
					return true;
			}
		}
		return false;
	}
}


