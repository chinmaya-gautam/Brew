

public class Constraints {
	float lower_rating;
	float upper_rating;
	String actor;
	String director;
	
	public Constraints(){
		lower_rating = 0.0f;
		upper_rating = 0.0f;
		actor = "";
		director = "";
	}
	
	public Constraints(float lower_rating, float upper_rating, String actor, String director){
		this.lower_rating = lower_rating;
		this.upper_rating = upper_rating;
		this.actor = actor;
		this.director = director;
	}
}
