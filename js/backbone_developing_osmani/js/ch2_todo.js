var Todo = Backbone.Model.extend({
  initialize: function() {
    console.log("Todo model initialized");
  },
  defaults: {
    title: 'unnamed todo',
    completed: false,
  },
});

var todo1 = new Todo();

var todo2 = new Todo({
  title: "check attributes",
  completed: true,
});

console.log(JSON.stringify(todo2));
