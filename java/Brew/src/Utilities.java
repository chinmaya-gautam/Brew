import java.util.ArrayList;
import org.apache.commons.text.similarity.*;
public class Utilities {
	private static Db_utilities dbu;
	private static JaroWinklerDistance distance;
	public Utilities(){
		dbu = new Db_utilities();
		distance = new JaroWinklerDistance();
	}

	public ArrayList<String> getActor(String actor1_text, String actor2_text) {
		ArrayList<String> actors = dbu.getAllActors();
		ArrayList<String> result = new ArrayList<String>();
		String actor1 = "";
		String actor2 = "";
		Double max_d1 = 0.0;
		Double max_d2 = 0.0;
		for (String actor:actors){
			Double d1 = distance.apply(actor, actor1_text);
			if (d1 > max_d1){
				max_d1 = d1;
				actor1 = actor;
			}
			
			if (actor2_text != ""){
				Double d2 = distance.apply(actor, actor2_text);
				if (d2 > max_d2){
					max_d2 = d2;
					actor2 = actor;
				}
			}
		}
		result.add(actor1);
		result.add(actor2);
		return result;
	}
}
