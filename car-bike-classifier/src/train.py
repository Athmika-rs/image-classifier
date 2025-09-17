package emp;
public class employee{
    public String empid;
    public String empname, empaddress;
    public void personal()
    {
        System.out.println("Employee ID: "+empid);
        System.out.println("Employee Name: "+empname);
        System.out.println("Employee Address: "+empaddress);
    }
}
Employee.java:
import emp.employee;

import java.util.Scanner;

// Subclass emp1 extending employee
class emp1 extends employee {
    String desig, dept;

    // Method to print department and designation details
    void depart() {
        System.out.println("Employee Designation: " + desig);
        System.out.println("Employee Department: " + dept);
    }
}

public class Employee {
    public static void main(String args[]) {
        Scanner inp = new Scanner(System.in);

        // Create an object of emp1 (which inherits from employee)
        emp1 e = new emp1();

        // Taking input from the user
        System.out.println("Enter employee id");
        e.empid = inp.nextLine();

        System.out.println("Enter employee name");
        e.empname = inp.nextLine();

        System.out.println("Enter employee address");
        e.empaddress = inp.nextLine();

        System.out.println("Enter employee designation");
        e.desig = inp.nextLine();

        System.out.println("Enter employee department");
        e.dept = inp.nextLine();

        // Display personal details and department details
        e.personal();
        e.depart();

        inp.close();  // Close the scanner resource
    }
}
 