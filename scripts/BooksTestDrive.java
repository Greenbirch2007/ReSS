class Books{
    String title;
    String author;

}

class BooksTestDrive{
    public static void main(String[] args) {
        Books [] myBooks = new Books[3];
        int x =0;

        myBooks[0].title = "the grape of java";
        myBooks[1].title = "the java gatsby";
        myBooks[2].title = "the java cookbook";


        myBooks[0].author = "bob";
        myBooks[0].author = "boasdfb";
        myBooks[0].author = "bosdfb";

        while (x<3){
            System.out.print(myBooks[x].title);
            System.out.print("by");
            System.out.println(myBooks[x].author);
            x = x+1;
        }
        
        
        
        
    }
}