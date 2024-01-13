
## Check these codes
1. 
```cpp
class A
{ 
	int i;
	A()
	{ 
		i=0; cout&lt;&lt;i; 
	}
	A(int x=0)
	{ 
		i=x;  cout&lt;&lt;I;  
	}
};
A obj1;
```

> **This will give Compile Time Error**
> When a default constructor is defined and another constructor with 1 default value argument is defined, creating object without parameter will create ambiguity for the compiler.

2. 
```cpp
   class student
{
    int marks;
    public: student(){}
    student(int x)
    { 
         marks=x; 
    }
};
main()
{
    student s1(100);
    student s2();
    student s3=100;
    return 0;
}
```
> **This will work**
> It is a special case of constructor with only 1 argument. While calling a constructor with one argument, you are actually implicitly creating a conversion from the argument type to the type of class.