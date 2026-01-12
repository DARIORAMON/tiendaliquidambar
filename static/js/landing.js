TweenMax.set(".contenido_i", { rotationY: 0});
TweenMax.set(".contenido_texto", { autoAlpha: 0, y: 0 });
TweenMax.set(".imagen_principal_landing", { autoAlpha: 1, y: 0 });
TweenMax.set(".img_fondo_lin", { autoAlpha: 0, y: 0 });
TweenMax.set(".imagen_principal_landing2", { autoAlpha: 1, y: 0 });
console.clear();
$(".trigger").each(createHovers);

function createHovers(i, element) {
  var tl = new TimelineMax({ paused: true, reversed: true });
  tl.to($(this).find(".contenido_i"), 0.25, { rotationY: 180 });
  tl.to($(this).find(".imagen_principal_landing"), 0.25, { autoAlpha: 0}, '-=0.25'); 
  tl.to($(this).find(".imagen_principal_landing2"), 0.25, { autoAlpha: 0 }, '-=0.25');
  tl.to($(this).find(".contenido_texto"), 0.25, { rotationY: 180, autoAlpha: 1}, '-=0.25');
  tl.to($(this).find(".img_fondo_lin"), 0.25, {  autoAlpha: 1},'-=0.25');   
  $(element).hover(hoverIt);

  function hoverIt() {
    tl.reversed() ? tl.play() : tl.reverse();
  }
}



	
	
	
	
	
	