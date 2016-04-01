var Movies = Backbone.Collection.extend({
  model: Movie,

  resetSelected: function() {
    this.each(function(model) {
      model.set({ "selected": false });
    });
    // inefficient, maybe find the selected and then unselect it?
    // var m = movies.findWhere({ "selected": true });
    // m.set("selected", false);
    
  },
  
  selectById: function(id) {
    this.resetSelected();
    var movie = this.get(id);
    movie.set({ "selected": true });
    return movie.id;
  },
    
});
