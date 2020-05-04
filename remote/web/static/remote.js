$( document ).ready(function() {
  $("#card").flip();

  $('#exampleModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) 
    var overview = button.data('overview')
    var genre = button.data('genre')
    var modal = $(this)
    modal.find('.overview').text('Overview: ' + overview)
    modal.find('.genre').text('Genre: ' + genre)
  })
});
