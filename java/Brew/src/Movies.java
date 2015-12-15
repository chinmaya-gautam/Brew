

import java.awt.Image;

public class Movies {
	public String movieName;
	public float rating;
	public String contentRating;
	public String[] genre;
	public String[] actors;
	public String director;
	public Image poster;
	public int runningTime;
	public String description;
	
	public Movies(String name, float rating, 
			String cRating, String[] genre,
			String[] actors, String director,
			int runtime, String description,
			Image poster){
		this.movieName = name;
		this.rating = rating;
		this.contentRating = cRating;
		this.genre = genre;
		this.actors = actors;
		this.director = director;
		this.poster = poster;
		this.runningTime = runtime;
		this.description = description;
	}
	
	public Movies(){
		this.movieName = "";
		this.rating = 0.0f;
		this.contentRating = "";
		this.genre = null;
		this.actors = null;
		this.director = "";
		this.poster = null;
		this.runningTime = 0;
		this.description = "";
	}
	
}
