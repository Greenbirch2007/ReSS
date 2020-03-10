class Movie{
    String title;
    String genre;
    int rating;

    void playIt(){
        System.out.println("Playing the movie");
    }
}



public class MovieTestDrive {
    public static void main(String[] args) {
        Movie one =new Movie();
        one.title = "Gone with the Stock";
        one.genre= "Tragic";
        one.rating = -2;
        Movie two = new Movie();
        two.title = "lost in cubb";
        two.genre = "comedy";
        two.rating = 5;
        two.playIt();

        Movie three = new Movie();
        three.title = "byte";
        three.genre = "tragic butre~~~";
        three.rating = 127;

    }
}