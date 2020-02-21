(function() {

    var mainContainer = document.querySelector('.view'),
        gridEl = mainContainer.querySelector('.grid'),
        gridItems = [].slice.call(gridEl.querySelectorAll('.grid__item')),
        titleEl = mainContainer.querySelector('.title-wrap > .title--main'),
        subtitleEl = mainContainer.querySelector('.title-wrap > .title--sub'),
        pagemover = mainContainer.querySelector('.page--mover'),
        winsize = {width: window.innerWidth, height: window.innerHeight},
        introPositions = [
            // translation values: 
                // tx and ty: percentages of the item´s width and height
            // s: scale, r: rotation (z) value
            {tx: -1.1, ty:-.7, s:1.6, r:-22},
			{tx: 0, ty:-1.1, s:1.4, r:2},
			{tx: .7, ty:-.7, s:1.55, r:15},
			{tx: -.6, ty:-.45, s:1.4, r:-25},
			{tx: -.3, ty:-.5, s:1.1, r:-18},
			{tx: .95, ty:-.3, s:1.2, r:25}
        ],
        deviceEl = mainContainer.querySelector('.device'),
        showGridCtrl = document.getElementById('showgrid'),
        pageTitleEl = mainContainer.querySelector('.page__title > .page__title-main'),
        pageSubTitleEl = mainContainer.querySelector('.page__title > .page__title-sub'),
        isAnimating,
        scrolled,
        view = 'stack';

console.log(gridItems)
        // Initializing
        function init() {
            document.body.classList.add("overflow");
            mainContainer.classList.add('view--loaded');
                showIntro();
                //initEvents();
            
        }

function showIntro() {
	// display the first set of 6 grid items behind the phone
	gridItems.slice(0,6).forEach(function(item, pos) {
		// positioning each of the 6 items on the bottom of the page 
		// (item´s center is positioned on the middle of the page bottom)
		// then we move them up and to the sides (extra values) 
		// and also apply a scale and rotation
		var itemOffset = item.getBoundingClientRect(),
			settings = introPositions[pos],
			center = {
				x : winsize.width/2 - (itemOffset.left + item.offsetWidth/2),
				y : winsize.height - (itemOffset.top + item.offsetHeight/2)
			}

		// first position the items behind the phone
		dynamics.css(item, {
			opacity: 1,
			translateX: center.x,
			translateY: center.y,
			scale: 0.5
		});

		// animation for each item to their final position
		dynamics.animate(item, {
			translateX: center.x + settings.tx*item.offsetWidth,
			translateY: center.y + settings.ty*item.offsetWidth,
			scale : settings.s,
			rotateZ: settings.r
		}, {
            type: dynamics.spring,
            frequency: 150,
            friction: 300,
			duration: 1000,
			delay: pos * 80
		});
	});

	// animation (sliding) the phone in:
	    // first, push it slightly down; to make it disappear completely below the viewport
    	// for that we need to set the translateY to winsize.height * 0.45 --> 45vh)
	dynamics.css(deviceEl, { translateY: winsize.height * 0.35 } );
	// then animate it up
	dynamics.animate(deviceEl, { translateY: 0 }, {
		type: dynamics.bezier,
		points: [{"x":0,"y":0,"cp":[{"x":0.2,"y":1}]},{"x":1,"y":1,"cp":[{"x":0.3,"y":1}]}],
		duration: 1000
	});
}

    init();

/*end of IIFE*/
})();