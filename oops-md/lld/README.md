## SOLID PRINCIPLES
- ### SINGLE RESPONSIBILITY PRINCIPLE
	- **A class should have only 1 reason to change**
	- Below code breaks SRP, as it has 3 reasons to change:
		1. If the calculate logic changes,
		2. If the print invoice logic changes,
		3. If save to db logic changes
	```java
	class Invoice {
	private Marker marker;
	private int quantity;
	
	public Invoice(Marker marker, int quantity) {
		this.marker = marker;
		this.quantity = quantity; 
	}
	public int calculateTotal() {
		int price = ((marker.price) * this.quantity);
		return price;
	} 
	public void printInvoice() {
	//print the invoice
	}
	public void saveToDB() {
	//save data to db
	}

	//Corrected
	class Invoice {
		private Marker marker;
		private int quantity;
		public Invoice(Marker marker, int quantity){
			this.marker = marker;
			this.quantity = quantity;
		}
		public int calculateTotal(){
			int price = ((marker.price)*this.quantity);
			return price;
		}
	}
	class InvoiceDao{
		Invoice invoice;
		public InvoiceDao(Invoice invoice) {
			this.invoice = invoice;	
		}
		public void saveToDB(){
		//save to db
		}
	}

	```

- ### OPEN/CLOSE PRINCIPLE
	- **Open for Extension but closed for modification**
	```java
	class InvoiceDao{
		Invoice invoice;
		public InvoiceDao(Invoice invoice) {
			this.invoice = invoice;
		}
		public void saveToDB(){
			//Save to DB
		}
		//Adding saveToFile here in this class breaks OPEN/CLOSE PRINCIPLE, as we are modyfing a well serving class.
	}
		```
	```java
	//Solution:
	// We just have to extend this interface, so in future even if we have to save to say DB, File, S3 storage etc, we dont modify the actual class, but extend the functionality of the interface.
	interface InvoiceDao{
		public void save(Invoice invoice);
	}
	class DatabaseInvoiceDao implements InvoiceDao{
		@Override
		public void save(Invoice invoice){
		//Save to DB
		}
	}
	class FileInvoiceDao implements InvoiceDao{
		@Override
		public void save(Invoice invoice){
		//Save to File
		}
	}
	```

- ### Liskov Substitution Principle
	- If Class B is subtype of Class A, then we should be able to replace object of A with B without breaking the behavior of the program
	- *Subclass should extend the capabilities of parent class not narrow it down*
	- B,C implements/extends A, so if we pass B or C instead of A, code
	- should not break.
	```java
	interface Bike{
		void turnOnEngine();
		void accelerate();
	}
	class MotorCycle implements Bike {
		boolean isEngineOn;
		int speed;
		public void turnOnEngine(){
			//turn on the engine
			isEngineOn = true;
		}
		public void accelerate(){
			speed = speed+10;
		}
	}
	class Bicycle implements Bike {
		int speed;
		public void turnOnEngine(){
			throw new AssertionError("No engine in bicycle");
		}
		public void accelerate(){
			speed = speed;
		}
	}
	```
	- In the above example, if I had to pass a motorcycle as a bike somewhere, it will be done fine, but if I pass Bicycle as a bike, things will break, because Bike does not have an engine, hence turnOnEngine function will throw exception, hence breaking Liskov Substitution Principle.

- ### Interface Segregation
	- **Interfaces should be such, that client should not implement unnecessary functions they do not need.**
	```java
	interface RestaurantEmployee {
		void washDishes();
		void serveCustomers();
		void cookFood();
	}
	class waiter implements RestaurantEmployee {
		// this is bad, since waiter will have to override cookFood(), or washDishes(), which is not waiter's task
	}

	//CORRECT:
	interface WaiterInterface{
		void serveCustomers();
		void takeOrders(); 
	}
	interface ChefInterface{
		void cookFood();
		void decideMenu();
	}
	```

- ### Dependency Inversion Principle
	- **Class should depend on interfaces, rather than concrete classes**
	- *High level* modules should not depend on the *low-level* modules. Both should depend on abstractions/interfaces.
	- It is discussed around the **has-a** relationship.
	- **High-Level object**: Any object referencing another object (HAS-A relationship).
	- **Low-Level object**: The object that is being referenced. (HAS-A relationship in the reverse direction)
	```java
	class Macbook {
		private final WiredKeyboard keyboard; //breaks DIP, as WiredKeyboard is a concrete class not interface, and it is now tightly coupled with the WiredKeyboard. 
		private final Keyboard keyboard; // this is correct
	}
	```

## DESIGN PATTERNS
- ### Strategy Design Pattern or Policy Pattern
	- When the children classes have similar code
	- This results in duplication
	- Strategy Design Pattern uses *composition (has-a relation)* instead of *inheritance (is-a relation)*.
	- ![[strategy-pattern.png]]