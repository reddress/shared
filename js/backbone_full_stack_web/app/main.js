var data = [
  { "id": 10, "title": "The Artist (JSON)" },
  { "id": 20, "title": "Taxi Driver (JSON)" },
  { "id": 30, "title": "La Dolce Vita (JSON)" },
];

// p. 28
// movie.get('title');
// movie.set('title', 'New Title');
// movie.set({ "title": "Newer Title" });

var movies = new Movies(data);

// p. 30
// > movies.get(id).get(key);
// > movies.get(30).get("title");
//
// > movies.at(position in collection) 
// > movies.first().toJSON();
//
// > movies.map(function(m) { return m.get('title'); });
//
// > movies.where({ title: "The Artist" });
// > movies.findWhere({ title: "The Artist" });

// when using a predicate function to test. Returns first one
// > movies.find(function(movie) { return movie.year > 2000 });

// filter returns all, using predicate or attributes
// > movies.filter({ "selected": false });

var monitor = new Monitor(movies);

// events may be silenced
// > movies.first().set({ "selected": true }, { silent: true });

// after adding MovieView:
// > var movie = app.movies.get(20);
// > view = new MovieView({ model: movie });
// > document.body.appendChild(view.render().el);

// render movies List

moviesList = new MoviesList({ collection: movies });
document.body.appendChild(moviesList.render().el);
