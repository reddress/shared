var Todo = Backbone.Model.extend({
  defaults: {
    title: '',
    completed: false,
  },
  initialize: function() {
    console.log("New todo initialized");
  },
  
});

var TodoView = Backbone.View.extend({
  tagName: 'li',

  todoTpl: _.template($("#item-template").html()),

  events: {
    'dblclick label': "edit",
    'keypress .edit': 'updateOnEnter',
    'blur .edit': 'close',
  },

  initialize: function() {
    this.$el = $('#todo');
    this.model.bind('change', _.bind(this.render, this));
  },

  render: function() {
    this.$el.html(this.todoTpl(this.model.toJSON()));
    this.input = this.$('.edit');

    // common convention, makes view reusable in parent views
    // also, creating a list of elements, drawing only once when the
    // entire list is populated
    return this;
  },

  edit: function() {

  },

  close: function() {

  },

  updateOnEnter: function(e) {

  },
});


var TodosCollection = Backbone.Collection.extend({
  model: Todo,

});

var myTodo = new Todo({
  title: "Check <b>attributes</b> property...",
});

var todoView = new TodoView({ model: myTodo });

todoView.render();

var todos = new TodosCollection([myTodo]);
console.log("Collection size: " + todos.length);
