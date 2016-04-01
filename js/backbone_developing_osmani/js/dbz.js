var Person = Backbone.Model.extend({
  defaults: {
    name: "Goku",
  },
  
  validate: function(attrs) {
    if (attrs.powerLevel < 9000) {
      return "Not powerful enough.";
    }
  },

  initialize: function() {
    console.log("Over 9000!!");
  },
});

var PersonView = Backbone.View.extend({
  el: ".person",
  render: function() {
    this.$el.html(this.model.get("name"));
    return this;
  },
});
  
var p = new Person;
var pv = new PersonView({ model: p });
pv.render();
