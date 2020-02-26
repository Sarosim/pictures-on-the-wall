(function() {

    var mainContainer = document.querySelector('.view'),
        gridEl = mainContainer.querySelector('.grid'),
        gridItems = [].slice.call(gridEl.querySelectorAll('.grid__item')),
        titleEl = mainContainer.querySelector('.title-wrap > .title--main'),
        subtitleElements = [].slice.call(mainContainer.querySelectorAll('.title-wrap > .title--sub')),
        pagemover = mainContainer.querySelector('.page--mover'),
        winsize = {width: window.innerWidth, height: window.innerHeight},
        introPositions = [
            // translation values: 
                // tx and ty: percentages of the item´s width and height
            // s: scale, r: rotation (z) value
            {tx: -1.1, ty:-.6, s:1.5, r:-32}, // Animals category
			{tx: 0, ty:-0.9, s:1.4, r:-4}, // Abstract category
			{tx: .7, ty:-.7, s:1.55, r:15}, // Architecture category
			{tx: -.6, ty:-.45, s:1.4, r:-25}, // Food category
			{tx: -.3, ty:-.5, s:1.1, r:-18}, // Flowers category
			{tx: .85, ty:-.3, s:1.2, r:35} // Painting category
        ],
        deviceEl = mainContainer.querySelector('.device'),
        showGridButton = document.getElementById('showgrid'),
        pageTitleElement = mainContainer.querySelector('.page__title > .page__title-main'),
        pageSubTitleEl = mainContainer.querySelector('.page__title > .page__title-sub'),
        isAnimating = false,
        currentView = 'stack';

    // Initializing
    function init() {
        //document.body.classList.add("overflow");
        mainContainer.classList.add('view--loaded');
        showIntro();
        initEvents();
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

    function initEvents() {
        showGridButton.addEventListener('click', showGrid);
        
        // The function that executes the transition to grid view on scroll event
        var scrollToGrid = function() {
            window.removeEventListener('scroll', scrollToGrid);
            showGrid();
        }
        window.addEventListener('scroll', scrollToGrid);
    }

    function showGrid() {
        if( isAnimating ) return;
        isAnimating = true;
        
        // Stopping the pagescroll for the duration of the intro
        mainContainer.classList.add('fix-for-intro'); 
        setTimeout(function(){ 
            console.log("Ez a SET TIMOUT vege")
            mainContainer.classList.remove('fix-for-intro'); 
        }, 2000);

        showGridButton.style.display = "none";

        dynamics.animate(titleEl, { translateY: -winsize.height/2, opacity: 0 }, {
            type: dynamics.linear,
            duration: 600
        });

        subtitleElements.slice().forEach(function(element, pos) {
            dynamics.animate(element, { translateY: -winsize.height/2, opacity: 0 }, {
            type: dynamics.linear,
            duration: 600,
            delay: 10
            });
        });

        dynamics.animate(deviceEl, { translateY: winsize.height/2, opacity: 0 }, {
            type: dynamics.linear,
            duration: 600,
        });

        //moving the initial page that covers the grid view up and out of the viewport
        dynamics.animate(pagemover, { translateY: -winsize.height }, {
            type: dynamics.easeIn,
            friction: 400,
            duration: 600,
            complete: function(element) {
                // once it's out we set it transparent 
                element.style.opacity = 0;
                // change our currentView variable to grid
                currentView = "grid";
                mainContainer.classList.add('view--grid');
            }
        });
        gridItems.slice(0,6).forEach(function(item, pos) {
            dynamics.stop(item);
            dynamics.animate(item, { scale: 1, translateX: 0, translateY: 0, rotateZ: 0 }, {
                type: dynamics.easeInOut,
			    duration: 600
            });
        });
        dynamics.animate(pageTitleElement, { translateY: winsize.height/4, opacity: 0 });
        dynamics.animate(pageTitleElement, { translateY: 0, opacity: 1 }, {
            type: dynamics.forceWithGravity,
            bounciness: 200,
            elasticity: 100,
            returnToSelf: false,
            duration: 600,

        });


    }

    init();

/*end of IIFE*/
})();