!function ($) {
  $(function(){

    // Allow videos to take the full width of a page
    $(".container").fitVids();

    // YouTube URL parser. Source: http://stackoverflow.com/questions/2964678/jquery-youtube-url-validation-with-regex/10315969#10315969
    function parse_youtube_url(url) {
      var p = /^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$/;
      return (url.match(p)) ? RegExp.$1 : false;
    };


  });
}(window.jQuery);
