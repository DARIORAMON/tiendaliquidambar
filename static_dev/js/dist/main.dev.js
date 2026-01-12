"use strict";

document.addEventListener("DOMContentLoaded", function () {
  new Glide(".glide", {
    type: "carousel",
    startAt: 0,
    animationTimingFunc: "ease-in-out",
    gap: 100,
    perView: 3
  }).mount();
  var prevBtn = document.getElementById("prev");
  var nextBtn = document.getElementById("next");
  var background = document.querySelector(".background");
  var indices = document.querySelectorAll(".index"); //let bgImgs = ["Indonesia.jpg", "Kerala.jpg", "Bali.jpg" ];

  var bgImgs = ["imgj1.jpg", "imgj2.jpg", "imgj3.jpg"];
  var currentIndex = 0;
  indices.forEach(function (index) {
    return index.classList.remove("active");
  });
  indices[currentIndex].classList.add("active");
  var myAnimation = new hoverEffect({
    parent: document.querySelector(".background"),
    intensity: 0.3,
    imagesRatio: 1080 / 1920,
    image1: "media/intro/".concat(bgImgs[0]),
    image2: "media/intro/".concat(bgImgs[1]),
    displacementImage: "media/intro/14.jpg",
    hover: false
  });
  var myAnimation2 = new hoverEffect({
    parent: document.querySelector(".background"),
    intensity: 0.3,
    imagesRatio: 1080 / 1920,
    image1: "media/intro/".concat(bgImgs[1]),
    image2: "media/intro/".concat(bgImgs[2]),
    displacementImage: "media/intro/14.jpg",
    hover: false
  });
  var myAnimation3 = new hoverEffect({
    parent: document.querySelector(".background"),
    intensity: 0.3,
    imagesRatio: 1080 / 1920,
    image1: "media/intro/".concat(bgImgs[2]),
    image2: "media/intro/".concat(bgImgs[0]),
    displacementImage: "media/intro/14.jpg",
    hover: false
  });
  var distortAnimations = [myAnimation, myAnimation2, myAnimation3];

  function startNextDistortAnimation() {
    var prevIndex = currentIndex;
    currentIndex = (currentIndex + 1) % 3;
    indices.forEach(function (index) {
      return index.classList.remove("active");
    });
    indices[currentIndex].classList.add("active");
    distortAnimations[prevIndex].next();
    showTextAnimation("next");
    setTimeout(function () {
      var canvas = background.querySelectorAll("canvas");
      background.appendChild(canvas[0]);
      distortAnimations[prevIndex].previous();
    }, 1200);
  }

  function startPrevDistortAnimation() {
    currentIndex = currentIndex - 1 < 0 ? 2 : currentIndex - 1;
    indices.forEach(function (index) {
      return index.classList.remove("active");
    });
    indices[currentIndex].classList.add("active");
    distortAnimations[currentIndex].next();
    showTextAnimation("prev");
    setTimeout(function () {
      var canvas = background.querySelectorAll("canvas");
      background.insertBefore(canvas[canvas.length - 1], background.firstChild);
      distortAnimations[currentIndex].previous();
    }, 500);
  }

  nextBtn.addEventListener("click", function () {
    startNextDistortAnimation();
  });
  prevBtn.addEventListener("click", function () {
    startPrevDistortAnimation();
  });
  var titleDisplacement = 0;
  var descriptionDisplacement = 0;

  function showTextAnimation(direction) {
    if (titleDisplacement === 0 && direction === "prev") {
      titleDisplacement = -540;
    } else if (titleDisplacement === -540 && direction === "next") {
      titleDisplacement = 0;
    } else {
      titleDisplacement = direction === "next" ? titleDisplacement - 180 : titleDisplacement + 180;
    }

    if (descriptionDisplacement === 0 && direction === "prev") {
      descriptionDisplacement = -165;
    } else if (descriptionDisplacement === -165 && direction === "next") {
      descriptionDisplacement = 0;
    } else {
      descriptionDisplacement = direction === "next" ? descriptionDisplacement - 55 : descriptionDisplacement + 55;
    }

    var title = document.querySelectorAll("#title h4");
    var description = document.querySelectorAll("#description p");
    title.forEach(function (title) {
      TweenMax.to(title, 1, {
        top: "".concat(titleDisplacement, "px"),
        ease: Strong.easeInOut
      });
    });
    description.forEach(function (description, index) {
      var opacity = 0;

      if (index === currentIndex) {
        opacity = 1;
      } else {
        opacity = 0;
      }

      TweenMax.to(description, 1, {
        top: "".concat(descriptionDisplacement, "px"),
        ease: Strong.easeInOut,
        opacity: opacity
      });
    });
  }
});
//# sourceMappingURL=main.dev.js.map
