var MoviesList = Backbone.View.extend({
  tagName: 'section',

  render: function() {
    var moviesView = this.collection.map(function(movie) {
      return (new MovieView({ model: movie })).render().el;
    });

    this.$el.html(moviesView);
    return this;
  }

  // moviesList = new MoviesList({ collection: movies });  // in index.html
  // moviesList.render().el;
  // document.body.appendChild(moviesList.render().el);


});
