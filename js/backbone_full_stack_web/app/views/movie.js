var MovieView = Backbone.View.extend({
  tagName: 'article',
  className: 'movie',

  template: '<h1><%= title %><hr></h1>',

  render: function() {
    var tmpl = _.template(this.template);
    
    this.$el.html(tmpl(this.model.toJSON()));
    this.$el.toggleClass('selected', this.model.get('selected'));
    return this;
  },

  // p. 39
  // it is usually a good idea to fix the view context (the 'this'
  // reference) explicitly to the view scope. By binding the 'this'
  // context of a view to 'render', all properties of the object will
  // be accessible even when a view context would have changed to a
  // different callback scope.
  initialize: function() {
    _.bindAll(this, "render");

    // Note: no space after 'change:'
    this.listenTo(this.model, 'change:title', this.render);
  },

  events: {
    'click': '_selectMovie',
  },

  _selectMovie: function(event) {
    event.preventDefault();
    // console.log($(event.currentTarget).html());
    this.model.collection.resetSelected();
    this.model.collection.selectById(this.model.id);
  },
});

