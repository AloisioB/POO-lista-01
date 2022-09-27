package homework02;

public class Rectangle {
	double width;
	double height;
	
	double area() {
		return width * height;
	}
	double perimeter() {
		return (width * 2) + (height * 2);
	}
	double diagonal() {
		return Math.sqrt((width * width) + (height * height));
	}
}
