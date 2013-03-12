
/*
	* LayerSlider
	*
	* (c) 2011-2013 George Krupa, John Gera & Kreatura Media
	*
	* web:					http://kreaturamedia.com/
	* Facebook: 			http://facebook.com/kreaturamedia/
	* standalone version: 	http://kreaturamedia.com/codecanyon/plugins/layerslider/
	* WordPress version: 	http://wordpress.kreatura.hu/layersliderwp/
	* email: 				contact<AT>kreaturamedia<DOT>com
	*
	* Licenses:
	*
	* http://codecanyon.net/licenses/
*/



function lsShowNotice(lsobj,issue,ver){

	if( typeof lsobj == 'string' ){
		var el = jQuery('#'+lsobj);
	}else if( typeof lsobj == 'object' ){
		var el = lsobj;
	}

	var errorTitle, errorText;

	switch(issue){
		case 'jquery':
		errorTitle = 'multiple jQuery issue';
		errorText = 'It looks like that one of your other plugins or your theme itself loads an extra copy of the jQuery library which causes a Javascript conflict and LayerSlider WP can\'t load your slider. <strong>Please navigate on your WordPress admin area to edit this slider and enable the "Put JS includes to body" option in the Global Settings under the Troubleshooting section.</strong><br><br>If this doesn\'t solve your problem, please try to disable every other plugin one-by-one to find out which one causes this issue. If you have found the corresponding plugin, please contact with the plugin author to solve this case. If none of your plugins causes this problem, it must be your theme and you should contact with the author of the theme. Ask help from them to remove any duplicates of the jQuery library.<br><br>If there is no one to help you, please write a comment in the comments section of the item on CodeCanyon.';
		break;
		case 'oldjquery':
		errorTitle = 'old jQuery issue';
		errorText = 'It looks like you are using an old version ('+ver+') of the jQuery library. LayerSlider requires at least version 1.7.2 or newer. If you are using the WordPress version of LayerSlider, you can try out the "jQuery Updater" plugin from the WP plugin depository. If you don\'t know what to do, you can write us a private message from our CodeCanyon profile page. We need a temporary WP admin account (or a temporary FTP account in some cases) to solve this issue.';
		break;
		case 'transit':
		errorTitle = 'jQuery Transit issue';
		errorText = 'It looks like one of your other plugins also uses jQuery Transit and loads an extra copy of this library which can cause issues. Please navigate on your WordPress admin area to edit this slider and enable the "Put JS includes to body" option in your Global Settings under the Troubleshooting section.';
		break;
	}

	el.addClass('ls-error');
	el.append('<p class="ls-exclam">!</p>');
	el.append('<p class="ls-error-title">LayerSlider WP: '+errorTitle+'</p>');
	el.append('<p class="ls-error-text">'+errorText+'</p>');
}

(function($) {

	$.fn.layerSlider = function( options ){

		// IMPROVEMENT v4.1.0 Checking jQuery version
		
		var reqVer = '1.7.2';
		var curVer = $.fn.jquery;
		var el = $(this);

		var checkVersions = function(v1,v2){
			
		    var v1parts = v1.split('.');
		    var v2parts = v2.split('.');

		    for (var i = 0; i < v1parts.length; ++i) {

		        if (v2parts.length == i) {
					lsShowNotice( el, 'oldjquery', curVer );
					return false;
		        }

		        if (v1parts[i] == v2parts[i]) {
		            continue;
		        }
		        else if (v1parts[i] > v2parts[i]) {
					lsShowNotice( el, 'oldjquery', curVer );
					return false;
		        }
		        else {
					return true;
		        }
		    }

		    if (v1parts.length != v2parts.length) {
				return true;
		    }

			return true;
		};
	
		// Initializing if jQuery version is greater than 1.7.2

		if( checkVersions(reqVer,curVer) ){
			
			if( (typeof(options)).match('object|undefined') ){
				return this.each(function(i){
					new layerSlider(this, options);
				});
			}else{
				if( options == 'data' ){
					var lsData = $(this).data('LayerSlider').g;
					if( lsData ){
						return lsData;
					}
				}else{
					return this.each(function(i){

						// Control functions: prev, next, start, stop & change

						var lsData = $(this).data('LayerSlider');
						if( lsData ){
							if( !lsData.g.isAnimating && !lsData.g.isLoading ){
								if( typeof(options) == 'number' ){
									if( options > 0 && options < lsData.g.layersNum + 1 && options != lsData.g.curLayerIndex ){
										lsData.change(options);
									}						
								}else{
									switch(options){
										case 'prev':
											lsData.o.cbPrev(lsData.g);
											lsData.prev('clicked');
											break;
										case 'next':
											lsData.o.cbNext(lsData.g);
											lsData.next('clicked');
											break;
										case 'start':
											if( !lsData.g.autoSlideshow ){
												lsData.o.cbStart(lsData.g);
												lsData.g.originalAutoSlideshow = true;
												lsData.start();
											}							
											break;
									}
								}
							}
							if( options == 'debug' ){
								lsData.d.show();							
							}
							if( ( lsData.g.autoSlideshow || ( !lsData.g.autoSlideshow && lsData.g.originalAutoSlideshow ) ) && options == 'stop' ){
								lsData.o.cbStop(lsData.g);
								lsData.g.originalAutoSlideshow = false;
								lsData.g.curLayer.find('iframe[src*="www.youtu"], iframe[src*="player.vimeo"]').each(function(){

									// Clearing videoTimeouts

									clearTimeout( $(this).data( 'videoTimer') );
								});

								lsData.stop();
							}
						}
					});				
				}
			}
		}
	};

	// LayerSlider methods

	var layerSlider = function(el, options) {

		var ls = this;
		ls.$el = $(el).addClass('ls-container');
		ls.$el.data('LayerSlider', ls);

		ls.load = function(){

			// Setting options (user settings) and global (not modificable) parameters
			
			ls.o = $.extend({},layerSlider.options, options);
			ls.g = $.extend({},layerSlider.global);

			// If layerslider.transitions.js is loaded...

			if( typeof(layerSliderTransitions) != 'undefined' ){
				ls.t = $.extend({},layerSliderTransitions);
			}

			// If custom transitions are loaded...

			if( typeof(layerSliderCustomTransitions) != 'undefined' ){
				ls.ct = $.extend({},layerSliderCustomTransitions);
			}

			// NEW IMPROVEMENT v3.6 forbid to call the init code more than once on the same element

			if( !ls.g.initialized ){

				ls.g.initialized = true;

				// Added debug mode v3.5

				ls.debug();			

				if( $('html').find('meta[content*="WordPress"]').length ){
					ls.g.wpVersion = $('html').find('meta[content*="WordPress"]').attr('content').split('WordPress')[1];
				}

				if( $('html').find('script[src*="layerslider"]').length ){
					if( $('html').find('script[src*="layerslider"]').attr('src').indexOf('?') != -1 ){
						ls.g.lswpVersion = $('html').find('script[src*="layerslider"]').attr('src').split('?')[1].split('=')[1];					
					}
				}

				ls.d.aT('LayerSlider controls');
				ls.d.aU('<a href="#">prev</a> | <a href="#">next</a> | <a href="#">start</a> | <a href="#">stop</a> | <a href="#">force stop</a>');
				ls.d.history.find('a').each(function(){
					$(this).click(function(e){
						e.preventDefault();
						if( $(this).text() == 'force stop' ){
							$(el).find('*').stop(true,false);
							$(el).layerSlider('stop');
						}else{
							$(el).layerSlider($(this).text());
						}
					});					
				});

				ls.d.aT('LayerSlider version information');
				ls.d.aU('JS version: <strong>' + ls.g.version + '</strong>');			
				if(ls.g.lswpVersion){
					ls.d.aL('WP version: <strong>' + ls.g.lswpVersion + '</strong>');
				}
				if(ls.g.wpVersion){
					ls.d.aL('WordPress version: <strong>' + ls.g.wpVersion + '</strong>');
				}

				ls.d.aL('jQuery version: <strong>' + $().jquery + '</strong>');

				if( $(el).attr('id') ){

					ls.d.aT('LayerSlider container');
					ls.d.aU('#'+$(el).attr('id'));
				}

				ls.d.aT('Init code');
				ls.d.aeU();

				for( var prop in ls.o ){
					ls.d.aL(prop+': <strong>' + ls.o[prop] + '</strong>');
				}

				// NEW LOAD METHOD v3.5
				// FIXED v4.0 If the selected skin is already loaded, calling the ls.init() function immediately

				if( !ls.o.skin || ls.o.skin == '' || !ls.o.skinsPath || ls.o.skinsPath == '' ){

					ls.d.aT('Loading without skin. Possibilities: mistyped skin and / or skinsPath.');

					ls.init();
				}else{

					ls.d.aT('Trying to load with skin: '+ls.o.skin, true);

					// Applying skin

					$(el).addClass('ls-'+ls.o.skin);

					var skinStyle = ls.o.skinsPath+ls.o.skin+'/skin.css';

					cssContainer = $('head');

					if( !$('head').length ){
						cssContainer = $('body');
					}

					if( $('link[href="'+skinStyle+'"]').length ){

						ls.d.aU('Skin "'+ls.o.skin+'" is already loaded.');

						curSkin = $('link[href="'+skinStyle+'"]');

						if( !ls.g.loaded ){

							ls.g.loaded = true;
							ls.init();
						}
						
					}else{
						if (document.createStyleSheet){
							document.createStyleSheet(skinStyle);
							var curSkin = $('link[href="'+skinStyle+'"]');
						}else{
							var curSkin = $('<link rel="stylesheet" href="'+skinStyle+'" type="text/css" />').appendTo( cssContainer );					
						}						
					}

					// curSkin.load(); function for most of the browsers.

					curSkin.load(function(){

						if( !ls.g.loaded ){

							ls.d.aU('curSkin.load(); fired');

							ls.g.loaded = true;
							ls.init();
						}
					});

					// $(window).load(); function for older webkit ( < v536 ).

					$(window).load(function(){

						if( !ls.g.loaded ){

							ls.d.aU('$(window).load(); fired');

							ls.g.loaded = true;
							ls.init();
						}
					});

					// Fallback: if $(window).load(); not fired in 2 secs after $(document).ready(),
					// curSkin.load(); not fired at all or the name of the skin and / or the skinsPath
					// mistyped, we must call the init function manually.

					setTimeout( function(){

						if( !ls.g.loaded ){

							ls.d.aT('Fallback mode: Neither curSkin.load(); or $(window).load(); were fired');

							ls.g.loaded = true;
							ls.init();
						}					
					}, 2000);
				}
			}
		};
		
		ls.init = function(){
			
			ls.d.aT('FUNCTION ls.init();');
			ls.d.aeU();

			// IMPROVEMENT v4.0.1 Trying to add special ID to <body> or <html> (required to overwrite WordPresss global styles)
			
			if( !$('html').attr('id') ){
				$('html').attr('id','ls-global');				
			}else if( !$('body').attr('id') ){
				$('body').attr('id','ls-global');
			}

			// NEW FEATURE v1.7 making the slider responsive

			ls.g.sliderWidth = function(){
				if( ls.g.normalWidth && ls.g.goingNormal ){
					return ls.g.normalWidth;
				}else{
					return $(el).width();
				}
			}
			
			ls.g.sliderHeight = function(){
				if( ls.g.normalHeight && ls.g.goingNormal ){
					return ls.g.normalHeight;
				}else{
					return $(el).height();
				}
			}

			// REPLACED FEATURE v2.0 If there is only ONE layer, instead of duplicating it, turning off slideshow and loops, hiding all controls, etc.
			
			if( $(el).find('.ls-layer').length == 1 ){
				ls.o.autoStart = false;
				ls.o.navPrevNext = false;
				ls.o.navStartStop = false;
				ls.o.navButtons	 = false;
				ls.o.loops = 0;
				ls.o.forceLoopNum = false;
				ls.o.autoPauseSlideshow	= true;
				ls.o.firstLayer = 1;
				ls.o.thumbnailNavigation = 'disabled';
			}

			ls.d.aL('Number of layers found: <strong>' + $(el).find('.ls-layer').length + '</strong>');

			// NEW FEATURE v3.0 added "normal" responsive mode with image and font resizing
			// NEW FEATURE v3.5 responsiveUnder

			if( ls.o.width ){
				ls.g.sliderOriginalWidthRU = ls.g.sliderOriginalWidth = '' + ls.o.width;
			}else{
				ls.g.sliderOriginalWidthRU = ls.g.sliderOriginalWidth = $(el)[0].style.width;
			}

			ls.d.aL('sliderOriginalWidth: <strong>' + ls.g.sliderOriginalWidth + '</strong>');
			
			if( ls.o.height ){
				ls.g.sliderOriginalHeight = '' + ls.o.height;
			}else{
				ls.g.sliderOriginalHeight = $(el)[0].style.height;
			}
			
			ls.d.aL('sliderOriginalHeight: <strong>' + ls.g.sliderOriginalHeight + '</strong>');

			if( ls.g.sliderOriginalWidth.indexOf('%') == -1 && ls.g.sliderOriginalWidth.indexOf('px') == -1 ){
				ls.g.sliderOriginalWidth += 'px';
			}

			if( ls.g.sliderOriginalHeight.indexOf('%') == -1 && ls.g.sliderOriginalHeight.indexOf('px') == -1 ){
				ls.g.sliderOriginalHeight += 'px';
			}

			if( ls.o.responsive && ls.g.sliderOriginalWidth.indexOf('px') != -1 && ls.g.sliderOriginalHeight.indexOf('px') != -1 ){
				ls.g.responsiveMode = true;
			}else{
				ls.g.responsiveMode = false;
			}
			
			// IMPROVEMENT v3.0 preventing WordPress to wrap your sublayers in <code> or <p> elements	
			
			$(el).find('*[class*="ls-s"], *[class*="ls-bg"]').each(function(){
				if( !$(this).parent().hasClass('ls-layer') ){
					$(this).insertBefore( $(this).parent() );
				}
			});
			
			$(el).find('.ls-layer').each(function(){
				$(this).children(':not([class*="ls-"])').each(function(){
					$(this).remove();					
				});
			});

			// Storing unique settings of layers and sublayers into object.data

			ls.d.aT('LayerSlider Content');

			$(el).find('.ls-layer, *[class*="ls-s"]').each(function(){

				if( $(this).hasClass('ls-layer') ){
					ls.d.aU('<strong>LAYER ' + ( $(this).index() + 1 ) + '</strong>');
					ls.d.aUU();
					ls.d.aL('<strong>LAYER ' + ( $(this).index() + 1 ) + ' properties:</strong><br><br>');
				}else{
					ls.d.aU('&nbsp;&nbsp;&nbsp;&nbsp;Sublayer ' + ( $(this).index() + 1 ));
					ls.d.aF($(this));
					ls.d.aUU();
					ls.d.aL('<strong>SUBLAYER ' + ( $(this).index() + 1 ) + ' properties:</strong><br><br>');
					ls.d.aL('type: <strong>' + $(this).prev().prop('tagName')+'</strong>');
					ls.d.aL('class: <strong>'+$(this).attr('class')+'</strong>');
				}

				if( $(this).attr('rel') || $(this).attr('style') ){
					if( $(this).attr('rel') ){
						var params = $(this).attr('rel').toLowerCase().split(';');
					}else{
						var params = $(this).attr('style').toLowerCase().split(';');						
					}
					for(x=0;x<params.length;x++){
						param = params[x].split(':');

						if( param[0].indexOf('easing') != -1 ){
							param[1] = ls.ieEasing( param[1] );
						}

						var p2 = '';
						if( param[2] ){
							p2 = ':'+$.trim(param[2]);
						}

						if( param[0] != ' ' && param[0] != '' ){
							$(this).data( $.trim(param[0]), $.trim(param[1]) + p2 );

							ls.d.aL( $.trim(param[0]) + ': <strong>' + $.trim(param[1]) + p2 + '</strong>' );							
						}
					}
				}

				// NEW FEATURE v1.7 and v3.0 making the slider responsive - we have to use style.left instead of jQuery's .css('left') function!

				var sl = $(this);
				
				sl.data( 'originalLeft', sl[0].style.left );
				sl.data( 'originalTop', sl[0].style.top );
				
				if( $(this).is('a') && $(this).children().length > 0 ){
					sl = $(this).children();
				}

				var _w = sl.width();
				var _h = sl.height();

				if( sl[0].style.width && sl[0].style.width.indexOf('%') != -1 ){
					_w = sl[0].style.width;
				}
				if( sl[0].style.height && sl[0].style.height.indexOf('%') != -1 ){
					_h = sl[0].style.height;
				}

				sl.data( 'originalWidth', _w );
				sl.data( 'originalHeight', _h );

				sl.data( 'originalPaddingLeft', sl.css('padding-left') );
				sl.data( 'originalPaddingRight', sl.css('padding-right') );
				sl.data( 'originalPaddingTop', sl.css('padding-top') );
				sl.data( 'originalPaddingBottom', sl.css('padding-bottom') );

				// iOS fade bug when GPU acceleration is enabled #1

				if( ls.g.isMobile() == true && lsBrowser().webkit ){
					var _o = typeof parseFloat( sl.css('opacity') ) == 'number'  ? Math.round( parseFloat( sl.css('opacity') ) * 100 ) / 100  : 1;
					$(this).data( 'originalOpacity', _o );
				}

				if( sl.css('border-left-width').indexOf('px') == -1 ){
					sl.data( 'originalBorderLeft', sl[0].style.borderLeftWidth );
				}else{
					sl.data( 'originalBorderLeft', sl.css('border-left-width') );					
				}
				if( sl.css('border-right-width').indexOf('px') == -1 ){
					sl.data( 'originalBorderRight', sl[0].style.borderRightWidth );
				}else{
					sl.data( 'originalBorderRight', sl.css('border-right-width') );
				}
				if( sl.css('border-top-width').indexOf('px') == -1 ){
					sl.data( 'originalBorderTop', sl[0].style.borderTopWidth );				
				}else{
					sl.data( 'originalBorderTop', sl.css('border-top-width') );
				}
				if( sl.css('border-bottom-width').indexOf('px') == -1 ){
					sl.data( 'originalBorderBottom', sl[0].style.borderBottomWidth );				
				}else{
					sl.data( 'originalBorderBottom', sl.css('border-bottom-width') );
				}

				sl.data( 'originalFontSize', sl.css('font-size') );
				sl.data( 'originalLineHeight', sl.css('line-height') );				
			});

			// CHANGED FEATURE v3.5 url- / deep linking layers

			if( document.location.hash ){
				for( var dl = 0; dl < $(el).find('.ls-layer').length; dl++ ){
					if( $(el).find('.ls-layer').eq(dl).data('deeplink') == document.location.hash.split('#')[1] ){
						ls.o.firstLayer = dl+1;
					}
				}
			}

			// NEW FEATURE v2.0 linkTo

			$(el).find('*[class*="ls-linkto-"]').each(function(){
				var lClasses = $(this).attr('class').split(' ');
				for( var ll=0; ll<lClasses.length; ll++ ){
					if( lClasses[ll].indexOf('ls-linkto-') != -1 ){
						var linkTo = parseInt( lClasses[ll].split('ls-linkto-')[1] );
						$(this).css({
							cursor: 'pointer'
						}).click(function(e){
							e.preventDefault();
							$(el).layerSlider( linkTo );
						});
					}
				}
			});

			// Setting variables

			ls.g.layersNum = $(el).find('.ls-layer').length;

			// NEW FEATURE v3.5 randomSlideshow
			
			if( ls.o.randomSlideshow && ls.g.layersNum > 2 ){
				ls.o.firstLayer == 'random';
				ls.o.twoWaySlideshow = false;
			}else{
				ls.o.randomSlideshow = false;
			}

			// NEW FEATURE v3.0 random firstLayer

			if( ls.o.firstLayer == 'random' ){
				ls.o.firstLayer = Math.floor(Math.random() * ls.g.layersNum+1);
			}

			ls.o.firstLayer = ls.o.firstLayer < ls.g.layersNum + 1 ? ls.o.firstLayer : 1;
			ls.o.firstLayer = ls.o.firstLayer < 1 ? 1 : ls.o.firstLayer;
			
			// NEW FEATURE v2.0 loops
			
			ls.g.nextLoop = 1;
			
			if( ls.o.animateFirstLayer ){
				ls.g.nextLoop = 0;
			}
			
			// NEW FEATURE v2.0 videoPreview

			// Youtube videos
			
			$(el).find('iframe[src*="www.youtu"]').each(function(){

				// BUGFIX v4.1.0 Firefox embedded video fix
				
				$(this).parent().addClass('ls-video-layer');

				if( $(this).parent('[class*="ls-s"]') ){

					var iframe = $(this);

					// Getting thumbnail
					
					$.getJSON('http://gdata.youtube.com/feeds/api/videos/' + $(this).attr('src').split('embed/')[1].split('?')[0] + '?v=2&alt=json&callback=?', function(data) {

						iframe.data( 'videoDuration', parseInt(data['entry']['media$group']['yt$duration']['seconds']) * 1000 );
					});
					
					var vpContainer = $('<div>').addClass('ls-vpcontainer').appendTo( $(this).parent() );

					$('<img>').appendTo( vpContainer ).addClass('ls-videopreview').attr('src', 'http://img.youtube.com/vi/' + $(this).attr('src').split('embed/')[1].split('?')[0] + '/' + ls.o.youtubePreview );
					$('<div>').appendTo( vpContainer ).addClass('ls-playvideo');

					$(this).parent().css({
						width : $(this).width(),
						height : $(this).height()
					}).click(function(){

						ls.g.isAnimating = true;

						if( ls.g.paused ){
							if( ls.o.autoPauseSlideshow != false ){
								ls.g.paused = false;								
							}
							ls.g.originalAutoSlideshow = true;
						}else{
							ls.g.originalAutoSlideshow = ls.g.autoSlideshow;
						}

						if( ls.o.autoPauseSlideshow != false ){
							ls.stop();
						}

						ls.g.pausedByVideo = true;

						$(this).find('iframe').attr('src', $(this).find('iframe').data('videoSrc') );
						$(this).find('.ls-vpcontainer').delay(ls.g.v.d).fadeOut(ls.g.v.fo, function(){							
							if( ls.o.autoPauseSlideshow == 'auto' && ls.g.originalAutoSlideshow == true ){
								var videoTimer = setTimeout(function() {
										ls.start();
								}, iframe.data( 'videoDuration') - ls.g.v.d );
								iframe.data( 'videoTimer', videoTimer );
							}
							ls.g.isAnimating = false;
						});
					});

					var sep = '&';
					
					if( $(this).attr('src').indexOf('?') == -1 ){
						sep = '?';
					}

					$(this).data( 'videoSrc', $(this).attr('src') + sep + 'autoplay=1' );
					$(this).data( 'originalWidth', $(this).attr('width') );
					$(this).data( 'originalHeight', $(this).attr('height') );
					$(this).attr('src','');
				}
			});

			// Vimeo videos

			$(el).find('iframe[src*="player.vimeo"]').each(function(){

				// BUGFIX v4.1.0 Firefox embedded video fix
				
				$(this).parent().addClass('ls-video-layer');

				if( $(this).parent('[class*="ls-s"]') ){

					var iframe = $(this);

					// Getting thumbnail

					var vpContainer = $('<div>').addClass('ls-vpcontainer').appendTo( $(this).parent() );

					$.getJSON('http://vimeo.com/api/v2/video/'+ ( $(this).attr('src').split('video/')[1].split('?')[0] ) +'.json?callback=?', function(data){

						$('<img>').appendTo( vpContainer ).addClass('ls-videopreview').attr('src', data[0]['thumbnail_large'] );						
						iframe.data( 'videoDuration', parseInt( data[0]['duration'] ) * 1000 );
						$('<div>').appendTo( vpContainer ).addClass('ls-playvideo');						
					});


					$(this).parent().css({
						width : $(this).width(),
						height : $(this).height()
					}).click(function(){

						ls.g.isAnimating = true;

						if( ls.g.paused ){
							if( ls.o.autoPauseSlideshow != false ){
								ls.g.paused = false;								
							}
							ls.g.originalAutoSlideshow = true;
						}else{
							ls.g.originalAutoSlideshow = ls.g.autoSlideshow;
						}

						if( ls.o.autoPauseSlideshow != false ){
							ls.stop();
						}

						ls.g.pausedByVideo = true;

						$(this).find('iframe').attr('src', $(this).find('iframe').data('videoSrc') );
						$(this).find('.ls-vpcontainer').delay(ls.g.v.d).fadeOut(ls.g.v.fo, function(){
							if( ls.o.autoPauseSlideshow == 'auto' && ls.g.originalAutoSlideshow == true ){
								var videoTimer = setTimeout(function() {
										ls.start();
								}, iframe.data( 'videoDuration') - ls.g.v.d );
								iframe.data( 'videoTimer', videoTimer );
							}
							ls.g.isAnimating = false;
						});
					});

					var sep = '&';
					
					if( $(this).attr('src').indexOf('?') == -1 ){
						sep = '?';
					}

					$(this).data( 'videoSrc', $(this).attr('src') + sep + 'autoplay=1' );
					$(this).data( 'originalWidth', $(this).attr('width') );
					$(this).data( 'originalHeight', $(this).attr('height') );
					$(this).attr('src','');
				}
			});

			// NEW FEATURE v1.7 animating first layer
			
			if( ls.o.animateFirstLayer ){
				ls.o.firstLayer = ls.o.firstLayer - 1 == 0 ? ls.g.layersNum : ls.o.firstLayer-1;
			}

			ls.g.curLayerIndex = ls.o.firstLayer;
			ls.g.curLayer = $(el).find('.ls-layer:eq('+(ls.g.curLayerIndex-1)+')');			

			// Moving all layers to .ls-inner container

			$(el).find('.ls-layer').wrapAll('<div class="ls-inner"></div>');

			// Adding a transparent container under .ls-inner

			$('<div>').addClass('ls-webkit-hack').prependTo( $(el) );

			// NEW FEATURE v4.0 Adding loading indicator into the element

			ls.g.li = $('<div>').css({
				zIndex: -1,
				display: 'none'
			}).addClass('ls-loading-container').appendTo( $(el) );

			$('<div>').addClass('ls-loading-indicator').appendTo( ls.g.li );

			// Adding styles

			if( $(el).css('position') == 'static' ){
				$(el).css('position','relative');
			}

			$(el).find('.ls-inner').css({
				backgroundColor : ls.o.globalBGColor
			});
			
			if( ls.o.globalBGImage ){
				$(el).find('.ls-inner').css({
					backgroundImage : 'url('+ls.o.globalBGImage+')'
				});
			}

			// NEW FEATURE Creating fullscreen button (will be working only in Chrome, Safari and Firefox with sliders in responsive mode)

			if( ls.g.responsiveMode && ls.g.isMobile() != true && ls.o.allowFullScreenMode && ( lsPrefixes( document, 'FullScreen') != undefined || lsPrefixes( document, 'IsFullScreen') != undefined ) ){

				var fs = $('<a>').css(  'display', 'none' ).addClass('ls-fullscreen').click(function(){ ls.goFullScreen(); }).appendTo( $(el).find('.ls-inner') );
				$(el).hover(
					function(){
						if( ls.g.ie78 ){
							fs.css({
								display: 'block'
							});
						}else{
							fs.stop(true,true).fadeIn(300);
						}
					},
					function(){
						if( ls.g.ie78 ){
							fs.css({
								display: 'none'
							});
						}else{
							fs.stop(true,true).fadeOut(300);
						}
					}
				);
			}

			// Creating navigation

			if( ls.o.navPrevNext ){

				$('<a class="ls-nav-prev" href="#" />').click(function(e){
					e.preventDefault();
					$(el).layerSlider('prev');
				}).appendTo($(el));

				$('<a class="ls-nav-next" href="#" />').click(function(e){
					e.preventDefault();
					$(el).layerSlider('next');
				}).appendTo($(el));
				
				if( ls.o.hoverPrevNext ){
					$(el).find('.ls-nav-prev, .ls-nav-next').css({
						display: 'none'
					});
					
					$(el).hover(
						function(){
 							if( !ls.g.forceHideControls ){
								if( ls.g.ie78 ){
									$(el).find('.ls-nav-prev, .ls-nav-next').css('display','block');
								}else{
									$(el).find('.ls-nav-prev, .ls-nav-next').stop(true,true).fadeIn(300);
								}
							}
						},
						function(){
							if( ls.g.ie78 ){
								$(el).find('.ls-nav-prev, .ls-nav-next').css('display','none');
							}else{
								$(el).find('.ls-nav-prev, .ls-nav-next').stop(true,true).fadeOut(300);
							}
						}						
					);
				}
			}

			// Creating bottom navigation

			if( ls.o.navStartStop || ls.o.navButtons ){
				
				var bottomNav = $('<div class="ls-bottom-nav-wrapper" />').appendTo( $(el) );
				
				ls.g.bottomWrapper = bottomNav;
				
				if( ls.o.thumbnailNavigation == 'always' ){
					bottomNav.addClass('ls-above-thumbnails');
				}

				if( ls.o.navButtons && ls.o.thumbnailNavigation != 'always' ){

					$('<span class="ls-bottom-slidebuttons" />').appendTo( $(el).find('.ls-bottom-nav-wrapper') );

					// NEW FEATURE v3.5 thumbnailNavigation ('hover')

					if( ls.o.thumbnailNavigation == 'hover' ){

						var thumbs = $('<div class="ls-thumbnail-hover"><div class="ls-thumbnail-hover-inner"><div class="ls-thumbnail-hover-bg"></div><div class="ls-thumbnail-hover-img"><img></div><span></span></div></div>').appendTo( $(el).find('.ls-bottom-slidebuttons') );
					}

					for(x=1;x<ls.g.layersNum+1;x++){

						var btn = $('<a href="#" />').appendTo( $(el).find('.ls-bottom-slidebuttons') ).click(function(e){
							e.preventDefault();
							$(el).layerSlider( ($(this).index() + 1) );
						});
						
						// NEW FEATURE v3.5 thumbnailNavigation ('hover')

						if( ls.o.thumbnailNavigation == 'hover' ){
							
							$(el).find('.ls-thumbnail-hover, .ls-thumbnail-hover-img').css({
								width : ls.o.tnWidth,
								height : ls.o.tnHeight								
							});
							
							var th = $(el).find('.ls-thumbnail-hover');

							var ti = th.find('img').css({
								height : ls.o.tnHeight
							});

							var thi = $(el).find('.ls-thumbnail-hover-inner').css({
								visibility : 'hidden',
								display: 'block'
							});

							btn.hover(
								function(){

									var hoverLayer = $(el).find('.ls-layer').eq( $(this).index() );

									if( hoverLayer.find('.ls-tn').length ){
										var tnSrc = hoverLayer.find('.ls-tn').attr('src');
									}else if( hoverLayer.find('.ls-videopreview').length ){
										var tnSrc = hoverLayer.find('.ls-videopreview').attr('src');
									}else if( hoverLayer.find('.ls-bg').length ){
										var tnSrc = hoverLayer.find('.ls-bg').attr('src');
									}else{
										var tnSrc = ls.o.skinsPath+ls.o.skin+'/nothumb.png';
									}

									$(el).find('.ls-thumbnail-hover-img').css({
										left: parseInt( th.css('padding-left') ),
										top: parseInt( th.css('padding-top') )
									});

									ti.load(function(){

										if( $(this).width() == 0 ){
											ti.css({
												position: 'relative',
												margin: '0 auto',
												left: 'auto'
											});
										}else{
											ti.css({
												position: 'absolute',
												marginLeft : - $(this).width() / 2,
												left: '50%'
											});
										}			
									}).attr( 'src', tnSrc );

									th.css({
										display: 'block'
									}).stop().animate({
										left: $(this).position().left + ( $(this).width() - th.outerWidth() ) / 2
									}, 250, 'easeInOutQuad');

									thi.css({
										display : 'none',
										visibility : 'visible'
									}).stop().fadeIn(250);
								},
								function(){
									thi.stop().fadeOut(250, function(){
										th.css({
											visibility : 'hidden',
											display: 'block'
										});
									});
								}
							);
						}						
					}

					if( ls.o.thumbnailNavigation == 'hover' ){

						thumbs.appendTo( $(el).find('.ls-bottom-slidebuttons') );
					}

					$(el).find('.ls-bottom-slidebuttons a:eq('+(ls.o.firstLayer-1)+')').addClass('ls-nav-active');
				}

				if( ls.o.navStartStop ){
					
					var buttonStart = $('<a class="ls-nav-start" href="#" />').click(function(e){
						e.preventDefault();
						$(el).layerSlider('start');
					}).prependTo( $(el).find('.ls-bottom-nav-wrapper') );

					var buttonStop = $('<a class="ls-nav-stop" href="#" />').click(function(e){
						e.preventDefault();
						$(el).layerSlider('stop');
					}).appendTo( $(el).find('.ls-bottom-nav-wrapper') );
					
				}else if( ls.o.thumbnailNavigation != 'always' ){

					$('<span class="ls-nav-sides ls-nav-sideleft" />').prependTo( $(el).find('.ls-bottom-nav-wrapper') );
					$('<span class="ls-nav-sides ls-nav-sideright" />').appendTo( $(el).find('.ls-bottom-nav-wrapper') );						
				}
				
				if( ls.o.hoverBottomNav && ls.o.thumbnailNavigation != 'always' ){
					
					bottomNav.css({
						display: 'none'
					});
					
					$(el).hover(
						function(){
							if( !ls.g.forceHideControls ){
								if( ls.g.ie78 ){
									bottomNav.css('display','block');
								}else{
									bottomNav.stop(true,true).fadeIn(300);									
								}
							}
						},
						function(){
							if( ls.g.ie78 ){
								bottomNav.css('display','none');
							}else{
								bottomNav.stop(true,true).fadeOut(300);
							}
						}						
					)
				}
			}

			// NEW FEATURE v3x.5 thumbnailNavigation ('always')

			if( ls.o.thumbnailNavigation == 'always' ){

				var thumbsWrapper = $('<div class="ls-thumbnail-wrapper"></div>').appendTo( $(el) );
				var thumbs = $('<div class="ls-thumbnail"><div class="ls-thumbnail-inner"><div class="ls-thumbnail-slide-container"><div class="ls-thumbnail-slide"></div></div></div></div>').appendTo( thumbsWrapper );
			
				ls.g.thumbnails = $(el).find('.ls-thumbnail-slide-container');
				
				if( !('ontouchstart' in window) ){
					ls.g.thumbnails.hover(
						function(){
							$(this).addClass('ls-thumbnail-slide-hover');
						},
						function(){
							$(this).removeClass('ls-thumbnail-slide-hover');
							ls.scrollThumb();
						}
					).mousemove(function(e){

						var mL = parseInt(e.pageX - $(this).offset().left ) / $(this).width() * ( $(this).width() - $(this).find('.ls-thumbnail-slide').width() );
						$(this).find('.ls-thumbnail-slide').stop().css({
							marginLeft : mL
						});
					});				
				}else{
					ls.g.thumbnails.addClass('ls-touchscroll');
				}
				
				$(el).find('.ls-layer').each(function(){
					
					var tempIndex = $(this).index() + 1;

					if( $(this).find('.ls-tn').length ){
						var tnSrc = $(this).find('.ls-tn').attr('src');
					}else if( $(this).find('.ls-videopreview').length ){
						var tnSrc = $(this).find('.ls-videopreview').attr('src');
					}else if( $(this).find('.ls-bg').length ){
						var tnSrc = $(this).find('.ls-bg').attr('src');
					}

					if( tnSrc ){
						var thumb = $('<a href="#" class="ls-thumb-' + tempIndex + '"><img src="'+tnSrc+'"></a>');
					}else{
						var thumb = $('<a href="#" class="ls-nothumb ls-thumb-' + tempIndex + '"><img src="'+ls.o.skinsPath+ls.o.skin+'/nothumb.png"></a>');
					}	

					thumb.appendTo( $(el).find('.ls-thumbnail-slide') );
					
					if( !('ontouchstart' in window) ){

						thumb.hover(
							function(){
								$(this).children().stop().fadeTo(300,ls.o.tnActiveOpacity/100);
							},
							function(){
								if( !$(this).children().hasClass('ls-thumb-active') ){
									$(this).children().stop().fadeTo(300,ls.o.tnInactiveOpacity/100);										
								}
							}								
						);					
					}
					
					thumb.click(function(e){
						e.preventDefault();
						$(el).layerSlider( tempIndex );
					});						
				});
				
				if( buttonStart && buttonStop ){
					var lsBottomBelowTN = $('<div class="ls-bottom-nav-wrapper ls-below-thumbnails"></div>').appendTo( $(el) );
					buttonStart.clone().click(function(e){
						e.preventDefault();
						$(el).layerSlider('start');
					}).appendTo( lsBottomBelowTN );
					buttonStop.clone().click(function(e){
						e.preventDefault();
						$(el).layerSlider('stop');
					}).appendTo( lsBottomBelowTN );
				}				

				if( ls.o.hoverBottomNav ){
					
					thumbsWrapper.css({
						visibility: 'hidden'
					});

					if( lsBottomBelowTN ){						
						ls.g.bottomWrapper = lsBottomBelowTN.css('display') == 'block' ? lsBottomBelowTN : $(el).find('.ls-above-thumbnails');

						ls.g.bottomWrapper.css({
							display: 'none'
						});
					}
					
					$(el).hover(
						function(){
							if( ls.g.ie78 ){
								thumbsWrapper.css({
									visibility: 'visible'
								});
								if( bottomWrapper ){
									bottomWrapper.css('display','block');
								}
							}else{
								thumbsWrapper.css({
									visibility: 'visible',
									display: 'none'
								}).stop(true,false).fadeIn(300);
								if( bottomWrapper ){
									bottomWrapper.stop(true,true).fadeIn(300);								
								}								
							}
						},
						function(){
							if( ls.g.ie78 ){
								thumbsWrapper.css({
									visibility: 'hidden'
								});
								if( bottomWrapper ){
									bottomWrapper.css('display','none');
								}
							}else{
								thumbsWrapper.stop(true,true).fadeOut(300, function(){
									$(this).css({
										visibility: 'hidden',
										display: 'block'
									});
								});
								if( bottomWrapper ){
									bottomWrapper.stop(true,true).fadeOut(300);
								}
							}
						}						
					)
				}
			}

			// Adding shadow wrapper
			
			var shadow = $('<div class="ls-shadow"></div>').appendTo( $(el) );
			shadow.data('originalHeight', shadow.height() );

			// Appending skin shadow if shadow wrapper has display: 'block' style property
			// 150ms delay needed because of caching bugs

			shadowTimer = 150;

			setTimeout(function(){
				if( $(el).find('.ls-shadow').css('display') == 'block' ){
					ls.g.shadow = $(el).find('.ls-shadow').append( $('<img />').attr('src',ls.o.skinsPath+ls.o.skin+'/shadow.png') );
				}
				ls.resizeShadow();
			}, shadowTimer);

			// Adding keyboard navigation if turned on and if number of layers > 1

			if( ls.o.keybNav && $(el).find('.ls-layer').length > 1 ){
				
				$('body').bind('keydown',function(e){
					if( !ls.g.isAnimating && !ls.g.isLoading ){
						if( e.which == 37 ){
							ls.o.cbPrev(ls.g);							
							ls.prev('clicked');
						}else if( e.which == 39 ){
							ls.o.cbNext(ls.g);							
							ls.next('clicked');
						}
					}
				});
			}

			// Adding touch-control navigation if number of layers > 1
			
			if('ontouchstart' in window && $(el).find('.ls-layer').length > 1 && ls.o.touchNav ){

			   $(el).find('.ls-inner').bind('touchstart', function( e ) {
					var t = e.touches ? e.touches : e.originalEvent.touches;
					if( t.length == 1 ){
						ls.g.touchStartX = ls.g.touchEndX = t[0].clientX;
					}
			    });

			   $(el).find('.ls-inner').bind('touchmove', function( e ) {
					var t = e.touches ? e.touches : e.originalEvent.touches;
					if( t.length == 1 ){
						ls.g.touchEndX = t[0].clientX;
					}
					if( Math.abs( ls.g.touchStartX - ls.g.touchEndX ) > 45 ){
						e.preventDefault();							
					}
			    });

				$(el).find('.ls-inner').bind('touchend',function( e ){
					if( Math.abs( ls.g.touchStartX - ls.g.touchEndX ) > 45 ){
						if( ls.g.touchStartX - ls.g.touchEndX > 0 ){
							ls.o.cbNext(ls.g);
							$(el).layerSlider('next');
						}else{
							ls.o.cbPrev(ls.g);
							$(el).layerSlider('prev');
						}
					}
				});
			}
			
			// Feature: pauseOnHover (if number of layers > 1)
			
			if( ls.o.pauseOnHover == true && $(el).find('.ls-layer').length > 1 ){
				
				// BUGFIX v1.6 stop was not working because of pause on hover

				$(el).find('.ls-inner').hover(
					function(){

						// Calling cbPause callback function

						ls.o.cbPause(ls.g);
						if( ls.g.autoSlideshow ){
							ls.g.paused = true;
							ls.stop();
						}
					},
					function(){
						if( ls.g.paused == true ){
							ls.start();								
							ls.g.paused = false;
						}						
					}
				);
			}

			ls.resizeSlider();

			// NEW FEATURE v1.7 added yourLogo
			
			if( ls.o.yourLogo ){
				ls.g.yourLogo = $('<img>').addClass('ls-yourlogo').appendTo($(el)).attr('style', ls.o.yourLogoStyle ).css({
					visibility: 'hidden',
					display: 'bock'
				}).load(function(){

					// NEW FEATURE v3.0 added responsive yourLogo

					var logoTimeout = 0;
					
					if( !ls.g.yourLogo ){
						logoTimeout = 1000;
					}
					
					setTimeout( function(){
						
						ls.g.yourLogo.data( 'originalWidth', ls.g.yourLogo.width() );
						ls.g.yourLogo.data( 'originalHeight', ls.g.yourLogo.height() );
						if( ls.g.yourLogo.css('left') != 'auto' ){
							ls.g.yourLogo.data( 'originalLeft', ls.g.yourLogo[0].style.left );
						}					
						if( ls.g.yourLogo.css('right') != 'auto' ){
							ls.g.yourLogo.data( 'originalRight', ls.g.yourLogo[0].style.right );
						}
						if( ls.g.yourLogo.css('top') != 'auto' ){
							ls.g.yourLogo.data( 'originalTop', ls.g.yourLogo[0].style.top );
						}
						if( ls.g.yourLogo.css('bottom') != 'auto' ){					
							ls.g.yourLogo.data( 'originalBottom', ls.g.yourLogo[0].style.bottom );
						}

						// NEW FEATURES v1.8 added yourLogoLink & yourLogoTarget

						if( ls.o.yourLogoLink != false ){
							$('<a>').appendTo($(el)).attr( 'href', ls.o.yourLogoLink ).attr('target', ls.o.yourLogoTarget ).css({
								textDecoration : 'none',
								outline : 'none'
							}).append( ls.g.yourLogo );
						}

						ls.g.yourLogo.css({
							display: 'none',
							visibility: 'visible'
						});

						ls.resizeYourLogo();
						
					}, logoTimeout );

				}).attr( 'src', ls.o.yourLogo );
			}

			// NEW FEATURE v1.7 added window resize function for make responsive layout better

			$(window).resize(function() {
				
				var timer = 0;
				if( ls.g.normalWidth != false && ls.g.goingNormal ){
					timer = 400;
				}
				if( ls.g.resizeTimeout ){
					clearTimeout(ls.g.resizeTimeout);
				}
				ls.g.resizeTimeout = setTimeout(function(){
					ls.makeResponsive( ls.g.curLayer, function(){return;});
					if( ls.g.yourLogo ){
						ls.resizeYourLogo();					
					}					
				},timer);
			});

			ls.g.showSlider = true;

			// NEW FEATURE v1.7 animating first layer

			if( ls.o.animateFirstLayer == true ){
				if( ls.o.autoStart ){
					ls.g.autoSlideshow = true;
					$(el).find('.ls-nav-start').addClass('ls-nav-start-active');
				}else{
					$(el).find('.ls-nav-stop').addClass('ls-nav-stop-active');
				}
				ls.next();		
			}else{
				ls.imgPreload(ls.g.curLayer,function(){
					ls.g.curLayer.fadeIn(1000, function(){

						ls.g.isLoading = false;

						$(this).addClass('ls-active');

						// NEW FEATURE v2.0 autoPlayVideos

						if( ls.o.autoPlayVideos ){
							$(this).delay( $(this).data('delayin') + 25 ).queue(function(){
								$(this).find('.ls-videopreview').click();
								$(this).dequeue();
							});							
						}

						// NEW FEATURE v3.0 showUntil sublayers

						ls.g.curLayer.find(' > *[class*="ls-s"]').each(function(){

							if( $(this).data('showuntil') > 0 ){

								ls.sublayerShowUntil( $(this) );
							}
						});
					});

					ls.changeThumb(ls.g.curLayerIndex)

					// If autoStart is true

					if( ls.o.autoStart ){
						ls.g.isLoading = false;
						ls.start();
					}else{
						$(el).find('.ls-nav-stop').addClass('ls-nav-stop-active');							
					}
				});
			}

			// NEW FEATURE v1.7 added cbInit function

			ls.o.cbInit($(el));				
		};

		ls.goFullScreen = function(){

			if( !ls.g.isAnimating && !ls.g.isLoading ){
				
				if (lsPrefixes(document, 'FullScreen') || lsPrefixes(document, 'IsFullScreen')) {
					ls.g.goingNormal = true;
					lsPrefixes(document, 'CancelFullScreen');
					$(el).removeClass('ls-container-fullscreen');
				}
				else {
					ls.g.normalWidth = ls.g.sliderWidth();
					ls.g.normalHeight = ls.g.sliderHeight();
					ls.g.normalRatio = ls.g.ratio;
					lsPrefixes($(el)[0], 'RequestFullScreen');
					$(el).addClass('ls-container-fullscreen');
				}
			}
		};

		ls.start = function(){

			if( ls.g.autoSlideshow ){
				if( ls.g.prevNext == 'prev' && ls.o.twoWaySlideshow ){
					ls.prev();
				}else{
					ls.next();
				}
			}else{
				ls.g.autoSlideshow = true;
				if( !ls.g.isAnimating && !ls.g.isLoading ){
					ls.timer();
				}
			}

			$(el).find('.ls-nav-start').addClass('ls-nav-start-active');
			$(el).find('.ls-nav-stop').removeClass('ls-nav-stop-active');
		};
		
		ls.timer = function(){

			var delaytime = $(el).find('.ls-active').data('slidedelay') ? parseInt( $(el).find('.ls-active').data('slidedelay') ) : ls.o.slideDelay;

			// BUGFIX v3.0 delaytime did not work on first layer if animateFirstLayer was set to off
			// BUGFIX v3.5 delaytime did not work on all layers in standalone version after bugfix 3.0 :)
			
			if( !ls.o.animateFirstLayer && !$(el).find('.ls-active').data('slidedelay') ){
				var tempD = $(el).find('.ls-layer:eq('+(ls.o.firstLayer-1)+')').data('slidedelay');
				delaytime = tempD ? tempD : ls.o.slideDelay;
			}

			clearTimeout( ls.g.slideTimer );
			ls.g.slideTimer = window.setTimeout(function(){
				ls.start();
			}, delaytime );
		};

		ls.stop = function(){

			if( !ls.g.paused && !ls.g.originalAutoSlideshow ){
				$(el).find('.ls-nav-stop').addClass('ls-nav-stop-active');
				$(el).find('.ls-nav-start').removeClass('ls-nav-start-active');
			}
			clearTimeout( ls.g.slideTimer );
			ls.g.autoSlideshow = false;
		};

		// Because of an ie7 bug, we have to check & format the strings correctly

		ls.ieEasing = function( e ){

			// BUGFIX v1.6 and v1.8 some type of animations didn't work properly

			if( $.trim(e.toLowerCase()) == 'swing' || $.trim(e.toLowerCase()) == 'linear'){
				return e.toLowerCase();
			}else{
				return e.replace('easeinout','easeInOut').replace('easein','easeIn').replace('easeout','easeOut').replace('quad','Quad').replace('quart','Quart').replace('cubic','Cubic').replace('quint','Quint').replace('sine','Sine').replace('expo','Expo').replace('circ','Circ').replace('elastic','Elastic').replace('back','Back').replace('bounce','Bounce');				
			}
		};

		// Calculating prev layer

		ls.prev = function(clicked){

			// NEW FEATURE v2.0 loops

			if( ls.g.curLayerIndex < 2 ){
				ls.g.nextLoop += 1;
			}

			if( ( ls.g.nextLoop > ls.o.loops ) && ( ls.o.loops > 0 ) && !clicked ){
				ls.g.nextLoop = 0;
				ls.stop();
				if( ls.o.forceLoopNum == false ){
					ls.o.loops = 0;						
				}
			}else{
				var prev = ls.g.curLayerIndex < 2 ? ls.g.layersNum : ls.g.curLayerIndex - 1;
				ls.g.prevNext = 'prev';
				ls.change(prev,ls.g.prevNext);
			}
		};

		// Calculating next layer

		ls.next = function(clicked){

			// NEW FEATURE v2.0 loops

			if( !ls.o.randomSlideshow ){
				
				if( !(ls.g.curLayerIndex < ls.g.layersNum) ){
					ls.g.nextLoop += 1;
				}

				if( ( ls.g.nextLoop > ls.o.loops ) && ( ls.o.loops > 0 ) && !clicked ){

					ls.g.nextLoop = 0;
					ls.stop();
					if( ls.o.forceLoopNum == false ){
						ls.o.loops = 0;						
					}
				}else{

					var next = ls.g.curLayerIndex < ls.g.layersNum ? ls.g.curLayerIndex + 1 : 1;
					ls.g.prevNext = 'next';
					ls.change(next,ls.g.prevNext);
				}
			}else if( !clicked ){

				// NEW FEATURE v3.5 randomSlideshow

				var next = ls.g.curLayerIndex;

				var calcRand = function(){
					
					next = Math.floor(Math.random() * ls.g.layersNum) + 1;

					if( next == ls.g.curLayerIndex ){

						calcRand();
					}else{
						ls.g.prevNext = 'next';
						ls.change(next,ls.g.prevNext);						
					}
				}
				
				calcRand();
			}else if( clicked ){
				
				var next = ls.g.curLayerIndex < ls.g.layersNum ? ls.g.curLayerIndex + 1 : 1;
				ls.g.prevNext = 'next';
				ls.change(next,ls.g.prevNext);
			}

		};

		ls.change = function(num,prevnext){

			// NEW FEATURE v2.0 videoPreview & autoPlayVideos

			if( ls.g.pausedByVideo == true ){

				ls.g.pausedByVideo = false;
				ls.g.autoSlideshow = ls.g.originalAutoSlideshow;
				
				ls.g.curLayer.find('iframe[src*="www.youtu"], iframe[src*="player.vimeo"]').each(function(){

					$(this).parent().find('.ls-vpcontainer').fadeIn(ls.g.v.fi,function(){
						$(this).parent().find('iframe').attr('src','');						
					});
				});
			}
			
			$(el).find('iframe[src*="www.youtu"], iframe[src*="player.vimeo"]').each(function(){
				
				// Clearing videoTimeouts
				
				clearTimeout( $(this).data( 'videoTimer') );
			});

			clearTimeout( ls.g.slideTimer );
			ls.g.nextLayerIndex = num;
			ls.g.nextLayer = $(el).find('.ls-layer:eq('+(ls.g.nextLayerIndex-1)+')');

			// BUGFIX v1.6 fixed wrong directions of animations if navigating by slidebuttons

			if( !prevnext ){

				if( ls.g.curLayerIndex < ls.g.nextLayerIndex ){
					ls.g.prevNext = 'next';
				}else{
					ls.g.prevNext = 'prev';
				}				
			}

			// Added timeOut to wait for the fade animation of videoPreview image...

			var timeOut = 0;
			
			if( $(el).find('iframe[src*="www.youtu"], iframe[src*="player.vimeo"]').length > 0 ){
				timeOut = ls.g.v.fi;
			}

			clearTimeout( ls.g.changeTimer );
			ls.g.changeTimer = setTimeout(function() {

				var waitForGoingNormal = function(){
					if( ls.g.goingNormal ){
						setTimeout(function(){
							waitForGoingNormal();
						}, 500);
					}else{
						ls.imgPreload(ls.g.nextLayer,function(){
							ls.animate();
						});						
					}
				}
				
				waitForGoingNormal();

			}, timeOut );
		};
		
		// Preloading images

		ls.imgPreload = function(layer,callback){

			ls.g.isLoading = true;

			// Showing slider for the first time

			if( ls.g.showSlider ){
				$(el).css({
					visibility : 'visible'
				});				
			}
			
			// If image preload is on

			if( ls.o.imgPreload ){

				var preImages = [];
				var preloaded = 0;

				// NEW FEATURE v1.8 Prealoading background images of layers
				
				if( layer.css('background-image') != 'none' && layer.css('background-image').indexOf('url') != -1 ){
					var bgi = layer.css('background-image');
					bgi = bgi.match(/url\((.*)\)/)[1].replace(/"/gi, '');
					preImages.push(bgi);
				}
				
				// Images inside layers

				layer.find('img').each(function(){
					preImages.push($(this).attr('src'));
				});

				// Background images inside layers

				layer.find('*').each(function(){
					
					// BUGFIX v1.7 fixed preload bug with sublayers with gradient backgrounds

					if( $(this).css('background-image') != 'none' && $(this).css('background-image').indexOf('url') != -1 ){
						var bgi = $(this).css('background-image');
						bgi = bgi.match(/url\((.*)\)/)[1].replace(/"/gi, '');
						preImages.push(bgi);
					}
				});

				// BUGFIX v1.7 if there are no images in a layer, calling the callback function

				if(preImages.length == 0){
					ls.makeResponsive(layer, callback);
				}else{

					// NEW FEATURE v4.0 Showing loading indicator

					if( ls.g.ie78 ){
						ls.g.li.css('display','block');
					}else{
						ls.g.li.fadeIn(300);						
					}

					for(x=0;x<preImages.length;x++){
						$('<img>').load(function(){
							if( ++preloaded == preImages.length ){

								// NEW FEATURE v4.0 Hiding loading indicator
								
								ls.g.li.dequeue().css({
									display: 'none'
								});

								$('.ls-thumbnail-wrapper, .ls-nav-next, .ls-nav-prev, .ls-bottom-nav-wrapper').css({
									visibility : 'visible'
								});

								ls.makeResponsive(layer, callback);
							}
						}).attr('src',preImages[x]);
					}					
				}
			}else{

				$('.ls-thumbnail-wrapper, .ls-nav-next, .ls-nav-prev, .ls-bottom-nav-wrapper').css({
					visibility : 'visible'
				});

				ls.makeResponsive(layer, callback);
			}
		};
		
		// NEW FEATURE v1.7 making the slider responsive

		ls.makeResponsive = function(layer, callback ){

			layer.css({
				visibility: 'hidden',
				display: 'block'
			});

			ls.resizeSlider();

			if( ls.o.thumbnailNavigation == 'always' ){
				ls.resizeThumb();				
			}
			layer.children().each(function(){
				
				var sl = $(this);

				// positioning

				var ol = sl.data('originalLeft') ? sl.data('originalLeft') : '0';
				var ot = sl.data('originalTop') ? sl.data('originalTop') : '0';
				
				if( sl.is('a') && sl.children().length > 0 ){
					sl.css({
						display : 'block'
					});
					sl = sl.children();
				}

				var ow = 'auto';
				var oh = 'auto';

				if( sl.data('originalWidth') ){
					if( typeof( sl.data('originalWidth') ) == 'number' ){
						ow = parseInt( sl.data('originalWidth') ) * ls.g.ratio;						
					}else if( sl.data('originalWidth').indexOf('%') != -1 ){
						ow = sl.data('originalWidth');
					}
				}
				
				if( sl.data('originalHeight') ){
					if( typeof( sl.data('originalHeight') ) == 'number' ){
						oh = parseInt( sl.data('originalHeight') ) * ls.g.ratio;						
					}else if( sl.data('originalHeight').indexOf('%') != -1 ){
						oh = sl.data('originalHeight');
					}
				}
				
				// padding

				var opl = sl.data('originalPaddingLeft') ? parseInt( sl.data('originalPaddingLeft') ) * ls.g.ratio : 0;
				var opr = sl.data('originalPaddingRight') ? parseInt( sl.data('originalPaddingRight') ) * ls.g.ratio : 0;
				var opt = sl.data('originalPaddingTop') ? parseInt( sl.data('originalPaddingTop') ) * ls.g.ratio : 0;
				var opb = sl.data('originalPaddingBottom') ? parseInt( sl.data('originalPaddingBottom') ) * ls.g.ratio : 0;

				// border
				
				var obl = sl.data('originalBorderLeft') ? parseInt( sl.data('originalBorderLeft') ) * ls.g.ratio : 0;
				var obr = sl.data('originalBorderRight') ? parseInt( sl.data('originalBorderRight') ) * ls.g.ratio : 0;
				var obt = sl.data('originalBorderTop') ? parseInt( sl.data('originalBorderTop') ) * ls.g.ratio : 0;
				var obb = sl.data('originalBorderBottom') ? parseInt( sl.data('originalBorderBottom') ) * ls.g.ratio : 0;

				// font

				var ofs = sl.data('originalFontSize');
				var olh = sl.data('originalLineHeight');

				// NEW FEATURE v3.0 added "normal" responsive mode with image and font resizing
				// NEW FEATURE v3.5 added responsiveUnder

				if( ls.g.responsiveMode || ls.o.responsiveUnder > 0 ){

					if( sl.is('img') ){
						sl.css({
							width : 'auto',
							height : 'auto'
						});

						ow = sl.width();
						oh = sl.height();

						sl.css({
							width : ow * ls.g.ratio,
							height : oh * ls.g.ratio
						});
					}
					
					if( !sl.is('img') ){
						sl.css({
							width : ow,
							height : oh,
							'font-size' : parseInt(ofs) * ls.g.ratio +'px',
							'line-height' : parseInt(olh) * ls.g.ratio + 'px'
						});
					}
					
					if( sl.is('div') && sl.find('iframe').data('videoSrc') ){
						
						var videoIframe = sl.find('iframe');
						videoIframe.attr('width', parseInt( videoIframe.data('originalWidth') ) * ls.g.ratio ).attr('height', parseInt( videoIframe.data('originalHeight') ) * ls.g.ratio );
						
						sl.css({
							width : parseInt( videoIframe.data('originalWidth') ) * ls.g.ratio,
							height : parseInt( videoIframe.data('originalHeight') ) * ls.g.ratio
						});
					}

					sl.css({
						padding : opt + 'px ' + opr + 'px ' + opb + 'px ' + opl + 'px ',
						borderLeftWidth : obl + 'px',
						borderRightWidth : obr + 'px',
						borderTopWidth : obt + 'px',
						borderBottomWidth : obb + 'px'						
					});
				}

				// If it is NOT a bg sublayer

				if( !sl.hasClass('ls-bg') ){

					var sl2 = sl;

					if( sl.parent().is('a') ){
						sl = sl.parent();
					}
								
					// NEW FEATURE v3.5 sublayerContainer

					var slC = ls.o.sublayerContainer > 0 ? ( ls.g.sliderWidth() - ls.o.sublayerContainer ) / 2 : 0;
					slC = slC < 0 ? 0 : slC;

					// (RE)positioning sublayer (left property)

					if( ol.indexOf('%') != -1 ){
						sl.css({
							left : ls.g.sliderWidth() / 100 * parseInt(ol) - sl2.width() / 2 - opl - obl
						});
					}else if( slC > 0 || ls.g.responsiveMode || ls.o.responsiveUnder > 0 ){
						sl.css({
							left : slC + parseInt(ol) * ls.g.ratio
						});
					}	

					// (RE)positioning sublayer (top property)

					if( ot.indexOf('%') != -1 ){
						sl.css({
							top : ls.g.sliderHeight() / 100 * parseInt(ot) - sl2.height() / 2 - opt - obt
						});
					}else if( ls.g.responsiveMode || ls.o.responsiveUnder > 0 ){
						sl.css({
							top : parseInt(ot) * ls.g.ratio
						});
					}

				}else{

					sl.css({
						width : 'auto',
						height : 'auto'
					});

					ow = sl.width();
					oh = sl.height();

					sl.css({
						width : Math.round(ow * ls.g.ratio),
						height : Math.round(oh * ls.g.ratio),
						marginLeft : - Math.round( ow * ls.g.ratio ) / 2 +'px',
						marginTop : - Math.round( oh * ls.g.ratio ) / 2 +'px'
					});
				}
			});

			layer.css({
				display: 'none',
				visibility: 'visible'
			});

			// Resizing shadow

			ls.resizeShadow();
			
			callback();

			$(this).dequeue();

			if( ls.g.normalWidth && ls.g.goingNormal ){
				ls.g.normalWidth = false;
				ls.g.normalHeight = false;
				ls.g.normalRatio = false;
				ls.g.goingNormal = false;
			}
			
		};
		
		// Resizing shadow
		
		ls.resizeShadow = function(){
			
			if( ls.g.shadow ){
				ls.g.shadow.css({
					height: Math.round(ls.g.shadow.data('originalHeight') * ls.g.ratio)
				});				
			}				
		};

		// Resizing the slider

		ls.resizeSlider = function(){

			if( ls.o.responsiveUnder > 0 ){
				
				if( $(window).width() < ls.o.responsiveUnder ){
					ls.g.responsiveMode = true;
					ls.g.sliderOriginalWidth = ls.o.responsiveUnder + 'px';
				}else{
					ls.g.responsiveMode = false;
					ls.g.sliderOriginalWidth = ls.g.sliderOriginalWidthRU;
					ls.g.ratio = 1;
				}
			}
		
			// NEW FEATURE v3.0 added "normal" responsive mode with image and font resizing

			if( ls.g.responsiveMode ){
				
				var parent = $(el).parent();

				if( ls.g.normalRatio && ls.g.goingNormal ){
					$(el).css({
						width : ls.g.normalWidth
					});
					ls.g.ratio = ls.g.normalRatio;
					$(el).css({
						height : ls.g.normalHeight
					});
				}else{
					// BUGFIX v4.0 there is no need to subtract the values of the left and right paddings of the container element!

					$(el).css({
						width : parent.width() - parseInt($(el).css('padding-left')) - parseInt($(el).css('padding-right'))
					});
					ls.g.ratio = $(el).width() / parseInt( ls.g.sliderOriginalWidth );
					$(el).css({
						height : ls.g.ratio * parseInt( ls.g.sliderOriginalHeight )
					});
				}

			}else{
				ls.g.ratio = 1;
				$(el).css({
					width : ls.g.sliderOriginalWidth,
					height : ls.g.sliderOriginalHeight
				});
			}
			
			// WP fullWidth mode (originally forceResponsive mode)
			
			if( $(el).closest('.ls-wp-fullwidth-container').length ){

				$(el).closest('.ls-wp-fullwidth-helper').css({
					height : $(el).outerHeight(true)
				});

				$(el).closest('.ls-wp-fullwidth-container').css({
					height : $(el).outerHeight(true)
				});

				$(el).closest('.ls-wp-fullwidth-helper').css({
					width : $(window).width(),
					left : - $(el).closest('.ls-wp-fullwidth-container').offset().left
				});

				if( ls.g.sliderOriginalWidth.indexOf('%') != -1 ){

					var percentWidth = parseInt( ls.g.sliderOriginalWidth );
					var newWidth = $('body').width() / 100 * percentWidth - ( $(el).outerWidth() - $(el).width() );
					$(el).width( newWidth );
				}
			}

			$(el).find('.ls-inner, .ls-lt-container').css({
				width : ls.g.sliderWidth(),
				height : ls.g.sliderHeight()
			});
			
			// BUGFIX v2.0 fixed width problem if firstLayer is not 1

			if( ls.g.curLayer && ls.g.nextLayer ){

				ls.g.curLayer.css({
					width : ls.g.sliderWidth(),
					height : ls.g.sliderHeight()
				});

				ls.g.nextLayer.css({
					width : ls.g.sliderWidth(),
					height : ls.g.sliderHeight()
				});

			}else{

				$(el).find('.ls-layer').css({
					width : ls.g.sliderWidth(),
					height : ls.g.sliderHeight()
				});
			}	
		};

		// NEW FEATURE v3.0 added responsive yourLogo

		ls.resizeYourLogo = function(){

			ls.g.yourLogo.css({
				width : ls.g.yourLogo.data( 'originalWidth' ) * ls.g.ratio,
				height : ls.g.yourLogo.data( 'originalHeight' ) * ls.g.ratio
			});
			
			if( ls.g.ie78 ){
				ls.g.yourLogo.css('display','block');
			}else{
				ls.g.yourLogo.fadeIn(300);				
			}

			var oL = oR = oT = oB = 'auto';

			if( ls.g.yourLogo.data( 'originalLeft' ) && ls.g.yourLogo.data( 'originalLeft' ).indexOf('%') != -1 ){
				oL = ls.g.sliderWidth() / 100 * parseInt( ls.g.yourLogo.data( 'originalLeft' ) ) - ls.g.yourLogo.width() / 2 + parseInt( $(el).css('padding-left') );
			}else{
				oL = parseInt( ls.g.yourLogo.data( 'originalLeft' ) ) * ls.g.ratio;
			}

			if( ls.g.yourLogo.data( 'originalRight' ) && ls.g.yourLogo.data( 'originalRight' ).indexOf('%') != -1 ){
				oR = ls.g.sliderWidth() / 100 * parseInt( ls.g.yourLogo.data( 'originalRight' ) ) - ls.g.yourLogo.width() / 2 + parseInt( $(el).css('padding-right') );
			}else{
				oR = parseInt( ls.g.yourLogo.data( 'originalRight' ) ) * ls.g.ratio;
			}

			if( ls.g.yourLogo.data( 'originalTop' ) && ls.g.yourLogo.data( 'originalTop' ).indexOf('%') != -1 ){
				oT = ls.g.sliderHeight() / 100 * parseInt( ls.g.yourLogo.data( 'originalTop' ) ) - ls.g.yourLogo.height() / 2 + parseInt( $(el).css('padding-top') );
			}else{
				oT = parseInt( ls.g.yourLogo.data( 'originalTop' ) ) * ls.g.ratio;
			}

			if( ls.g.yourLogo.data( 'originalBottom' ) && ls.g.yourLogo.data( 'originalBottom' ).indexOf('%') != -1 ){
				oB = ls.g.sliderHeight() / 100 * parseInt( ls.g.yourLogo.data( 'originalBottom' ) ) - ls.g.yourLogo.height() / 2 + parseInt( $(el).css('padding-bottom') );
			}else{
				oB = parseInt( ls.g.yourLogo.data( 'originalBottom' ) ) * ls.g.ratio;
			}

			ls.g.yourLogo.css({
				left : oL,
				right : oR,
				top : oT,
				bottom : oB
			});
		};

		// NEW FEATURE v3.5 thumbnailNavigation ('always')

		// Resizing thumbnails

		ls.resizeThumb = function(){

			$(el).find('.ls-thumbnail-slide a').css({
				width : parseInt( ls.o.tnWidth * ls.g.ratio ),
				height : parseInt( ls.o.tnHeight * ls.g.ratio )
			});

			$(el).find('.ls-thumbnail-slide a:last').css({
				margin: 0
			});

			$(el).find('.ls-thumbnail-slide').css({
				height : parseInt( ls.o.tnHeight * ls.g.ratio )
			});
			
			var tn = $(el).find('.ls-thumbnail');

			var originalWidth = ls.o.tnContainerWidth.indexOf('%') == -1 ? parseInt( ls.o.tnContainerWidth ) : parseInt( parseInt( ls.g.sliderOriginalWidth ) / 100 * parseInt( ls.o.tnContainerWidth ) );

			tn.css({
				width : originalWidth * Math.floor( ls.g.ratio * 100 ) / 100
			});

			if( tn.width() > $(el).find('.ls-thumbnail-slide').width() ){
				tn.css({
					width : $(el).find('.ls-thumbnail-slide').width()
				});
			}
		};
		
		// Changing thumbnails
		
		ls.changeThumb = function(index){
			
			var curIndex = index ? index : ls.g.nextLayerIndex;

			$(el).find('.ls-thumbnail-slide a:not(.ls-thumb-'+curIndex+')').children().each(function(){
				$(this).removeClass('ls-thumb-active').stop().fadeTo(750,ls.o.tnInactiveOpacity/100);
			});
			
			$(el).find('.ls-thumbnail-slide a.ls-thumb-'+curIndex).children().addClass('ls-thumb-active').stop().fadeTo(750,ls.o.tnActiveOpacity/100);
		};

		// Scrolling thumbnails

		ls.scrollThumb = function(){

			if( !$(el).find('.ls-thumbnail-slide-container').hasClass('ls-thumbnail-slide-hover') ){				
				var curThumb = $(el).find('.ls-thumb-active').length ? $(el).find('.ls-thumb-active').parent() : false;
				if( curThumb ){
					var thumbCenter = curThumb.position().left + curThumb.width() / 2;
					var mL = $(el).find('.ls-thumbnail-slide-container').width() / 2 - thumbCenter;
					mL = mL > 0 ? 0 : mL;
					mL = mL < $(el).find('.ls-thumbnail-slide-container').width() - $(el).find('.ls-thumbnail-slide').width() ? $(el).find('.ls-thumbnail-slide-container').width() - $(el).find('.ls-thumbnail-slide').width() : mL;
					$(el).find('.ls-thumbnail-slide').animate({
						marginLeft : mL
					}, 600, 'easeInOutQuad');				
				}
			}
		};
		
		// Animating layers and sublayers

		ls.animate = function(){

			/* GLOBAL (used by both old and new transitions ) */

					// Changing variables

					ls.g.isAnimating = true;
					ls.g.isLoading = false;

					// Clearing timeouts

					clearTimeout( ls.g.slideTimer );
					clearTimeout( ls.g.changeTimer );

					ls.g.stopLayer = ls.g.curLayer;

					// Calling cbAnimStart callback function

					ls.o.cbAnimStart(ls.g);

					// NEW FEATURE v3.5 thumbnailNavigation ('always')

					if( ls.o.thumbnailNavigation == 'always' ){

						// ChangeThumb

						ls.changeThumb();

						// ScrollThumb

						if( !('ontouchstart' in window) ){
							ls.scrollThumb();
						}
					}

					// Adding .ls-animating class to next layer

					ls.g.nextLayer.addClass('ls-animating');



			/* OLD layer transitions (version 3.x) */

					// Setting position and styling of current and next layers

					var curLayerLeft = curLayerRight = curLayerTop = curLayerBottom = nextLayerLeft = nextLayerRight = nextLayerTop = nextLayerBottom = layerMarginLeft = layerMarginRight = layerMarginTop = layerMarginBottom = 'auto';
					var curLayerWidth = nextLayerWidth = ls.g.sliderWidth();
					var curLayerHeight = nextLayerHeight = ls.g.sliderHeight();

					// Calculating direction

					var prevOrNext = ls.g.prevNext == 'prev' ? ls.g.curLayer : ls.g.nextLayer;
					var chooseDirection = prevOrNext.data('slidedirection') ? prevOrNext.data('slidedirection') : ls.o.slideDirection;

					// Setting the direction of sliding

					var slideDirection = ls.g.slideDirections[ls.g.prevNext][chooseDirection];

					if( slideDirection == 'left' || slideDirection == 'right' ){
						curLayerWidth = curLayerTop = nextLayerWidth = nextLayerTop = 0;
						layerMarginTop = 0;				
					}
					if( slideDirection == 'top' || slideDirection == 'bottom' ){
						curLayerHeight = curLayerLeft = nextLayerHeight = nextLayerLeft = 0;
						layerMarginLeft = 0;
					}

					switch(slideDirection){
						case 'left':
							curLayerRight = nextLayerLeft = 0;
							layerMarginLeft = -ls.g.sliderWidth();
							break;
						case 'right':
							curLayerLeft = nextLayerRight = 0;
							layerMarginLeft = ls.g.sliderWidth();
							break;
						case 'top':
							curLayerBottom = nextLayerTop = 0;
							layerMarginTop = -ls.g.sliderHeight();
							break;
						case 'bottom':
							curLayerTop = nextLayerBottom = 0;
							layerMarginTop = ls.g.sliderHeight();
							break;
					}

					// Setting start positions and styles of layers

					ls.g.curLayer.css({
						left : curLayerLeft,
						right : curLayerRight,
						top : curLayerTop,
						bottom : curLayerBottom			
					});
					ls.g.nextLayer.css({
						width : nextLayerWidth,
						height : nextLayerHeight,
						left : nextLayerLeft,
						right : nextLayerRight,
						top : nextLayerTop,
						bottom : nextLayerBottom
					});

					// Creating variables for the OLD transitions of CURRENT LAYER

					// BUGFIX v1.6 fixed some wrong parameters of current layer
					// BUGFIX v1.7 fixed using of delayout of current layer

					var curDelay = ls.g.curLayer.data('delayout') ? parseInt(ls.g.curLayer.data('delayout')) : ls.o.delayOut;

					var curDuration = ls.g.curLayer.data('durationout') ? parseInt(ls.g.curLayer.data('durationout')) : ls.o.durationOut;
					var curEasing = ls.g.curLayer.data('easingout') ? ls.g.curLayer.data('easingout') : ls.o.easingOut;

					// Creating variables for the OLD transitions of NEXT LAYER

					var nextDelay = ls.g.nextLayer.data('delayin') ? parseInt(ls.g.nextLayer.data('delayin')) : ls.o.delayIn;
					var nextDuration = ls.g.nextLayer.data('durationin') ? parseInt(ls.g.nextLayer.data('durationin')) : ls.o.durationIn;
					var nextEasing = ls.g.nextLayer.data('easingin') ? ls.g.nextLayer.data('easingin') : ls.o.easingIn;

					var curLayer = function(){

						// BUGFIX v1.6 added an additional delaytime to current layer to fix the '1px gap' bug
						// BUGFIX v3.0 modified from curDuration / 80 to curDuration / 15

						ls.g.curLayer.delay( curDelay + curDuration / 15).animate({
							width : curLayerWidth,
							height : curLayerHeight
						}, curDuration, curEasing,function(){

							curLayerCallback();
						});						
					};
					
					var curLayerCallback = function(){

						// Stopping current sublayer animations if needed (they are not visible at this point).

						ls.g.stopLayer.find(' > *[class*="ls-s"]').stop(true,true);

						// FIXED v4.0 Calling cbAnimStop callback function before changing layer indexes

						ls.o.cbAnimStop(ls.g);

						// Setting current layer

						ls.g.curLayer = ls.g.nextLayer;
						ls.g.curLayerIndex = ls.g.nextLayerIndex;

						// Changing some css classes

						$(el).find('.ls-layer').removeClass('ls-active');
						$(el).find('.ls-layer:eq(' + ( ls.g.curLayerIndex - 1 ) + ')').addClass('ls-active').removeClass('ls-animating');
						$(el).find('.ls-bottom-slidebuttons a').removeClass('ls-nav-active');
						$(el).find('.ls-bottom-slidebuttons a:eq('+( ls.g.curLayerIndex - 1 )+')').addClass('ls-nav-active');

						// Setting timer if needed

						if( ls.g.autoSlideshow ){
							ls.timer();
						}	

						// Changing variables

						ls.g.isAnimating = false;
					};

					var curSubLayers = function(sublayersDurationOut){

						ls.g.curLayer.find(' > *[class*="ls-s"]').each(function(){

							var curSubSlideDir = $(this).data('slidedirection') ? $(this).data('slidedirection') : slideDirection;
							var lml, lmt;

							switch(curSubSlideDir){
								case 'left':
									lml = -ls.g.sliderWidth();
									lmt = 0;
									break;
								case 'right':
									lml = ls.g.sliderWidth();
									lmt = 0;
									break;
								case 'top':
									lmt = -ls.g.sliderHeight();
									lml = 0;
									break;
								case 'bottom':
									lmt = ls.g.sliderHeight();
									lml = 0;
									break;
							}

							// NEW FEATURE v1.6 added slideoutdirection to sublayers

							var curSubSlideOutDir = $(this).data('slideoutdirection') ? $(this).data('slideoutdirection') : false;

							switch(curSubSlideOutDir){
								case 'left':
									lml = ls.g.sliderWidth();
									lmt = 0;
									break;
								case 'right':
									lml = -ls.g.sliderWidth();
									lmt = 0;
									break;
								case 'top':
									lmt = ls.g.sliderHeight();
									lml = 0;
									break;
								case 'bottom':
									lmt = -ls.g.sliderHeight();
									lml = 0;
									break;
							}

							// IMPROVEMENT v4.0 Distance (P.level): -1

							var curSubPLevel = parseInt( $(this).attr('class').split('ls-s')[1] );
							
							if( curSubPLevel == -1 ){
								var endLeft = parseInt( $(this).css('left') );
								var endTop = parseInt( $(this).css('top') );
								if( lmt < 0 ){
									lmt = - ( ls.g.sliderHeight() - endTop );
								}else if( lmt > 0 ){
									lmt = endTop + $(this).outerHeight();
								}
								if( lml < 0 ){
									lml = - ( ls.g.sliderWidth() - endLeft );
								}else if( lml > 0 ){
									lml = endLeft + $(this).outerWidth();
								}
								var curSubPar = 1;
							}else{
								var curSubParMod = ls.g.curLayer.data('parallaxout') ? parseInt(ls.g.curLayer.data('parallaxout')) : ls.o.parallaxOut;
								var curSubPar = curSubPLevel * curSubParMod;
							}

							var curSubDelay = $(this).data('delayout') ? parseInt($(this).data('delayout')) : ls.o.delayOut;
							var curSubTime = $(this).data('durationout') ? parseInt($(this).data('durationout')) : ls.o.durationOut;								
							var curSubEasing = $(this).data('easingout') ? $(this).data('easingout') : ls.o.easingOut;

							// On new layer transitions, all sublayer will be slide / fade out in 500ms without any delays

							if(sublayersDurationOut){
								curSubDelay = 0;
								curSubTime = sublayersDurationOut;
								// curSubEasing = 'easeInExpo';
							}

							// NEW FEATURE v1.6 added fade transition to sublayers

							if( curSubSlideOutDir == 'fade' || ( !curSubSlideOutDir && curSubSlideDir == 'fade' )){

								if(sublayersDurationOut && ls.g.ie78 ){
									$(this).dequeue().css({
										visibility: 'hidden'
									});
								}else{
									
									// iOS fade bug when GPU acceleration is enabled #2
									
									if( ls.g.isMobile() == true && lsBrowser().webkit ){
										$(this).stop().delay( curSubDelay ).fadeTo(curSubTime, 0, curSubEasing,function(){
											$(this).css({
												visibility: 'hidden',
												opacity: $(this).data( 'originalOpacity')
											});
										});									
									}else{
										$(this).stop(true,true).delay( curSubDelay ).fadeOut(curSubTime, curSubEasing,function(){
											$(this).css({
												visibility: 'hidden',
												display: 'block'
											});
										});									
									}									
								}
							}else{

								$(this).stop().dequeue().delay( curSubDelay ).animate({
									marginLeft : -lml * curSubPar,
									marginTop : -lmt * curSubPar
								}, curSubTime, curSubEasing);						
							}
						});	
					};

					var nextLayer = function(){

						ls.g.nextLayer.delay( curDelay + nextDelay ).animate({
							width : ls.g.sliderWidth(),
							height : ls.g.sliderHeight()
						}, nextDuration, nextEasing );
					};

					var nextSubLayers = function(){

						if( ls.g.totalDuration ){
							curDelay = 0;
						}

						ls.g.nextLayer.find(' > *[class*="ls-s"]').each(function(){

							// Replacing global parameters with unique if need

							var nextSubSlideDir = $(this).data('slidedirection') ? $(this).data('slidedirection') : slideDirection;
							var lml, lmt;

							switch(nextSubSlideDir){
								case 'left':
									lml = -ls.g.sliderWidth();
									lmt = 0;
									break;
								case 'right':
									lml = ls.g.sliderWidth();
									lmt = 0;
									break;
								case 'top':
									lmt = -ls.g.sliderHeight();
									lml = 0;
									break;
								case 'bottom':
									lmt = ls.g.sliderHeight();
									lml = 0;
									break;
								case 'fade':
									lmt = 0;
									lml = 0;
									break;
							}

							// IMPROVEMENT v4.0 Distance (P.level): -1

							var nextSubPLevel = parseInt( $(this).attr('class').split('ls-s')[1] );
							
							if( nextSubPLevel == -1 ){
								var endLeft = parseInt( $(this).css('left') );
								var endTop = parseInt( $(this).css('top') );
								if( lmt < 0 ){
									lmt = - ( endTop + $(this).outerHeight() );
								}else if( lmt > 0 ){
									lmt = ls.g.sliderHeight() - endTop;
								}
								if( lml < 0 ){
									lml = - ( endLeft + $(this).outerWidth() );
								}else if( lml > 0 ){
									lml = ls.g.sliderWidth() - endLeft;
								}
								var nextSubPar = 1;
							}else{
								var nextSubParMod = ls.g.nextLayer.data('parallaxin') ? parseInt(ls.g.nextLayer.data('parallaxin')) : ls.o.parallaxIn;
								var nextSubPar = nextSubPLevel * nextSubParMod;								
							}

							var nextSubDelay = $(this).data('delayin') ? parseInt($(this).data('delayin')) : ls.o.delayIn;
							var nextSubTime = $(this).data('durationin') ? parseInt($(this).data('durationin')) : ls.o.durationIn;
							var nextSubEasing = $(this).data('easingin') ? $(this).data('easingin') : ls.o.easingIn;

							var cursub = $(this);

							var nextSubCallback = function(){
								
								// NEW FEATURE v2.0 autoPlayVideos

								if( ls.o.autoPlayVideos == true ){

									cursub.find('.ls-videopreview').click();
								}					

								// NEW FEATURE v3.0 showUntil sublayers

								if( cursub.data('showuntil') > 0 ){

									ls.sublayerShowUntil( cursub );
								}								
							}

							// NEW FEATURE v1.6 added fade transition to sublayers

							if( nextSubSlideDir == 'fade' ){

								// iOS fade bug when GPU acceleration is enabled #3

								if( ls.g.isMobile() == true && lsBrowser().webkit ){

									$(this).css({
										opacity: 0,
										visibility: 'visible',
										marginLeft : 0,
										marginTop : 0
									}).stop().delay( curDelay + nextDelay + nextSubDelay ).fadeTo(nextSubTime, $(this).data( 'originalOpacity'), nextSubEasing, function(){

										nextSubCallback();
									});
									
								}else{
									$(this).css({
										display: 'none',
										visibility: 'visible',
										marginLeft : 0,
										marginTop : 0
									}).stop(true,true).delay( curDelay + nextDelay + nextSubDelay ).fadeIn(nextSubTime, nextSubEasing, function(){

										nextSubCallback();
									});
									
								}
								
							}else{

								// iOS fade bug when GPU acceleration is enabled #4

								if( ls.g.isMobile() == true && lsBrowser().webkit ){
									$(this).css({
										opacity : $(this).data( 'originalOpacity')
									});
								}

								// BUGFIX v1.7 added display : block to sublayers that don't fade

								$(this).css({
									marginLeft : lml * nextSubPar,
									marginTop : lmt * nextSubPar,
									display : 'block',
									visibility: 'visible'
								});

								$(this).stop().delay( curDelay + nextDelay + nextSubDelay ).animate({
									marginLeft : 0,
									marginTop : 0
								}, nextSubTime, nextSubEasing, function(){

									nextSubCallback();
								});								
							}
						});
					};



			/* NEW FEATURE v4.0 2D & 3D Layer Transitions */

					// Selecting ONE transition (random)
					// If the browser doesn't support CSS3 3D, 2D fallback mode will be used instead
					// In this case, if user didn't specify any 2D transitions, a random will be selected

					var selectTransition = function(){
						
						// if the browser supports CSS3 3D and user specified at least one of 3D transitions

						if( lsSupport3D( $(el) ) && $.transit != undefined && ( ls.g.nextLayer.data('transition3d') || ls.g.nextLayer.data('customtransition3d') ) ){

							if( ls.g.nextLayer.data('transition3d') && ls.g.nextLayer.data('customtransition3d') ){
								var rnd = Math.floor(Math.random() * 2);
								var rndT = [['3d',ls.g.nextLayer.data('transition3d')],['custom3d',ls.g.nextLayer.data('customtransition3d')]];
								getTransitionType(rndT[rnd][0],rndT[rnd][1]);
							}else if( ls.g.nextLayer.data('transition3d') ){
								getTransitionType('3d',ls.g.nextLayer.data('transition3d'));
							}else{
								getTransitionType('custom3d',ls.g.nextLayer.data('customtransition3d'));
							}
							
						}else{

							if( ls.g.nextLayer.data('transition2d') && ls.g.nextLayer.data('customtransition2d') ){
								var rnd = Math.floor(Math.random() * 2);
								var rndT = [['2d',ls.g.nextLayer.data('transition2d')],['custom2d',ls.g.nextLayer.data('customtransition2d')]];
								getTransitionType(rndT[rnd][0],rndT[rnd][1]);
							}else if( ls.g.nextLayer.data('transition2d') ){
								getTransitionType('2d',ls.g.nextLayer.data('transition2d'));
							}else if( ls.g.nextLayer.data('customtransition2d') ){
								getTransitionType('custom2d',ls.g.nextLayer.data('customtransition2d'));
							}else{
								getTransitionType('2d','all');								
							}
						}
					};							

					// Choosing layer transition type (2d, 3d, or both)

					var getTransitionType = function(type,transitionlist){

						var tr = type.indexOf('custom') == -1 ? ls.t : ls.ct;
						var tt = '3d', lt, number;

						if( type.indexOf('2d') != -1 ){
							tt = '2d';
						}

						if( transitionlist.indexOf('last') != -1 ){
							number = tr['t'+tt].length-1;
							lt = 'last';
						}else if( transitionlist.indexOf('all') != -1){						
							number = Math.floor(Math.random() * lsCountProp(tr['t'+tt]) );
							lt = 'random from all';
						}else{
							var t = transitionlist.split(',');
							var l = t.length;
							number = parseInt(t[Math.floor(Math.random() * l)])-1;
							lt = 'random from specified';
						}

						layerTransition(tt,tr['t'+tt][number]);

//						$('.test').html('Originals:<br><br>t3D: '+ls.g.nextLayer.data('transition3d')+'<br>t2D: '+ls.g.nextLayer.data('transition2d')+'<br>custom3D: '+ls.g.nextLayer.data('customtransition3d')+'<br>custom2D: '+ls.g.nextLayer.data('customtransition2d')+'<br><br>Support 3D: '+lsSupport3D( $(el) )+'<br><br>Selected transition:<br><br>Type: '+type+' ('+lt+')<br>Number in transition list: '+(number+1)+'<br>Name of the transition: '+tr['t'+tt][number]['name']);
					};

					// The layerTransition function

					var layerTransition = function(type,prop){

						var inner = $(el).find('.ls-inner');

						// sublayersDurationOut - for future usage

						var sublayersDurationOut = 1000;

						// Calculating cols and rows

						var cols = typeof(prop.cols) == 'number' ? prop.cols : Math.floor( Math.random() * ( prop.cols[1] - prop.cols[0] + 1) ) + prop.cols[0];
						var rows = typeof(prop.rows) == 'number' ? prop.rows : Math.floor( Math.random() * ( prop.rows[1] - prop.rows[0] + 1) ) + prop.rows[0];

						if( ( ls.g.isMobile() == true && ls.o.optimizeForMobile == true ) || ( ls.g.ie78 && ls.o.optimizeForIE78 == true ) ){

							// Reducing cols in three steps

							if( cols >= 15 ){
								cols = 7;
							}else if( cols >= 5 ){
								cols = 4;
							}else if( cols >= 4 ){
								cols = 3;
							}else if( cols > 2 ){
								cols = 2;
							}

							// Reducing rows in three steps

							if( rows >= 15 ){
								rows = 7;
							}else if( rows >= 5 ){
								rows = 4;
							}else if( rows >= 4 ){
								rows = 3;
							}else if( rows > 2 ){
								rows = 2;
							}
							
							// Reducing more :)
							
							if( rows > 2 && cols > 2 ){								
								rows = 2;
								if( cols > 4){
									cols = 4;
								}
							}
						}

						var tileWidth = $(el).find('.ls-inner').width() / cols;
						var tileHeight = $(el).find('.ls-inner').height() / rows;

						// Creating HTML markup for layer transitions

						if( !ls.g.ltContainer ){
							ls.g.ltContainer = $('<div>').addClass('ls-lt-container').addClass('ls-overflow-hidden').css({
								width : inner.width(),
								height : inner.height()
							}).prependTo( inner );
						}else{
							ls.g.ltContainer.empty().css({
								width : inner.width(),
								height : inner.height()
							});
						}

						// Setting size

						var restW = inner.width() - Math.floor(tileWidth) * cols;
						var restH = inner.height() - Math.floor(tileHeight) * rows;

						var tileSequence = [];

						for(var ts=0; ts<cols * rows; ts++){
							tileSequence.push(ts);
						}

						// Setting the sequences of the transition

						switch( prop.tile.sequence ){
							case 'reverse':
								tileSequence.reverse();
							break;
							case 'col-forward':
								tileSequence = lsOrderArray(rows,cols,'forward');
							break;
							case 'col-reverse':
								tileSequence = lsOrderArray(rows,cols,'reverse');
							break;
							case 'random':
								tileSequence.randomize();
							break;
						}

						if( type == '3d' ){
							ls.g.totalDuration = sublayersDurationOut + ((cols * rows) - 1) * prop.tile.delay;

							var stepDuration = 0;

							if( prop.before && prop.before.duration ){
								stepDuration += prop.before.duration;
							}
							if( prop.animation && prop.animation.duration ){
								stepDuration += prop.animation.duration;
							}
							if( prop.after && prop.after.duration ){
								stepDuration += prop.after.duration;
							}

							ls.g.totalDuration += stepDuration;

							var stepDelay = 0;

							if( prop.before && prop.before.delay ){
								stepDelay += prop.before.delay;
							}
							if( prop.animation && prop.animation.delay ){
								stepDelay += prop.animation.delay;
							}
							if( prop.after && prop.after.delay ){
								stepDelay += prop.after.delay;
							}

							ls.g.totalDuration += stepDelay;

						}else{
							ls.g.totalDuration = sublayersDurationOut + ((cols * rows) - 1) * prop.tile.delay + prop.transition.duration;
						}

						// Creating cuboids for 3d or tiles for 2d transition (cols * rows)

						for(var tiles=0; tiles < cols * rows; tiles++){

							var rW = tiles%cols == 0 ? restW : 0;
							var rH = tiles > (rows-1)*cols-1 ? restH : 0;

							var tile = $('<div>').addClass('ls-lt-tile').css({
								width : Math.floor(tileWidth) + rW,
								height : Math.floor(tileHeight) + rH
							}).appendTo( ls.g.ltContainer );

							var curTile, nextTile;

							// If current transition is a 3d transition

							if( type == '3d' ){

								tile.addClass('ls-3d-container');

								var W = Math.floor(tileWidth) + rW;
								var H = Math.floor(tileHeight) + rH;
								var D;

								if( prop.animation.direction == 'horizontal' ){
									if( Math.abs(prop.animation.transition.rotateY) > 90 && prop.tile.depth != 'large' ){
										D = Math.floor( W / 10 ) + rW;
									}else{
										D = W;
									}
								}else{
									if( Math.abs(prop.animation.transition.rotateX) > 90 && prop.tile.depth != 'large' ){
										D = Math.floor( H / 10 ) + rH;
									}else{
										D = H;
									}
								}

								var W2 = W/2;
								var H2 = H/2;
								var D2 = D/2;

								// createCuboids function will append cuboids with their style settings to their container

								var createCuboids = function(c,a,w,h,tx,ty,tz,rx,ry){
									$('<div>').addClass(c).css({
										width: w,
										height: h,
										'transform': 'translate3d('+tx+'px, '+ty+'px, '+tz+'px) rotateX('+rx+'deg) rotateY('+ry+'deg) rotateZ(0deg) scale3d(1, 1, 1)',
										'-o-transform': 'translate3d('+tx+'px, '+ty+'px, '+tz+'px) rotateX('+rx+'deg) rotateY('+ry+'deg) rotateZ(0deg) scale3d(1, 1, 1)',
										'-ms-transform': 'translate3d('+tx+'px, '+ty+'px, '+tz+'px) rotateX('+rx+'deg) rotateY('+ry+'deg) rotateZ(0deg) scale3d(1, 1, 1)',
										'-moz-transform': 'translate3d('+tx+'px, '+ty+'px, '+tz+'px) rotateX('+rx+'deg) rotateY('+ry+'deg) rotateZ(0deg) scale3d(1, 1, 1)',
										'-webkit-transform': 'translate3d('+tx+'px, '+ty+'px, '+tz+'px) rotateX('+rx+'deg) rotateY('+ry+'deg) rotateZ(0deg) scale3d(1, 1, 1)'
									}).appendTo(a);
								};

								createCuboids('ls-3d-box',tile,0,0,0,0,-D2,0,0);

								var backRotX = 0
								var topRotX = 0
								var bottomRotX = 0

								if( prop.animation.direction == 'vertical' && Math.abs(prop.animation.transition.rotateX) > 90){
									createCuboids('ls-3d-back',tile.find('.ls-3d-box'),W,H,-W2,-H2,-D2,180,0);
								}else{
									createCuboids('ls-3d-back',tile.find('.ls-3d-box'),W,H,-W2,-H2,-D2,0,180);								
								}

								createCuboids('ls-3d-bottom',tile.find('.ls-3d-box'),W,D,-W2,H2-D2,0,-90,0);
								createCuboids('ls-3d-top',tile.find('.ls-3d-box'),W,D,-W2,-H2-D2,0,90,0);
								createCuboids('ls-3d-front',tile.find('.ls-3d-box'),W,H,-W2,-H2,D2,0,0);
								createCuboids('ls-3d-left',tile.find('.ls-3d-box'),D,H,-W2-D2,-H2,0,0,-90);
								createCuboids('ls-3d-right',tile.find('.ls-3d-box'),D,H,W2-D2,-H2,0,0,90);

								curTile = tile.find('.ls-3d-front');

								if( prop.animation.direction == 'horizontal' ){
									if( Math.abs(prop.animation.transition.rotateY) > 90 ){
										nextTile = tile.find('.ls-3d-back');
									}else{
										nextTile = tile.find('.ls-3d-left, .ls-3d-right');
									}
								}else{
									if( Math.abs(prop.animation.transition.rotateX) > 90 ){
										nextTile = tile.find('.ls-3d-back');
									}else{
										nextTile = tile.find('.ls-3d-top, .ls-3d-bottom');
									}
								}

								// Animating cuboids

								var curCubDelay = sublayersDurationOut + tileSequence[tiles] * prop.tile.delay;

								var curCub = ls.g.ltContainer.find('.ls-3d-container:eq('+tiles+') .ls-3d-box');

								if( prop.before && prop.before.transition ){
									prop.before.transition.delay = prop.before.transition.delay ? prop.before.transition.delay + curCubDelay : curCubDelay;
									curCub.transition( prop.before.transition, prop.before.duration, prop.before.easing );
								}else{
									prop.animation.transition.delay = prop.animation.transition.delay ? prop.animation.transition.delay + curCubDelay : curCubDelay;
								}

								curCub.transition( prop.animation.transition, prop.animation.duration, prop.animation.easing )

								if( prop.after ){
									curCub.transition( $.extend({},{ scale3d : 1 }, prop.after.transition), prop.after.duration, prop.after.easing );
								}
								
							}else{

								// If current transition is a 2d transition

								var T1 = L1 = T2 = L2 = 'auto';
								var O1 = O2 = 1;

								if( prop.transition.direction == 'random' ){
									var dir = ['top','bottom','right','left'];
									var direction = dir[Math.floor(Math.random() * dir.length )];
								}else{
									var direction = prop.transition.direction;
								}

								// Selecting direction

								switch( direction ){
									case 'top':
										T1 = T2 = -tile.height();
										L1 = L2 = 0;
									break;
									case 'bottom':
										T1 = T2 = tile.height();
										L1 = L2 = 0;
									break;
									case 'left':
										T1 = T2 = 0;
										L1 = L2 = -tile.width();
									break;
									case 'right':
										T1 = T2 = 0;
										L1 = L2 = tile.width();
									break;
									case 'topleft':
										T1 = tile.height();
										T2 = 0;
										L1 = tile.width(); 
										L2 = 0;
									break;
									case 'topright':
										T1 = tile.height();
										T2 = 0;
										L1 = - tile.width(); 
										L2 = 0;
									break;
									case 'bottomleft':
										T1 = - tile.height();
										T2 = 0;
										L1 = tile.width(); 
										L2 = 0;
									break;
									case 'bottomright':
										T1 = - tile.height();
										T2 = 0;
										L1 = - tile.width(); 
										L2 = 0;
									break;
								}

								// Selecting the type of the transition

								if( !ls.g.ie78 || ( ls.g.ie78 && !ls.o.optimizeForIE78 ) || ( ls.g.ie78 && ls.o.optimizeForIE78 == true && prop.name.toLowerCase().indexOf('crossfade') != -1 ) ){
									switch( prop.transition.type ){
										case 'fade':
											T1 = T2 = L1 = L2 = 0;
											O1 = 0;
											O2 = 1;
										break;
										case 'mixed':
											O1 = 0;
											O2 = 1;
											T2 = L2 = 0;
										break;
									}									
								}

								curTile = $('<div>').addClass('ls-curtile').appendTo( tile );

								nextTile = $('<div>').addClass('ls-nexttile').appendTo( tile ).css({
									top : -T1,
									left : -L1,
									dispay : 'block',
									opacity : O1
								});

								// Animating tiles

								var curTileDelay = sublayersDurationOut + tileSequence[tiles] * prop.tile.delay;

								if( ls.g.cssTransitions && $.transit != undefined ){
									nextTile.transition({
										delay : curTileDelay,
										top : 0,
										left : 0,
										opacity : O2
									}, prop.transition.duration, prop.transition.easing );
									curTile.transition({
										delay : curTileDelay,
										top : T2,
										left : L2
									}, prop.transition.duration, prop.transition.easing );								
								}else{
									nextTile.delay( curTileDelay ).animate({
										top : 0,
										left : 0,
										opacity : O2
									}, prop.transition.duration, prop.transition.easing );
									curTile.delay( curTileDelay ).animate({
										top : T2,
										left : L2
									}, prop.transition.duration, prop.transition.easing );								
								}
							}

							// Appending the background images of current and next layers into the tiles on both of 2d & 3d transitions

							var curBG = ls.g.curLayer.find('.ls-bg');
							if( curBG.length ){
								curTile.append($('<img>').attr('src', curBG.attr('src')).css({
									width : curBG[0].style.width,
									height : curBG[0].style.height,
									marginLeft : inner.width() / 2 + parseFloat(curBG.css('margin-left')) - parseInt(tile.position().left),
									marginTop : inner.height() / 2 + parseFloat(curBG.css('margin-top')) - parseInt(tile.position().top)
								}));
							}

							var nextBG = ls.g.nextLayer.find('.ls-bg');
							if( nextBG.length ){
								nextTile.append($('<img>').attr('src', nextBG.attr('src') ).css({
									width : nextBG[0].style.width,
									height : nextBG[0].style.height,
									marginLeft : inner.width() / 2 + parseFloat(nextBG.css('margin-left')) - parseInt(tile.position().left),
									marginTop : inner.height() / 2 + parseFloat(nextBG.css('margin-top')) - parseInt(tile.position().top)
								}));
							}
						}

						// Storing current and next layer elements in a local variable (needed by setTimeout functions in some cases)
						
						var curLayer = ls.g.curLayer;
						var nextLayer = ls.g.nextLayer;

						// Hiding the background image of the next layer (immediately)

						nextLayer.find('.ls-bg').css({
							visibility : 'hidden'
						});
						
						// Hiding controls and yourLogo during 3D transitions if needed

						if( type == '3d' && ls.g.isHideOn3D($(el)) ){
							ls.g.forceHideControls = true;
							if( ls.g.bottomWrapper ){
								ls.g.bottomWrapper.stop(true,true).fadeOut(300);								
							}
							if( ls.g.yourLogo && ls.o.hideYourLogo ){
								ls.g.yourLogo.stop(true,true).fadeOut(500);
							}
						}

						// Hiding fullscreen button during 3D transitions

						if( type == '3d' ){
							$(el).find('.ls-fullscreen').stop(true,true).fadeOut(300);							
						}
						
						// Sliding out the sublayers of the current layer 
						// (immediately, delay out and duration out properties are not applied to the sublayers during the new layer transitions)
						
						curSubLayers(sublayersDurationOut);

						// Hiding current layer after its sublayers animated out

						setTimeout(function(){

							curLayer.css({
								width: 0
							});

							ls.g.ltContainer.removeClass('ls-overflow-hidden');
							
							// Hiding shadow during 3d transitions if needed
			
							if( ls.g.shadow && type == '3d' && ls.g.isHideOn3D($(el)) ){
								ls.g.shadow.fadeOut( 250 );									
							}

						},sublayersDurationOut );

						// Calculating next layer delay

						var nextLayerTimeShift = parseInt(nextLayer.data('timeshift')) ? parseInt(nextLayer.data('timeshift')) : 0;
						var nextLayerDelay = ls.g.totalDuration + nextLayerTimeShift > 0 ? ls.g.totalDuration + nextLayerTimeShift : 0;

						// Showing next layer and sliding sublayers of the next layer in after the current layer transition ended

						setTimeout(function(){
							
							// Sliding in / fading in the sublayers of the next layer

							nextSubLayers();

							// Displaying the next layer (immediately)

							nextLayer.css({
								width : ls.g.sliderWidth(),
								height : ls.g.sliderHeight()
							});
						}, nextLayerDelay );

						// Changing visibility to visible of the background image of the next layer and overflow to hidden of .ls-lt-container after the transition and calling callback function

						setTimeout(function(){

							ls.g.ltContainer.addClass('ls-overflow-hidden');

							nextLayer.addClass('ls-active');

							if( nextLayer.find('.ls-bg').length ){

								nextLayer.find('.ls-bg').css({
									display : 'none',
									visibility : 'visible'
								});
								if( ls.g.ie78 ){
									nextLayer.find('.ls-bg').css('display','block');
									setTimeout(function(){
										curLayerCallback();										
									},500);
								}else{
									nextLayer.find('.ls-bg').fadeIn(500, function(){
										curLayerCallback();
									});
								}
							}else{
								curLayerCallback();								
							}

							// Showing controls after 3D transitions

							if( type == '3d' && ls.g.isHideOn3D($(el)) ){
								ls.g.forceHideControls = false;							
								// $(el).find('.ls-nav-prev, .ls-nav-next').stop(true,true).fadeIn(300);
								if( ls.g.bottomWrapper ){
									ls.g.bottomWrapper.stop(true,true).fadeIn(300);
								}
								if( ls.g.yourLogo && ls.o.hideYourLogo ){
									ls.g.yourLogo.stop(true,true).fadeIn(500);
								}
							}

						}, ls.g.totalDuration );

						// Showing shadow after 3d transitions

						if( ls.g.shadow && type == '3d' && ls.g.isHideOn3D($(el)) ){
							setTimeout(function(){
								ls.g.shadow.fadeIn( 250 );
							}, ls.g.totalDuration - 125 );
						}
					};



			/* Selecting and running the transition */

					transitionType = ( ( ls.g.nextLayer.data('transition3d') || ls.g.nextLayer.data('transition2d') ) && ls.t ) || ( ( ls.g.nextLayer.data('customtransition3d') || ls.g.nextLayer.data('customtransition2d') ) && ls.ct ) ? 'new' : 'old';

					if( ls.o.animateFirstLayer && !ls.g.firstLayerAnimated ){

						// BUGFIX v3.5 there is no need to animate 'current' layer if the following conditions are true
						//			   this fixes the sublayer animation direction bug

						if( ls.g.layersNum == 1 ){
							var curDelay = 0;
							
							// IMPROVEMENT v4.1.0 Calling cbAnimStop(); function if only one layer is in the slider

							ls.o.cbAnimStop(ls.g);
							
						}else{
							var nextLayerTimeShift = parseInt(ls.g.nextLayer.data('timeshift')) ? parseInt(ls.g.nextLayer.data('timeshift')) : 0;
							var d = transitionType == 'new' ? 0 : curDuration;
							setTimeout(function(){
								curLayerCallback();
							}, d + Math.abs(nextLayerTimeShift) );
						}
						
						// curDelay must be 0!

						ls.g.totalDuration = true;			

						// Animating SUBLAYERS of the first layer

						nextSubLayers();							

						// Displaying the first layer (immediately)

						ls.g.nextLayer.css({
							width : ls.g.sliderWidth(),
							height : ls.g.sliderHeight()
						});

						if( !ls.g.ie78 ){
							ls.g.nextLayer.find('.ls-bg').css({
								display : 'none'
							}).fadeIn(500);							
						}

						ls.g.firstLayerAnimated = true;
						ls.g.isLoading = false;
					}else{						

						switch(transitionType){

							// Old transitions (sliding layers)

							case 'old':

								ls.g.totalDuration = false;

								// Animating CURRENT LAYER and its SUBLAYERS

								curLayer();
								curSubLayers();

								// Animating NEXT LAYER and its SUBLAYERS

								nextLayer();
								nextSubLayers();							
							break;

							// NEW FEATURE v4.0 2D & 3D Layer Transitions

							case 'new':

								selectTransition();							
							break;
						}
					}
		};

		ls.sublayerShowUntil = function( sublayer ){
			
			var prevOrNext = ls.g.curLayer;

			if( ls.g.prevNext != 'prev' && ls.g.nextLayer ){
				prevOrNext = ls.g.nextLayer;
			}

			var chooseDirection = prevOrNext.data('slidedirection') ? prevOrNext.data('slidedirection') : ls.o.slideDirection;

			// Setting the direction of sliding

			var slideDirection = ls.g.slideDirections[ls.g.prevNext][chooseDirection];

			var curSubSlideDir = sublayer.data('slidedirection') ? sublayer.data('slidedirection') : slideDirection;
			var lml, lmt;

			switch(curSubSlideDir){
				case 'left':
					lml = -ls.g.sliderWidth();
					lmt = 0;
					break;
				case 'right':
					lml = ls.g.sliderWidth();
					lmt = 0;
					break;
				case 'top':
					lmt = -ls.g.sliderHeight();
					lml = 0;
					break;
				case 'bottom':
					lmt = ls.g.sliderHeight();
					lml = 0;
					break;
			}

			var curSubSlideOutDir = sublayer.data('slideoutdirection') ? sublayer.data('slideoutdirection') : false;

			switch(curSubSlideOutDir){
				case 'left':
					lml = ls.g.sliderWidth();
					lmt = 0;
					break;
				case 'right':
					lml = -ls.g.sliderWidth();
					lmt = 0;
					break;
				case 'top':
					lmt = ls.g.sliderHeight();
					lml = 0;
					break;
				case 'bottom':
					lmt = -ls.g.sliderHeight();
					lml = 0;
					break;
			}

			// IMPROVEMENT v4.0 Distance (P.level): -1

			var curSubPLevel = parseInt( sublayer.attr('class').split('ls-s')[1] );
			
			if( curSubPLevel == -1 ){
				var endLeft = parseInt( sublayer.css('left') );
				var endTop = parseInt( sublayer.css('top') );
				if( lmt < 0 ){
					lmt = - ( ls.g.sliderHeight() - endTop );
				}else if( lmt > 0 ){
					lmt = endTop + sublayer.outerHeight();
				}
				if( lml < 0 ){
					lml = - ( ls.g.sliderWidth() - endLeft );
				}else if( lml > 0 ){
					lml = endLeft + sublayer.outerWidth();
				}
				var curSubPar = 1;
			}else{
				var curSubParMod = ls.g.curLayer.data('parallaxout') ? parseInt(ls.g.curLayer.data('parallaxout')) : ls.o.parallaxOut;
				var curSubPar = curSubPLevel * curSubParMod;
			}
			
			var curSubDelay = parseInt( sublayer.data('showuntil') );

			var curSubTime = sublayer.data('durationout') ? parseInt(sublayer.data('durationout')) : ls.o.durationOut;
			var curSubEasing = sublayer.data('easingout') ? sublayer.data('easingout') : ls.o.easingOut;

			if( curSubSlideOutDir == 'fade' || ( !curSubSlideOutDir && curSubSlideDir == 'fade' )){
				
				// iOS fade bug when GPU acceleration is enabled #5

				if( ls.g.isMobile() == true && lsBrowser().webkit ){
					sublayer.delay( curSubDelay ).fadeTo(curSubTime, 0, curSubEasing);
				}else{
					sublayer.delay( curSubDelay ).fadeOut(curSubTime, curSubEasing);
				}
			}else{
				
				sublayer.delay( curSubDelay ).animate({
					marginLeft : -lml * curSubPar,
					marginTop : -lmt * curSubPar
				}, curSubTime, curSubEasing);
			}
		};

		// v3.6 Improved Debug Mode

		ls.debug = function(){
			
			ls.d = {				
				history : $('<div>'),
				// adds a H1 (title)
				aT : function(content){
					$('<h1>'+content+'</h1>').appendTo( ls.d.history );
				},
				// adds an empty UL
				aeU : function(){
					$('<ul>').appendTo( ls.d.history );
				},
				// adds an UL with a LI
				aU : function(content){
					$('<ul><li>'+content+'</li></ul>').appendTo( ls.d.history );
				},
				// adds a LI into the last UL
				aL : function(content){
					$('<li>'+content+'</li>').appendTo( ls.d.history.find('ul:last') );
				},
				// adds an UL into the last LI of the last UL
				aUU : function(content){
					$('<ul>').appendTo( ls.d.history.find('ul:last li:last') );
				},
				// adds a Function to the first LI inside the last UL
				aF : function(elem){
					ls.d.history.find('ul:last li:last').hover(
						function(){
							elem.css({
								border: '2px solid red',
								marginTop : parseInt( elem.css('margin-top') ) - 2,
								marginLeft : parseInt( elem.css('margin-left') ) - 2
							});
						},
						function(){
							elem.css({
								border: '0px',
								marginTop : parseInt( elem.css('margin-top') ) + 2,
								marginLeft : parseInt( elem.css('margin-left') ) + 2
							});
						}
					);
				},
				show : function(){
					if( !$('body').find('.ls-debug-console').length ){
						var dc = $('<div>').addClass('ls-debug-console').css({
							position: 'fixed',
							zIndex: '10000000000',
							top: '10px',
							right: '10px',
							width: '300px',
							padding: '20px',
							background: 'black',
							'border-radius': '10px',
							height: $(window).height() - 60,
							opacity: 0,
							marginRight: 150
						}).appendTo( $('body') ).animate({
							marginRight: 0,
							opacity: .9
						}, 600, 'easeInOutQuad').click(function(e){
							if(e.shiftKey && e.altKey){
								$(this).animate({
									marginRight: 150,
									opacity: 0
								}, 600, 'easeInOutQuad', function(){
									$(this).remove();
								});
							}							
						});
						var ds = $('<div>').css({
							width: '100%',
							height: '100%',
							overflow: 'auto'
						}).appendTo( dc );
						var dd = $('<div>').css({
							width: '100%'
						}).appendTo( ds ).append( ls.d.history );						
					}
				},
				hide : function(){
					$('body').find('.ls-debug-console').remove();
				}
			};
			
			$(el).click(function(e){
				if(e.shiftKey && e.altKey){
					ls.d.show();
				}
			});
		};

		// initializing
		ls.load();
	};

	// Support3D checks the CSS3 3D capability of the browser (based on the idea of Modernizr.js)

	var lsSupport3D = function( el ) {
		
		var testEl = $('<div>'),
			s3d1 = false,
			s3d2 = false,
			properties = ['perspective', 'OPerspective', 'msPerspective', 'MozPerspective', 'WebkitPerspective'];
			transform = ['transformStyle','OTransformStyle','msTransformStyle','MozTransformStyle','WebkitTransformStyle'];

		for (var i = properties.length - 1; i >= 0; i--){
			s3d1 = s3d1 ? s3d1 : testEl[0].style[properties[i]] != undefined;
		};
		
		// preserve 3D test
		
		for (var i = transform.length - 1; i >= 0; i--){
			testEl.css( 'transform-style', 'preserve-3d' );
			s3d2 = s3d2 ? s3d2 : testEl[0].style[transform[i]] == 'preserve-3d';
		};

		// If browser has perspective capability and it is webkit, we must check it with this solution because Chrome can give false positive result if GPU acceleration is disabled

        if (s3d1 && testEl[0].style[properties[4]] != undefined){
			testEl.attr('id','ls-test3d').appendTo( el );
            s3d1 = testEl[0].offsetHeight === 3 && testEl[0].offsetLeft === 9;
			testEl.remove();
        }

        return (s3d1 && s3d2);
	};

	// Order array function

	var lsOrderArray = function(x,y,dir) {
		var i = [];
		if(dir=='forward'){
			for( var a=0; a<x;a++){
				for( var b=0; b<y; b++){
					i.push(a+b*x);	
				}
			}
		}else{
			for( var a=x-1; a>-1;a--){
				for( var b=y-1; b>-1; b--){
					i.push(a+b*x);
				}
			}
		}
		return i;
	};

	// Randomize array function

	Array.prototype.randomize = function() {
	  var i = this.length, j, tempi, tempj;
	  if ( i == 0 ) return false;
	  while ( --i ) {
	     j       = Math.floor( Math.random() * ( i + 1 ) );
	     tempi   = this[i];
	     tempj   = this[j];
	     this[i] = tempj;
	     this[j] = tempi;
	  }
	  return this;
	}

	// CountProp counts the properties in an object

	var lsCountProp = function(obj) {
	    var count = 0;

	    for(var prop in obj) {
	        if(obj.hasOwnProperty(prop)){
	            ++count;
			}
	    }
	    return count;
	};
	
	// We need the browser function (removed from jQuery 1.9)

	var lsBrowser = function(){

		uaMatch = function( ua ) {
			ua = ua.toLowerCase();

			var match = /(chrome)[ \/]([\w.]+)/.exec( ua ) ||
				/(webkit)[ \/]([\w.]+)/.exec( ua ) ||
				/(opera)(?:.*version|)[ \/]([\w.]+)/.exec( ua ) ||
				/(msie) ([\w.]+)/.exec( ua ) ||
				ua.indexOf("compatible") < 0 && /(mozilla)(?:.*? rv:([\w.]+)|)/.exec( ua ) ||
				[];

			return {
				browser: match[ 1 ] || "",
				version: match[ 2 ] || "0"
			};
		};

		var matched = uaMatch( navigator.userAgent ), browser = {};

		if ( matched.browser ) {
			browser[ matched.browser ] = true;
			browser.version = matched.version;
		}

		if ( browser.chrome ) {
			browser.webkit = true;
		} else if ( browser.webkit ) {
			browser.safari = true;
		}
		return browser;			
	};
	
	lsPrefixes = function(obj, method){

		var pfx = ['webkit', 'khtml', 'moz', 'ms', 'o', ''];
		var p = 0, m, t;
		while (p < pfx.length && !obj[m]) {
			m = method;
			if (pfx[p] == '') {
				m = m.substr(0,1).toLowerCase() + m.substr(1);
			}
			m = pfx[p] + m;
			t = typeof obj[m];
			if (t != 'undefined') {
				pfx = [pfx[p]];
				return (t == 'function' ? obj[m]() : obj[m]);
			}
			p++;
		}		
	};

	layerSlider.global = {
		
		// Global parameters (Do not change these settings!)

		version				: '4.1.0',
		
		isMobile			: function(){
								if( navigator.userAgent.match(/Android/i) || navigator.userAgent.match(/webOS/i) || navigator.userAgent.match(/iPhone/i) || navigator.userAgent.match(/iPad/i) || navigator.userAgent.match(/iPod/i) || navigator.userAgent.match(/BlackBerry/i) || navigator.userAgent.match(/Windows Phone/i) ){
									return true;
								}else{
									return false;
								}
							},
		isHideOn3D			: function(el){
								if( el.css('padding-bottom') == 'auto' || el.css('padding-bottom') == 'none' || el.css('padding-bottom') == 0 || el.css('padding-bottom') == '0px' ){
									return true;
								}else{
									return false;									
								}
							},

		// NEW FEATURE 4.0 CSS3 transitions
		//				   (beta, currently animating only the new 2D and 3D layer tranisitons with CSS3)
		//				   (2D layer transitions are working also with jQuery fallback mode)

		cssTransitions		: !lsBrowser().msie || ( lsBrowser().msie && lsBrowser().version > 9 ) ? true : false,
		ie78				: lsBrowser().msie && lsBrowser().version < 9 ? true : false,
		normalWidth			: false,
		normalHeight		: false,
		normalRatio			: false,
		goingNormal			: false,
		paused				: false,
		pausedByVideo		: false,
		autoSlideshow		: false,
		isAnimating			: false,
		layersNum			: null,
		prevNext			: 'next',
		slideTimer			: null,
		sliderWidth			: null,
		sliderHeight		: null,
		slideDirections		: {
								prev : {
									left	: 'right',
									right	: 'left',
									top		: 'bottom',
									bottom	: 'top'
								},
								next : {
									left	: 'left',
									right	: 'right',
									top		: 'top',
									bottom	: 'bottom'
								}
							},

		// Default delay time, fadeout and fadein durations of videoPreview images

		v					: {
								d	: 500,
								fo	: 750,
								fi	: 500	
							}
	};

	layerSlider.options = {
		
		// User settings (can be modified)
		
		autoStart			: true,						// If true, slideshow will automatically start after loading the page.
		firstLayer			: 1,						// LayerSlider will begin with this layer. Use the word 'random' to start with a random layer.
		twoWaySlideshow		: true, 					// If true, slideshow will go backwards if you click the prev button.
		keybNav				: true,						// Keyboard navigation. You can navigate with the left and right arrow keys.
		imgPreload			: true,						// Image preload. Preloads all images and background-images of the next layer.
		navPrevNext			: true,						// If false, Prev and Next buttons will be invisible.
		navStartStop		: true,						// If false, Start and Stop buttons will be invisible.
		navButtons			: true,						// If false, slide buttons will be invisible.
		skin				: 'glass',					// You can change the skin of the Slider, use 'noskin' to hide skin and buttons. (Pre-defined skins are: 'deafultskin', 'lightskin', 'darkskin', 'glass' and 'minimal'.)
		skinsPath			: '/layerslider/skins/',	// You can change the default path of the skins folder. Note, that you must use the slash at the end of the path.
		pauseOnHover		: true,						// SlideShow will pause when mouse pointer is over LayerSlider.

		// NEW FEATURES v1.6 optional globalBGColor & globalBGImage

		globalBGColor		: 'transparent',			// Background color of LayerSlider. You can use all CSS methods, like hexa colors, rgb(r,g,b) method, color names, etc. Note, that background sublayers are covering the background.
		globalBGImage		: false,					// Background image of LayerSlider. This will be a fixed background image of LayerSlider by default. Note, that background sublayers are covering the global background image.

		// NEW FEATURES v1.7 animateFirstLayer, yourLogo & yourLogoStyle

		animateFirstLayer	: true,						// If true, first layer will animate (slide in) instead of fading
		yourLogo			: false,					// This is a fixed image that will be shown above of LayerSlider container. For example if you want to display your own logo, etc. You have to add the correct path to your image file.
		yourLogoStyle		: 'left: -10px; top: -10px;', // You can style your logo. You are allowed to use any CSS properties, for example add left and top properties to place the image inside the LayerSlider container anywhere you want.

		// NEW FEATURES v1.8 yourLogoLink & yourLogoTarget
		
		yourLogoLink		: false,					// You can add a link to your logo. Set false is you want to display only an image without a link.
		yourLogoTarget		: '_blank',					// If '_blank', the clicked url will open in a new window.

		// NEW FEATURES v2.0 touchNav, loops, forceLoopNum, autoPlayVideos, autoPauseSlideshow & youtubePreview
		
		touchNav			: true,						// Touch-control (on mobile devices)
		loops				: 0,						// Number of loops if autoStart set true (0 means infinite!)
		forceLoopNum		: true,						// If true, the slider will always stop at the given number of loops even if the user restarts the slideshow
		autoPlayVideos		: true,						// If true, slider will autoplay youtube / vimeo videos - you can use it with autoPauseSlideshow
		autoPauseSlideshow	: 'auto',					// 'auto', true or false. 'auto' means, if autoPlayVideos is set to true, slideshow will stop UNTIL the video is playing and after that it continues. True means slideshow will stop and it won't continue after video is played.
		youtubePreview		: 'maxresdefault.jpg',		// Default thumbnail picture of YouTube videos. Can be 'maxresdefault.jpg', 'hqdefault.jpg', 'mqdefault.jpg' or 'default.jpg'. Note, that 'maxresdefault.jpg' os not available to all (not HD) videos.

		// NEW FEATURE v3.0 responsive
		
		responsive			: true,						// Responsive mode with smart-resizing feature

		// NEW FEATURES v3.5 responsiveUnder, randomSlideshow, sublayerContainer, thumbnailMode

		randomSlideshow		: false,					// If true, LayerSlider will change to a random layer instead of changing to the next / prev layer. Note that 'loops' feature won't work with randomSlideshow!
		responsiveUnder		: 0,						// You can force the slider to change automatically into responsive mode but only if the slider width is smaller than responsiveUnder pixels. It can be used if you need a full-width slider with fixed height but you also need it to be responsive if the browser is smaller... Important! If you enter a value higher than 0, the normal responsive mode will be switched off automatically!
		sublayerContainer	: 0,						// This feature is needed if you are using a full-width slider and you need that your sublayers forced to positioning inside a centered custom width container. Just specify the width of this container in pixels! Note, that this feature is working only with pixel-positioned sublayers, but of course if you add left: 50% position to a sublayer it will be positioned horizontally to the center, as before!
		thumbnailNavigation	: 'hover',					// Thumbnail navigation mode. Can be 'disabled', 'hover', 'always'. Note, that 'hover' setting needs navButtons true!
		tnWidth				: 100,						// Width of the thumbnails (in pixels).
		tnHeight			: 60,						// Height of the thumbnails (in pixels).
		tnContainerWidth	: '60%',					// Default width of the thumbnail container.
		tnActiveOpacity		: 35,						// Opacity of the active thumbnail (0-100).
		tnInactiveOpacity	: 100,						// Opacity of the active thumbnail (0-100).
		hoverPrevNext		: true,						// If true, the prev and next buttons will be shown only if you move your mouse over the slider.
		hoverBottomNav		: false,					// If true, the bottom navigation controls (with also thumbnails) will be shown only if you move your mouse over the slider.
		
		// NEW FEATURES optimizeForMobile, optimizeForIE78, hideYourLogo
		
		optimizeForMobile	: true,						// If true and the slider is animating with one of the new layer transitions and the user is viewing the slider on mobile / tablet, the rows and cols of the transition will be maximized for better performance.
		optimizeForIE78		: true,						// If true and the slider is animating with one of the new layer transitions and the user is viewing the slider on IE7 / 8, the rows and cols of the transition will be maximized and slide will be used instead of mixed and fade transitions for better performance.
		hideYourLogo		: false,					// If true and the slider is animating with a 3D transition and the slider has borderless skin, yourLogo will be hidden during the transition

		// NEW FEATURE allowFullScreenMode (beta, do not use it!)

		allowFullScreenMode : false,					// If true and you click on the full screen icon, the slider will go to full screen mode in modern browsers
		
		// LayerSlider API callback functions

		cbInit				: function(element){},		// Calling when LayerSlider loads, returns the LayerSlider jQuery object of the LayerSlider container HTML element.
		cbStart				: function(data){},			// Calling when you click the slideshow start button, returns the LayerSlider Data object.
		cbStop				: function(data){},			// Calling when click the slideshow stop / pause button, returns the LayerSlider Data object.
		cbPause				: function(data){},			// Calling when slideshow pauses (if pauseOnHover is true), returns the LayerSlider Data object.
		cbAnimStart			: function(data){},			// Calling when animation starts, returns the LayerSlider Data object.
		cbAnimStop			: function(data){},			// Calling when the animation of current layer ends, but the sublayers of this layer still may be animating, returns the LayerSlider Data object.
		cbPrev				: function(data){},			// Calling when you click the previous button (or if you use keyboard or touch navigation), returns the LayerSlider Data object.
		cbNext				: function(data){},			// Calling when you click the next button (or if you use keyboard or touch navigation), returns the LayerSlider Data object.

		// The following global settings can be override separately by each layers and / or sublayers local settings (see the documentation for more information).
		
		slideDirection		: 'right',					// Slide direction. New layers will sliding FROM(!) this direction.
		slideDelay			: 4000,						// Time before the next slide will be loading.
		parallaxIn			: .45,						// Modifies the parallax-effect of the slide-in animation.
		parallaxOut			: .45,						// Modifies the parallax-effect of the slide-out animation.
		durationIn			: 1500,						// Duration of the slide-in animation.
		durationOut			: 1500,						// Duration of the slide-out animation.
		easingIn			: 'easeInOutQuart',			// Easing (type of transition) of the slide-in animation.
		easingOut			: 'easeInOutQuart',			// Easing (type of transition) of the slide-out animation.
		delayIn				: 0,						// Delay time of the slide-in animation.
		delayOut			: 0							// Delay time of the slide-out animation.
	};

})(jQuery);