 
function tamVentana() {
	  var tam = [0, 0];
	  if (typeof window.innerWidth != 'undefined')
	  {
		tam = [window.innerWidth,window.innerHeight];
	  }
	  else if (typeof document.documentElement != 'undefined'
		  && typeof document.documentElement.clientWidth !=
		  'undefined' && document.documentElement.clientWidth != 0)
	  {
		tam = [
			document.documentElement.clientWidth,
			document.documentElement.clientHeight
		];
	  }
	  else   {
		tam = [
			document.getElementsByTagName('body')[0].clientWidth,
			document.getElementsByTagName('body')[0].clientHeight
		];
	  }
	  return tam;
	}
 



document.addEventListener("DOMContentLoaded", () => {
  
 
	console.log("cambio");
  	console.log(tamVentana())
	console.log(tamVentana()[0])
	if (tamVentana()[0] < 1100){
		  new Glide(".glide", {
			type: "carousel",
			startAt: 0,
			animationTimingFunc: "ease-in-out",
			gap: 100,
			perView: 1
		  }).mount();
		console.log("celu");
	}else if(tamVentana()[0] > 700 && tamVentana()[0] < 1700){
		  new Glide(".glide", {
			type: "carousel",
			startAt: 0,
			animationTimingFunc: "ease-in-out",
			gap: 100,
			perView: 2
		  }).mount();
		console.log("notebook");
	}else{
		  new Glide(".glide", {
			type: "carousel",
			startAt: 0,
			animationTimingFunc: "ease-in-out",
			gap: 100,
			perView: 3
		  }).mount();
		console.log("960");
	}
		
 

  
  
  
  
  /*
  new Glide(".glide", {
    type: "carousel",
    startAt: 0,
    animationTimingFunc: "ease-in-out",
    gap: 100,
    perView: 3
  }).mount();*/

  let prevBtn = document.getElementById("prev");
  let nextBtn = document.getElementById("next");

  let background = document.querySelector(".background");
  let indices = document.querySelectorAll(".index");

  //let bgImgs = ["Indonesia.jpg", "Kerala.jpg", "Bali.jpg" ];
  let bgImgs = ["imgj1.jpg", "imgj2.jpg", "imgj3.jpg", "imgj4.jpg" ];
  let currentIndex = 0;

  indices.forEach(index => index.classList.remove("active"));
  indices[currentIndex].classList.add("active");

  var myAnimation = new hoverEffect({
    parent: document.querySelector(".background"),
    intensity: 0.3,
    imagesRatio: 1080 / 1920,
    image1: `media/intro/${bgImgs[0]}`,
    image2: `media/intro/${bgImgs[1]}`,
    displacementImage: "media/intro/14.jpg",
    hover: false
  });

  var myAnimation2 = new hoverEffect({
    parent: document.querySelector(".background"),
    intensity: 0.3,
    imagesRatio: 1080 / 1920,
    image1: `media/intro/${bgImgs[1]}`,
    image2: `media/intro/${bgImgs[2]}`,
    displacementImage: "media/intro/14.jpg",
    hover: false
  });
  var myAnimation3 = new hoverEffect({
    parent: document.querySelector(".background"),
    intensity: 0.3,
    imagesRatio: 1080 / 1920,
    image1: `media/intro/${bgImgs[2]}`,
    image2: `media/intro/${bgImgs[3]}`,
    displacementImage: "media/intro/14.jpg",
    hover: false
  });
  var myAnimation4 = new hoverEffect({
    parent: document.querySelector(".background"),
    intensity: 0.3,
    imagesRatio: 1080 / 1920,
    image1: `media/intro/${bgImgs[3]}`,
    image2: `media/intro/${bgImgs[0]}`,
    displacementImage: "media/intro/14.jpg",
    hover: false
  });

 

  let distortAnimations = [
    myAnimation,
    myAnimation2,
    myAnimation3,
	myAnimation4,
  ];

  function startNextDistortAnimation() {
    let prevIndex = currentIndex;
    currentIndex = (currentIndex + 1) % 4;
    indices.forEach(index => index.classList.remove("active"));
    indices[currentIndex].classList.add("active");
    distortAnimations[prevIndex].next();
    showTextAnimation("next");
    setTimeout(() => {
      let canvas = background.querySelectorAll("canvas");
      background.appendChild(canvas[0]);
      distortAnimations[prevIndex].previous();
    }, 1200);
  }

  function startPrevDistortAnimation() {
    currentIndex = currentIndex - 1 < 0 ? 3 : currentIndex - 1;
    indices.forEach(index => index.classList.remove("active"));
    indices[currentIndex].classList.add("active");
    distortAnimations[currentIndex].next();
    showTextAnimation("prev");
    setTimeout(() => {
      let canvas = background.querySelectorAll("canvas");
      background.insertBefore(canvas[canvas.length - 1], background.firstChild);
      distortAnimations[currentIndex].previous();
    }, 500);
  }

  nextBtn.addEventListener("click", () => {
    startNextDistortAnimation();
  });

  prevBtn.addEventListener("click", () => {
    startPrevDistortAnimation();
  });

  let titleDisplacement = 0;
  let descriptionDisplacement = 0;

  function showTextAnimation(direction) {
    if (titleDisplacement === 0 && direction === "prev") {
      titleDisplacement = -540;
    } else if (titleDisplacement === -540 && direction === "next") {
      titleDisplacement = 0;
    } else {
      titleDisplacement =
        direction === "next"
          ? titleDisplacement - 180
          : titleDisplacement + 180;
    }

    if (descriptionDisplacement === 0 && direction === "prev") {
      descriptionDisplacement = -165;
    } 
    else if(descriptionDisplacement === -165 && direction === "next"){
      descriptionDisplacement = 0;
    }
    else {
      descriptionDisplacement =
        direction === "next" 
          ? descriptionDisplacement - 55
          : descriptionDisplacement + 55;
    }

    let title = document.querySelectorAll("#title h4");
    let description = document.querySelectorAll("#description p");

    title.forEach(title => {
      TweenMax.to(title, 1, {
        top: `${titleDisplacement}px`,
        ease: Strong.easeInOut
      });
    });

    description.forEach((description, index) => {
      let opacity = 0;
      if(index === currentIndex){
        opacity = 1;
      }else {
        opacity = 0;
      }
      TweenMax.to(description, 1, {
        top: `${descriptionDisplacement}px`,
        ease: Strong.easeInOut,
        opacity: opacity
      });
    })
  }
 
});
 