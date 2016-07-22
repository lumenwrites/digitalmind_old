/**
*	Site-specific configuration settings for Highslide JS
*/
hs.graphicsDir = 'highslide/graphics/';
hs.showCredits = false;
hs.outlineType = null;
hs.dimmingOpacity = 0.75;
hs.fadeInOut = true;
hs.align = 'center';
hs.marginBottom = 105;


// Add the slideshow controller
hs.addSlideshow({
	slideshowGroup: 'group1',
	interval: 5000,
	repeat: false,
	useControls: false,
	thumbstrip: {
		mode: 'horizontal',
		position: 'bottom center',
		relativeTo: 'viewport'
	}

});

// gallery config object
var config1 = {
	slideshowGroup: 'group1',
	transitions: ['expand', 'crossfade']
};
