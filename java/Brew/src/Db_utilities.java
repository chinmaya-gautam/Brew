

import java.awt.Image;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.sql.*;
import java.util.*;

import javax.imageio.ImageIO;
public class Db_utilities {

	private static Connection conn;
	private static Statement stmt;
	private static ArrayList movies;
	
	public Db_utilities(){
		try {
			Class.forName("org.sqlite.JDBC");
			conn = DriverManager.getConnection("jdbc:sqlite:/Users/chinmaya/Documents/programming/brew_project/movies.db");
		}catch(Exception e){
			e.printStackTrace();
		}
		System.out.println("Opened db successfully");
	}

	public void test_db(){
		try {
			stmt = conn.createStatement();
			String query = "select * from movies";
			ResultSet rs = stmt.executeQuery(query);
			while(rs.next()){
				String movieName = rs.getString(1);
				System.out.println(movieName);
				
				String runningTime = rs.getString(2);
				System.out.println(runningTime);
				
				String contentRating = rs.getString(3);
				System.out.println(contentRating);
				
				String imdbRating = rs.getString(4);
				System.out.println(imdbRating);
				
				String desc = rs.getString(5);
				System.out.println(desc);
				
				System.out.println("");
				stmt.close();
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}	
	}
	
	public ArrayList getResult(Constraints constraints){
		ArrayList<Movies> movieList = new ArrayList();
		
		String query = "select * from movies, media where movies.m_name = media.md_movie and ";
		if (constraints.upper_rating == 0.0 && constraints.lower_rating > 0.0){
			query = query + "m_imdbRating >= " + constraints.lower_rating;
		} else if (constraints.upper_rating > 0.0){
			query = query + "m_imdbRating between " + constraints.lower_rating + " and "  + constraints.upper_rating;
		}
		try {
			stmt = conn.createStatement();
			ResultSet rs = stmt.executeQuery(query);
			while(rs.next()){
				Movies tempMovie = new Movies();
				
				byte[] poster_raw =  rs.getBytes(10);
				Image img = ImageIO.read(new ByteArrayInputStream(poster_raw));
				String movie_name = rs.getString(1);
				String movie_rating = rs.getString(4);
				System.out.println("Movie: " + movie_name);
				System.out.println("Rating: " + movie_rating);
				tempMovie.movieName = movie_name;
				tempMovie.rating = Float.parseFloat(movie_rating);
				tempMovie.poster = img;
				movieList.add(tempMovie);
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	
		System.out.println(query);
		
		
		return movieList;
	}
}
