## INHERITANCE *is-a relationship*
- Parent Class (Super/Base class) -> Child Class (Subclass/Derived class)
- ## 4 types:
	- #### Single
	- #### Multilevel
	- #### Hierarchical
	- #### Hybrid

## ENCAPSULATION
- Bind the data with code that manipulates it, and keeps the data and code safe from external interference 
- Done using **access modifiers**.
	- **Private**: Accessible only within the class
	- **Default (no modifier)**: Accessible within the package.
	- **Protected**: Accessible within package and by subclasses.
	- **Public**: Accessible from everywhere.
## ABSTRACTION 
- Only essential details are displayed to the user
- Trivial/non-essential units are not displayed
- In JAVA, abstraction is achieved by **interfaces**, and **abstract classes**.
## POLYMORPHISM
- If _one task is performed in different ways_, it is known as polymorphism.
- Polymorphism allows objects of different classes to be treated as objects of a common base class. It comes in two forms: compile-time (method overloading) and runtime (method overriding).
- Achieved through 2 ways:
	- **Overloading**:
	- **Overriding**: 

# Object Oriented Design

## Coupling
- Dependency of a class on another class.
- It means classes are _aware_ of each other.
- We can use **interfaces** for weaker coupling
## Cohesion
- Level of a component which performs a single well defined task.
- Weak cohesion -> Split the task into separate parts.
## Association
- Relationship between the objects.
- 4 types of association between two objects:
	1. **One to One**
	2. **One to Many**
	3. **Many to One**
	4. **Many to Many**
- Association can be **unidirectional** or **bidirectional**.
## Aggregation *has-a relationship* 
- Aggregation is a way to achieve **Association**.
- Aggregation represents the relationship where one object contains other objects as a part of its state.
## Composition
- Also a way to achieve **Association**.
- Relationship where one object contains other objects as a part of its state.
- Strong relationship between the containing object and the dependent object.
- If we delete the parent object, all the child objects will be deleted automatically.