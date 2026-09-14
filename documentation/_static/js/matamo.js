/*
 * This script should add Matamo (formerly piwik) analytics to the Standard docs
 * It is intended to be sourced via conf.py, by adding it to the html_js_files array
 *
 * The code from this is taken from an older version of the Standard Docs
 * See: _templates-old/layout.html
 *
 */


var _paq = _paq || [];
  /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
  _paq.push(['disableCookies']);
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="//analytics.threesixtygiving.org/";
    _paq.push(['setTrackerUrl', u+'matomo.php']);
    _paq.push(['setSiteId', '13']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
  })();
