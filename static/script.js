// all the html, js, py code for search bar

//  Js content 

// // Wait for the DOM to fully load
// document.addEventListener("DOMContentLoaded", function() {
//     // Get the search form element
//     const searchForm = document.querySelector("form.d-flex");

//     // Add an event listener for the form submit
//     searchForm.addEventListener("submit", function(event) {
//         event.preventDefault();  // Prevent the form from submitting
        
//         // Get the value from the search input field
//         const searchTerm = document.querySelector("input[type='search']").value;
        
//         // If search term is empty, alert the user
//         if (searchTerm === '') {
//             alert('Please enter a search term');
//         } else {
//             // You can handle the search term here, for now, we'll just log it to the console
//             console.log('Searching for:', searchTerm);
            
//             // Redirect to the search results page, you can update the URL as per your backend
//             window.location.href = `/search?q=${searchTerm}`;
//         }
//     });
// });

// app.py content 

// @app.route('/search')
// def search():
//     query = request.args.get('q')
//     if query:
//         # Example: Search in the database (you can modify this based on your app)
//         results = Todo.query.filter(Todo.title.contains(query)).all()
//         return render_template('search_results.html', results=results, query=query)
//     return render_template('search_results.html', results=[], query=query)


//searchResult.html content

// {% extends 'base.html' %}
// {% block title %} Search Results for "{{ query }}" {% endblock title %}

// {% block body %}
//     <div class="container my-4">
//         <h2>Search Results for "{{ query }}"</h2>
//         {% if results %}
//             <ul class="list-group">
//                 {% for todo in results %}
//                     <li class="list-group-item">
//                         {{ todo.title }} - {{ todo.details }}
//                     </li>
//                 {% endfor %}
//             </ul>
//         {% else %}
//             <div class="alert alert-dark">No results found for "{{ query }}"</div>
//         {% endif %}
//     </div>
// {% endblock body %}
