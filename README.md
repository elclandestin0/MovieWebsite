# MovieWebsite
A compilation of my favourite movies' trailers, names and descriptions.

To run this project, open <b> entertainment_center.py </b> in your favourite
text editor, and run it. 

To play around with the <b> populate_data() </b> function in the
entertainment_center.py, simply change the elements in the
movie_search_string array. Note that the algorithm works by taking
the most confident search term (the first one) in The Movie Database.

If you have questions, do not hesitate to contact me.



<b> NOTE:<b>
If you would like to play with the populate_data() algorithm, make sure that 
the search strings are confident queries. Sometimes if the search doesn't work,
then <b> s['poster_path'] </b> comes out as a NoneType object. This gives you
a run-time error as a NoneType object cannot be concatenated with a str type 
object
 
