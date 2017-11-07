# MovieWebsite
A compilation of my favourite movies' trailers, names and descriptions.

To run this project, open <b> entertainment_center.py </b> in your favourite
text editor, and run it. 

To play around with the <b> populate_data() </b> function in the
entertainment_center.py, simply change the elements in the
movie_search_string array. Note that the algorithm works by taking
the most confident search term (the first one) in The Movie Database.

![populate play](https://user-images.githubusercontent.com/5374699/32476825-f82c96dc-c347-11e7-8480-0c0b3f5506e4.png)

Hit run in your favourite text editor to open the website in your default browser. The website populates the movies' data based on your search strings. 

![preview](https://user-images.githubusercontent.com/5374699/32476827-f844cce8-c347-11e7-99e9-5c108e363897.png)

Click on any of the movies' to play their trailer:
![youtube](https://user-images.githubusercontent.com/5374699/32476828-f853485e-c347-11e7-86fd-2c17d98c90bc.png)


If you have questions, do not hesitate to contact me.

<b> NOTE:<b>
If you would like to play with the populate_data() algorithm, make sure that 
the search strings are confident queries. Sometimes if the search doesn't work,
then <b> s['poster_path'] </b> comes out as a NoneType object. This gives you
a run-time error as a NoneType object cannot be concatenated with a str type 
object.

![error](https://user-images.githubusercontent.com/5374699/32476826-f8387c40-c347-11e7-9689-2e417ef8521c.png)


 
