$( document ).ready(function() {
  $("#card").flip();

  $('#exampleModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) 

    var title_ = button.data('title_')
    var overview = button.data('overview')
    var year = button.data('year')
    var filename = button.data('filename')
    var modal = $(this)

    modal.find('.title_').text(title_)
    modal.find('.overview').text(overview)
    modal.find('.year').text(year)

    modal.find('#trailer').prop('href', 'https://www.youtube.com/results?search_query=' + title_ + ' trailer')
    modal.find('#copy').prop('href', 'copy/' + filename)
    modal.find('#delete').prop('href', 'delete/' + filename)
  })
});
