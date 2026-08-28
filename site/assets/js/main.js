/* ==========================================================================
   RC TABLE CAR RACING — interactions & animations
   Vanilla JS, zéro dépendance. Respecte prefers-reduced-motion.
   ========================================================================== */
(function () {
  'use strict';

  /* Les contenus restent visibles si JavaScript est indisponible. */
  document.documentElement.classList.add('js');

  var REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------------------------------------------------------------- 1. Nav */
  function initNav() {
    var header = $('.site-header');
    var burger = $('.btn-burger');
    var nav = $('.nav-main');

    if (burger && nav) {
      burger.addEventListener('click', function () {
        var open = nav.classList.toggle('is-open');
        burger.setAttribute('aria-expanded', String(open));
        burger.textContent = open ? 'FERMER' : 'MENU';
      });
    }

    $$('.nav-top[aria-haspopup]').forEach(function (btn) {
      var li = btn.parentNode;
      var close = function () { btn.setAttribute('aria-expanded', 'false'); };
      var open = function () {
        $$('.nav-top[aria-haspopup]').forEach(function (o) { if (o !== btn) o.setAttribute('aria-expanded', 'false'); });
        btn.setAttribute('aria-expanded', 'true');
      };
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        btn.getAttribute('aria-expanded') === 'true' ? close() : open();
      });
      if (window.matchMedia('(min-width:901px)').matches) {
        li.addEventListener('mouseenter', open);
        li.addEventListener('mouseleave', close);
      }
      li.addEventListener('focusout', function (e) {
        if (!li.contains(e.relatedTarget)) close();
      });
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        $$('.nav-top[aria-haspopup]').forEach(function (b) { b.setAttribute('aria-expanded', 'false'); });
        if (nav) nav.classList.remove('is-open');
        if (burger) { burger.setAttribute('aria-expanded', 'false'); burger.textContent = 'MENU'; }
      }
    });

    document.addEventListener('click', function (e) {
      if (!e.target.closest('.nav-main') && !e.target.closest('.btn-burger')) {
        $$('.nav-top[aria-haspopup]').forEach(function (b) { b.setAttribute('aria-expanded', 'false'); });
      }
    });

    if (header) {
      var onScroll = function () { header.classList.toggle('is-stuck', window.scrollY > 8); };
      onScroll();
      window.addEventListener('scroll', onScroll, { passive: true });
    }
  }

  /* ------------------------------------------------------- 2. Révélations */
  function initReveal() {
    var els = $$('[data-reveal],[data-stagger]');
    if (REDUCED || !('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  /* --------------------------------------------------------- 3. Compteurs */
  function animateCount(el) {
    var raw = el.getAttribute('data-count');
    var target = parseFloat(String(raw).replace(',', '.'));
    if (isNaN(target)) return;
    var suffix = el.getAttribute('data-suffix') || '';
    var prefix = el.getAttribute('data-prefix') || '';
    var decimals = (String(raw).split(/[.,]/)[1] || '').length;
    var dur = 1250, t0 = null;
    function frame(ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      var v = (target * eased).toFixed(decimals).replace('.', ',');
      el.textContent = prefix + v + suffix;
      if (p < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  function initCounters() {
    var els = $$('[data-count]');
    if (!els.length) return;
    if (REDUCED || !('IntersectionObserver' in window)) {
      els.forEach(function (el) {
        el.textContent = (el.getAttribute('data-prefix') || '') + el.getAttribute('data-count') + (el.getAttribute('data-suffix') || '');
      });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { animateCount(en.target); io.unobserve(en.target); }
      });
    }, { threshold: 0.5 });
    els.forEach(function (el) { el.classList.add('counting'); io.observe(el); });
  }

  /* ------------------------------------------------ 4. Tracés SVG animés */
  function initPaths() {
    $$('.track-line').forEach(function (p) {
      try {
        var len = Math.ceil(p.getTotalLength());
        p.style.setProperty('--len', len);
        p.style.strokeDasharray = len;
        if (!REDUCED) p.style.strokeDashoffset = len;
      } catch (e) { /* pas un path */ }
    });
  }

  /* --------------------------------------- 5. Voiture qui suit le circuit */
  function initRunners() {
    if (REDUCED) return;
    $$('[data-runner]').forEach(function (car) {
      var svg = car.closest('svg');
      var path = svg && svg.querySelector('#' + car.getAttribute('data-runner'));
      if (!path) return;
      var len = path.getTotalLength();
      var speed = parseFloat(car.getAttribute('data-speed')) || 105; // px/s
      var dist = Math.random() * len, last = null, running = true;

      var io = new IntersectionObserver(function (e) { running = e[0].isIntersecting; });
      io.observe(svg);

      function tick(ts) {
        if (last === null) last = ts;
        var dt = Math.min((ts - last) / 1000, 0.05);
        last = ts;
        if (running) {
          dist = (dist + speed * dt) % len;
          var p = path.getPointAtLength(dist);
          var p2 = path.getPointAtLength((dist + 4) % len);
          var ang = Math.atan2(p2.y - p.y, p2.x - p.x) * 180 / Math.PI;
          car.setAttribute('transform', 'translate(' + p.x.toFixed(2) + ',' + p.y.toFixed(2) + ') rotate(' + ang.toFixed(1) + ')');
        }
        requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    });
  }

  /* --------------------------------------------------------- 6. Parallaxe */
  function initParallax() {
    var els = $$('[data-parallax]');
    if (!els.length || REDUCED) return;
    // pas de parallaxe sous 900 px : peu lisible sur téléphone et coûteux en rendu
    var wide = window.matchMedia('(min-width:901px)');
    var ticking = false;
    function update() {
      var vh = window.innerHeight;
      if (!wide.matches) {
        els.forEach(function (el) { el.style.transform = ''; });
        ticking = false;
        return;
      }
      els.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < -100 || r.top > vh + 100) return;
        var amt = parseFloat(el.getAttribute('data-parallax')) || 0.08;
        var mid = r.top + r.height / 2 - vh / 2;
        el.style.transform = 'translate3d(0,' + (-mid * amt).toFixed(1) + 'px,0)';
      });
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    window.addEventListener('resize', update, { passive: true });
    update();
  }

  /* ------------------------------------------------- 7. Barre de lecture */
  function initProgress() {
    var bar = $('#read-progress');
    if (!bar) return;
    var upd = function () {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.transform = 'scaleX(' + (h > 0 ? window.scrollY / h : 0) + ')';
    };
    upd();
    window.addEventListener('scroll', upd, { passive: true });
    window.addEventListener('resize', upd);
  }

  /* -------------------------------------------------- 8. Copier un bloc */
  function initCopy() {
    $$('[data-copy]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var src = $(btn.getAttribute('data-copy'));
        if (!src || !navigator.clipboard) return;
        navigator.clipboard.writeText(src.innerText.trim()).then(function () {
          var old = btn.textContent;
          btn.textContent = 'COPIÉ ✓';
          setTimeout(function () { btn.textContent = old; }, 2000);
        });
      });
    });
  }

  /* ---------------------------------------------------- 9. Année en cours */
  function initYear() {
    $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
  }

  /* ------------------------------------------------------------- Démarrage */
  function boot() {
    initNav(); initReveal(); initCounters(); initPaths();
    initRunners(); initParallax(); initProgress(); initCopy(); initYear();
    document.documentElement.classList.add('js-ready');
  }

  document.readyState === 'loading'
    ? document.addEventListener('DOMContentLoaded', boot)
    : boot();
})();
