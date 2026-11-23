document.querySelectorAll('.slides').forEach(function(s){var t=s.querySelector('.track');
s.querySelectorAll('button').forEach(function(b){b.addEventListener('click',function(){t.scrollBy({left:t.clientWidth*Number(b.dataset.d)})})});
t.addEventListener('keydown',function(e){if(e.key==='ArrowRight')t.scrollBy({left:t.clientWidth});if(e.key==='ArrowLeft')t.scrollBy({left:-t.clientWidth})})});
