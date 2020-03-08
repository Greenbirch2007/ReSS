
class An{
    void eat(){
        System.out.println("animal:eat~");
    }
}


class Dog extends An{
    void eat() {
        System.out.println("dog:eatin~~~");
    }

    void eatTest(){
        this.eat();
        super.eat();
    }
}


public class Animal {
    public static void main(String[] args) {
        An a = new An();
        a.eat();
        Dog d = new Dog();
        d.eatTest();

    }
}