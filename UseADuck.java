public Duck(){
	size =34;
}



public class Duck{
	int size;
	public Duck(){
	System.out.println("duck~~~");
}
	public void setSize (int newSize){
		size = newSize;
	}
	
}


public class UseADuck{
	public static void main(String[] args)
	Duck D = new Duck();
	d.setSize(42);
}
}