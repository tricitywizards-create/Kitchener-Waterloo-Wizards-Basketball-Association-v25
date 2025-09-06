// Ultra-lightweight mobile JS - 3KB compressed
(function(){
'use strict';

// Mobile detection
const m=()=>window.innerWidth<=768||/Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);

// Debounce utility
const d=(f,w)=>{let t;return(...a)=>{clearTimeout(t);t=setTimeout(()=>f(...a),w)}};

// Mobile navigation
function n(){
  const t=document.getElementById('menu-toggle'),
        l=document.getElementById('nav-links'),
        g=document.querySelector('.nav-logo');
  
  if(!t||!l)return;
  
  t.onclick=e=>{
    e.preventDefault();
    const a=l.classList.contains('active');
    l.classList.toggle('active');
    t.classList.toggle('active');
    if(g)g.classList.toggle('hidden');
    if(!m())document.body.style.overflow=a?'':'hidden';
  };
  
  l.onclick=e=>{
    if(e.target.tagName==='A'){
      l.classList.remove('active');
      t.classList.remove('active');
      if(g)g.classList.remove('hidden');
      if(!m())document.body.style.overflow='';
    }
  };
  
  document.onclick=d(e=>{
    const nav=document.querySelector('nav');
    if(!nav.contains(e.target)&&l.classList.contains('active')){
      l.classList.remove('active');
      t.classList.remove('active');
      if(g)g.classList.remove('hidden');
      if(!m())document.body.style.overflow='';
    }
  },100);
}

// Mobile viewport optimization - PERFORMANCE OPTIMIZED
function v(){
  if(!m())return;
  
  // Cache viewport height to prevent layout thrashing
  let cachedVH = window.innerHeight * 0.01;
  
  const updateVH = () => {
    const newVH = window.innerHeight * 0.01;
    // Only update if there's a significant change (>0.1px)
    if (Math.abs(newVH - cachedVH) > 0.1) {
      document.documentElement.style.setProperty('--vh', newVH + 'px');
      cachedVH = newVH;
    }
  };
  
  // Initial set
  document.documentElement.style.setProperty('--vh', cachedVH + 'px');
  
  // Use requestAnimationFrame instead of setTimeout for better performance
  const debouncedUpdateVH = d(updateVH, 150);
  window.addEventListener('resize', debouncedUpdateVH, {passive: true});
  window.addEventListener('orientationchange', () => {
    requestAnimationFrame(debouncedUpdateVH);
  }, {passive: true});
  
  // Optimized scroll handling - removed body height manipulation
  let y=window.scrollY,tick=false;
  
  const hs=()=>{
    if(!tick){
      requestAnimationFrame(()=>{
        // Simple scroll direction tracking without layout thrashing
        const isScrollingDown = window.scrollY > y && window.scrollY > 100;
        if(isScrollingDown) {
          // Optional: Add scroll-based class for CSS-only effects
          document.body.classList.add('scrolling-down');
        } else {
          document.body.classList.remove('scrolling-down');
        }
        y=window.scrollY;
        tick=false;
      });
      tick=true;
    }
  };
  
  window.addEventListener('scroll',hs,{passive:true});
}

// Ultra-minimal star animation for mobile
function stars(){
  const c=document.getElementById('stars');
  if(!c)return;
  
  // Drastically reduced stars for mobile performance
  const count = m() ? 3 : 15;
  const f=document.createDocumentFragment();
  
  for(let i=0;i<count;i++){
    const s=document.createElement('div');
    s.className='star';
    s.style.cssText=`transform: translate3d(0,0,0); will-change: opacity; backface-visibility: hidden; width:${Math.random()*1.5+0.5}px;height:${Math.random()*1.5+0.5}px;left:${Math.random()*100}%;top:${Math.random()*100}%;opacity:${Math.random()*0.4+0.2};animation:star-twinkle`;
    f.appendChild(s);
  }
  
  c.appendChild(f);
  
  // Add minimal CSS animation
  if(!document.querySelector('#sa')){
    const st=document.createElement('style');
    st.id='sa';
    st.textContent='@keyframes twinkle{0%,100%{opacity:.2}50%{opacity:.6}}@media (prefers-reduced-motion:reduce){.star{animation:none!important}}';
    document.head.appendChild(st);
  }
}

// Lazy loading with Intersection Observer
function lazy(){
  if(!('IntersectionObserver' in window))return;
  
  const o=new IntersectionObserver(e=>{
    e.forEach(t=>{
      if(t.isIntersecting){
        t.target.classList.add('ai');
        o.unobserve(t.target);
      }
    });
  },{threshold:0.1,rootMargin:'20px'});
  
  document.querySelectorAll('section,.rep-team-box,.calendar-box').forEach(el=>{
    el.classList.add('aos');
    o.observe(el);
  });
  
  // Minimal animation styles
  if(!document.querySelector('#las')){
    const st=document.createElement('style');
    st.id='las';
    st.textContent='.aos{opacity:0;transform:translateY(10px);transition:opacity .4s ease,transform .4s ease}.aos.ai{opacity:1;transform:translateY(0)}@media (prefers-reduced-motion:reduce){.aos{opacity:1!important;transform:none!important;transition:none!important}}';
    document.head.appendChild(st);
  }
}

// NO EXTERNAL FONTS - System fonts only for maximum speed
// Font loading completely eliminated

// Initialize everything
function init(){
  document.body.classList.remove('loading');
  document.body.classList.add('loaded');
  
  n(); // Navigation
  
  if(m())v(); // Mobile viewport
  
  // Use requestAnimationFrame for non-critical features
  requestAnimationFrame(() => {
    stars();
    lazy();
  });
}

// Start
if(document.readyState==='loading'){
  document.addEventListener('DOMContentLoaded',init);
}else{
  init();
}

})();
