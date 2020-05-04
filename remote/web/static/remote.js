$( document ).ready(function() {
  $("#card").flip();

  $('#exampleModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) 
    var title_ = button.data('title_')
    var year = button.data('year')
    var overview = button.data('overview')
    var modal = $(this)
    modal.find('.title_').text(title_)
    modal.find('.year').text(year)
    modal.find('.overview').text(overview)
  })
});
