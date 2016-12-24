

public class Constraints {
	float lower_rating;
	float upper_rating;
	String genre;
	String actor1, actor2;
	String director;
	
	public Constraints(){
		lower_rating = 0.0f;
		upper_rating = 0.0f;
		genre = "";
		actor1 = "";
		actor2 = "";
		director = "";
	}
	
	public Constraints(float lower_rating, float upper_rating, String genre, String actor1, String actor2){
		this.lower_rating = lower_rating;
		this.upper_rating = upper_rating;
		this.genre = genre;
		this.actor1 = actor1;
		this.actor2 = actor2;
	}
}
